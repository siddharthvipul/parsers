'''
This program is a test program for modules
'''
import parser_auto as pa
inventory = dict()
print(pa.get_data(inventory, 'outputFioRead.csv'))

#MODS:
# if read/write passed instead of , change it accordingly
# it should automatically detect jobs (column 3) or checking IOPs column
