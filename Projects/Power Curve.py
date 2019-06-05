'''
 Program to make the power curve.
A plot of p verses 1 - Beta
Name: William Jorgensen
ID: 014721822
Date: 4/22/19

'''
import matplotlib.pyplot as power

p = [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00]

#The Beta values corresponding to the p values above

Beta = [0.8923, 0.7910, 0.6448, 0.4657, 0.2825, 0.1327, 0.0423, 0.0064, 0.0002, 0.0]

b = []
for i in Beta:
	b.append(1 - i)

power.plot(p,b)
power.xlabel("P values")
power.ylabel("1 - Beta")
power.title("Power Curve")

power.show()