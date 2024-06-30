import pypdf

reader = pypdf.PdfReader('file3.pdf')
print(reader)

out = ''

for key in open('PDFuck.txt').readlines():
    print(key)
