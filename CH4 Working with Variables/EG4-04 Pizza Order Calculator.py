import time

def main():
    
    numStudents = int(input('How many students: '))

    numPizza = int(numStudents/1.5)

    print('You will need', numPizza, 'pizzas')

if __name__ == "__main__":
    main()