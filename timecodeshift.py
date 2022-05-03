import shift
import openpyxl
minutes=1
seconds=40

wb=openpyxl.load_workbook(filename='D:/python_code/files/test.xlsx')
from openpyxl import Workbook
wb_new=Workbook()
sheet=wb['Sheet1']
sheet_new=wb_new.active

for i in range(9,15):
    text='E'+str(i)
    code='F'+str(i)
    new_text='B'+str(i-8)
    new_code='A'+str(i-8)
    script_text=str(sheet[text].value)
    timecode=str(sheet[code].value)
    time_new=shift.timecode_shift(timecode, minutes, seconds)
    sheet_new[new_text]=script_text
    sheet_new[new_code]=time_new
    #print('Old code is: ',timecode,' and new code is ', time_new)
#print(time_new)
wb_new.save('D:/python_code/files/edit.xlsx')

