import PyPDF2

# pdf = open('travel.pdf','rb')
# pdfRd = PyPDF2.PdfFileReader(pdf)
# p1 = pdfRd.getPage(0)
# txt = p1.extractText()
# print(txt)
# print(pdfRd.isEncrypted)
# print(type(pdfRd))
# print(pdfRd.numPages)

pdfObj = open('travel.pdf','rb')
pdfRd = PyPDF2.PdfFileReader(pdfObj)

pdfWr = PyPDF2.PdfFileWriter()              # 新的PDF物件
for pageNum in range(pdfRd.numPages):
    pdfWr.addPage(pdfRd.getPage(pageNum))   # 一次將一頁放入新的PDF物件

pdfOutFile = open('out27_6.pdf', 'wb')      # 開啟二進位檔案供寫入
pdfWr.write(pdfOutFile)                     # 執行寫入
pdfOutFile.close()