import gzip
import git

f = gzip.open('test.als', 'rb')
file_content = f.read()
f.close()

outF = file("test.xml", 'wb')
outF.write(file_content)
outF.close()

infile = file("test.xml", 'r')
gOut = gzip.open('testOut.als', 'wb')
gOut.writelines(infile)

repo = git.Repo('./')
print repo.git.status()