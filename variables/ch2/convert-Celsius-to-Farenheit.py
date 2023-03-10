tmp=1
while tmp!=0:
    tmp=input('Enter a temperature value in Celsius and I will convert it to Fahrenheit:(for Exit insert 0) ')
    # Check input value (int or float)
    if tmp.isnumeric():
        tmp=float(tmp)
        print('onvert it to Fahrenheit ',tmp,'is: ',(tmp*9/5)+32)
    else:
        print('Sorry ',tmp,'is not Number: ')
    # Accept Only number 