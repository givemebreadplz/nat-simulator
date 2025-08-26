import random

class NATSimulator:
    def __init__(self, public_ip):
        self.public_ip = public_ip
        self.translation_table = {}

    def send_packet(self, private_ip, private_port):
        # Assign a random public port
        public_port = random.randint(2000, 65000)
        self.translation_table[(private_ip, private_port)] = (self.public_ip, public_port)

        print(f"Packet sent: {private_ip}:{private_port} -> {self.public_ip}:{public_port}")

    def show_table(self):
        print("\n--- NAT Translation Table ---")
        for (p_ip, p_port), (pub_ip, pub_port) in self.translation_table.items():
            print(f"{p_ip}:{p_port} -> {pub_ip}:{pub_port}")
        print("-----------------------------\n")


# Example usage
if __name__ == "__main__":
    router = NATSimulator("203.0.113.5")

    router.send_packet("192.168.1.2", 1234)
    router.send_packet("192.168.1.3", 5678)
    router.show_table()
