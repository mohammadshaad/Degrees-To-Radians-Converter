from math import pi


noOfInputs = int(input("βEnter the total number of values you want to convert from Degrees to Radians: "))
list_of_inputs = []
print("βPlease input the values to convert into radians [πππ© ππ£π©ππ§ πΌππ©ππ§ ππππ ππͺπ’πππ§]")
i = 1
while i <= noOfInputs:
    degrees = float(input("ππ» "))
    list_of_inputs.append(degrees)
    i += 1

confirmation = input("\nYou wish to convert" + str(list_of_inputs) + "into radians? [Y/N]: ")
if confirmation.lower() == "y":
    list_of_outputs = []
    for value in list_of_inputs:
        radians = (pi / 180) * value
        list_of_outputs.append(radians)
    print("\nβ¨Radians Values: ", list_of_outputs)
    print("-"*100)

elif confirmation.lower() == "n":
    list_of_inputs = []
    list_of_outputs = []
    i = 1
    while i <= noOfInputs:
        degrees = float(input("βRe-enter the values to convert into radians: "))
        list_of_inputs.append(degrees)
        i += 1
        for value in list_of_inputs:
            radians = (pi / 180) * value
            list_of_outputs.append(radians)
    print("Radians Values: ", list_of_outputs)


else:
    print("Try Again π")

# #Rerunning the programme
rerun = input("\nβEnter 1 to rerun the programme else enter 0: ")
if rerun != 1:
    print("Invalid Input π Programme Terminates!!!")

elif rerun == 0:
    print("Programme Terminates Successfully π")

elif rerun == 1:
    while True:
        noOfInputs = int(input("βEnter the total number of values you want to convert from Degrees to Radians: "))
        list_of_inputs = []
        i = 1
        while i <= noOfInputs:
            print(
                "βPlease input the values to convert into radians [πππ© ππ£π©ππ§ πΌππ©ππ§ ππππ ππͺπ’πππ§]")
            degrees = float(input("ππ» "))
            list_of_inputs.append(degrees)
            i += 1

        confirmation = input("\nYou wish to convert" + str(list_of_inputs) + "into radians? [Y/N]: ")
        if confirmation.lower() == "y":
            list_of_outputs = []
            for value in list_of_inputs:
                radians = (pi / 180) * value
                list_of_outputs.append(radians)

            print("\nβ¨Radians Values: ", list_of_outputs)

        elif confirmation.lower() == "n":
            list_of_inputs = []
            list_of_outputs = []
            i = 1
            while i <= noOfInputs:
                degrees = float(input("βRe-enter the values to convert into radians: "))
                list_of_inputs.append(degrees)
                i += 1
                for value in list_of_inputs:
                    radians = (pi / 180) * value
                    list_of_outputs.append(radians)
            print("Radians Values: ", list_of_outputs)


        else:
            print("Try Again π")



