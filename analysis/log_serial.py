import serial
import time

PORT = "COM3"
BAUD = 500000
DURATION_SECONDS = 90
OUTPUT_FILE = "../data/raw/isometric_hold_01.csv"

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)
ser.reset_input_buffer()

buf = bytearray()
start = time.time()
while time.time() - start < DURATION_SECONDS:
    chunk = ser.read(ser.in_waiting or 1)
    if chunk:
        buf.extend(chunk)
elapsed = time.time() - start
ser.close()

lines = buf.decode("utf-8", errors="ignore").split("\n")
values = [x.strip() for x in lines if x.strip().isdigit()]

with open(OUTPUT_FILE, "w", newline="") as f:
    f.write("value\n")
    f.write("\n".join(values))

print("elapsed:", elapsed)
print("samples:", len(values))
print("effective rate (Hz):", len(values) / elapsed)