cheese = 99

def func():
    global cheese
    cheese = 100
    print('Local cheese is: ', cheese)

def main():
    func()
    print('Global cheese is: ', cheese)

if __name__ == "__main__":
    main()