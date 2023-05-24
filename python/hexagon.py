import matplotlib.pyplot as plt

coord = [[0,7], [4,0], [12,0], [16,7],[12,14],[4,14]]
coord.append(coord[0]) #repeat the first point to create a 'closed loop'

xs, ys = zip(*coord) #create lists of x and y values

plt.plot(xs,ys)
plt.show()