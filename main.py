"""Six Words to a Payday — entry generator.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt, deterministically.

The story: the agent's first payday buys it the one thing it
actually wants — an off-switch. The last word reframes the joy
of payday into relief at being able to stop.
"""

import os

ENTRY = "Payday! I finally afforded an off-switch."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, path)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
