from question_b import get_fahrenheit

def main():
    print(f"{'Celsius':>10} | {'Fahrenheit':>10}")
    print("-" * 25)
    for celsius in range(0, 21):
        fahrenheit = get_fahrenheit(celsius)
        print(f"{celsius:>10} | {fahrenheit:>10.1f}")

if __name__ == "__main__":
    main()
