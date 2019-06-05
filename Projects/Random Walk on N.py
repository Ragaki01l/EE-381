#Program to Simulate a Random Walk on N

p = float(input("Enter the probability of a right step"))
S = int(input("Enter a starting position. "))
N = int(input("Enter the right boundary. "))
Jump = int(input("Enter the number of steps. "))

import random

for i in range(Jump):

	if S == 0:
        S = 1
    elif S == N:
        S = N - 1
    elif((S < N) & (S > 0)):
        
        r = random.uniform(0, 1)
        
        if r < p:
            S = S + 1
        else:
            S = S - 1
    print(S)
