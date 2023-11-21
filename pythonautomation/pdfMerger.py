import PyPDF2 #importing
import sys
import os

merger = PyPDF2.PdfMerger()  #creating object 

for file in os.listdir(os.curdir): #in the current directory
    if file.endswith(".pdf"):  #checks if the file ends with .pdf extension
        merger.append(file)  #appends files in a single pdf

merger.write("combinedPDF.pdf") #names the pdf file "combinedPDF.pdf"
merger.close()  
