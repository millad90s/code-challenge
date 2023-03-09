num=1
while num!=0:
    num=input('Insert an integer:(for Exit insert 0) ')
    # Check input value 
    if num.isdigit():
        num=int(num)
        print('Double ',num,'is: ',2*num)
    else:
        print(' ',num,'is not integer: ')
    # Accept Only integer number 

