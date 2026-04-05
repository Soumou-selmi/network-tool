from fastapi import FastAPI, HTTPException
import ipaddress

app = FastAPI()

@app.get("/network-info")
def network_info(network: str, cidr: int):
    try:
        net = ipaddress.ip_network(f"{network}/{cidr}", strict=False)
        hosts = [str(ip) for ip in net.hosts()]
        return {
            "network": str(net.network_address),
            "broadcast": str(net.broadcast_address),
            "netmask": str(net.netmask),
            "total_hosts": net.num_addresses - 2,
            "gateway": hosts[0] if hosts else "N/A",
            "hosts": hosts
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
