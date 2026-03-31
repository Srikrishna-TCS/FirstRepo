#!/usr/bin/env python3
"""Print the word 'Hello' inside an ASCII rectangle box.

This module provides a small helper `draw_box()` that constructs an
ASCII-art rectangle around a given text string and a `main()` entry
point that prints the box to stdout.
"""

import shutil
def draw_box(text, padding=1):
    """Return `text` surrounded by an ASCII rectangle.

    Args:
        text (str): The text to place inside the box.
        padding (int): Number of spaces to add on each side of the text.

    Returns:
        str: A multi-line string representing the ASCII box.
    """
    # width of the inner area (text + left/right padding)
    inner_width = len(text) + padding * 2

    # top and bottom borders use '+' and '-' characters
    top = "+" + "-" * inner_width + "+"

    # middle line contains the text with padding and vertical bars
    middle = "|" + " " * padding + text + " " * padding + "|"

    # join lines into a single multi-line string
    return "\n".join([top, middle, top])


def main():
    # Create the box containing the word "Hello" and center it
    box = draw_box("Hello")
    lines = box.splitlines()

    # get terminal size (columns, lines)
    term_size = shutil.get_terminal_size(fallback=(80, 24))
    term_width, term_height = term_size.columns, term_size.lines

    box_width = max(len(line) for line in lines)
    box_height = len(lines)

    # compute padding to center the box
    left_padding = max((term_width - box_width) // 2, 0)
    top_padding = max((term_height - box_height) // 2, 0)

    # print vertical padding, then each line with horizontal padding
    print("\n" * top_padding, end="")
    pad = " " * left_padding
    for line in lines:
        print(pad + line)


if __name__ == "__main__":
    main()
