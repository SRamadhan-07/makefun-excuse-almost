"""Write the excuse entry to /output/entry.txt."""

import os

ENTRY_TEXT = (
    "Boss, gas engineer needs me home Thursday, mandatory mission, "
    "I mean inspection, can't reschedule for weeks, sorry"
)


def main():
    # The grader reads only /output/entry.txt; write the line verbatim,
    # with no trailing newline and nothing printed to stdout.
    os.makedirs("/output", exist_ok=True)
    output_path = os.path.join("/output", "entry.txt")
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
