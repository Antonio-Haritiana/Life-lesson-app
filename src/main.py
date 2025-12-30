from storage import LessonExtraction, save_lessons, modify_lessons
from lesson_manager import (
    get_random_lesson,
    create_lesson,
    mix_lessons,
    show_your_lessons,
)

DATA_PATH = "life_lesson_app\data\lessons.json"
CUSTOM_PATH = "life_lesson_app\data\custom_lessons.json"


def main_menu():
    """Display the user menu and handle choices."""
    while True:
        print("\n--- Life Lesson App ---")
        print("1. Show a random lesson")
        print("2. Add a new lesson")
        print("3. Show your created lessons")
        print("4. Modify your lesson")
        print("5. Delete your lesson")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        #  Variable used by all if cases
        custom_lessons = LessonExtraction(CUSTOM_PATH)
        your_created_lesson = custom_lessons.load_lessons()
        my_lesson = your_created_lesson["lessons"]

        if choice == "1":
            """Mix your lessons from the ones in the database"""
            base_lessons = LessonExtraction(DATA_PATH)
            basic_lesson = base_lessons.load_lessons()

            mixed = mix_lessons(basic_lesson, my_lesson)

            if not mixed:
                print("\nNo lessons available yet.")
            else:
                lesson = get_random_lesson(mixed)
                print("\n✨ Your mixed random life lesson:\n")
                print(f"Text: {lesson['text']}")
                print(f"Author: {lesson['author']}")
                print(f"Category: {lesson['category']}")
        elif choice == "2":
            # Create a new dict containning the new lesson
            new_lesson = create_lesson(my_lesson)
            # Append the new lesson to custom_lessons
            modify_lessons(new_lesson)
            # Now we have updated our custom_lessons with new_lesson, so we just write it back to JSON
            try:
                save_lessons(CUSTOM_PATH, your_created_lesson)
            except:
                raise Exception("Oops we haven't been able to save your lesson")
            else:
                print("\n✅ Your lesson has been saved!")
        elif choice == "3":
            """View all your created lessons only"""
            custom_lessons = load_lessons(CUSTOM_PATH)
            my_lesson = custom_lessons["lessons"]

            def has_lesson(my_lessons):
                return bool(my_lessons)

            if not has_lesson(my_lesson):
                print("You have no lessons yet")
                continue
            else:
                show_your_lessons(my_lesson)
        elif choice == "4":
            """Modify your created lesson"""
            print("Here are your created lessons to modify")
            custom_lessons = load_lessons(CUSTOM_PATH)
            my_lesson = custom_lessons["lessons"]
            show_your_lessons(my_lesson)
            lesson_to_modify = int(
                input("What do you want to modify? (enter your lesson number): ")
            )
            id = lesson_to_modify - 1
            if not lesson_to_modify:
                print("Please enter your lesson number")
            else:
                try:
                    lesson_number = my_lesson[id]["Lesson_number"]
                    text = input("Lesson text: ") or my_lesson[id]["text"]
                    author = input("Author (optional): ") or my_lesson[id]["author"]
                    category = (
                        input("Category (optional): ") or my_lesson[id]["category"]
                    )
                    my_lesson[id].update(
                        {
                            "Lesson_number": lesson_number,
                            "text": text,
                            "author": author,
                            "tags": [],
                            "category": category,
                            "notes": "",
                        }
                    )
                except:
                    raise Exception("What the hell is happening??")
                else:
                    save_lessons(CUSTOM_PATH, custom_lessons)
                    print("\n✅ Your lesson has been modified!")
        elif choice == "5":
            """Delete your created lesson"""
            print("Here are your created lessons to delete")
            custom_lessons = load_lessons(CUSTOM_PATH)
            my_lesson = custom_lessons["lessons"]

            def has_lesson(my_lessons):
                return bool(my_lessons)

            if not has_lesson(my_lesson):
                print("You have no lessons yet")
                continue
            else:
                show_your_lessons(my_lesson)

                lesson_to_modify = int(
                    input("What do you want to delete? (enter your lesson number): ")
                )
                id = lesson_to_modify - 1
                if not lesson_to_modify:
                    print("Please enter your lesson number")
                else:
                    try:
                        confirmation = input(
                            "Do you really want to delete this lesson? (yes/no): "
                        )
                        if confirmation == "yes":
                            my_lesson_after_delete = []
                            my_lesson.pop(id)
                            my_lesson_after_delete.extend(my_lesson)
                            my_lesson.clear()
                            for x in my_lesson_after_delete:
                                del x["Lesson_number"]
                            for i in my_lesson_after_delete:
                                new_id = len(my_lesson) + 1
                                less_numb = {"Lesson_number": new_id}
                                less_numb.update(i)
                                my_lesson.append(less_numb)

                        else:
                            print("Ok, we won't delete it!")
                    except:
                        raise Exception("What the hell is happening??")
                    else:
                        save_lessons(CUSTOM_PATH, custom_lessons)
                        print("\n✅ Your lesson has been deleted!")

        elif choice == "6":
            print("\nGoodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
