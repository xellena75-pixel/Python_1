def fizz_buzz(n):
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

if __name__ == "__main__":
    try:
        n_value = int(input("Введите число: "))
        fizz_buzz(n_value)
    except ValueError:
        print("Ошибка: введено некорректное число.")

