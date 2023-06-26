def add_time(start, duration, day = ' ' ):
  hour_add = 0
  day_count = 0

  for i, check in enumerate(start):
    hours,part_day = start.split()
    hours = hours.split(':')
    hour = hours[0]
    minute = hours[1] 
    
  for b, see in enumerate(duration):
    hour_two,minute_two = duration.split(':')
  
  #Minutes adding
  total_minutes = int(minute) + int(minute_two)
  while total_minutes >= 60:
    total_minutes = total_minutes - 60
    hour_add += 1
  # Hours adding
  total_hours = hour_add + int(hour_two) + int(hour) 
  #very confusing if if days > 24 how to get next
  while total_hours > 12:
    total_hours = total_hours - 12
    if part_day == 'PM':
      part_day = 'AM'
      day_count += 1
    else:
      part_day = 'PM'

  if int(hour) <= 11 and total_hours == 12:
    if part_day == 'PM':
      part_day = 'AM'
      day_count += 1
    else:
      part_day = 'PM'
  # Adding 0 infront of numbers with single digits
  if len(str(total_minutes)) == 1:    
    total_minutes = '0'+ str(total_minutes)
  # Checking day
  
  week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

  if day.isspace() == False:
    day = day.capitalize()
    day_found = week_days.index(day) 
    real_day = ((day_found + day_count) % 7)
  new_time = str(total_hours) + ":" + str(total_minutes) + ' ' + str(part_day)
  if int(hour_two) >= 24 and day.isspace() == True and day_count > 1:
    new_time += " (" + str((day_count)) + " days later)"
  else:
    if day.isspace() == False:
      new_time +=  ", " + str(week_days[real_day])
  if day_count == 1:
    new_time +=  " (next day)" 
  elif day_count != 0 and day.isspace() == False:
      new_time += " (" + str((day_count)) + " days later)"
  return new_time