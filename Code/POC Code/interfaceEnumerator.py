import ifaddr, socket

adapters = ifaddr.get_adapters()

for adapter in adapters:
    if "VMware" not in adapter.nice_name:
        #adapter.name is the actual name of the adapter. In linux this would appear as "eth0" and so on.
        print (adapter.nice_name + "\n" + adapter.name.decode("utf-8") )
        for ip in adapter.ips:
            print ("   %s/%s" % (ip.ip, ip.network_prefix))