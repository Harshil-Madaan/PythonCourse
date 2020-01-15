ofile=open("sample.txt","r")
for line in ofile:
    print(line,end='')
print(ofile.read(12))
ofile.close()
