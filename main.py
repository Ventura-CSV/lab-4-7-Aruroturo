def main():
    numbers = []
    Fvalue = 0
    while True: 
        Value = int(input("Input number"))
        if Fvalue is 0 or Value < Fvalue:
            numbers.append(Value)
            Fvalue = Value
        else:
            break
       
   
   
   
   
    """
    ########################################
    Code Your Program here
    ########################################
    """

    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
