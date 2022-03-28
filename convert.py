import csv

with open('documents.csv', 'r', newline='') as file, open('tourist_attractions.csv', 'r', newline='') as iFile, open(
        'final_documents.csv', 'w', newline='') as oFile:
    csvref = csv.reader(file, delimiter=',', quotechar='"')
    csvreader = csv.reader(iFile, delimiter=',', quotechar='"')
    csvwriter = csv.writer(oFile, delimiter=',', quotechar='"')
    header = next(csvref)
    tmp = next(csvreader)
    csvwriter.writerow(header)

    i = 1
    for row in csvreader:
        if len(row) > 5:
            newRow = [i, row[5], row[0], row[4], row[1], row[6], row[7], row[2], row[3]]
            for j in range(8, 19):
                if len(row) > j:
                    newRow += [row[j]]
            csvwriter.writerow(newRow)
            i += 1
