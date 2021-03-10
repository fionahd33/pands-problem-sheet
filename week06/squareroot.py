# Write a program yhat takes a positive floating - point number as input and outputs an approx of its square root
# Do not use built in functions x**.5 or math.sqrt()
# Author: Fiona Healy Donnelly
# https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
# https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html

numberToEnter = float(input("Please enter a positive number:"))
print(numberToEnter)
def newton_method(number, number_iters = 500):
    a = float(number) # number to get square root of
    for i in range(number_iters): # iteration number
        number = 0.5 * (number + a / number) # update
    return number

numberToSqr = newton_method(numberToEnter)
print("The square root of {} is {}".format(numberToEnter,numberToSqr))
