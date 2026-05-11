# #accept student information - student name,marks,percentage 
# Student_name=input("Enter student Name:")
# marks=int(input("Enter marks:"))
# percentage=float(input("Enter percentage"))

# info=f"{Student_name} scored {marks} marks with {percentage:.1f}% percentage."
# print(info)



# age=(input("Enter Your age:"))
# a=int(age)+10
# s=f"Your age aafter 10 years will be {a}"
# print(s)

# print(f"{"Name":<10}{"Marks":<10}")
# print("-"*25)
# print(f"{"Amit":<10}{78:<10}")
# print("-"*25)
# print(f"{"Rohit":<10}{89:<10}")
# print("-"*25)
# print(f"{"Priya":<10}{92:<10}")

print("=====The Kiran Academy Report Card=====")
Studednt_Name=input("Enter Your name:")
p=int(input("Enter Marks obtained in Python:"))
j=int(input("Enter  Marks obtained in Java:"))
H=int(input("Enter  Marks obtained in html :"))
c=int(input("Enter  Marks obtained in css :"))
s=int(input("Enter  Marks obtained in SQL :"))
total=p+j+H+c+s
per=(total/500)*100


print("")
print(f"{"Subject name":^13} {"Marks":^7}")
print("-"*25)
print(f"{"Python":^13} {p:^7}")
print("-"*25)
print(f"{"Java":^13} {j:^7}")
print("-"*25)
print(f"{"Html":^13} {H:^7}")
print("-"*25)
print(f"{"css":^13} {c:^7}")
print("-"*25)
print(f"{"SQL":^13} {s:^7}")
print("-"*25)
print(f"{"Total":^13} {total:^7}/500")
if total>400:
    print(f"{"Grade":^13} {"A":^7}")
elif 200<total<400:
    print(f"{"Grade":^13} {"B":^7}")
elif 150<total<200:
    print(f"{"Grade":^13} {"C":^7}")
else:
    print(f"{"Grade":^13} {"Fail":^7}")
    print("-"*25)
print(f"{"Percentage":^13} {per:^7}%")


