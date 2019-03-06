import ifaddr

adapters = ifaddr.get_adapters()

for adapter in adapters:
    if "VMware" not in adapter.nice_name:
        print ("IPs of network adapter " + adapter.nice_name)
        for ip in adapter.ips:
            print ("   %s/%s" % (ip.ip, ip.network_prefix))