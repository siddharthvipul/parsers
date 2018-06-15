'''
This program is a test program for modules
'''
import parser
inventory = dict()
print(parser.get_data([6, 7, 8, 9], inventory, 'outputFioRandomRead.csv'))

#MODS:
# if read/write passed instead of , change it accordingly
# it should automatically detect jobs (column 3) or checking IOPs column
