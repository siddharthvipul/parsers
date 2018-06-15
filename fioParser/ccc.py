import csv
import sys

var = '''output version
fio version
job name
group id
error
total io
bandwidth
IOPS
runtime
submission latency (min)
submission latency (max)
submission latency (mean)
submission latency (deviation)
Completion latency (min)
Completion latency (max)
Completion latency (mean)
Completion latency (deviation)
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Total latency (min)
Total latency (max)
Total latency (avg)
Total latency (deviation)
Bandwidth (min)
Bandwidth (max)
Bandwidth (aggregate percentage of total)
Bandwidth (mean)
Bandwidth (deviation)
total io
bandwidth
IOPS
runtime
submission latency (min)
submission latency (max)
submission latency (mean)
submission latency (deviation)
Completion latency (min)
Completion latency (max)
Completion latency (mean)
Completion latency (deviation)
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Completion latency percentiles
Total latency (min)
Total latency (max)
Total latency (avg)
Total latency (deviation)
Bandwidth (min)
Bandwidth (max)
Bandwidth (aggregate percentage of total)
Bandwidth (mean)
Bandwidth (deviation)
CPU usage: user
CPU usage: system
CPU usage: context switches
CPU usage: major page faults
CPU usage: minor page faults
IO depth distribution <= 1
IO depth distribution 2
IO depth distribution 4
IO depth distribution 8
IO depth distribution 16
IO depth distribution 32
IO depth distribution >= 64
IO latency distribution <= 2 usec
IO latency distribution 4 usec
IO latency distribution 10 usec
IO latency distribution 20 usec
IO latency distribution 50 usec
IO latency distribution 100 usec
IO latency distribution 250 usec
IO latency distribution 500 usec
IO latency distribution 750 usec
IO latency distribution 1000 usec
IO latency distribution <=2 msec
IO latency distribution 4 msec
IO latency distribution 10 msec
IO latency distribution 20 msec
IO latency distribution 50 msec
IO latency distribution 100 msec
IO latency distribution 250 msec
IO latency distribution 500 msec
IO latency distribution 750 msec
IO latency distribution 1000 msec
IO latency distribution 2000 msec
IO latency distribution >=2000 msec
'''

row_with_name = var.split("\n")
row_with_number = list(range(1,122))
with open(sys.argv[1], 'a+') as f:
    wr = csv.writer(f)
    wr.writerow(row_with_name)
    wr.writerow(row_with_number)

