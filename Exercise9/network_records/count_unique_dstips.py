# Function to extract and count unique dst IPs from records
def count_unique_dst_ips(filename):
    unique_dst_ips = set()

    with open(filename, "r") as file:
        for line in file:
            # Split the line by spaces
            parts = line.split()
            for part in parts:
                # Check if part starts with "dst=" to find dst IPs
                if part.startswith("dst="):
                    # Extract the dst IP (removing "dst=")
                    dst_ip = part[4:]
                    unique_dst_ips.add(dst_ip)

    return unique_dst_ips


if __name__ == "__main__":
    filename = "simulated_records.txt"
    unique_dst_ips = count_unique_dst_ips(filename)

    # Print the unique dst IPs and the count
    print("Unique Destination IPs:")
    for ip in unique_dst_ips:
        print(ip)

    print(f"Number of unique Destination IPs: {len(unique_dst_ips)}")
