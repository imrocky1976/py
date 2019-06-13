# -*- coding:utf-8 -*-

import os
import time

if '__main__' == __name__:
    while True:

        with os.popen('VBoxManage list runningvms') as o:
            if 'win7-1' not in o.read():
                # vm is not running, start it
                if os.system('VBoxManage startvm win7-1 --type gui') == 0:
                    # success
                    time.sleep(120) # sleep 120s
                else:
                    print('error system command `VBoxManage startvm win7-1 --type gui`')
                    time.sleep(60) # sleep 60s
            else:
                # vm is running
                print('vm is running')
                time.sleep(120) # sleep 120s

        time.sleep(60) # sleep 60s
