
'''
Fio commands

Large file, sequential I/O workloads
====================================

* fio --name=writetest --ioengine=sync --rw=write --direct=0 --create_on_open=1
--fsync_on_close=1 --bs=128k --directory=<test-dir-gluster>
--filesize=16g --size=16g --numjobs=4 --minimal > outputFioSeqWrite.csv

* sync; echo 3 > /proc/sys/vm/drop_caches # on clients, then on servers

* fio --name=readtest --ioengine=sync --rw=read --direct=0 --bs=128k
--directory=<test-dir-gluster> --filesize=16g --size=16g --numjobs=4 --minimal
> outputFioSeqRead.csv


Important data
==============

6	Total I/O (KB)
7	bandwidth (KB/s)
8	IOPS
9	runtime (ms)
16      Completion latency mean
5       Bandwidth mean
read_data = [6, 7, 8, 9, 16, 45], columns from csv

47	Total I/O (KB)
48	bandwidth (KB/s)
49	IOPS
50	runtime (ms)
57      Completion latency mean
86      Bandwidth mean
write_data = [47, 48, 49, 50, 57, 86], columns from csv

Code variable explanation
=========================

job_name = [3], column from csv
data = {jobName:[write_row_numbers], jobname:[read_row_numbers]}
example:
data = {'readtest': [108676, 17992, 140, 58277, 7102.775, 17748, 613505]
'''
import sys

def get_data(inventory, file_path):
    '''
    accepts columns that are to be extracted from the given csv file and
    returns the dictionary with job name as key and important data (included
    columns) as value
    '''
    included_cols_read = [5, 6, 7, 8, 15, 44]
    included_cols_write = [46, 47, 48, 49, 56, 85]
    data = list()
#    counter = 0
    try:
        with open(file_path, "r") as file_object:
            for rows in file_object:
                cells = rows.split(";")
                if cells[5] != '0':
                    for each_column in included_cols_read:
                        data.append(cells[each_column])
                    inventory[cells[2]] = data
                if cells[46] != '0':
                    for each_column in included_cols_write:
                        data.append(cells[each_column])
                    inventory[cells[2]] = data
                return inventory

    except IOError:
        print("File not found")

def main():
    '''
    * takes file name as an argument
    * passes included columns with other parameters
    * prints data
    '''
    filename = sys.argv[1]
    inventory = dict()
    result = get_data(inventory, filename)
    if result:
        print(result)

if __name__ == '__main__':
    main()
