
# DGT302 – A Comprehensive Comparison of Butterworth and Chebyshev Filters

A Python-based Digital Signal Processing (DSP) project comparing the frequency-domain and time-domain characteristics of **Butterworth** and **Chebyshev Type I** low-pass filters.

The project also includes a simplified, parameter-based illustration examining how the two filter families behave under four sets of assumed frequency-selectivity requirements associated with 2G, 3G, 4G, and 5G labels.

> **Scope and Interpretation:** The 2G–5G section is an educational comparison using selected, simplified filter specifications. It is intended only to examine how Butterworth and Chebyshev Type I filters respond to different assumed requirements. It does NOT represent actual filter architectures, RF front ends, channel plans, or implementation practices used in commercial 2G/3G/4G/5G networks. All numerical specifications are illustrative assumptions, not official cellular standards.

---

## Table of Contents

- [1. Project Overview](#1-project-overview)
- [2. Project Objectives](#2-project-objectives)
- [3. Theoretical Background](#3-theoretical-background)
- [4. Project Architecture](#4-project-architecture)
- [5. Project Structure](#5-project-structure)
- [6. Technologies and Requirements](#6-technologies-and-requirements)
- [7. Simulation Methodology](#7-simulation-methodology)
- [8. Comparative Analysis](#8-comparative-analysis)
- [9. 2G–5G Parameter-Based Illustration](#9-2g5g-parameter-based-illustration)
- [10. Installation and Execution](#10-installation-and-execution)
- [11. Simulation Results](#11-simulation-results)
- [12. Discussion and Limitations](#12-discussion-and-limitations)
- [13. References](#13-references)

---

## 1. Project Overview

This project focuses on the design, simulation, and comparative analysis of two classical Infinite Impulse Response (IIR) low-pass filter families:

- **Butterworth Filter:** Characterized by a maximally flat magnitude response in the passband.
- **Chebyshev Type I Filter:** Allows controlled passband ripple to achieve a sharper transition between the passband and stopband.

The project is implemented in Python using NumPy, SciPy, and Matplotlib.

It consists of two main simulation programs:

1. `so_sanh_butterworth_chebyshev.py`: Designs and compares Butterworth and Chebyshev Type I filters under common digital-filter parameters.
2. `ung_dung_2G_5G.py`: Performs an illustrative comparison using four sets of assumed specifications labelled 2G, 3G, 4G, and 5G.

The main emphasis is on frequency response, phase response, group delay, filter order, pole-zero distribution, and the trade-offs between magnitude selectivity and phase characteristics.

## 2. Project Objectives

The primary objectives are:

- Design Butterworth and Chebyshev Type I low-pass filters.
- Understand the theoretical differences between the two filter families.
- Compare magnitude and phase responses.
- Analyze analog prototypes and digital filter implementations.
- Investigate pole-zero distributions and filter stability.
- Examine impulse, step, and group-delay responses.
- Calculate the required filter order under different passband and stopband constraints.
- Evaluate the trade-offs between passband flatness, transition sharpness, and filter complexity.
- Provide graphical and numerical results to support engineering analysis.

## 3. Theoretical Background

### 3.1 Butterworth Filter

The Butterworth filter is designed to provide a maximally flat magnitude response in the passband.

Its main characteristics include:

- No intentional passband ripple.
- Smooth magnitude response.
- Monotonic passband and stopband characteristics.
- Relatively gradual transition compared with Chebyshev Type I filters under comparable design constraints.

### 3.2 Chebyshev Type I Filter

The Chebyshev Type I filter introduces controlled equiripple behavior in the passband.

Its main characteristics include:

- Controlled passband ripple.
- Sharper transition between passband and stopband.
- Potentially lower filter order for the same passband and stopband requirements.
- Different phase and group-delay characteristics compared with Butterworth filters.

### 3.3 IIR Filter Characteristics

Both filter families belong to the Infinite Impulse Response (IIR) filter category.

Their characteristics are determined by poles and zeros.

For a discrete-time IIR filter, stability requires all poles to lie strictly inside the unit circle.

Group delay describes the frequency-dependent delay experienced by signal components and is useful for examining phase distortion.

## 4. Project Architecture

The project follows two independent simulation workflows.

### 4.1 Common Filter Comparison

```text
          Filter Specifications
                   |
                   v
          Analog Filter Design
                   |
          +--------+--------+
          |                 |
          v                 v
      Butterworth       Chebyshev I
          |                 |
          v                 v
       Bilinear          Bilinear
       Transform         Transform
          |                 |
          +--------+--------+
                   |
                   v
          Digital Filter Analysis
                   |
          +--------+--------+
          |        |        |
          v        v        v
       Magnitude  Phase   Group Delay
       Response  Response  Analysis
          |        |        |
          +--------+--------+
                   |
                   v
          Pole-Zero Analysis
                   |
                   v
          Simulation Results
```

### 4.2 2G–5G Parameter-Based Illustration

```text
        Assumed Filter Specifications
                   |
                   v
          +--------+--------+
          |        |        |
          v        v        v
         2G       3G       4G       5G
          |        |        |        |
          +--------+--------+--------+
                   |
                   v
          Butterworth Design
                   |
                   v
          Chebyshev Type I Design
                   |
                   v
          Calculate Filter Orders
                   |
                   v
          Frequency Response Analysis
                   |
                   v
          Group Delay Comparison
                   |
                   v
          Numerical and Graphical Results
```

## 5. Project Structure

```text
DGT-18/
|
|-- anh_mo_phong.pdf
|
|-- result.txt
|
|-- so_sanh_butterworth_chebyshev.py
|
|-- ung_dung_2G_5G.py
|
|-- orgin_image/
|   |
|   |-- so_sanh_butterworth_chebyshev.png
|   |
|   |-- ung_dung_2G_5G.png
|
|-- README.md
```

| File / Directory | Description |
|---|---|
| `anh_mo_phong.pdf` | Supporting simulation report and documentation. |
| `result.txt` | Numerical results generated from the simulations. |
| `so_sanh_butterworth_chebyshev.py` | Main program for common Butterworth and Chebyshev filter comparison. |
| `ung_dung_2G_5G.py` | Parameter-based filter comparison using four illustrative scenarios. |
| `orgin_image/` | Contains simulation images and graphical results. |
| `README.md` | Project documentation. |

## 6. Technologies and Requirements

### 6.1 Programming Language

- Python 3.9 or later.

### 6.2 Libraries

| Library | Purpose |
|---|---|
| NumPy | Numerical computation and array processing. |
| SciPy | Analog and digital filter design and signal analysis. |
| Matplotlib | Data visualization and plotting. |

### 6.3 Installation

Install the required libraries using:

```bash
python -m pip install numpy scipy matplotlib
```

## 7. Simulation Methodology

### 7.1 Common Digital Filter Comparison

The first simulation program uses common filter design parameters to compare Butterworth and Chebyshev Type I filters.

| Parameter | Value |
|---|---:|
| Filter Type | Low-pass IIR |
| Filter Order | 5 |
| Sampling Frequency | 8,000 Hz |
| Cutoff Frequency | 1,000 Hz |
| Chebyshev Passband Ripple | 1 dB |

The simulation performs the following operations:

1. Design analog Butterworth and Chebyshev Type I prototypes.
2. Apply low-pass frequency scaling.
3. Convert analog prototypes into digital filters using the bilinear transform.
4. Calculate frequency responses.
5. Analyze phase responses.
6. Calculate group delay.
7. Generate impulse and step responses.
8. Analyze pole-zero distributions.

### 7.2 2G–5G Parameter-Based Comparison

The second simulation program defines four sets of assumed low-pass filter specifications.

Each scenario includes:

- Passband edge frequency.
- Stopband edge frequency.
- Maximum passband ripple.
- Minimum stopband attenuation.

The program estimates the minimum filter order required by each filter family using SciPy filter-order estimation functions.

The resulting analog filter responses and group-delay characteristics are then evaluated and compared.

## 8. Comparative Analysis

The project evaluates the two filter families based on several important characteristics.

| Characteristic | Butterworth | Chebyshev Type I |
|---|---|---|
| Passband Response | Maximally flat | Equiripple |
| Passband Ripple | None | Controlled |
| Transition Sharpness | Relatively gradual | Sharper |
| Filter Order | May be higher | May be lower |
| Phase Characteristics | Frequency-dependent | Frequency-dependent |
| Group Delay | Varies with frequency | Varies with frequency |
| Main Advantage | Smooth passband | Better selectivity for a given order |
| Main Trade-off | Potentially higher order | Passband ripple |

The comparison demonstrates that neither filter family is universally superior.

The appropriate filter depends on the required magnitude response, phase characteristics, filter complexity, and system constraints.

## 9. 2G–5G Parameter-Based Illustration

This section investigates how Butterworth and Chebyshev Type I filters behave under four different sets of assumed design specifications.

The labels 2G, 3G, 4G, and 5G are used only as illustrative comparison scenarios.

### 9.1 Assumed Filter Specifications

| Scenario | Passband Edge | Stopband Edge | Passband Ripple | Stopband Attenuation |
|---|---:|---:|---:|---:|
| 2G (GSM) | 100 kHz | 300 kHz | 3 dB | 40 dB |
| 3G (WCDMA) | 1.92 MHz | 3.6 MHz | 1 dB | 45 dB |
| 4G (LTE) | 9 MHz | 11.5 MHz | 0.5 dB | 50 dB |
| 5G (NR) | 49.5 MHz | 58 MHz | 0.25 dB | 55 dB |

**Important:** These values are selected simulation parameters. They are not official 3GPP frequency allocations, bandwidth specifications, RF filter requirements, or mandatory filter configurations.

### 9.2 Filter Order Comparison

The following values are recorded in the current `result.txt` file.

| Scenario | Butterworth Order | Chebyshev Type I Order |
|---|---:|---:|
| 2G-labelled case | 5 | 4 |
| 3G-labelled case | 10 | 6 |
| 4G-labelled case | 28 | 11 |
| 5G-labelled case | 49 | 15 |

The results illustrate how different assumed frequency-selectivity requirements can affect the required filter order.

Chebyshev Type I filters generally achieve the selected transition requirements with a lower order by allowing passband ripple.

Butterworth filters prioritize passband flatness and may require a higher order to satisfy the same stopband constraints.

These results depend on the selected simulation parameters and should not be generalized to actual cellular network implementations.

### 9.3 Comparison Metrics

The simulation examines:

- Required filter order.
- Magnitude response.
- Passband ripple.
- Stopband attenuation.
- Group delay.
- Group-delay variation.

The generated plots allow the two filter families to be compared across all four illustrative scenarios.

## 10. Installation and Execution

### 10.1 Clone the Repository

```bash
git clone https://github.com/BlackWater006/DGT302-A-comprehensive-comparison-of-Butterworth-and-Chebyshev-filters..git
```

Navigate to the project directory:

```bash
cd DGT-18
```

### 10.2 Install Dependencies

```bash
python -m pip install numpy scipy matplotlib
```

### 10.3 Run the Common Filter Comparison

```bash
python so_sanh_butterworth_chebyshev.py
```

### 10.4 Run the 2G–5G Illustration

```bash
python ung_dung_2G_5G.py
```

The programs calculate numerical results and generate graphical comparisons.

A graphical environment is required to display figures interactively through Matplotlib.

## 11. Simulation Results

### 11.1 Butterworth and Chebyshev Comparison

The first program generates graphical results covering:

- Magnitude response.
- Phase response.
- Group-delay response.
- Analog and digital filter responses.
- Impulse response.
- Step response.
- Pole-zero distribution.

### 11.2 2G–5G Parameter-Based Comparison

The second program generates graphical comparisons covering:

- Magnitude responses for each illustrative scenario.
- Butterworth and Chebyshev filter orders.
- Passband ripple.
- Group-delay characteristics.
- Group-delay variation.

The images included in the `orgin_image/` directory provide visual references for the simulation results.

## 12. Discussion and Limitations

### 12.1 Discussion

The simulation highlights the fundamental design trade-offs between Butterworth and Chebyshev Type I filters.

Butterworth filters provide a smooth and maximally flat passband response, making them suitable when passband flatness is an important requirement.

Chebyshev Type I filters introduce controlled passband ripple to obtain sharper transition characteristics and potentially lower filter order.

The results also demonstrate that filter magnitude response should not be considered independently of phase and group-delay behavior.

### 12.2 Limitations

The project has several limitations:

1. The 2G–5G scenarios are simplified educational simulations.
2. The selected specifications are assumptions for comparative analysis, not official cellular standards.
3. The project does not reproduce actual RF front-end architectures or commercial mobile communication systems.
4. The simulations focus on idealized low-pass filter characteristics.
5. Real-world effects such as hardware non-idealities, propagation channels, modulation, coding, synchronization, and RF implementation constraints are outside the project scope.
6. Numerical results depend on the selected parameters and simulation environment.

Therefore, the 2G–5G section should be interpreted strictly as a comparative study of two filter families under different assumed design constraints.

It should not be interpreted as a description of how actual 2G, 3G, 4G, or 5G networks implement their filtering systems.

## 13. References

1. SciPy Signal Processing Documentation: https://docs.scipy.org/doc/scipy/reference/signal.html
2. SciPy Butterworth Filter Design: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html
3. SciPy Chebyshev Type I Filter Design: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.cheby1.html
4. SciPy Butterworth Order Estimation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.buttord.html
5. SciPy Chebyshev Type I Order Estimation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.cheb1ord.html
6. NumPy Documentation: https://numpy.org/doc/
7. Matplotlib Documentation: https://matplotlib.org/stable/

---

**Project Type:** Academic Digital Signal Processing Simulation

**Main Topic:** Butterworth and Chebyshev Type I Low-Pass Filter Comparison

**Programming Language:** Python

**Purpose:** Educational simulation and comparative signal analysis.
