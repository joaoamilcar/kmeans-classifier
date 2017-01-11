import csv


def parse_to_array(filename):
    dataset = []

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            dataset.append(row)

    # convert str to float
    for row in dataset:
        for position in range(len(row) - 1):
            row[position] = float(row[position])

    return dataset
