# AI Notebooks 🧠

> Collection of AI search algorithm implementations and educational notebooks

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org/)
[![OpenAI Gym](https://img.shields.io/badge/OpenAI-Gym-blue)](https://gym.openai.com/)
[![License](https://img.shields.io/badge/License-Educational-green)]()

## 🎯 Overview

This repository contains a collection of Jupyter notebooks and Python implementations of classic AI search algorithms and problems. Each project demonstrates different search strategies, environment modeling, and problem-solving approaches commonly used in artificial intelligence and machine learning.

**Educational Focus**: These notebooks are designed for learning AI concepts through hands-on implementation of classic problems.

## 📚 Projects

### 1. 🌊 River Crossing Puzzle

Classic constraint satisfaction problem where a farmer must transport a goat, cabbage, and wolf across a river.

#### Implementations:
- **`riverCross/`** - Input agent with graph visualization
- **`riverCrossBFS/`** - Breadth-First Search solution

#### Features:
- Custom OpenAI Gym environment
- State space representation
- Graph visualization of solution paths
- Multiple solving strategies

#### The Problem:
A farmer needs to cross a river with a goat, cabbage, and wolf. The boat can only carry the farmer and one item. If left alone:
- The goat will eat the cabbage
- The wolf will eat the goat

**Files:**
```
riverCross/
├── Clase 1 Input Agent.ipynb           # Interactive input-based solver
├── Clase 1 Input Agent with Graph.ipynb # Graph visualization
├── riverCrossEnv.py                    # Gym environment
├── riverCrossGraph.py                  # Graph utilities
├── riverCrossInputAgent.py             # Input agent implementation
└── riverCrossUtils.py                  # Utility functions

riverCrossBFS/
├── BFS Agent.ipynb                     # BFS algorithm implementation
└── riverCrossModel.py                  # Model definition
```

### 2. 🎮 Maze Solver

Maze navigation using search algorithms with custom OpenAI Gym environment.

#### Features:
- Custom Gym environment for maze navigation
- Multiple search algorithms (A*, BFS, DFS)
- Visual rendering (2D and ANSI)
- Priority queue implementation
- Configurable maze sizes and complexity

#### Based On:
[gym-maze by tuzzer](https://github.com/tuzzer/gym-maze)

**Files:**
```
Maze/
├── Test Maze.ipynb                     # Testing and examples
├── agent.py                            # Agent implementation
├── model.py                            # Model definition
├── modelExample.py                     # Usage examples
├── priorityQueue.py                    # Priority queue for A*
├── mazeEnvExtended.py                  # Extended environment
├── gym_maze/                           # Custom Gym environment
│   ├── __init__.py
│   ├── setup.py
│   ├── envs/
│   │   ├── maze.py                     # Maze generation
│   │   ├── maze_env.py                 # Gym environment
│   │   ├── maze_view_2d.py             # 2D rendering
│   │   └── maze_view_ansi.py           # Terminal rendering
└── readme.txt                          # Setup instructions
```

### 3. ❄️ Air Conditioning Simulation

Simulation notebook for air conditioning system modeling.

**Files:**
```
AireAcondicionado/
├── AireAcondicionado.ipynb             # Main simulation notebook
└── Modelo.png                          # System diagram
```

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Notebooks**: Jupyter
- **Environment Framework**: OpenAI Gym
- **Visualization**: Pygame, Matplotlib
- **Algorithms**: BFS, DFS, A*, Graph Search

## 📋 Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- pip package manager

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/figlesias221/AI_Notebooks.git
cd AI_Notebooks
```

### 2. Install Dependencies

#### For River Crossing Projects:
```bash
pip install gym numpy jupyter
```

#### For Maze Solver:
```bash
pip install pygame gym numpy jupyter matplotlib
```

#### Install Custom Maze Environment:
```bash
cd Maze/gym_maze
pip install -e .
cd ../..
```

### 3. Launch Jupyter Notebook

```bash
jupyter notebook
```

## 💡 Usage Examples

### River Crossing with BFS

```python
# Open riverCrossBFS/BFS Agent.ipynb
# The notebook demonstrates:
# - State space representation
# - BFS algorithm implementation
# - Solution path visualization
```

### Interactive River Crossing

```python
# Open riverCross/Clase 1 Input Agent.ipynb
# Allows manual solving with:
# - User input for actions
# - Real-time state validation
# - Visual feedback
```

### Maze Solving

```python
# Open Maze/Test Maze.ipynb
import gym
import gym_maze

env = gym.make('maze-v0')
env.reset()
# Implement your search algorithm
```

## 🔍 Algorithms Implemented

### Search Algorithms

#### Breadth-First Search (BFS)
- **Used in**: River Crossing puzzle
- **Properties**: Complete, optimal for unweighted graphs
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)

#### A* Search
- **Used in**: Maze solver
- **Properties**: Complete, optimal with admissible heuristic
- **Time Complexity**: O(b^d)
- **Heuristic**: Manhattan distance

#### Depth-First Search (DFS)
- **Used in**: Maze exploration
- **Properties**: Memory efficient
- **Time Complexity**: O(V + E)

### Problem-Solving Techniques

- **State Space Search**: Representing problems as graphs
- **Constraint Satisfaction**: River crossing constraints
- **Path Planning**: Maze navigation
- **Graph Visualization**: Solution path rendering

## 📊 Project Structure

```
AI_Notebooks/
├── riverCross/              # River crossing with input agent
│   ├── *.ipynb             # Jupyter notebooks
│   └── *.py                # Python modules
├── riverCrossBFS/          # River crossing with BFS
│   ├── BFS Agent.ipynb
│   └── riverCrossModel.py
├── Maze/                   # Maze solver project
│   ├── gym_maze/           # Custom Gym environment
│   ├── *.ipynb             # Test notebooks
│   └── *.py                # Agent and model code
├── AireAcondicionado/      # Air conditioning simulation
│   ├── AireAcondicionado.ipynb
│   └── Modelo.png
└── README.md
```

## 🧪 Running the Notebooks

### River Crossing Notebooks

1. **Input Agent**:
   ```bash
   jupyter notebook "riverCross/Clase 1 Input Agent.ipynb"
   ```
   - Interactive solving
   - Manual action selection

2. **Input Agent with Graph**:
   ```bash
   jupyter notebook "riverCross/Clase 1 Input Agent with Graph.ipynb"
   ```
   - Visual graph representation
   - Solution path tracking

3. **BFS Agent**:
   ```bash
   jupyter notebook "riverCrossBFS/BFS Agent.ipynb"
   ```
   - Automatic BFS solving
   - Optimal path finding

### Maze Notebook

```bash
jupyter notebook "Maze/Test Maze.ipynb"
```
- Custom maze generation
- Search algorithm testing
- Visual rendering

### Air Conditioning Simulation

```bash
jupyter notebook "AireAcondicionado/AireAcondicionado.ipynb"
```
- System simulation
- Parameter tuning

## 📝 Code Examples

### River Crossing Environment

```python
from riverCross.riverCrossEnv import RiverCrossEnv

# Create environment
env = RiverCrossEnv()

# Reset to initial state
state = env.reset()

# Take action: move farmer with goat
action = {
    "direction": 0,  # left to right
    "passenger": 1   # goat
}

next_state, reward, done, info = env.step(action)
```

### Maze Environment

```python
import gym
import gym_maze

# Create maze environment
env = gym.make('maze-v0')
observation = env.reset()

# Render the maze
env.render()

# Take action (0: up, 1: down, 2: left, 3: right)
observation, reward, done, info = env.step(1)
```

### Priority Queue (for A*)

```python
from Maze.priorityQueue import PriorityQueue

pq = PriorityQueue()
pq.push(item, priority)
next_item = pq.pop()
```

## 🎓 Learning Objectives

### Covered Concepts

1. **Search Algorithms**
   - Uninformed search (BFS, DFS)
   - Informed search (A*)
   - Graph traversal

2. **Problem Modeling**
   - State space representation
   - Action spaces
   - Transition functions
   - Reward shaping

3. **Environment Design**
   - OpenAI Gym interface
   - Custom environments
   - Observation/action spaces

4. **Algorithm Analysis**
   - Time complexity
   - Space complexity
   - Optimality guarantees

5. **Visualization**
   - Graph plotting
   - Path rendering
   - State representation

## 🔧 Customization

### Create Your Own Maze

```python
from Maze.gym_maze.envs.maze_env import MazeEnv

# Custom maze size
env = MazeEnv(maze_size=(10, 10))

# Custom complexity
env = MazeEnv(enable_render=True)
```

### Modify River Crossing

Edit `riverCrossEnv.py` to:
- Add more passengers
- Change constraints
- Modify reward structure
- Add new rules

## 🐛 Troubleshooting

### Gym Environment Not Found
```bash
# Reinstall gym_maze
cd Maze/gym_maze
pip install -e .
```

### Pygame Not Rendering
```bash
# Install pygame dependencies
pip install pygame
# On macOS, you may need:
pip install pygame --upgrade
```

### Import Errors
```bash
# Ensure you're in the correct directory
cd AI_Notebooks
# Add to Python path if needed
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Jupyter Kernel Issues
```bash
# Reinstall Jupyter kernel
pip install ipykernel
python -m ipykernel install --user
```

## 📚 Resources

### OpenAI Gym
- [Gym Documentation](https://www.gymlibrary.dev/)
- [Creating Custom Environments](https://www.gymlibrary.dev/content/environment_creation/)

### Search Algorithms
- [A* Pathfinding](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [BFS Algorithm](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Constraint Satisfaction Problems](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem)

### Python & Jupyter
- [Jupyter Documentation](https://jupyter.org/documentation)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)

## 🤝 Contributing

These are educational notebooks. Feel free to:
- Add new algorithms
- Improve visualizations
- Add more classic AI problems
- Enhance documentation

## 📄 License

Educational project - free to use for learning purposes.

## 🙏 Acknowledgments

- **Maze Environment**: Based on [gym-maze by tuzzer](https://github.com/tuzzer/gym-maze)
- **OpenAI Gym**: Framework for developing RL algorithms
- **Classic AI Problems**: River crossing, maze solving, and more

## 📞 Support

For questions or issues:
- Check notebook comments and documentation
- Review the troubleshooting section
- Open an issue on GitHub

---

**Educational AI implementations for learning search algorithms and problem-solving techniques** 🧠✨

**Happy learning and exploring AI!** 🚀
