

# Create an empty list for entries
TabeEntries = [] 

#Opening the Show ip route file and reading its lines
with open('ShowIpRoute.txt', 'r') as f:
    for i in range(11):
        f.__next__()
    for entry in f:
        lst = f.readlines()


#Split the lines of the files
for entry in lst:
    TabeEntries.append(entry.split())

#Check the protocols and print each proper information
for entry in TabeEntries:
    if (entry[0] == 'O' and entry[1] == 'E2'):
        prefix= entry[2]
        AdMetric= entry[3][1:-1]
        NextHop= entry[5]
        LastUpdate= entry[7][:-1]
        OutboundInt= entry[8]
        print('Protocol: OSPF')
        print('Prefix: '+prefix)
        print('AD/Metric: '+AdMetric)
        print('Next Hop: '+NextHop)
        print('Last Update: '+LastUpdate)
        print('Outbound Interface: '+OutboundInt)
        print('\n')
        
    elif (entry[0] == 'H'):
        prefix= entry[1]
        AdMetric= entry[2][1:-1]
        LastUpdate= entry[5][:-1]
        OutboundInt= entry[6]
        print('Protocol: HSRP')
        print('Prefix: '+prefix)
        print('AD/Metric: '+AdMetric)
        print('Next Hop: '+NextHop)
        print('Last Update: '+LastUpdate)
        print('Outbound Interface: '+OutboundInt)
        print('\n')

    elif (entry[0] == 'C'):
        prefix= entry[1]
        Mask= entry[2]
        OutboundInt= entry[6]
        print('Protocol: Directly connected route')
        print('Prefix: '+prefix)
        print('Mask: '+Mask)
        print('Outbound Interface: '+OutboundInt)
        print('\n')

    elif (entry[0] == 'i'): 
        prefix= entry[2]
        AdMetric= entry[3][1:-1]
        NextHop= entry[5]
        LastUpdate= entry[7][:-1]
        OutboundInt= entry[8]
        print('Protocol: IS-IS')
        print('Prefix: '+prefix)
        print('AD/Metric: '+AdMetric)
        print('Next Hop: '+NextHop)
        print('Last Update: '+LastUpdate)
        print('Outbound Interface: '+OutboundInt)
        print('\n')

    else:
        prefix= entry[1]
        AdMetric= entry[2][1:-1]
        NextHop= entry[4]
        LastUpdate= entry[6][:-1]
        OutboundInt= entry[7]
        print('Protocol: EIGRP')
        print('Prefix: '+prefix)
        print('AD/Metric: '+AdMetric)
        print('Next Hop: '+NextHop)
        print('Last Update: '+LastUpdate)
        print('Outbound Interface: '+OutboundInt)
        print('\n')    

f.close() 