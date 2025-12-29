import json
import os


def load_lessons(filepath):
    """Load lessons from a JSON file."""
    if not os.path.exists(filepath):
        return []  # If file missing, return empty list, no crash

    with open(filepath, "r", encoding="utf-8") as f:
        """ "Convert from Json to python"""
        global data
        data = json.load(f)
        return data


def modify_lessons(lessons):
    data["lessons"].append(lessons)


def save_lessons(filepath, lessons):
    """Save lessons to a JSON file."""
    with open(filepath, "w", encoding="utf-8") as f:
        """ "Convert from Python to Json"""
        json.dump(lessons, f, indent=4, ensure_ascii=False)
