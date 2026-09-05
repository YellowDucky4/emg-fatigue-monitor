import serial
import csv
import time

PORT = "COM3"       # match whatever Tools > Port shows in Arduino IDE
BAUD = 115200
DURATION_SECONDS = 15
OUTPUT_FILE = "../data/raw/test_log.csv"

ser = serial.Serial(PORT, BAUD)
time.sleep(2)  # let the Arduino reset after the serial connection opens

with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    start = time.time()
    while time.time() - start < DURATION_SECONDS:
        line = ser.readline().decode("utf-8").strip()
        if line and "timestamp" not in line:
            parts = line.split(",")
            if len(parts) == 2:
                writer.writerow(parts)

ser.close()
print(f"Saved to {OUTPUT_FILE}")