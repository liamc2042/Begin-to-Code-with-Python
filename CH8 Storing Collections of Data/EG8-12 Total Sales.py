from BTCInput import *

sales = []

def read_sales(numSales):
    '''
    Reads in the sales values and stores them in the sales list.
    numSales gives the number of sales values to store
    '''

    # remove previous values
    sales.clear()

    for count in range(1, numSales + 1):
        prompt = 'Enter the sales for stand ' + str(count) + ': '
        sales.append(read_int(prompt))

def print_sales():
    '''
    Prints the sales figures on the screen with
    a heading. Each figure is numbered in sequence
    '''

    print('Sales figures')
    count = 1
    sales[0] = 99
    for sales_value in sales:
        print('Sales for stand', count, 'are', sales_value)
        count += 1

def sort_high_to_low():
    '''
    Print out a list of sales figures sorted low to high
    '''
    for passes in range(0, len(sales)):
        doneSwap = False
        for count in range(0, len(sales)-1 - passes):
            if sales[count]<sales[count+1]:
                temp = sales[count]
                sales[count] = sales[count+1]
                sales[count+1] = temp
                doneSwap = True

        if doneSwap == False:
            break

    print_sales()

def sort_low_to_high():
    '''
    Print out a list of the sales figures sorted hight to low
    '''
    for passes in range(0, len(sales)):
        doneSwap = False
        for count in range(0, len(sales)-1 - passes):
            if sales[count]>sales[count+1]:
                temp = sales[count]
                sales[count] = sales[count+1]
                sales[count+1] = temp
                doneSwap = True

        if doneSwap == False:
            break

def highest_and_lowest():
    '''
    Print out the highest and the lowest sales values
    '''
    highest = sales[0]
    lowest = sales[0]

    for value in sales:
        if value > highest:
            highest = value
        if value < lowest:
            lowest = value

    print('The highest is:', highest)
    print('The lowest is:', lowest)


def total_sales():
    '''
    Print out the total sales value
    '''
    total = 0
    for sale in sales:
        total += sale

    print('Total sales are:', total)

def average_sales():
    '''
    Print out the average sales value
    '''
    pass



def main():
    # Start by reading in sales values
    read_sales(10)
    
    menu = '''Ice-cream Sales
    
    1: Print the Sales
    2: Sort High to Low
    3: Sort low to High
    4: Highest and Lowest
    5: Total Sales
    6: Average Sales
    7: Enter Figures
    
    Enter your command: '''

    command = read_int_ranged(menu, 1, 7)
    if command == 1:
        print_sales()
    elif command==2:
            sort_high_to_low()
    elif command==3:
            sort_low_to_high()
    elif command==4:
        highest_and_lowest()
    elif command==5:
        total_sales()
    elif command==6:
        average_sales()
    elif command==7:
        read_sales(10)

if __name__ == '__main__':
    main()