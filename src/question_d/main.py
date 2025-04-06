from question_d import get_person_category

def main():
    while True:
        user_input = input("Enter a person's age (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        age = int(user_input)
        category = get_person_category(age)
        print(f"Category: {category}\n")

if __name__ == "__main__":
    main()
