import math
number_list = []
pi = math.pi

def addition(x,y):
  Verbose = True
  while Verbose == True:
    try:
      x = float(input("Enter first number: "))
      y = float(input("Enter second number: "))
      return x + y
    except ValueError:
      return x + pi
      number_list.append(addition(x,y))

(addition(x,y))

if __name__ == '__main__':

    addition(5, 12, Verbose=True)
