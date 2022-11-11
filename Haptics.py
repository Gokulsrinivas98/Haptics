# -----------------------------------------------------------------------------
#   Naive polygon generation algorithm
# -----------------------------------------------------------------------------

from src.Edge import Edge
from src.Polygon import Polygon
from src.Math import quickhull
import sys
import matplotlib.pyplot as plt
import time
import random

def create():
    n = int(input("Number of vertices: "))
    points = []
    for i in range(n):
        x = random.random()
        y = random.random()
        points.append([x,y])
    # start timer
    start = time.time()

    # initialize the polygon as a convex hull of the points
    polygon = Polygon(quickhull(points))

    # update points set to exclude polygon vertices
    points = [x for x in points if x not in polygon.vertices]

    # while the list of available points is not empty
    while points:
        # get the closest point and removing edge
        (e, point) = polygon.findClosest(points)
        # find the index to insert the vertex and edges in
        i = polygon.edges.index(e)
        polygon.vertices.insert(i + 1, point)
        polygon.edges[i] = Edge(e.start, point)
        polygon.edges.insert(i + 1, Edge(point, e.end))
        # remove newly added vertex from
        points.remove(point)

    # plot the polygon
    pset = polygon.vertices
    pset.append(pset[0])
    xs, ys = zip(*pset)
    plt.plot(xs, ys)
    plt.show()

def main(args = None):
    create()


if __name__ == "__main__":
    main()