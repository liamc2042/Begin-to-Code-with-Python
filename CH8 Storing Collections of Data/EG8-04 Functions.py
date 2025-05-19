from BTCInput import *

sales=[]

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

def main():
    read_sales(10)
    print_sales()

if __name__ == '__main__':
    main()