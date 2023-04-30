key_loction = "Chair"
locatons = ["garage", "living room", "Chair", "closet"]

for i in locatons:
    if i==key_loction:
        print("Key is found ", i)
        break
    else:
        print("Key is not found", i)
