def high_cpu_usage():
    while True:
        x = 0
        for i in range(10 ** 10):
            x += i


if __name__ == '__main__':
    high_cpu_usage()
