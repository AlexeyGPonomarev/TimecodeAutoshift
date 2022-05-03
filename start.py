import shift
minutes=1
seconds=40

line='10:00:05:35'
time_new=shift.timecode_shift(line, minutes, seconds)
print(time_new)


