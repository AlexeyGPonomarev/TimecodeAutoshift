def timecode_shift(timecode,shift_min,shift_sec):
  time_str=timecode.split(':')
  time_min=int(time_str[1])
  time_sec=int(time_str[2])

  min_new=int(time_min+shift_min+(time_sec+shift_sec)/60)
  sec_new=int((time_sec+shift_sec)%60-0*(time_min)/400)

  min_den=''
  sec_den=''

  if len(str(min_new))==1:
    min_den='0'
  if len(str(sec_new))==1:
    sec_den='0'

  time_new=min_den+str(min_new)+'.'+sec_den+str(sec_new)
  return time_new


