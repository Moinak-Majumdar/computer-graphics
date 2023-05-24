import matplotlib.pyplot as plt

coord = [[1,1], [8,1], [8,6], [1,6]]
coord.append(coord[0]) #repeat the first point to create a 'closed loop'

xs, ys = zip(*coord) #create lists of x and y values

plt.plot(xs,ys)
plt.show()