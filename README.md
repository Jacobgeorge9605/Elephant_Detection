🛡️ **SmartFence AI Detection System**

SmartFence is an intelligent edge-based object detection system powered by the Sony IMX500 AI Vision Sensor. It is designed to detect wildlife and domestic animals (like elephants, birds, cows, etc.) in real-time and trigger appropriate alert mechanisms such as playing sounds and sending SMS alerts.

**Features**
Edge AI Inference: Utilizes the Sony IMX500 sensor to run deep learning models on-device.

Real time Object Detection: Detects elephants, birds, people, and more using SSD-MobileNet/NanoDet models.

Audio Alerts: Plays species-specific alert sounds (e.g: beehive buzz for elephants, chirping for birds).

SMS Notifications: Sends real-time SMS alerts via GSM when critical detections are made (e.g., elephants, birds).

Bounding Box Overlay: Displays detected objects with labels and confidence scores.

Modular Design: Easily customize detection classes, model paths, and alert logic.

**Requirements**
Hardware
- Raspberry Pi (recommended: Raspberry Pi 4/5)
- Sony IMX500 Vision Sensor
- Speaker (connected to Pi)
- Optional: GSM Module (for SMS alerts)

Software
Python 3.7+

Dependencies:
pip install opencv-python playsound numpy


**Directory Structure**



![Screenshot 2025-07-09 123102](https://github.com/user-attachments/assets/f280f271-2b7a-40f9-89de-9a0fd4c7ea9c)



**How to Run**
1. Connect and setup IMX500 on Raspberry Pi
Ensure your IMX500 is recognized and configured properly.

2. Place the model
Copy your .rpk object detection model (default: SSD MobileNet) to:
/usr/share/imx500-models/imx500_network_ssd_mobilenetv2_fpnlite_320x320_pp.rpk

4. Add sound files
Place the alert sound files under the music/ directory (or modify the paths in label_to_sound dictionary).

5. Run the detection system
python3 main.py
You can customize the run using flags:
python3 main.py --threshold 0.6 --fps 5 --max-detections 5 postprocess nanodet

**Command-Line Arguments**

| Flag                   | Description                      | Default                  |
| ---------------------- | -------------------------------- | ------------------------ |
| `--model`              | Path to `.rpk` model             | SSD-MobileNet            |
| `--fps`                | Frame rate                       | Device default           |
| `--threshold`          | Detection threshold (0–1)        | 0.55                     |
| `--iou`                | IOU threshold for postprocessing | 0.65                     |
| `--bbox-normalization` | Normalize bounding boxes         | False                    |
| `--bbox-order`         | Format of bounding box coords    | `yx`                     |
| `--postprocess`        | Use postprocessing (`nanodet`)   | None                     |
| `--max-detections`     | Max objects per frame            | 10                       |
| `--labels`             | Path to label list               | `assets/coco_labels.txt` |


Supported Classes & Sound Mapping
Detection labels are mapped to specific sound alerts:

| Detected Class               | Sound Triggered           |
| ---------------------------- | ------------------------- |
| elephant                     | `Beehive_sound.mp3` + SMS |
| bird                         | `Chirp.aac` + SMS         |
| cow, dog, cat, sheep, person | Corresponding MP3         |


**GSM Integration**
The system uses a gsm2 module to trigger alerts via a GSM modem. Make sure:

- gsm2.py contains working functions: alert(entity) and send_sms(entity)
- Your GSM module is properly configured with AT commands (SIM800/900, etc.)

**Detection Visualization**
The system overlays:

- Bounding boxes on each object
- Confidence scores
- Labels (adjusted for certain cases, e.g., person → object)

🔒 License
This project is for educational/research use. Use responsibly in wildlife areas. Contact the developer for deployment permissions.

Support
For technical support or contribution:

Email: jacobgeorge@ieee.org
Contributor: Jacob George



