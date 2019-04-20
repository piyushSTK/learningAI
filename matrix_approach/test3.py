import matplotlib.pyplot as plt

circle1 = plt.Circle((0, 0), 0.2,fill=False, color='r')
circle2 = plt.Circle((0.5, 0.5), 0.2,fill=False, color='blue')


fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

ax.add_artist(circle1)
ax.add_artist(circle2)
plt.axis('equal')
fig.savefig('plotcircles.png')
plt.show()
