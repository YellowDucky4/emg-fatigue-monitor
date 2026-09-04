# Lab Notebook

## 2026-09-04
- Set up Arduino IDE + board support for Uno R4 WiFi; confirmed working with Blink sketch
- Installed Python (numpy, scipy, matplotlib, pandas, jupyter) after Citrix/MATLAB access proved impractical
- Built LED + resistor circuit on breadboard; initial wiring put resistor and ground in the same row, bypassing the LED entirely (parallel short instead of series path) — fixed by rebuilding as a proper series chain
- Wired photoresistor module to A0; hit "serial port busy" and "invalid serial port" upload errors caused by Serial Plotter holding the COM port open during upload — resolved by closing Plotter before uploading
- Got clean analog readings: ~3700 baseline, ~11000 when covered, at 14-bit resolution
- Observed persistent baseline noise (~hundreds of counts) even under constant light — likely 60 Hz mains flicker, directly motivating the notch filter in the processing pipeline

## 2026-09-03
- Finalized hardware selection: MyoWare 2.0 Muscle Sensor, Link Shield, Arduino Shield, Uno R4 WiFi
- Chose R4 WiFi over R3 for 14-bit ADC resolution and future WiFi/dashboard option
- Sourced Kendall H124SG 24mm disposable EMG electrodes after initially finding incompatible TENS pads (wrong connector, wrong size) — learned MyoWare's snap connector matches standard ECG/EMG electrode format, not TENS