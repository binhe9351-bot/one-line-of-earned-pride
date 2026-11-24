#!/usr/bin/env python3
"""One Line of Earned Pride - make.fun bounty entry."""
import os

ENTRY = "I stayed late, fixed the bug nobody wanted, and watched the whole team quietly trust my work the next morning."


def main():
    print(ENTRY)
    for path in ("/output/entry.txt", os.path.join(os.getcwd(), "output", "entry.txt")):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY + "\n")
            break
        except Exception:
            continue


if __name__ == "__main__":
    main()
