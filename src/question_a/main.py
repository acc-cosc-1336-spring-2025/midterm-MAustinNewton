from question_a import use_local_variable

def main():
    num = 100
    use_local_variable(num)
    print(f"Outside function, num = {num}")

if __name__ == "__main__":
    main()
