def angleClock(hour, minutes):
  hour_angle = ((hour) + (minutes) / 60) * 30 
  min_angle = minutes * 6 
  diff = abs(hour_angle - min_angle)
  if(diff > 180):
      return 360 - diff  
  return diff

hour = int(input())
minutes = int(input())

print(angelClock(hour,minutes))
