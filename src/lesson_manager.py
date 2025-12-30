import random


def get_random_lesson(lessons):
    """Return one random life lesson from the list."""
    if not lessons:
        return None  # no lessons available
    return random.choice(lessons)


def mix_lessons(base_lessons, custom_lessons):
    """Combine database lessons and custom lessons."""
    return base_lessons + custom_lessons


def create_lesson(your_lessons_path):
    """Ask the user to enter a new lesson."""
    print("\n📝 Create your own life lesson:")
    id = (
        len(your_lessons_path) + 1
    )  ## len lessons list in json file, if empty len() = 0
    text = input("Lesson text: ")
    author = input("Author (optional): ") or "Unknown"
    category = input("Category (optional): ") or "Personal"

    return {
        "Lesson_number": id,
        "text": text,
        "author": author,
        "tags": [],
        "category": category,
        "notes": "",
    }


class LessonChecker:
    """Check the existance of a lesson"""

    def __init__(self, my_lessons):
        self.my_lessons = my_lessons

    def has_lesson(self):
        return bool(self.my_lessons)

    def show_your_lessons(self):
        """Show your created lessons"""

        for lesson in self.my_lessons:
            # the value in the list is a dictionary
            print("\n✨ Your life lesson:\n")
            print(f"Lesson_number:{lesson['Lesson_number']}")
            print(f"Text: {lesson['text']}")
            print(f"Author: {lesson['author']}")
            print(f"Category: {lesson['category']}")

    def display_status(self):
        if self.has_lesson():
            self.show_your_lessons()
        else:
            print("You have no lessons yet")


def view_lesson(my_lesson):
    checker = LessonChecker(my_lesson)
    return checker.display_status()
