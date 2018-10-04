import numpy as np
import matplotlib.pyplot as plt

def p(x):
    return np.exp(-x**2)
    
#let's plot it
x = np.linspace(-3,3,100)
y = p(x)

print("I'm about to plot!")

plt.plot(x,y)
plt.show()
