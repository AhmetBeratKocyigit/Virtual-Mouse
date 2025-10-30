<h1 align="center">🖐️ Virtual Mouse | Hand Gesture Controlled Mouse</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv" />
  <img src="https://img.shields.io/badge/CvZone-1.5.6-orange" />
  <img src="https://img.shields.io/badge/Autopy-1.0-lightgrey" />
</p>

<p align="center">
  <b>Control your mouse using only your hand gestures through your webcam!<br>
  Real-time hand tracking, click detection, and smooth cursor movement 🚀</b>
</p>

---

## 🧠 About the Project

This project enables **virtual mouse control using hand gestures** via your webcam.  
With an AI-powered hand tracking system, you can:
- 🖱️ Move the cursor using your index finger  
- ✌️ Click by raising both the index and middle fingers  
- ⚙️ Enjoy smooth and stable cursor motion  

---

## 📸 Features

✅ Real-time hand and finger detection  
✅ Automatic screen resolution detection  
✅ Cursor control with index finger  
✅ Click action with index + middle finger  
✅ Smoothened movement for precision  
✅ Exit easily with the **`q` key**  

---

## 🧩 Requirements

Install the following Python libraries before running:

```bash
pip install opencv-python cvzone autopy numpy
```

---

## 🧰 Technologies Used

| Technology | Purpose |
|-------------|----------|
| **OpenCV** | Camera access and image processing |
| **cvzone.HandTrackingModule** | Detects hand and finger landmarks |
| **autopy** | Simulates real mouse movement and clicks |
| **NumPy** | Used for coordinate mapping and calculations |

---

## ⚙️ Adjustable Parameters

| Variable | Description | Default |
|-----------|--------------|----------|
| `wCam`, `hCam` | Camera resolution | `640x480` |
| `frameR` | Frame margin for motion area | `100` |
| `smoothening` | Cursor smoothening factor | `7` |

---

## 🚀 How to Use

1. Run the script:
   ```bash
   python virtual_mouse.py
   ```
2. When the webcam starts:
   - ☝️ **Raise only your index finger** → Move the cursor  
   - ✌️ **Raise index + middle finger** → Perform a click  
   - ✊ **Lower your hand** → Stop controlling  
3. Press **`q`** to quit the program.

---

## 💡 How It Works

1. The `cvzone.HandTrackingModule` detects hand landmarks.  
2. The tip of the index finger (`lmList[8]`) is tracked as the cursor point.  
3. `numpy.interp()` maps camera coordinates to screen coordinates.  
4. `autopy.mouse.move()` moves the actual mouse pointer.  
5. A click is triggered when both index and middle fingers are raised.

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and share it!

---

<p align="center">
  💻 <b>Developed by Ahmet Berat Koçyiğit</b> | 2025
</p>
