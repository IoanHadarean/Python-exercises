# employees = open("employees_file", "r")
# for employee in employees:
#     print(employee)
# employees.close()

for n in range (int(input())):
    s = input()
    print(s[::2], s[1::2])