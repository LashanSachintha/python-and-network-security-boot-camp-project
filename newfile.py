import hashlib
text="Boot Camp"

HashConvert=hashlib.md5(text.encode())
Convert=HashConvert.hexdigest()



print(Convert)