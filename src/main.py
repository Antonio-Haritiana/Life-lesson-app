from storage import LessonExtraction, save_lessons, modify_lessons
from lesson_manager import (
    get_random_lesson,
    create_lesson,
    mix_lessons,
    view_your_lesson,
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

        #  Variable used by most of if cases
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
            """Add a new lesson"""
            # Create a new dict containning the new lesson
            new_lesson = create_lesson(my_lesson)
            # Append the new lesson to custom_lessons
            modify_lessons(new_lesson)
            # Now we have updated our custom_lessons with new_lesson, so we just write it back to JSON
            try:
                save_lessons(CUSTOM_PATH, your_created_lesson)
                print("\n✅ Your lesson has been saved!")
            except:
                raise Exception("Oops we haven't been able to save your lesson")

        elif choice == "3":
            """View all your created lessons only"""

            view_your_lesson(my_lesson)

        elif choice == "4":
            """Modify your created lesson"""

            print("Here are your created lessons to modify")

            if not view_your_lesson(my_lesson):
                continue
            else:

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
                        save_lessons(CUSTOM_PATH, your_created_lesson)
                        print("\n✅ Your lesson has been modified!")
                    except:
                        raise Exception("Ohhh, an error occured!")

        elif choice == "5":
            """Delete your created lesson"""

            print("Here are your created lessons to delete")

            if not view_your_lesson(my_lesson):
                continue
            else:

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
                            for content in my_lesson_after_delete:
                                del content["Lesson_number"]
                                new_id = len(my_lesson) + 1
                                less_numb = {"Lesson_number": new_id}
                                less_numb.update(content)
                                my_lesson.append(less_numb)
                            print("\n✅ Your lesson has been deleted!")
                            save_lessons(CUSTOM_PATH, your_created_lesson)
                        elif confirmation == "no":
                            print("We won't delete it then 😊")
                        else:
                            print("Please enter yes or no!")
                    except:
                        raise Exception("We are sorry, something went wrong")

        elif choice == "6":
            """Exit the program"""

            print("\nGoodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
