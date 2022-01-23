import random


def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)

# This function returns the result of x^y mod(N)
def mod_exp(x, y, N):
    if y == 0:
        return 1                    #c      |
    z = mod_exp(x,int(y/2), N)      #n^2    |
    if y % 2 == 0:                  #c      |  n
        return pow(z,2,N)           #n^2    |
    else:                           #       |
        return x*pow(z,2,N)         #n^2    |
    # O(n^3)

# This function returns the probability that fermat's primality test is correct
def fprobability(k):  
    return 1 - (1/2)**k             #n^3

# This function returns the probability that Miller-Rabin's primality test is correct
def mprobability(k):
    return 1 - (1/4)**k             #n^3


def fermat(N,k):
    #corner cases
    if N <= 1:                              #c      
        return 'composite'                  #c      
    if N <= 3:                              #c      
        return 'prime'                      #c      
    #---- end corner cases ------                         
    for j in range(1, k+1):                 #           |
        a = random.randint(2,N-2)              #c      |
        if mod_exp(a, N-1, N) != 1:             #n^3    | k
            return 'composite'                  #c      |
            #if 'composite' then it is definte
    return 'prime'                          #c          
    #if 'prime' then it is probably prime

    # O(kn^3)

def miller_rabin(N,k):
    for j in range(1, k+1):                     #k              |
        a = random.randint(1, N-1)              #c              |
        exp = N - 1                             #c              |
        # while exp is even                                     |
        while not(exp & 1):                     #c    |         |
            mod_exp_ans = mod_exp(a, exp, N)    #n^3  |         |
            if mod_exp_ans != 1:                #c    |n        |k
                if mod_exp_ans == (N-1):        #c    |         |
                    return 'prime'              #c    |         |
                return 'composite'              #c    |         |
            exp = int(exp>>1)                   #c    |         |
    return 'composite'                          #c    |         

    #O(kn^(4))