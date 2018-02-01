import re
from netaddr import *
import pprint

def Vip(ip_addr):
    addr=ip_addr.split('.')
    if len(addr)==4:
        if 0<int(addr[0])<255 and 0<int(addr[1])<255 and 0<int(addr[2])<255 and 0<int(addr[3])<255:
            return True
        else:
            return False
    else:
         return False
        
def VMask(msk):
     if re.match("\/(\b[0-3]?[0-9]\b)", msk):
        return True
     else:
        return False
          
ip =input("Enter ip address:")
Vip_ret= Vip(ip)
while (Vip_ret) == False : 
     print ("Invalid IP address format")
     ip =input("Enter ip address:")
     break
    
mask =input("Enter subnet mask in decimal format:")
VMask_ret = VMask(mask)
while (VMask_ret) == False : 
     print ("Subnet mask is invalid")
     mask =input("Enter subnet mask in decimal format:")
     break

liste = ip.split('.')
print( '{:>10}'.format(liste[0])+'{:>10}'.format(liste[1])+'{:>10}'.format(liste[2])+'{:>10}'.format(liste[3]))
print('{:>10}'.format(bin(int(liste[0])).lstrip('-0b').zfill(8)),'{:>10}'.format(bin(int(liste[1])).lstrip('-0b').zfill(8)),'{:>10}'.format(bin(int(liste[2])).lstrip('-0b').zfill(8)),'{:>10}'.format(bin(int(liste[3])).lstrip('-0b').zfill(8)))

full_addr=ip+mask
inpt=IPNetwork(full_addr)
print('network address is: '+str(inpt.network)+'/'+str(inpt.prefixlen))
print('broadcast address is: '+str(inpt.broadcast)+'/'+str(inpt.prefixlen))


 