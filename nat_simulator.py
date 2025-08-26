import random

class NATSimulator:
    def __init__(self, public_ip):
        self.public_ip = public_ip
        self.translation_table = {}  # (private_ip, private_port) -> (public_ip, public_port, type)
        # Predefined static NAT mappings
        self.static_nat = {
            ("192.168.1.10", 5000): (self.public_ip, 4000),
            ("192.168.1.11", 6000): (self.public_ip, 4001)
        }

    def send_packet(self, private_ip, private_port, mode="dynamic"):
        key = (private_ip, private_port)

        if mode == "static":
            if key in self.static_nat:
                pub_ip, pub_port = self.static_nat[key]
            else:
                print("No static mapping for this IP/port. Using dynamic instead.")
                pub_port = random.randint(2000, 65000)
                pub_ip = self.public_ip
        else:  # dynamic NAT
            if key in self.translation_table:
                pub_ip, pub_port, _ = self.translation_table[key]
            else:
                pub_port = random.randint(2000, 65000)
                pub_ip = self.public_ip

        self.translation_table[key] = (pub_ip, pub_port, mode)
        print(f"Packet sent: {private_ip}:{private_port} -> {pub_ip}:{pub_port} ({mode})")

    def show_table(self):
        if not self.translation_table:
            print("\nNAT table is empty.\n")
            return
        print("\n--- NAT Translation Table ---")
        for (p_ip, p_port), (pub_ip, pub_port, mode) in self.translation_table.items():
            print(f"{p_ip}:{p_port} -> {pub_ip}:{pub_port} ({mode})")
        print("-----------------------------\n")


def main():
    router = NATSimulator("203.0.113.5")

    while True:
        print("=== NAT Simulator Menu ===")
        print("1. Send a packet (Dynamic NAT)")
        print("2. Send a packet (Static NAT)")
        print("3. Show NAT table")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1" or choice == "2":
            private_ip = input("Enter private IP: ")
            private_port = input("Enter private port: ")
            if not private_port.isdigit():
                print("Invalid port. Must be a number.\n")
                continue
            mode = "dynamic" if choice == "1" else "static"
            router.send_packet(private_ip, int(private_port), mode)
        elif choice == "3":
            router.show_table()
        elif choice == "4":
            print("Exiting NAT simulator.")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()

