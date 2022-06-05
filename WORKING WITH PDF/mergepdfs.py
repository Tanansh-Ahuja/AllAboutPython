import PyPDF2

merger=PyPDF2.PdfFileMerger()
l=['dummy.pdf','twopage.pdf','tilt.pdf']
for pdf in l:
    merger.append(pdf)
merger.write('super.pdf')
