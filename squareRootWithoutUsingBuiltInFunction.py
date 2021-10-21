def my_custom_sqrt_func(arb_num):
    df= arb_num-(arb_num//1)
    if arb_num==0:
        return "{0:.15f}".format(0)
    if arb_num>0:
        if(df==0):
            for k in range(0,arb_num+1):
                if (k*k)==arb_num:
                    return "{0:.15f}".format(k)
                else:
                        my_first_var=0
                        square_root=arb_num/2
                        while True:
                            my_first_var=square_root
                            square_root=(my_first_var+(arb_num/my_first_var))/2
                            if square_root==my_first_var:
                                return  "{0:.15f}".format(square_root)
        elif(df>0):
             my_second_var=0
             square_root=arb_num/2
             while True:
                 my_second_var=square_root
                 square_root=(my_second_var+(arb_num/my_second_var))/2
                 if square_root==my_second_var:
                    return  "{0:.15f}".format(square_root)
             
    else:
        raise Exception("Invalid Square Root!")
        



#Calling the above function (the function called my_custom_sqrt_func) with different real numbers.

print(my_custom_sqrt_func(4))
        
print(my_custom_sqrt_func(5))

print(my_custom_sqrt_func(3.5))

print(my_custom_sqrt_func(50))

print(my_custom_sqrt_func(8.5))

print(my_custom_sqrt_func(5.15))

print(my_custom_sqrt_func(16))

print(my_custom_sqrt_func(0))

print(my_custom_sqrt_func(-1))

        