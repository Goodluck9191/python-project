import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
from scipy.special import erfc

# -----------------------------
# RRC FILTER FUNCTION
# -----------------------------
def rrc_filter(beta, sps, span):
    N = span * sps
    t = np.arange(-N/2, N/2 + 1) / sps
    h = np.zeros(len(t))

    for i in range(len(t)):
        if t[i] == 0.0:
            h[i] = 1.0 - beta + (4 * beta / np.pi)
        elif abs(t[i]) == 1 / (4 * beta):
            h[i] = (beta / np.sqrt(2)) * (
                ((1 + 2/np.pi) * np.sin(np.pi / (4 * beta))) +
                ((1 - 2/np.pi) * np.cos(np.pi / (4 * beta)))
            )
        else:
            h[i] = (np.sin(np.pi * t[i] * (1 - beta)) +
                   4 * beta * t[i] * np.cos(np.pi * t[i] * (1 + beta))) / \
                   (np.pi * t[i] * (1 - (4 * beta * t[i])**2))
    return h


# -----------------------------
# PARAMETERS
# -----------------------------
beta = 0.25        # Roll-off factor
sps = 8            # Samples per symbol
span = 6           # Filter span
num_bits = 1000    # Number of bits
EbN0_dB = 10       # SNR in dB

# -----------------------------
# TRANSMITTER
# -----------------------------
bits = np.random.randint(0, 2, num_bits)
symbols = 2*bits - 1        # BPSK mapping (0->-1, 1->+1)

# Upsample
upsampled = np.zeros(len(symbols)*sps)
upsampled[::sps] = symbols

# RRC filter
h = rrc_filter(beta, sps, span)
tx_signal = np.convolve(upsampled, h)

# -----------------------------
# CHANNEL (Add AWGN Noise)
# -----------------------------
EbN0 = 10**(EbN0_dB/10)
noise_std = np.sqrt(1/(2*EbN0))
noise = noise_std * np.random.randn(len(tx_signal))
rx_signal = tx_signal + noise

# -----------------------------
# RECEIVER (Matched Filter)
# -----------------------------
rx_filtered = np.convolve(rx_signal, h)

# Downsample (account for delay)
delay = span * sps
rx_samples = rx_filtered[delay::sps][:num_bits]

# Decision
received_bits = (rx_samples > 0).astype(int)

# -----------------------------
# BER Calculation
# -----------------------------
bit_errors = np.sum(bits != received_bits)
BER = bit_errors / num_bits

print("Bit Error Rate (BER):", BER)

# -----------------------------
# PLOTS
# -----------------------------
plt.figure()
plt.plot(h)
plt.title("RRC Impulse Response")
plt.grid()

plt.figure()
plt.plot(rx_filtered[:200])
plt.title("Received Signal (First 200 samples)")
plt.grid()

plt.show()