# Alien Invasion Game

A simple space shooter game built with Python and Pygame, based on the project from **"Python Crash Course"** by Eric Matthes.

## About This Project

This is a learning project from the book **"Python Crash Course"** Chapter 12-14. The original project teaches fundamental game development concepts like:
- Object-oriented programming
- Sprite management
- Event handling

### My Additions

I've added some extra features while learning:
- **Score tracking system** - Earn points for each alien destroyed
- **Difficulty scaling** - Game gets progressively harder
- **Power-ups/Features** - Shield, Plasma bullets, and Bomb mechanics
- **Purchase system** - Buy upgrades with earned points

**Note:** This is a learning project. While the additions work, the codebase is being explored and refined as part of the learning process.

### Important Note

The **core idea of this project doesn't deserve extensive development or investment**. It's a simple learning exercise from a beginner programming book. The goal is to learn Python fundamentals and Pygame basics, not to build a polished game. 

If you're looking at this project, use it to:
-  Understand OOP concepts
-  Learn how game loops work
-  Practice collision detection
-  Get familiar with Pygame

**Don't expect:**
-  Production-quality code
-  Advanced game mechanics
-  Professional asset quality
-  Scalable architecture for larger games

---

## Game Features

### Core Gameplay
-  **Player Ship** - Control with arrow keys, shoot with SPACE
-  **Alien Fleet** - Enemies that move side-to-side and drop down
-  **Shooting System** - Fire bullets to destroy aliens
-  **Collision Detection** - Bullets destroy aliens, aliens damage ship

### Power-ups (Costs 200 Points Each)
- 🛡️ **Shield** - Absorbs one hit from aliens (shown with cyan outline)
- ⚡ **Plasma Bullets** - Yellow bullets that one-shot kill aliens
- 💣 **Bomb** - Destroys all aliens on screen instantly

### Game Mechanics
- **Scoring** - 100 points per alien killed, 50 points per bomb kill
- **Difficulty** - Aliens speed up after every 5 kills
- **Game Over** - When aliens reach bottom or hit unshielded ship

---

## How to Run

### Requirements
- Python 3.7+
- Pygame 2.0+

### Quick Start

**Option 1: With an existing virtual environment**
```bash
source path/to/your/venv/bin/activate
cd path/to/alien-invasion
python alien_invasion.py
```

**Option 2: Using system Python**
```bash
cd path/to/alien-invasion
pip install pygame
python3 alien_invasion.py
```

**Option 3: Create a fresh virtual environment**
```bash
cd path/to/alien-invasion
python3 -m venv venv
source venv/bin/activate
pip install pygame
python alien_invasion.py
```

---

## Controls

| Key | Action |
|-----|--------|
| **← →** | Move ship left/right |
| **SPACE** | Fire bullet |
| **1** | Buy Shield (200 pts) |
| **2** | Buy Plasma Bullets (200 pts) |
| **3** | Buy Bomb (200 pts) |
| **B** | Use bomb (if you have any) |
| **Q** | Quit game |

---

## File Structure

```
alien/
├── alien_invasion.py    # Main game loop and logic
├── settings.py          # Game configuration
├── ship.py              # Player ship class
├── alien.py             # Alien enemy class
├── bullet.py            # Bullet projectile class
├── images/
│   ├── ship.bmp
│   └── alien.bmp
└── README.md
```

---

## Resources & Learning

### Books
- **[Python Crash Course](https://nostarch.com/pythoncrashcourse2e)** by Eric Matthes
  - A great beginner book for learning Python game development
  - Covers OOP, Pygame, data visualization, and web scraping

### Pygame Documentation
- **[Official Pygame Docs](https://www.pygame.org/docs/)**
- **[Pygame Tutorials](https://www.pygame.org/wiki/tutorials)**
- **[Real Python - Pygame Tutorial](https://realpython.com/pygame-a-primer/)**

### AI & Code Assistance
- **[ChatGPT](https://openai.com/chatgpt)** - Used for concept explanations and debugging

---

## Learning Notes

- This project demonstrates:
- Class-based game architecture
- Sprite groups and collision detection
- Event-driven programming
- Game state management
- Simple difficulty scaling
- User interface with text rendering

### Potential Improvements
- Level progression
- High score saving
- Animated sprites
- Particle effects

---

## Status

This is an **active learning project**. Features may be refined as understanding deepens. The core game is fully functional and playable.

---

## Author Notes

Built while learning Python game development. Special thanks to:
- Eric Matthes for the Python Crash Course book
- The Pygame community for excellent documentation
- AI tools for explaining concepts and debugging

Happy Learning!