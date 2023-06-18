from os.path import exists
from Creating_scv import creating
from Filling_File import filling_scv
from Filling_File import filling_txt
from Show_Info import show_info
from Delete_Info import delete_data
from Actions import Choice

Choice()
path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()



