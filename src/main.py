from src.customcsv import parse_to_array
from src.classifier import KMEANS

dataset = parse_to_array('iris.data')
classifier = KMEANS(dataset, 4)

classifier.run()
print('')
print('======= Result =======')
print('Centroids:', classifier.centroids)
print('Clusters: ', sorted(classifier.clusters.items()))