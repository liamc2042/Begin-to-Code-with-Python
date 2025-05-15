def func_2():
    i = 99

def func_1():
    i = 0
    func_2()
    print('The value of i is: ', i)

def main():
    func_1()

if __name__ == "__main__":
    main()