# 🏃‍♂️ Prison Escape Game | لعبة هروب من السجن

![Game Screenshot](screenshot.png)

A terminal-based Python game where you navigate through a prison maze to escape, featuring simple pathfinding visualization.

## ✨ Features | المميزات
- 🎮 **WASD Movement** - Navigate using keyboard controls
- � **Guard Obstacles** - Avoid stationary guards
- 🔍 **Path Visualization** - Shows escape path when pressing SPACE
- 🏁 **Simple Rules** - Reach 'E' to escape
- 📦 **Zero Dependencies** - Runs with standard Python libraries

## 📥 Installation | التثبيت

### Requirements | المتطلبات
- Python 3.6+
🚀 How to Run
Copy the code to a file named prison_escape.py:

git clone https://github.com/yourusername/prison-escape.git
cd prison-escape
Run the game:


python prison_escape.py
🎮 Gameplay

▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓
▓ P       G       ▓
▓   ▓     ▓   ▓   ▓
▓ G   ▓       ▓   ▓
▓ ▓   ▓ ▓ ▓   ▓ ▓ ▓
▓     ▓     G     ▓
▓ ▓ ▓ ▓ ▓ ▓   ▓ ▓ ▓
▓           ▓   E ▓
▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓
Controls
Key	Action
W	Move Up
S	Move Down
A	Move Left
D	Move Right
SPACE	Show Path
Q	Quit
🧠 How It Works
The game uses a simple right-hand rule algorithm for pathfinding:

Generates a random 15x10 prison layout

Places 5 guards at random positions

Uses directional scanning to find paths


📂 File Structure
Copy
prison_escape/
├── prison_escape.py    # Main game code
├── README.md           # This documentation
└── screenshot.png      # Game preview image
🌟 Future Improvements
Add moving guards

Implement scoring system

Create difficulty levels

Add ASCII animations


This project is licensed under the MIT License - see the LICENSE file for details.



Created by Mohamed Wahba
✉️ mohamed@baianat.com
🐍 Made with Python 3
