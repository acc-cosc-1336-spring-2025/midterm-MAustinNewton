from question_c import get_sum_of_evens

def main():
    while True:
        user_input = input("Enter a number to sum even numbers up to (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        if not user_input.isdigit():
            print("Please enter a valid positive integer.")
            continue

        num = int(user_input)
        total = get_sum_of_evens(num)
        print(f"Sum of even numbers up to {num} is {total}\n")

if __name__ == "__main__":
    main()