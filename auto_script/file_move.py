import os
import time

target_node = 'ztgk1'
source_dirs = ('/users/ems/sophic/deployment/data/anti/ftp',
               '/users/ems/sophic/deployment/data/anti/data')


def move_file(dir, file):
    os.chdir(dir)
    #for node in target_nodes:
    os.system('scp %s %s:`pwd`' % (file, target_node))
    print('move file %s to %s:%s OK!' %
          (os.path.join(dir, file), target_node, os.path.join(dir, file)))
    os.remove(file)


if __name__ == '__main__':
    while True:
        for source_dir in source_dirs:
            files = os.listdir(source_dir)
            for file in files:
                path = os.path.join(source_dir, file)
                if os.path.isfile(path):
                    move_file(source_dir, file)
        time.sleep(3)