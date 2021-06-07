from subprocess import STDOUT, check_call
import os

CONFIG_PATH="/etc/proftpd/proftpd.conf"

check_call(['apt-get', 'install', '-y', 'proftpd'], stdout=open(os.devnull,'wb'), stderr=STDOUT) # installing proftpd service

try:
    oldfilecontent = []
    with open(CONFIG_PATH,'r') as file:
        for line in file:
            oldfilecontent.append(line)

    os.rename(CONFIG_PATH,CONFIG_PATH+".old")

    with open(CONFIG_PATH, 'w') as file:
        for line in oldfilecontent:
            if ("DefaultRoot" in line):
                file.write("DefaultRoot")
                print("Succesfully found 'DefaultRoot'")
            else:
                file.write(line)
    print("Succesfully enabled FTP server for everyone")


except:
    os.rename(CONFIG_PATH + ".old", CONFIG_PATH)
    print("Unable to auto-enable FTP for everyone\nPlease go to ->"+CONFIG_PATH+"\nFind '#DefaultRoot' and remove the '#'")