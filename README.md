# 🧠 Dynamic Difficulty Adjustment using Deep Learning

> An AI-driven project that automatically adjusts a game's difficulty in real-time to match the player's skill level. The primary goal is to maintain a state of "flow" 🌊, ensuring the game is engagingly challenging but never frustrating.

---

## 🚀 Project Architecture

The system is built upon three core components that work in synergy:

### 1. 🎮 Game Environment (The Data Collector)
* An endless runner game developed using **Pygame** in Python.
* Its main purpose is to serve as a data collection platform. On every player failure, a comprehensive snapshot of the game state (score, speed, player coordinates, and upcoming obstacle features) is logged to a `.csv` file.

### 2. 🔮 Risk Prediction Model (The Oracle)
* A machine learning model (e.g., a Neural Network) trained on the data collected from the game environment.
* Its function is to take the current game state as input and predict the probability of failure—the "risk score"—at any given moment.

### 3. 🤖 Difficulty Adjustment AI (The Director)
* An intelligent agent, likely based on **Reinforcement Learning**, that acts as the game's conductor.
* This AI uses the risk score from the prediction model to dynamically alter game parameters (like obstacle spacing, height, and speed) to maintain an optimal level of challenge for the player.

---

## 📊 Current Project Status

| Component                       | Status          | Description                                                                    |
| ------------------------------- | --------------- | ------------------------------------------------------------------------------ |
| **Game Environment & Data Logger** | ✅ Completed    | The game is fully functional, and the data logging mechanism is actively collecting data upon failure. |
| **Risk Prediction Model** | ❌ Not Started  | No models have been designed or trained to analyze game data or predict risk yet.      |
| **Difficulty Adjustment AI** | ❌ Not Started  | The implementation of the intelligent agent for dynamic difficulty adjustment has not yet begun. |

---

## ▶️ Getting Started

Follow these steps to run the game environment and begin collecting your own gameplay data.

### Prerequisites
* Python 3.x
* Pygame library

### Installation
1.  Install the Pygame library via pip:
    ```bash
    pip install pygame
    ```

### Execution
2.  Run the `main.py` script to start the game:
    ```bash
    python main.py
    ```
> Upon each failure, a new row of data will be appended to the `game_logs.csv` file in the `logs` directory.