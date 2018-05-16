#
# lab 1-3
#
from pysnmp.hlapi import *

result = getCmd(SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(("10.31.70.107", 161)),
                ContextData(),
                ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

result2 = nextCmd(SnmpEngine(),
                  CommunityData('public', mpModel=0),
                  UdpTransportTarget(("10.31.70.107", 161)),
                  ContextData(),
                  ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
                  lexicographicMode=False)

#snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
#snmp_object = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')
#print(result)
#print(result2)

for i in result:
    for y in i[3]:
        print(y)
for j in result2:
    for p in j[3]:
        print(p)


