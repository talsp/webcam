# Webcam over socket

A simple app that transfers the webcam feed from one app to another over socket
There are 2 python scripts

cam.py - Script to run on the machine that will send the webcam feed
receiver.py - Script to that will receive webcam feed

**How to use:**

```bash
pip install -r requirements.txt
python cam.py
python receiver.py
