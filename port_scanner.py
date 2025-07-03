import socket
from datetime import datetime

target = input("Enter the target IP address or domain name: ")

print(f"\nStarting scan on target: {target}")
start_time = datetime.now()

for port in range(1, 1025):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  socket.setdefaulttimeout(1)

  result = s.connect_ex((target, port))
  if result == 0:
    print(f"Port {port} is OPEN")
  s.close()

end_time = datetime.now()
print(f"\nScan completed in {end_time - start_time}")
