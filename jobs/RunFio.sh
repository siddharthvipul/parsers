#!/bin/bash

sequential_io()
{
    `fio --name=writetest --ioengine=sync --rw=write --direct=0 \
        --create_on_open=1 --fsync_on_close=1 --bs=128k \
        --directory=<test-dir-gluster> \
        --filename_format=f.\$jobnum.\$filenum \
        --filesize=16g --size=16g --numjobs=4`
}
runFio()
{
   case seq
