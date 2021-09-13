
def fib2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)

def fib(n):
    if n == 1 or n == 2:
        print(1)
        if n == 2:
            print(1)
        return 1

    else:
        answer = fib(n-1) + fib2(n-2)
        print(answer)
        return answer

#fib(10)

def fib3(n):
    if n == 1:
        print(1)
        return [1]
    elif n == 2:
        print(1)
        print(1)
        return [1,1]
    else:
        current = fib3(n - 1)
        current.append(current[-2] + current[-1])
        print(current[-1])
        return current

fib3(10)