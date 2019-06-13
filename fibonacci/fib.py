import matplotlib.pyplot as plt

def fib(n):
    x, y = 0, 1
    for _ in range(n):
        yield x
        x, y = y, x+y

def curve(fib_seq):
    plt.plot(fib_seq)
    plt.ylabel('fib value')
    plt.xlabel('n')
    plt.show()

if __name__ == "__main__":
    curve([i for i in fib(100)])