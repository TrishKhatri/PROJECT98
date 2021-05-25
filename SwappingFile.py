def SwapFileData():
    file1 = input("Enter File Name ")
    file2 = input("Enter File Name ")
    with open(file1,"r") as a:
        file1data = a.read()
    with open(file2,"r") as b:
        file2data = b.read()

    with open(file1,"w") as a:
        a.write(file2data)

    with open(file2,"w") as b:
        b.write(file1data)

SwapFileData()  
