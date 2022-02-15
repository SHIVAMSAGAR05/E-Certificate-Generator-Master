with open ("king.txt",'a+') as file:
    file.seek(0)
    content=file.read()
    file.seek(0)
    file.write("banana \n")
    file.write("apple \n")
print(content)
