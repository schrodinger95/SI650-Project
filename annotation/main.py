import csv

if __name__ == '__main__':
    with open('qrel.csv', 'w', newline='') as output:
        csvwriter = csv.writer(output, delimiter=',', quotechar='\"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['qid', 'docno', 'label'])
        for i in range(1, 31):
            path = "qrel/" + str(i) + ".csv"
            with open(path, newline='') as input:
                csvreader = csv.reader(input, delimiter=',', quotechar='\"')
                title = next(csvreader)
                for row in csvreader:
                    newrow = [row[4], row[0], row[3]]
                    csvwriter.writerow(newrow)


