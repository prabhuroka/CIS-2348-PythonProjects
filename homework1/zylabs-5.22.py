#Prabhu Roka
#1986444
print("Davy's auto shop services")
rate = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12}

print("Oil change -- $" + str(rate["Oil change"]))
print("Tire rotation -- $" + str(rate["Tire rotation"]))
print("Car wash -- $" + str(rate["Car wash"]))
print("Car wax -- $" + str(rate["Car wax"]))
print("")
print("Select first service:")
first_service = input()
print("Select second service:")
second_service = input()
print("")
print("Davy's auto shop invoice")
print("")
if (first_service == "-") and (second_service == "-"):
    print("Service 1: No service")
    print("Service 2: No service")
    print("")
    print("Total: $0")
elif (first_service == "-"):
    print("Service 1: No service")
    print("Service 2: " + str(second_service) + ", $" + str(rate[second_service]))
    print("")
    total = rate[second_service]
    print("Total: $" + str(total))
elif (second_service == "-"):
    print("Service 1: " + str(first_service) + ", $" + str(rate[first_service]))
    print("Service 2: No service")
    print("")
    total = rate[first_service]
    print("Total: $" + str(total))
else:
    print("Service 1: " + str(first_service) + ", $" + str(rate[first_service]))
    print("Service 2: " + str(second_service) + ", $" + str(rate[second_service]))
    print("")
    total = rate[first_service] + rate[second_service]
    print("Total: $" + str(total))
