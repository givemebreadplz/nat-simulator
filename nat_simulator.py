import random

class NATSimulator:
    def __init__(self, public_ip):
        self.public_ip = public_ip
        self.translation_table = {}

    def send_packet(self, private_ip, private_port):
        public_port = random.randint(2000, 65000)
        self.translation_table[(private_ip, private_port)] = (self.public_ip, public_port)
        print(f"Packet sent: {private_ip}:{private_port} -> {self.public_ip}:{public_port}")

    def show_table(self):
        if not self.translation_table:
            print("\nNAT table is empty.\n")
            return
        print("\n--- NAT Translation Table ---")
        for (p_ip, p_port), (pub_ip, pub_port) in self.translation_table.items():
            print(f"{p_ip}:{p_port} -> {pub_ip}:{pub_port}")
        print("-----------------------------\n")


def main():
    router = NATSimulator("203.0.113.5")

    while True:
        print("=== NAT Simulator Menu ===")
        print("1. Send a packet")
        print("2. Show NAT table")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            private_ip = input("Enter private IP: ")
            private_port = input("Enter private port: ")
            if not private_port.isdigit():
                print("Invalid port. Must be a number.\n")
                continue
            router.send_packet(private_ip, int(private_port))
        elif choice == "2":
            router.show_table()
        elif choice == "3":
            print("Exiting NAT simulator.")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
