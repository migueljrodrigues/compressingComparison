import gzip

def zippit(txt):
    with gzip.open('cipheredText', 'wb') as f:
        f.write(txt)

def unzippit():
    with gzip.open('cipheredText', 'rb') as f:
        file_content = f.read()
        f = open('decipheredText', 'w')
        f.write(file_content)
        f.close()