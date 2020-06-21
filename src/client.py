from pythonosc import udp_client

if __name__ == "__main__":
    with open("ip.txt") as f:
        ip_and_ports = f.readlines()
    for ip_and_port in ip_and_ports:
        ip = str(ip_and_port.split(":")[0])
        port = int(ip_and_port.split(":")[1].replace("\n", ""))
        client = udp_client.SimpleUDPClient(ip, port)
        client.send_message("/play-stop", 1)
    
