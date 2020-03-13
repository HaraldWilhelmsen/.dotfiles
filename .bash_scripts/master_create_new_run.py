#!/usr/bin/env python3
import os
import numpy as np
import sys


master_dir = os.environ['MASTER']
cwd = os.getcwd()

dir_nums_run = np.sort(np.array([int(entry.name[3:]) for entry in os.scandir() if entry.is_dir() and entry.name[0:3] == 'run']))

if 1 not in dir_nums_run:
    new_number = 1
else:
    new_avaiable_number = np.where(dir_nums_run[1:] - dir_nums_run[:-1] != 1)[0]

    if len(new_avaiable_number) == 0:
        new_number = np.max(dir_nums_run) + 1
    else:
        new_number = new_avaiable_number[0] + 2

dir_name = 'run' + str(new_number)

try:
    os.mkdir(dir_name)
    print('Directory "', dir_name ,  '" created.', sep='')
except FileExistsError:
    print("Error, cannot create directory " , dir_name)
    sys.exit()

os.mkdir(dir_name + '/run')
os.mkdir(dir_name + '/output')
os.mkdir(dir_name + '/inputs')
os.system('cp $MASTER/inputs/* '+dir_name+'/inputs/')

os.symlink(master_dir+'/my_ploting_scripts', dir_name+'/my_ploting_scripts')
os.symlink(master_dir+'/optical_data', dir_name+'/optical_data')
os.symlink(master_dir+'/python_tools', dir_name+'/python_tools')
#os.symlink(master_dir+'/run', dir_name+'/run')
os.symlink(master_dir+'/src', dir_name+'/src')
os.symlink(master_dir+'/src/r2dp_omp', dir_name+'/run/r2_omp')
