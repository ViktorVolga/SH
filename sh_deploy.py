#!/usr/bin/env python3

import paramiko
import os

host = '192.168.88.230'
port = 22

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username="debian", password="temppwd", look_for_keys=False, allow_agent=False)
sftp = ssh.open_sftp()

filesToDeploy = ['sh_i2c.py', 'test_i2c.py']
localPath = os.path.join(os.getcwd(), 'W1_temperature_reader')
remotepath = '/home/debian/sh'

stdin, stdout, stderr = ssh.exec_command('ls ~')
stdin.close()

out = stdout.read().decode()
folders = out.split('\n')
if 'sh' not in folders:
    stdin, stdout, stderr = ssh.exec_command('mkdir ~/sh')
    stdin.close()
else:
    stdin, stdout, stderr = ssh.exec_command('ls ~/sh/')
    stdin.close()
    out = stdout.read().decode()
    files = out.split('\n')
    for file in files:
        stdin, stdout, stderr = ssh.exec_command('rm -f ~/sh/' + file)
        stdin.close()

for file in filesToDeploy:    
   sftp.put(os.path.join(localPath, file), os.path.join(remotepath, file))
   #print('deployed', os.path.join(localPath, file), 'in', os.path.join(remotepath, file))

sftp.chmod(os.path.join(remotepath, 'test_i2c.py'),  777)

sftp.close()
ssh.close()