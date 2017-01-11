from src.metrics import distance_euclid
import random


def records_average(records, precision):
    average = [0] * (len(records[0]) - 1) # initialize list and reduce its size to a centroid's

    for r in records:
        for position in range(len(r) - 1):
            average[position] = average[position] + r[position]

    for position in range(len(average)):
        average[position] = round(average[position] / len(records), precision)

    return average


def is_different(dict1, dict2):
    different = False

    for key, value in dict1.items():
        value2 = dict2.get(key)

        if len([i for i, j in zip(value, value2) if i == j]) != len(value):
            different = True
            break

    return different


class KMEANS:
    def __init__(self, dataset, k):
        self.dataset = dataset
        self.k = k # number of clusters, partitions or classes
        self.centroids = {}
        self.clusters = {} # partitions or classes
        self.convergence = True  # centroids are destabilized. thus, making records moving between clusters
        self.iteration = 0

    def run(self):
        self.initialize_centroids()

        while self.convergence:
            self.iteration += 1
            self.assign_records_to_centroids()
            self.view()
            self.update_centroids()

    # TODO improve this method (Lloyd's heuristic)
    def initialize_centroids(self):
        count = 1
        s = random.sample(self.dataset, self.k)  # pick 'k' centroids without replacement

        for record in s:
            self.centroids[count] = record[:len(record) - 1]
            count += 1

    def assign_records_to_centroids(self):
        self.clusters.clear()

        for record in self.dataset:
            centroidKey = self.get_closest_centroid_key(record)

            # first assignment
            if centroidKey not in self.clusters:
                self.clusters[centroidKey] = []

            newClusterValue = self.clusters.get(centroidKey)
            newClusterValue.append(record)
            newCluster = {centroidKey: newClusterValue}

            self.clusters.update(newCluster)

    def get_closest_centroid_key(self, record):
        centroidKey = None
        shortestDistance = -1

        for key, value in self.centroids.items():
            distance = distance_euclid(value, record)

            # TODO case when record is equidistant from two or more centroids
            if distance < shortestDistance or shortestDistance == -1:
                shortestDistance = distance
                centroidKey = key

        return centroidKey

    def update_centroids(self):
        newCentroids = {}

        for key, value in self.clusters.items():
            newCentroids[key] = records_average(value, 1)

        self.convergence = is_different(self.centroids, newCentroids)

        if self.convergence:
            self.centroids.update(newCentroids)

    def view(self):
        print('Iteration #', self.iteration)
        print('Centroids:', self.centroids)
        print('Clusters :', sorted(self.clusters.items()))
