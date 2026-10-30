import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

SPECS = {
    "2G (GSM)":     dict(fp=100e3,  fst=300e3,  Rp=3.0,  As=40),
    "3G (WCDMA)":   dict(fp=1.92e6, fst=3.6e6,  Rp=1.0,  As=45),
    "4G (LTE)":     dict(fp=9e6,    fst=11.5e6, Rp=0.5,  As=50),
    "5G (NR)":      dict(fp=49.5e6, fst=58e6,   Rp=0.25, As=55),
}

def design(kind, sp):

    wp, ws = 1.0, sp["fst"] / sp["fp"]
    if kind == "butter":
        N, wn = signal.buttord(wp, ws, sp["Rp"], sp["As"], analog=True)
        z, p, k = signal.butter(N, wn, btype="low", analog=True, output="zpk")
    else:
        N, wn = signal.cheb1ord(wp, ws, sp["Rp"], sp["As"], analog=True)
        z, p, k = signal.cheby1(N, sp["Rp"], wn, btype="low", analog=True, output="zpk")
    return N, (z, p, k)

def metrics(zpk, sp):
    f = np.linspace(sp["fp"] * 1e-3, sp["fst"] * 2.0, 6000)
    W = f / sp["fp"]
    _, H = signal.freqs_zpk(*zpk, worN=W)
    mag_db = 20 * np.log10(np.abs(H) + 1e-12)
    phase = np.unwrap(np.angle(H))
    gd = -np.gradient(phase, W) / (2 * np.pi)
    inb = f <= sp["fp"]
    return dict(
        f=f, mag_db=mag_db, gd=gd,
        ripple=mag_db[inb].max() - mag_db[inb].min(),
        gd_var=(gd[inb].max() - gd[inb].min()),
        gd_mean=gd[inb].mean(),
    )

results = {}
for gen, sp in SPECS.items():
    results[gen] = {}
    for kind in ("butter", "cheby1"):
        N, zpk = design(kind, sp)
        m = metrics(zpk, sp)
        m["N"] = N
        results[gen][kind] = m

print(f"{'Thế hệ':<12}{'Lọc':<12}{'Bậc':>4}{'Gợn/sụt(dB)':>13}{'Méo độ trễ nhóm (% của 1/fp)':>34}")
for gen, sp in SPECS.items():
    for kind, label in (("butter", "Butterworth"), ("cheby1", "Chebyshev I")):
        m = results[gen][kind]

        gd_norm = m["gd_var"] * 100
        print(f"{gen:<12}{label:<12}{m['N']:>4}{m['ripple']:>13.2f}{gd_norm:>34.1f}")
    print()

fig, axes = plt.subplots(3, 4, figsize=(18, 11))
fig.suptitle("Butterworth và Chebyshev I qua các thế hệ 2G-5G (minh họa)",
             fontsize=15, fontweight="bold")
col = {"butter": "tab:blue", "cheby1": "tab:red"}
lab = {"butter": "Butterworth", "cheby1": "Chebyshev I"}

for j, (gen, sp) in enumerate(SPECS.items()):
    unit, div = ("MHz", 1e6) if sp["fp"] >= 1e6 else ("kHz", 1e3)

    ax = axes[0, j]
    for kind in ("butter", "cheby1"):
        m = results[gen][kind]
        ax.plot(m["f"] / div, m["mag_db"], color=col[kind],
                label=f"{lab[kind]} (N={m['N']})")
    ax.axvspan(0, sp["fp"] / div, color="green", alpha=0.08)
    ax.axvspan(sp["fst"] / div, ax.get_xlim()[1] * 10, color="red", alpha=0.08)
    ax.axhline(-sp["As"], color="gray", ls=":", lw=0.8)
    ax.set(title=f"{gen}\nRp={sp['Rp']} dB, As={sp['As']} dB",
           xlabel=f"Tần số ({unit})", ylim=(-80, 5),
           xlim=(0, sp["fst"] * 1.8 / div))
    if j == 0: ax.set_ylabel("Biên độ (dB)")
    ax.grid(alpha=0.3); ax.legend(fontsize=8)

    ax = axes[1, j]
    for kind in ("butter", "cheby1"):
        m = results[gen][kind]
        inb = m["f"] <= sp["fp"] * 1.1
        ax.plot(m["f"][inb] / sp["fp"], m["gd"][inb], color=col[kind],
                label=lab[kind])
    ax.set(xlabel="f / fp", title="Độ trễ nhóm chuẩn hóa (băng thông)")
    if j == 0: ax.set_ylabel("τg · fp")
    ax.grid(alpha=0.3); ax.legend(fontsize=8)

gens = list(SPECS)
x = np.arange(len(gens)); wd = 0.38
for i, (key, title, fmt) in enumerate([
        ("N", "Bậc bộ lọc cần dùng", None),
        ("ripple", "Gợn/sụt băng thông (dB)", None),
        ("gd_var", "Méo độ trễ nhóm (% 1/fp)", None)]):
    ax = axes[2, i]
    for s, kind in enumerate(("butter", "cheby1")):
        if key == "gd_var":
            vals = [results[g][kind]["gd_var"] * 100 for g in gens]
        else:
            vals = [results[g][kind][key] for g in gens]
        b = ax.bar(x + (s - 0.5) * wd, vals, wd, color=col[kind], label=lab[kind])
        ax.bar_label(b, fmt="%.1f" if key != "N" else "%d", fontsize=8)
    ax.set_xticks(x, [g.split()[0] for g in gens])
    ax.set_title(title); ax.grid(alpha=0.3, axis="y"); ax.legend(fontsize=8)
axes[2, 3].axis("off")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("ung_dung_2G_5G.png", dpi=140)
plt.show()
