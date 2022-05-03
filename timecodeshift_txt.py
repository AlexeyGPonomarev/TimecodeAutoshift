import openpyxl
import shift

#print('Please enter full excel file path to open')
original_path='D:/PYTHON_code/files/26_02_2020.xlsx' #input()
#print('Please enter full txt file path to write')
end_path='D:/PYTHON_code/files/26_02_20201.txt' #input()

#print('Please enter letter-name for narrator name column in excel file')
#name_column='B' #input()
#print('Please enter letter-name for text column in excel file')
script_column='B' #input()
#print('Please enter letter-name for timecode column in excel file')
timecode_column='A' #input()

#print('Please enter number for start-line of segment to shift in excel file')
start_value=1 #int(input())
#print('Please enter number for end-line of segment to shift in excel file')
end_value=205 #int(input())

print('Please enter timeshift value in mm.ss format')
shift_input=input()


shift_value=shift_input.split('.')
minutes=int(shift_value[0])
seconds=int(shift_value[1])



wb=openpyxl.load_workbook(filename=original_path)
sheet=wb['Sheet1']
new_script=open(end_path, 'w')


for i in range(start_value,end_value):
    text=script_column+str(i)
    code=timecode_column+str(i)
    #name=name_column+str(i)
    script_text=str(sheet[text].value)
    timecode=str(sheet[code].value)
    #narrator=str(sheet[name].value)
    time_new=shift.timecode_shift(timecode, minutes, seconds)
    new_script.write('\n\n'+time_new+'\n'+script_text)

new_script.close()
