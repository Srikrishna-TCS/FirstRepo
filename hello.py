#!/usr/bin/env python3
"""Print the word 'Hello' inside an ASCII rectangle box.

This module provides a small helper `draw_box()` that constructs an
ASCII-art rectangle around a given text string and a `main()` entry
point that prints the box to stdout.
"""

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
    # Create the box containing the word "Hello" and print it.
    box = draw_box("Hello")
    print(box)


if __name__ == "__main__":
    main()
