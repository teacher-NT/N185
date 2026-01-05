import os
os.system("cls")

with open("image.jpeg", "rb") as file:
    baytes = file.read()
    
with open('panda.jpeg', "wb") as file:
    file.write(baytes)