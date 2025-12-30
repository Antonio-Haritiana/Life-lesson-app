import json
import os


class LessonExtraction:
    """Retrieve a lesson from a Json file"""

    def __init__(self, filepath):
        self.filepath = filepath

    def load_lessons(self):
        """Load lessons from a JSON file."""
        if not os.path.exists(self.filepath):
            return []  # If file missing, return empty list, no crash

        with open(self.filepath, "r", encoding="utf-8") as f:
            """ "Convert from Json to python"""
            global data
            data = json.load(f)
            return data

    def get_lessons(self):
        """Get the lesson after Json loads it"""
        custom_lessons = self.load_lessons()
        my_lesson = custom_lessons["lessons"]
        return my_lesson


def modify_lessons(lessons):
    """Modify a lesson"""
    data["lessons"].append(lessons)


def save_lessons(filepath, lessons):
    """Save lessons to a JSON file."""
    with open(filepath, "w", encoding="utf-8") as f:
        """ "Convert from Python to Json"""
        json.dump(lessons, f, indent=4, ensure_ascii=False)
