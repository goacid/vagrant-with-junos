from jnpr.junos import Device
dev=Device(host="10.0.1.10", user="root", password="Juniper")
dev.open()
print ("the device "+ dev.facts["hostname"]+ " is a " + dev.facts['model'] + " running " + dev.facts["version"])
dev.close()
