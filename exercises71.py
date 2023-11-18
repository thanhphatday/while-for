# Write a program that implements Newton’s method to compute and display the square
# root of a number entered by the user. The algorithm for Newton’s method follows:
# Read x from the user
# Initialize guess to x/2
x=int(input('x='))
guess=x/2
while abs(guess*guess-x)>10**(-12):
    guess=(guess+x/guess)/2
print('The square root of',x,'=',guess)
