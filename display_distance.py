import base
from lcd import lcddriver

mylcd = lcddriver.lcd()

try:
  while True:
      mylcd.lcd_display_string("Distance: ", 1)
      mylcd.lcd_display_string(str(round(base.measure(), 8)) + "cm", 2)
      base.time.sleep(1)
      mylcd.lcd_clear()

finally:
  mylcd.lcd_clear()
  mylcd.lcd_write(lcddriver.LCD_DISPLAYCONTROL | lcddriver.LCD_DISPLAYOFF)
