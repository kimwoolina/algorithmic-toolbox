import functools

def custom_compare(n1, n2):
    num1 = str(n1)
    num2 = str(n2)
    return int(num1 + num2) - int(num2 + num1)

def largest_number(numbers):
    sorted_numbers = sorted(numbers, key=functools.cmp_to_key(custom_compare), reverse=True)
    largest = "".join(map(str, sorted_numbers))
    return largest

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(largest_number(input_numbers))
    