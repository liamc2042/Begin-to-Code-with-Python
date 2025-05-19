def main():
    input_file=open('test.txt','r')
    total_file=input_file.read()
    print(total_file)
    input_file.close()

if __name__ == '__main':
    main()