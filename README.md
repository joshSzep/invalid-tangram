# Invalid Tangram

A Python adaptation of the original game created at The Guildhall at SMU.

## Game Overview

Invalid Tangram is a **shooter/puzzle game hybrid**. At its surface, it's a Galaga-style top-down shoot-em-up, but with a unique twist: when enemies are killed, they transform into blocks that fall and stack at the bottom of the screen, creating a puzzle element that feeds back into the shooter mechanics.

## Core Mechanics

### Combat
- Top-down shooter with the player at the bottom of the screen
- Enemies (tangrams) descend from the top
- Player shoots upward to destroy enemies

### Enemies
- All enemies are **tangram shapes** (geometric puzzle pieces)
- Enemies come in **4 colors**: Yellow, Green, Blue, Red
- When killed, enemies transform into **blocks** of the corresponding color
- Blocks fall and stack at the bottom of the screen

### Block Matching & Power-ups
- When **2 or more blocks of the same color** are touching, they form a group
- The player can move on top of a matched group to **absorb** it
- Absorbing blocks grants a **temporary power-up** based on the color:

| Color  | Power-up Effect           |
|--------|---------------------------|
| Yellow | **Spread Shot** - Multiple projectiles in a fan pattern |
| Green  | **Seeking Shot** - Projectiles home in on enemies |
| Blue   | **Power Shot** - Increased damage per projectile |
| Red    | **Rapid Fire** - Increased rate of fire |

### Life System
- The player's "life" is represented as a **timer that constantly decreases**
- **Absorbing blocks** increases the remaining time
- **Getting hit by enemies** decreases the remaining time
- When the timer reaches zero, the game ends

### Scoring
- The goal is to **survive as long as possible**
- Points are accumulated over time and by defeating enemies
- High scores are achieved through skillful balance of combat and block management

## Strategy

Players must balance two competing priorities:
1. **Shooting enemies** to prevent being overwhelmed and to generate blocks
2. **Managing blocks** to create matched groups for power-ups and time extensions

The hybrid nature creates emergent gameplay:
- Killing enemies too fast may create unmatched block chaos
- Waiting too long risks running out of time or getting hit
- Strategic color targeting can set up powerful combos

## Technical Details

- Built with **Python 3.13+**
- Rendering: **pygame-ce** + **ModernGL** (OpenGL 3.3 Core)
- Target framerate: 120 FPS

## Development

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/invalid-tangram.git
cd invalid-tangram

# Create virtual environment and install dependencies
uv sync

# Run the game
uv run invalid-tangram
```

### Running Tests
```bash
uv run pytest
```

## License

See [LICENSE](LICENSE) for details.
