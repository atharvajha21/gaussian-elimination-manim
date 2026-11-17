# Gaussian Elimination — Animated Mathematics Video

An educational animation project built with Python and Manim Community Edition.

The project visually explains how to solve a system of three linear equations using Gaussian Elimination, row operations, row echelon form, and back substitution.

## Final Video

**MathsFinal vedio.mp4** — 1080p, approximately 3 minutes 55 seconds.

## Mathematical Example

Solve the system:

x + y + z = 6

2x + y - z = 1

x - y + 2z = 5

Final solution:

**x = 1, y = 2, z = 3**

## Project Structure

```text
gaussian-elimination-manim/
├── Code/
│   └── main_sync.py
├── Submission/
│   ├── narration.aiff
│   └── narration.txt
├── MathsFinal vedio.mp4
├── manim.cfg
├── requirements.txt
├── .gitignore
└── README.md
## Installation

Clone the repository:

git clone https://github.com/atharvajha21/gaussian-elimination-manim.git
cd gaussian-elimination-manim

Create a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

## Run the Animation

manim -pqh Code/main_sync.py GaussianElimination

## Technologies Used

- Python
- Manim Community Edition
- LaTeX
- FFmpeg

## Author

Atharva Jha
