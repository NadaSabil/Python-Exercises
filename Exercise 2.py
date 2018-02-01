import re

vlan_pattern = re.compile('(?<=vlan\s)(\d.+)')

all_commands_dict = [] # this will be a list of commands in dict format 
command_info = {} # Create the inner dictionary of command info

# Read all lines of command information from file
file = open('commands.txt','r')
for line in file:
    command_info_list = line.strip().split('#') # Get command info into list

    

    # locate the VLANs and put it into command_info dictionary
    vlan = vlan_pattern.search(line)
    if vlan:
    	command = vlan.group(1)
    else:
    	continue

    # add the dictionary element to the all_commands list 
    all_commands_dict.append(command)
   
	
all_commands_dict= list(all_commands_dict)
all_commands_dict= ",".join(all_commands_dict)
all_commands_dict1= list(all_commands_dict)
all_commands_dict1=all_commands_dict.split(',')

list1= [] #Create an empty list1
list2= [] #Create an empty list2
for numb in all_commands_dict1:
    # Count the number the VLAN has been repeated
    if all_commands_dict1.count(numb) == 1:
            list1.append(int(numb)) #Convert the retrieved data into integers
            list1.sort(); #Sorting number in ascending order

    # If the VLAN has been allowed in the 3 commands in the file
    elif all_commands_dict1.count(numb) > 2:
            list2.append(int(numb)) 
            list2=set(list2) #Convert the list to a set to remove duplicated VLAN numbers
            list2=list(list2)
            list2.sort()
            
    else:
        continue

# Printing the two lists
print ("Liste_1:", list1)

print ("Liste_2:", list2)

file.close() 