# UDP File Transfer with Reliable Protocols

This assignment implements reliable data transfer over UDP using Stop-and-Wait and Go-Back-N protocols. The objective is to transfer a large file while handling packet loss and to analyze how retransmission timeouts and window sizes affect throughput.

## Table of Contents
- [Requirements](#requirements)
- [Setup](#setup)
- [Code Structure](#code-structure)
- [Instructions](#instructions)
- [Results and Analysis](#results-and-analysis)

---

### Requirements
- **Python 3.x**
- `socket` library (pre-installed with Python)
- `matplotlib` for plotting throughput (for result analysis)

### Setup
1. Place the following files in the same directory:
   - `sender.py`
   - `receiver.py`
   - `sender_stopwait.py`
   - `receiver_stopwait.py`
   - `sender_gbn.py`
   - `receiver_gbn.py`
2. Ensure the file `testFile.jpg` (or any large file you wish to test) is also in this directory.

### Code Structure
- **`sender.py` and `receiver.py`**: Basic UDP communication without reliability.
- **`sender_stopwait.py` and `receiver_stopwait.py`**: Implements the Stop-and-Wait protocol with retransmissions.
- **`sender_gbn.py` and `receiver_gbn.py`**: Implements the Go-Back-N protocol with a sliding window, handling packet loss and retransmissions.

### Instructions
#### Step 1: Basic UDP Communication
1. Run `receiver.py` to start the receiver.
2. Run `sender.py` and input a message to send to the receiver.
3. Observe the message echo from the receiver.

#### Step 2: Stop-and-Wait Protocol
1. Set a timeout (around 15ms) in `sender_stopwait.py`.
2. Run `receiver_stopwait.py`.
3. Run `sender_stopwait.py` to start transferring `testFile.jpg`.
4. Observe retransmissions in the output if timeouts occur.

#### Step 3: Go-Back-N Protocol
1. Set the window size and timeout in `sender_gbn.py`.
2. Run `receiver_gbn.py`.
3. Run `sender_gbn.py` to begin file transfer.
4. For each experiment, note the throughput and number of retransmissions.

#### Step 4: Throughput Measurement and Analysis
1. Run each experiment 5 times with different window sizes (e.g., 1, 2, 4, 8, etc.) and delays (e.g., 5ms, 50ms, 150ms).
2. Calculate the average throughput and plot results if needed.
3. For plotting, set window size on the x-axis and average throughput on the y-axis, with separate curves for each delay.

### Results and Analysis
- **Window Size**: Throughput improves with larger window sizes but gains diminish as sizes increase further.
- **Propagation Delay**: Higher delays reduce throughput as packets take longer to be acknowledged.
- **Stop-and-Wait Timeout**: A 20ms timeout balances retransmissions and maintains high throughput.
- **Optimal Go-Back-N Window Size**: For smaller propagation delays, window sizes of 64 or 128 yield the highest throughput.

---

This README file provides all necessary steps to set up, run, and analyze your UDP file transfer implementation with reliable protocols.

