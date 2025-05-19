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
    pass

def sort_low_to_high():
    '''
    Print out a list of the sales figures sorted hight to low
    '''
    pass

def highest_and_lowest():
    '''
    Print out the highest and the lowest sales values
    '''
    pass


def total_sales():
    '''
    Print out the total sales value
    '''
    pass

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

    else: 
        if command==2:
            sort_high_to_low()
        else:
            if command==3:
                sort_low_to_high()
            else:
                if command==4:
                    highest_and_lowest()
                else:
                    if command==5:
                        total_sales()
                    else:
                        if command==6:
                            average_sales()
                        else:
                            if command==7:
                                read_sales(10)

if __name__ == '__main__':
    main()