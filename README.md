# Hello Box Python Script

This repository contains a minimal Python script that prints the word "Hello" inside an ASCII rectangle box.

Files
- [hello.py](hello.py): The Python script that draws and prints the ASCII box around the word "Hello".

Requirements
- Python 3.x

Run
```bash
python3 hello.py
```

Sample output
```
+-------+
| Hello |
+-------+
```

Description
- `hello.py` provides a `draw_box(text, padding=1)` helper which builds an ASCII box sized to the text, and a `main()` entrypoint which prints the box when the script is executed directly.

Comments
- The code includes docstrings and inline comments explaining how the box is constructed.
