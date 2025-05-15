def m2():
    print('the')

def m3():
    print('sat on')
    m2()

def m1():
    m2()
    print('cat')
    m3()
    print('mat')

def main():
    m1()

if __name__ == "__main__":
    main()