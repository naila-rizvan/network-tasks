import scapy.all as scapy
import ipaddress

# Function to scan the given IP or network range
def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the ARP and broadcast packets
    arp_broadcast_packet = broadcast_packet/arp_packet
    # Send the packets and capture the responses
    answered_list, unanswered_list = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)

    # Check if there are any responses
    if answered_list:
       print("\nFollowing are the active hosts in the network")
    else:
        print("\nThere are no active hosts in the network")

    # Loop through the answered list and print the IP addresses of active hosts
    for element in answered_list:
        print(element[1].psrc)


if __name__ == '__main__':
    # Prompt the user to enter a network range
    ip = input("Enter a network range to be scanned: ")

    try:
        # Validate if the IP or network range is valid
        ipaddress.ip_network(ip,strict=True)
        if '/' in ip:  # Ensure the input includes a subnet mask
            scan(ip)
        else:
            print("Please enter IP with CIDR notation")

    except ValueError:
        print("Invalid IP or network range. Please try again.")

