flag = 1

counter = 0

Q = int(input("Enter quantity of employee: "))

List_employee = []

for i in range(0, Q):
    Age = int(input("Enter your age: "))
    B = int(input("Enter your birthday's year: "))
    D = int(input("Enter your birthday's day: "))
    Heigth = int(input("Enter your heigth: "))
    Dict = {"Age":Age, "Birthday's year":B, "Birthday's day":D, "Heigth":Heigth}
    List_employee.append(Dict)
print()
print(List_employee)
print()

while flag == 1:
    j = int(input("Enter employee's number: "))
    Age = List_employee[j]["Age"]
    B = List_employee[j]["Birthday's year"]
    D = List_employee[j]["Birthday's day"]
    Heigth = List_employee[j]["Heigth"]
    for i in [B, Heigth]:
        num = i
        List1 = []
        while (num):
            NF = int(num % 10)
            num = int(num / 10)
            List1.append(NF)
        if i == B:
            List2 =[]
            List2.append(List1.pop())
            List2.append(List1.pop())
            B_L = int(str(List2[0]) + str(List2[1]))
            print(f"B_L: {B_L}")
        elif i == Heigth:
            List1.reverse()
            List2 =[]
            List2.append(List1.pop())
            List2.append(List1.pop())
            List2.reverse()
            H_R = int(str(List2[0]) + str(List2[1]))
            print(f"H_R: {H_R}")
    
    print()
    
    Password = int(str(Heigth - ((H_R - B_L) + Age)) + str(B)) + (D*D)
    
    print(f"Password: {Password}")
    
    print()

    while True:
        x = int(input("Enter your password: "))
        if x == Password:
            print("Correct password ! Welcome")
            print()
            break
        else:
            print("Permission denies !")
            print()
    counter += 1

    option = input("Does remain any other employee (y/n): ")

    print()

    if option == "y":
        if counter == Q:
            print("The entire employees are present !")
            break
        else:
            flag == 1
    else:
        print("Have a good day !")
        print()
        print(f"Number of employees: {counter}")
        break
