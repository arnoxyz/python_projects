
"""
Seven-segment display generator.

Each segment is labeled A to G:

 __A__
|     |
F     B
|__G__|
|     |
E     C
|__D__|

Example digits:
 __       __   __        __   __  __   __   __
|  |   |  __|  __| |__| |__  |__    | |__| |__|
|__|   | |__   __|    |  __| |__|   | |__|  __|
"""

DIGITS = {
    '0': [" __ ",
          "|  |",
          "|__|"],

    '1': ["    ",
          "   |",
          "   |"],

    '2': [" __ ",
          " __|",
          "|__ "],

    '3': [" __ ",
          " __|",
          " __|"],

    '4': ["    ",
          "|__|",
          "   |"],

    '5': [" __ ",
          "|__ ",
          " __|"],

    '6': [" __ ",
          "|__ ",
          "|__|"],

    '7': [" __ ",
          "   |",
          "   |"],

    '8': [" __ ",
          "|__|",
          "|__|"],

    '9': [" __ ",
          "|__|",
          " __|"],

    '-': ["    ",
          " __ ",
          "    "],

    '.': [" ",
          " ",
          "."],
}


def get_ssd_str(number, display_width=0):
    number = str(number).zfill(display_width)
    rows = ["", "", ""]

    for i, ch in enumerate(number):
        if ch not in DIGITS:
            raise ValueError(f"Unsupported character: {ch}")

        pattern = DIGITS[ch]
        for r in range(3):
            rows[r] += pattern[r]

        # add spacing between digits
        if i != len(number) - 1:
            for r in range(3):
                rows[r] += " "

    return "\n".join(rows)
