from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        ip_layer = packet["IP"]
        print(f"[+] New Packet: {ip_layer.src} -> {ip_layer.dst} | Protocol: {ip_layer.proto}")

def main():
    print("=== Packet Sniffer (Educational Use Only) ===")
    print("Capturing packets... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, count=0)  # count=0 → unlimited until stopped

if __name__ == "__main__":
    main()