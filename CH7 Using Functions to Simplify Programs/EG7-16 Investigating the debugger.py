def increment_function(inputVal):
    result = inputVal + 1
    return result

def main():
    x = 99
    y = increment_function(x)
    print('The answer is:', y)

if __name__ == '__main__':
    main()