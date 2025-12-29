import random


def get_random_lesson(lessons):
    """Return one random life lesson from the list."""
    if not lessons:
        return None  # no lessons available
    return random.choice(lessons)


def create_lesson(your_lessons_path):
    """Ask the user to enter a new lesson."""
    print("\n📝 Create your own life lesson:")
    id = (
        len(your_lessons_path) + 1
    )  ## len anle lessons list ao @ json file, si empty len() = 0
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


def mix_lessons(base_lessons, custom_lessons):
    """Combine database lessons and custom lessons."""
    return base_lessons + custom_lessons


def show_your_lessons(my_lessons):
    for lesson in my_lessons:
        # the value in the list is a dictionary
        print("\n✨ Your life lesson:\n")
        print(f"Lesson_number:{lesson['Lesson_number']}")
        print(f"Text: {lesson['text']}")
        print(f"Author: {lesson['author']}")
        print(f"Category: {lesson['category']}")
