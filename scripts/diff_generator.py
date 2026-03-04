#!/usr/bin/env python3
"""
Compute a simple diff/changelog between two JSON objects.
"""
import json
import sys

def compute_changes(old: dict, new: dict) -> str:
    lines = []
    for key in new:
        if old.get(key) != new.get(key):
            lines.append(f"Changed {key}: {old.get(key)} -> {new.get(key)}")
    return "\n".join(lines)

if __name__ == '__main__':
    old = json.load(open(sys.argv[1]))
    new = json.load(open(sys.argv[2]))
    print(compute_changes(old, new))