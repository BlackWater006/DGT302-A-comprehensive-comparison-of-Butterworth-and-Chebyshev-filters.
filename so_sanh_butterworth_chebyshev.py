import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 8000
fc = 1000
N = 5
rp = 1.0

def design_iir(kind, N, fc, fs, rp=1.0):

    if kind == "butter":
        z, p, k = signal.buttap(N)
    elif kind == "cheby1":
        z, p, k = signal.cheb1ap(N, rp)
    else:
        raise ValueError("kind phải là 'butter' hoặc 'cheby1'")

    wd = 2 * np.pi * fc / fs
    Wc = 2 * fs * np.tan(wd / 2)

    za, pa, ka = signal.lp2lp_zpk(z, p, k, wo=Wc)

    zd, pd, kd = signal.bilinear_zpk(za, pa, ka, fs)
    return (za, pa, ka), (zd, pd, kd)

filters = {
    "Butterworth": design_iir("butter", N, fc, fs),
    f"Chebyshev I ({rp} dB)": design_iir("cheby1", N, fc, fs, rp),
}
colors = {"Butterworth": "tab:blue", f"Chebyshev I ({rp} dB)": "tab:red"}

f = np.linspace(0, fs / 2, 4096)
w = 2 * np.pi * f / fs
results = {}
for name, (analog, digital) in filters.items():
    sos = signal.zpk2sos(*digital)
    _, H = signal.sosfreqz(sos, worN=w)

    b, a = signal.zpk2tf(*digital)
    _, gd = signal.group_delay((b, a), w=w)

    Wa = 2 * np.pi * f
    _, Ha = signal.freqs_zpk(*analog, worN=Wa)

    imp = signal.sosfilt(sos, np.r_[1, np.zeros(63)])
    step = signal.sosfilt(sos, np.ones(64))
    results[name] = dict(H=H, Ha=Ha, gd=gd, b=b, a=a, imp=imp, step=step,
                         poles=digital[1], zeros=digital[0])

fig = plt.figure(figsize=(16, 12))
fig.suptitle(f"So sánh Butterworth và Chebyshev I  |  bậc N={N}, "
             f"fc={fc} Hz, fs={fs} Hz", fontsize=15, fontweight="bold")
gs = fig.add_gridspec(3, 3)

ax = fig.add_subplot(gs[0, 0])
for n, r in results.items():
    ax.plot(f, 20 * np.log10(np.abs(r["H"]) + 1e-12), color=colors[n], label=n)
ax.axvline(fc, color="gray", ls="--", lw=0.8)
ax.axhline(-3, color="gray", ls=":", lw=0.8)
ax.set(title="Đáp ứng biên độ (dB)", xlabel="Tần số (Hz)", ylabel="|H| (dB)",
       ylim=(-100, 5))
ax.grid(alpha=0.3); ax.legend()

ax = fig.add_subplot(gs[0, 1])
for n, r in results.items():
    ax.plot(f, np.abs(r["H"]), color=colors[n], label=n)
ax.set(title="Biên độ tuyến tính (băng thông)", xlabel="Tần số (Hz)",
       ylabel="|H|", xlim=(0, 2000), ylim=(0, 1.1))
ax.grid(alpha=0.3); ax.legend()

ax = fig.add_subplot(gs[0, 2])
for n, r in results.items():
    ax.plot(f, 20 * np.log10(np.abs(r["Ha"]) + 1e-12), "--", color=colors[n],
            alpha=0.6, label=f"{n} (analog)")
    ax.plot(f, 20 * np.log10(np.abs(r["H"]) + 1e-12), color=colors[n],
            label=f"{n} (digital)")
ax.set(title="Analog và Digital (bilinear)", xlabel="Tần số (Hz)",
       ylabel="|H| (dB)", ylim=(-100, 5))
ax.grid(alpha=0.3); ax.legend(fontsize=7)

ax = fig.add_subplot(gs[1, 0])
for n, r in results.items():
    ax.plot(f, np.unwrap(np.angle(r["H"])), color=colors[n], label=n)
ax.set(title="Đáp ứng pha", xlabel="Tần số (Hz)", ylabel="Pha (rad)")
ax.grid(alpha=0.3); ax.legend()

ax = fig.add_subplot(gs[1, 1])
for n, r in results.items():
    ax.plot(f, r["gd"], color=colors[n], label=n)
ax.set(title="Độ trễ nhóm", xlabel="Tần số (Hz)", ylabel="Mẫu",
       xlim=(0, fs / 2))
ax.grid(alpha=0.3); ax.legend()

ax = fig.add_subplot(gs[1, 2])
for n, r in results.items():
    ax.plot(r["step"], color=colors[n], label=n)
ax.set(title="Đáp ứng bước đơn vị", xlabel="n (mẫu)", ylabel="y[n]")
ax.grid(alpha=0.3); ax.legend()

for i, (n, r) in enumerate(results.items()):
    ax = fig.add_subplot(gs[2, i])
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), "k--", lw=0.8)
    ax.plot(r["zeros"].real, r["zeros"].imag, "o", mfc="none", ms=10,
            color=colors[n], label=f"Không ({len(r['zeros'])}, bội)")
    ax.plot(r["poles"].real, r["poles"].imag, "x", ms=10, mew=2,
            color=colors[n], label="Cực")
    ax.axhline(0, color="gray", lw=0.5); ax.axvline(0, color="gray", lw=0.5)
    ax.set(title=f"Cực-không: {n}", xlabel="Phần thực", ylabel="Phần ảo",
           xlim=(-1.6, 1.6), ylim=(-1.6, 1.6))
    ax.set_aspect("equal"); ax.grid(alpha=0.3); ax.legend(loc="upper left")

ax = fig.add_subplot(gs[2, 2])
ax.plot(np.cos(th), np.sin(th), "k--", lw=0.8)
for n, r in results.items():
    ax.plot(r["poles"].real, r["poles"].imag, "x", ms=10, mew=2,
            color=colors[n], label=n)
ax.set(title="So sánh vị trí cực", xlabel="Phần thực", ylabel="Phần ảo",
       xlim=(-1.6, 1.6), ylim=(-1.6, 1.6))
ax.set_aspect("equal"); ax.grid(alpha=0.3); ax.legend(loc="upper left")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("so_sanh_butterworth_chebyshev.png", dpi=150)

print("=" * 60)
for n, r in results.items():
    mag = np.abs(r["H"])
    pb = mag[f <= fc]
    f_stop = 2 * fc
    idx = np.argmin(np.abs(f - f_stop))
    print(f"\n{n}")
    print("  Hệ số b:", np.round(r["b"], 6))
    print("  Hệ số a:", np.round(r["a"], 6))
    print(f"  |p| lớn nhất = {np.max(np.abs(r['poles'])):.4f} "
          f"-> {'ỔN ĐỊNH' if np.max(np.abs(r['poles'])) < 1 else 'KHÔNG ổn định'}")
    print(f"  Gợn băng thông (0..fc): {20*np.log10(pb.max()/pb.min()):.3f} dB")
    print(f"  Suy hao tại {f_stop} Hz: {20*np.log10(mag[idx]):.1f} dB")
    print(f"  Độ trễ nhóm TB (băng thông): "
          f"{r['gd'][f <= fc].mean():.2f} mẫu, "
          f"dao động {np.ptp(r['gd'][f <= fc]):.2f} mẫu")
plt.show()
