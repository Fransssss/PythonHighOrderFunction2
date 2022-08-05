# Author: Fransiskus Agapa

from operation import add
from operation import sub
from operation import mul
from operation import div
from operation import mod
# ==============================
# simple program to creat and call function inside a function
# ==============================

print("\n== Basic Math Operation ==")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Module")
print("e. Exit")
choice = input("choice: ").lower()    # make while-loop condition simpler

while choice != 'e':
    if choice == '1':
        print("\n -- Addition --\n")
        try:
            print("Input first number: ", end=" ")
            st_num = int(input())
            print("Input second number: ", end=" ")
            nd_num = int(input())
            print("\n> " + str(st_num) + " + " + str(nd_num) + " = ", end=" ")
            added = add(st_num)
            print(added(nd_num))

        except ValueError:
            print("\n[ Invalid input - digit only ]")

    elif choice == '2':
        print("\n -- Subtraction --\n")
        try:
            print("Input first number: ", end=" ")
            st_num = int(input())
            print("Input second number: ", end=" ")
            nd_num = int(input())
            print("\n> " + str(st_num) + " - " + str(nd_num) + " = ", end='')
            subbed = sub(st_num)
            print(subbed(nd_num))
        except ValueError:
            print("\n[ Invalid input - digit only ]")

    elif choice == '3':
        print("\n -- Multiplication --\n")
        try:
            print("Input first number: ", end=" ")
            st_num = int(input())
            print("Input second number: ", end=" ")
            nd_num = int(input())
            print("\n> " + str(nd_num) + " x " + str(nd_num) + " = ", end="")
            multip_val = mul(st_num)
            print(multip_val(nd_num))
        except ValueError:
            print("\n[ Invalid input - digit only ]")

    elif choice == '4':
        print("\n -- Division --\n")
        try:
            print("Input first number: ", end="")
            st_num = int(input())
            print("Input second number: ", end=" ")
            nd_num = int(input())
            print("\n> " + str(st_num) + " / " + str(nd_num) + " = ", end='')
            div_val = div(st_num)
            print(str("{:.2f}".format(div_val(nd_num))))        # 2 digit after comma
        except ValueError:
            print("\n[ Invalid input - digit only ]")

    elif choice == '5':
        print("\n -- Module -- \n")
        try:
            print("Input first number: ", end="")
            st_num = int(input())
            print("Input second number: ", end="")
            nd_num = int(input())
            print("\n> " + str(st_num) + " % " + str(nd_num) + " = ", end="")
            mod_val = mod(st_num)
            print(mod_val(nd_num))
        except ValueError:
            print("\n[ Invalid input - digit only ]")

    else:
        print("\n[ Invalid choice ]")

    print("\n== Basic Math Operation ==")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Module")
    print("e. Exit")
    choice = input("choice: ").lower()  # make while-loop condition simpler

print("\n== Exit Program ==")
