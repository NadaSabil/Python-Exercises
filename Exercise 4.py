import re


access_template = ['switchport mode access','switchport access vlan {}','switchport nonegotiate','spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q','switchport mode trunk', 'switchport trunk allowed vlan {}']

# Asking for the interface mode and its type and number
mode=input("Enter interface mode (access/trunk):")
int_type=input("Enter interface type and number: ")


if mode=='access':
    vlan_numb=input("Enter VLAN number: ")
    #Replace '{}' in the list by the VLAN number provided
    access_template = [w.replace('{}', vlan_numb) for w in access_template] 

    #Print the proper configuration for Access VLANs
    print ('-------------- Configuration --------------')
    print ("Interface",int_type)
    for command in access_template:
        print(command)


elif mode=='trunk':
    allowed_vlan=input("Enter allowed VLANs:")

     #Replace '{}' in the list by the allowed VLAN
    trunk_template = [w.replace('{}', allowed_vlan) for w in trunk_template] 
    
    #Print the proper configuration for Trunk VLANs
    print ('-------------- Configuration --------------')
    print ("Interface",int_type)
    for command in trunk_template:
        print (command)

else:
    print("sorry there was an error in your entry. Please try again")


