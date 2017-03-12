# takes user input and calculates compound interest.
# equation A = P(1 + (r/n))^nt
# P is the principal ammount
# r is the annual rate of interest
# t is the number of years the ammount is invested
# n is the number of times the interest compounded per years
# A is the ammount at the end of the investment.

from __future__ import division

P = int(input("What is the principal ammount? "))
r = float(input("What is the APR? "))
t = int(input("Number of years to be invested? "))
n = int(input("How many times is the interest compounded per year? "))

# formatt r. I.E r input of 4 is formatted to 0.04
r_formatted = r / 100

A = P * (1 + (r_formatted/n))**(n*t)
# formatt A to stop at the hundreth place
A_formatted = ("%.2f" % A)

print("{} invested at {}% \ffor {} years compounded {} times per year is {}".format(P, r_formatted, t, n, A_formatted))
