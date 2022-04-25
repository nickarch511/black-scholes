import sys
import scipy
from scipy.stats import norm as pnorm
import math

'''
This is a one-file command-line program that computes the Black-Scholes' no-arbitrage
cost of a call option for the given parameters:
s - the current price of the security
t - the time (as a fraction of a year) until the expiration
K - the strike price of the call
sigma - the volatility of the secruity
r - the continuously-compounded interest rate
'''

def black_scholes(s,t,K,sigma,r):
    w = (r*t - sigma**2*t/2 - math.log(K/s))/(sigma*t**(1/2))
    c = s*pnorm.cdf(w) - K*math.e**(-r*t)*pnorm.cdf(w-sigma*t**(1/2))
    print("\n\nFor correct answers, ensure your args are in this order: s,t,K,sigma,r")
    print("The no-arbitrage cost of the call option is {}".format(c))
    print("The number of shares to sell for delta-hedging is {}\n\n".format(pnorm.cdf(w)))



if __name__ == '__main__':
    try:
        args = [float(i) for i in sys.argv[1::]]
        black_scholes(*args)
    except Exception as e: 
        print(e)
        print("\n\nFor correct answers, ensure your args are in this order: s,t,K,sigma,r")
        print("The arguments you passed in were {} and the above error was thrown\n\n".format(sys.argv))