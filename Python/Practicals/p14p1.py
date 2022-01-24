import timeit
import sys

def time(name, function):
    count = 10000
    total = timeit.timeit(function, number=count)
    avg_time = total/count
    print(f"{name}: {avg_time:02f}s")

def test(number):

    def start_recursion():
        return recursive(number)

    def recursive(n: int):
        if n == 0:
            return 1
        else:
            return n * recursive(n - 1)

    def iterative():
        answer = 1
        for i in range(1, number+1):
            answer *= i
        return answer

    print(f"==== input: {number} ====")
    time("recursive", start_recursion)
    time("iterative", iterative)

print("=========")

X = [1, 10, 50, 100, 500, 978]
for x in X:
    test(x)


