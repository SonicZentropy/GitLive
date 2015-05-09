import gzip

f=gzip.open('test.als', 'rb')
file_content = f.read()
f.close
echo file_content

echo test