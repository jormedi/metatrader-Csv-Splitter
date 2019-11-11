import csv, os, sys

headerRow =  ['<DATE>','<TIME>','<BID>','<ASK>','<LAST>','<VOLUME>']
fileHeader = 'EURUSD.'

def getFileHeader():
    files = os.listdir()
    print(files)
    sys.exit()
    files = [ fi for fi in files if fi.endswith(".csv")]
    return files

def writeFile(data, headerRow, result):

     with open(data+'.csv', mode="w") as csvfile:

        spamwriter = csv.writer(csvfile, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(headerRow)

        for line in result:
            spamwriter.writerow(line)

     return


def workFlow(fileHeader, fileName):
    iteration = 0

    result = []

    #headerRow = []

    with open(fileName, "rt") as csvfile:

     spamreader = csv.reader(csvfile, delimiter='\t', quotechar=' ')

     for row in spamreader:
         #Limpia las "" del principio y el final
         row[0] = row[0].replace('"','')
         row[-1] = row[-1].replace('"','')

         if (iteration < 2):

             iteration+=1

             if (iteration == 1):

                 continue

             data = row[0]

             result.append(row)

             continue

         elif (row[0] != data):
             print("Generando dia "+data)
             writeFile(fileHeader+data, headerRow, result)

             result = []

             result.append(row)

             data = row[0]

         else:

             result.append(row)
     print("Generando dia "+data)
     writeFile(fileHeader+data, headerRow, result)
    return

def _main():
    files = getFileHeader()

    for file in files:
        fileHeader = file.split('_')[0]
        print("::DIVISA "+fileHeader+"::")
        fileHeader = fileHeader+'.'
        workFlow(fileHeader, file)


# -------------------------------------------------------------------------------------

if __name__ == "__main__":

    _main()
