indian = ["samosa", "bread", "rice"]
china = ["egg role", "fish role", "rice fry"]
america = ["Chicken", "chaumin", "pattato" ]
 
disk = input("enter disk :") 
if disk in indian:
    print("Disk are indian:")
elif disk in china:
    print("Disk are chiness")
elif disk in america:
    print("Disk is american")
else:
    print("Invalid")