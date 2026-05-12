jay=int(input("Enter Jay's age:"))
viru=int(input("Enter Viru's age:"))
gabbar=int(input("Enter Gabbar's age:"))
if jay > viru:
    if jay > gabbar:
        print("Jay is older")
    else:
        print("Gabbar is older")
else:
    if viru > gabbar:
        print("Viru is older")
    else:
        print("Gabbar is older")
