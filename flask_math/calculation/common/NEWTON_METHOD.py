def NEWTON_METHOD(number):
    number = float(number)
    ε = 10**-10

    num_old = number
    num_new = number/2
    while abs(1-num_old/num_new) > ε:
        num_old = num_new
        num_new = (num_old+number/num_old)/2
    return num_new
