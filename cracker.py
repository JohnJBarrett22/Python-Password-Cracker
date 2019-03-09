import zipfile

count = 1

with open('darkweb-2017.top10000.txt', 'rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile('locked.zip', 'r') as zf:
                zf.extractall(pwd=password)
