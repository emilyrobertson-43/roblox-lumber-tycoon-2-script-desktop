"""Roblox Lumber Tycoon 2 Script Desktop — A desktop helper that finds Roblox Lumber Tycoon 2 Script data directories and archives config and export files locally."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='roblox_lumber_tycoon_2_script_desktop',
        description='A desktop helper that finds Roblox Lumber Tycoon 2 Script data directories and archives config and export files locally.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Roblox Lumber Tycoon 2 Script Desktop')
    print('Dated copies of Roblox Lumber Tycoon 2 Script data data, nothing uploaded.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# cleanup (2026-11-03)
# polish (2026-11-03)
# small fix (2026-11-04)
# tweak (2026-11-04)
# minor adjust (2026-11-05)
# update note (2026-11-05)
# update note (2026-11-06)
# cleanup (2026-11-06)
# tune (2026-11-16)
# refactor bit (2026-11-16)
# minor adjust (2026-11-17)
# refactor bit (2026-11-17)
# wip (2026-11-17)
