# update set items
thisset = {"apple", "banana", "cherry"}
uniq = {"leoanl", "messi","Ronaldo "}
thisset.update(uniq)
print(thisset)

# sete items is not duplicate value allow
first= {1,2,3,4,5,6,7,8}
second = {4,5,6,7,8}
both =first|second
print(both)

# just common value asign
common = first & second
print(common)

# print key method
B = {
    "django":12,
    "project":8,
    "students":20
}
value =B.keys()
print(value)

# even ,odd and zero check
num = float(input("Enter your number:"))
if (num==0):
    print(f"this is a zero{num}")
elif (num%2==0):
    print("this is a even number")
else:
    print("this is a odd number ")
#tringale area 
b = float(input("Enter your base:"))
h = float(input("Enter your height:"))
area = 0.5*b*h
print(area)
