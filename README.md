# 🏃‍♂️ Prison Escape Game | لعبة هروب من السجن

![Game Screenshot](screenshot.png)

A terminal-based Python game where you navigate through a prison maze to escape, featuring simple pathfinding visualization.

لعبة بايثون في سطر الأوامر حيث تتجول في متاهة سجن للهروب، مع عرض مرئي لمسار الهروب.

## ✨ Features | المميزات
- 🎮 **WASD Movement** - Navigate using keyboard controls | التحكم باستخدام لوحة المفاتيح
- � **Guard Obstacles** - Avoid stationary guards | تجنب الحراس الثابتين
- 🔍 **Path Visualization** - Shows escape path when pressing SPACE | عرض مسار الهروب عند الضغط على المسافة
- 🏁 **Simple Rules** - Reach 'E' to escape | الوصول إلى 'E' للهروب
- 📦 **Zero Dependencies** - Runs with standard Python libraries | تعمل بمكتبات بايثون الأساسية

## 📥 Installation | التثبيت

### Requirements | المتطلبات
- Python 3.6+ | بايثون 3.6 أو أحدث

```bash
# No additional packages needed | لا حاجة لحزم إضافية
🚀 How to Run | طريقة التشغيل
Copy the code to a file named prison_escape.py:

bash
Copy
git clone https://github.com/yourusername/prison-escape.git
cd prison-escape
Run the game:

bash
Copy
python prison_escape.py
🎮 Gameplay | طريقة اللعب
Copy
▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓
▓ P       G       ▓
▓   ▓     ▓   ▓   ▓
▓ G   ▓       ▓   ▓
▓ ▓   ▓ ▓ ▓   ▓ ▓ ▓
▓     ▓     G     ▓
▓ ▓ ▓ ▓ ▓ ▓   ▓ ▓ ▓
▓           ▓   E ▓
▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓
Controls | عناصر التحكم
Key	Action	الزر	الوظيفة
W	Move Up	التحرك لأعلى
S	Move Down	التحرك لأسفل
A	Move Left	التحرك لليسار
D	Move Right	التحرك لليمين
SPACE	Show Path	عرض المسار
Q	Quit	الخروج
🧠 How It Works | كيف تعمل
The game uses a simple right-hand rule algorithm for pathfinding:

Generates a random 15x10 prison layout

Places 5 guards at random positions

Uses directional scanning to find paths

تستخدم اللعبة خوارزمية اليد اليمنى البسيطة:

تنشئ سجن عشوائي بحجم 15x10

تضع 5 حراس في مواقع عشوائية

تستخدم المسح الاتجاهي لإيجاد المسارات

📂 File Structure | هيكلة الملفات
Copy
prison_escape/
├── prison_escape.py    # Main game code
├── README.md           # This documentation
└── screenshot.png      # Game preview image
🌟 Future Improvements | تطويرات مستقبلية
Add moving guards | إضافة حراس متحركين

Implement scoring system | نظام النقاط

Create difficulty levels | مستويات صعوبة

Add ASCII animations | إضافة رسوم متحركة

📜 License | الترخيص
This project is licensed under the MIT License - see the LICENSE file for details.

هذا المشروع مرخص تحت رخصة MIT - راجع ملف LICENSE للتفاصيل.

Created by Mohamed Wahba
✉️ mohamed@baianat.com
🐍 Made with Python 3

Copy

### Key Features of This README:
1. **Professional Bilingual Format** - Clean English/Arabic presentation
2. **Visual Game Preview** - Space for screenshot
3. **Detailed Controls Table** - With both keybindings
4. **Technical Implementation** - Explains the right-hand rule algorithm
5. **Zero-Dependency Highlight** - Emphasizes no Pygame requirement
6. **Future Roadmap** - Clear development path
7. **Complete File Structure** - Shows project organization

To use:
1. Save this as `README.md` in your project folder
2. Add a `screenshot.png` of your game in action
3. Update the GitHub link with your actual repository
4. Customize contact information

The README presents your project professionally while maintaining the simple, terminal-based nature of the game. Would you like me to add any specific sections or modify any part?
