# Gaussian Elimination — Animated Mathematics Video

An educational animation project built with Python and Manim Community Edition.

The project visually explains how to solve a system of three linear equations using Gaussian elimination, elementary row operations, row echelon form, and back substitution.

## Final Video

**MathsFinal vedio.mp4** — 1080p, 16:9 landscape, approximately 3 minutes 55 seconds.

## Learning Objective

By the end of the video, viewers should be able to follow Gaussian elimination on a 3 × 3 system, explain the row operations, reach row echelon form, and use back substitution to find and verify the solution.

## Mathematical Example

Solve:

```text
x + y + z = 6
2x + y - z = 1
x - y + 2z = 5
```

Final solution: **x = 1, y = 2, z = 3**

The animation demonstrates these row operations:

```text
R2 -> R2 - 2R1
R3 -> R3 - R1
R3 -> R3 - 2R2
R3 -> R3 / 7
```

It then uses back substitution and checks the result in the original equations.

## Project Structure

```text
gaussian-elimination-manim/
├── Code/
│   └── main_sync.py
├── Submission/
│   ├── narration.aiff
│   └── narration.txt
├── MathsFinal vedio.mp4
├── Gaussian_Elimination_Storyboard.pdf
├── AI_TOOL_DISCLOSURE.md
├── manim.cfg
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.12+
- Manim Community Edition 0.22.1
- LaTeX installation
- FFmpeg

## Installation

```bash
git clone https://github.com/atharvajha21/gaussian-elimination-manim.git
cd gaussian-elimination-manim
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the Animation

```bash
manim -pqh Code/main_sync.py GaussianElimination
```

## Tools and AI Disclosure

Manim Community Edition, Python, and FFmpeg were used in the production workflow. ChatGPT assisted with planning, explanations, code guidance, troubleshooting, and documentation.

See [AI_TOOL_DISCLOSURE.md](AI_TOOL_DISCLOSURE.md) for the disclosure. Before submission, complete its voice-over, music, and visual-asset statements accurately. If background music is present, credit the track and creator/source.

## Project Documents

- [Six-scene storyboard](Gaussian_Elimination_Storyboard.pdf)
- [AI and production tool disclosure](AI_TOOL_DISCLOSURE.md)

## Author

Atharva Jha

**Student ID:** [Add your student ID before submission]
