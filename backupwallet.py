from subprocess import Popen, PIPE, STDOUT
import time
import os


# location of backups
destination = '/home/droid/backups/'
# filename
timestr = time.strftime("%Y%m%d-%H%M%S")
spacer = 'wallet-'
filename = destination + spacer + timestr


def backupwallet():
    # command that gets the file
    cmdsendcoinfromholdings = ["bitcoin-cli", "backupwallet", destination]
    proc = Popen(cmdsendcoinfromholdings, stdout=PIPE, stderr=STDOUT, universal_newlines=True)

    for f in os.listdir(destination):
        if f.startswith('wallet.d'):
            # rename file
            filenameold, file_extension = os.path.splitext(destination + f)
            newfilename = filename + file_extension
            filenameoldfull = filenameold + file_extension
            newfilenamedestinationfull = newfilename
            os.rename(filenameoldfull, newfilenamedestinationfull)


def syncbackup():
    rsynccmd = ["rsync -avP /home/droid/backups/*.dat bot@192.168.1.8:/home/bot/backups/wallet"]
    proc = Popen(rsynccmd, shell=True, stdout=PIPE, stderr=STDOUT, universal_newlines=False)


backupwallet()
syncbackup()