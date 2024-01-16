import numpy as np

"""
The following two lines of code, if uncommented, would generate a binomial distribution of 500 trials
where each trial is a coin flip (n=1) with a probability of success (getting heads) of 0.8
Then it would print the results of the above binomial distribution
"""
# coin_binomial = np.random.binomial(n=1, p=0.8, size=500)
# print(coin_binomial)

"""
This line generates a binomial distribution of 500 trials, where each trial consists of 100 coin flips (n=100)
with a probability of success (getting heads) of 0.8
Then it prints the results of the binomial distribution
"""
coin_binomial = np.random.binomial(n=100, p=0.8, size=500) 
print(coin_binomial)