from scapy.all import sniff

# Packet information function
def packet_info(packet):

    print("\n--- Packet Captured ---")

    # IP information
    if packet.haslayer("IP"):
        print("Source IP:", packet["IP"].src)
        print("Destination IP:", packet["IP"].dst)

    # Protocol details
    print("Protocol:", packet.summary())

# Capture 10 packets
sniff(prn=packet_info, count=10)