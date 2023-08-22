##############################################################################
#   Program to extract meaningful data from the crime data PDF file provided #
#   Written by Sahil Hussain                                                 #
##############################################################################

import csv
import pdfplumber

pdf = pdfplumber.open("crime-data.pdf")

page = pdf.pages[0]
table = page.extract_table()

# converts the data read into a CSV that we can visualize
with open('crime-data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(table[0])
    for row in table[1:]:
        writer.writerow(row)

pdf.close()
