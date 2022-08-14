import csv
def getCSVdata(filename):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    dataFile = open(filename,"r")
    # create a CSV reader from csv file
    reader = csv.reader(dataFile)
    #skip the header
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
