#Sorted  information alphabetically

information = str(input(f"Please input information : ")).strip()

new_list = information.split(",")
sorted_list = sorted(new_list)
result = ",".join(sorted_list)

print(result)
