import PyPDF2

with open('./dummy.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    #print(reader.numPages)
    #print(reader.getPage(0))
    pag = reader.getPage(0)
    pag.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(pag)
    with open('tilt.pdf','wb') as file2:
        writer.write(file2)