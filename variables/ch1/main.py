continues = 'y'
while continues=='y':
    continues = input('Do you continue?(y/n)')
    num=input('Insert an integer: ')
    # Check input value 
    if num.isdigit():
        num=int(num)
        print('Double ',num,'is: ',2*num)
    else:
        print(' ',num,'is not integer: ')
    # Accept Only integer number 

