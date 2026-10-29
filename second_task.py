#Print the name of resource
link = str(input(f"Plaese input link "))

link_list = link.split('/')

print(link_list[-1])
