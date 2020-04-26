# 4.1 Знакомсто с pyplot
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

fig = plt.figure()

plt.axis([0, 30, -1.5, 1.5])

plt.xlabel("x")
plt.ylabel("sin(x)")

xs = []
sin_vals = []

x = 0.0
while x < 30.0:
    sin_vals.append(math.sin(x))
    xs.append(x)
    x += 0.01

plt.plot(xs, sin_vals)

fig.show()
fig.savefig("sin.png")


dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.axis([0, 10, -1.5, 1.5])

plt.title('Sine & Cosine')
plt.xlabel('x')
plt.ylabel('F(x)')

xs = []
sin_vals = []
cos_vals = []

x = 0.0
while x < 10.0:
    sin_vals += [ math.sin(3 * x) ]
    cos_vals += [ math.cos(x) ]
    xs += [x]
    x += 0.1

plt.plot(xs, sin_vals, color = 'blue', linestyle = 'solid',
         label = 'sin(3x)')
plt.plot(xs, cos_vals, color = 'red', linestyle = 'dashed',
         label = 'cos(x)')

plt.legend(loc = 'upper right')
fig.show()
fig.savefig('trigan.png')
