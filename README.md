# 🎮 Gesture Play

Control games using your hands.

**Gesture Play** is a computer-vision-based game controller that lets you interact with keyboard-controlled games using real-time hand gestures. Instead of relying entirely on a physical keyboard, the project detects hand movements through a camera and translates recognized gestures into keyboard inputs such as **Up**, **Down**, **Left**, and **Right**.

Built as an experimental project to explore the intersection of **computer vision, hand tracking, and human-computer interaction**.

## ✨ Features

* 🖐️ Real-time hand detection and tracking
* 🎮 Gesture-based game control
* ⌨️ Converts recognized gestures into keyboard inputs
* 📷 Uses a webcam as the primary input device
* ⚡ Real-time interaction with supported games
* 🧩 Simple and extensible architecture

## 🛠️ Tech Stack

* **Python**
* **OpenCV**
* **MediaPipe**
* **PyAutoGUI**
* **NumPy**

## 🚀 How It Works

The project follows a simple pipeline:

```text
Webcam
   ↓
Hand Detection
   ↓
Hand Landmark Tracking
   ↓
Gesture Recognition
   ↓
Gesture → Keyboard Input
   ↓
Game Control 🎮
```

The webcam captures live video, the hand-tracking system identifies hand landmarks, and the detected gesture is mapped to a keyboard action. The corresponding key input is then sent to the active game.

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/gesture-play.git
```

Navigate to the project directory:

```bash
cd gesture-play
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Connect a webcam and make sure it is accessible by your computer.

Run the main program:

```bash
python main.py
```

Place your hand in front of the camera and use the supported gestures to control the game.

> **Note:** The exact gestures and controls may vary depending on the implementation and the game being controlled.

## 🎮 Supported Controls

| Gesture / Movement      | Keyboard Action |
| ----------------------- | --------------- |
| Hand movement / gesture | Up              |
| Hand movement / gesture | Down            |
| Hand movement / gesture | Left            |
| Hand movement / gesture | Right           |

> Update this table with the exact gestures used in the project.

## 🎥 Demo

Add a short GIF or video demonstrating the project here.

```text
[ Add demo GIF or video here ]
```

Example:

![Gesture Play Demo](assets/demo.gif)

## 🔮 Future Improvements

Some ideas for future development:

* Add support for more gestures
* Improve gesture recognition accuracy
* Reduce detection latency
* Add customizable gesture-to-key mappings
* Support multiple games and control schemes
* Add a graphical user interface
* Add gesture calibration
* Improve accessibility for hands-free gaming

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

If you would like to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push your branch.
6. Open a Pull Request.

For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 👨‍💻 Author

Created by **YOUR NAME**.

If you found this project interesting, feel free to ⭐ the repository!
