

def fibo(n: int):
    if (n <= 1):
        return n
    else:
        return fibo(n-1) + fibo(n-2)


hasil = fibo(2)

# print(hasil)


arr = [3, 9, 2, 7, 5, [1, 2]]
# print(findMax(arr, 0, len(arr) - 1))
# print(len(arr) - 1)


def print_nested_array(arr):
    for item in arr:
        if isinstance(item, list):
            print_nested_array(item)
        elif isinstance(item, int):
            print(item, end=", ")


# Example usage:
my_array = [1, 2, [3, 4]]
print_nested_array(arr)
