
from scapy.all import sniff

# Function to process each captured packet
def process_packet(packet):
    if packet.haslayer('IP'):
        ip_layer = packet['IP']
        print(f"Source IP: {ip_layer.src} -> Destination IP: {ip_layer.dst} | Protocol: {ip_layer.proto}")
        if packet.haslayer('TCP') or packet.haslayer('UDP'):
            print(f"Payload: {bytes(packet.payload)}")
        print('-' * 50)

# Start sniffing packets
print("Starting packet capture... Press Ctrl+C to stop.")
sniff(prn=process_packet, store=False)
