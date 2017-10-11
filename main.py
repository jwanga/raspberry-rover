import cwiid
import time
import RPi.GPIO as io

io.setmode(io.BOARD)

in1_pin = 12
in2_pin = 33

io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)

#The motorcontroller needs to operate at 340Hz intorder to center the duty cycle at 50%
frequency = 340
duty = 50
speed = 20
right = 0
left = 0

rightServo = io.PWM(in1_pin, frequency)
leftServo = io.PWM(in2_pin, frequency)

rightServo.start(duty)
leftServo.start(duty)

#import i2c 
#connecting to the Wiimote. This allows several attempts 
# as first few often fail. 
print("Press 1+2 on your Wiimote now...") 
wm = None 
i=2 
while not wm: 
  try: 
    wm=cwiid.Wiimote() 
  except RuntimeError: 
    print("Error opening wiimote connection") 
    print("attempt " + str(i)) 
    i += 1 

#set Wiimote to report button presses and accelerometer state 
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC 
 
#turn on led to show connected 
wm.led = 1
#print state every second


while True:
  buttons = wm.state['buttons']

  if buttons & cwiid.BTN_UP:
    right = -1
    left = -1
    #print(u'\u21E7')	
  elif buttons & cwiid.BTN_RIGHT:
    right = -1
    left = 1
    #print(u'\u21E8')
  elif buttons & cwiid.BTN_DOWN:
    right = 1
    left = 1
    #print(u'\u21E9')
  elif buttons & cwiid.BTN_LEFT:
    right = 1
    left = -1
    #print(u'\u21E6')
  else:
    right = 0
    left = 0   
  
  if buttons & cwiid.BTN_PLUS:
    if duty < 100:
      duty = duty + 1
  elif buttons & cwiid.BTN_MINUS:
    if duty > 1:
      duty = duty - 1
  
  rightServo.ChangeDutyCycle(duty + (right * speed))
  leftServo.ChangeDutyCycle(duty + (left * -1 * speed))
  
  #if buttons:
    #print("frequency:" + str(frequency) + " duty:" + str(duty) + " right:" + str(duty + (right * speed)) + " left:" + str(duty + (left * -1 * speed))) 

  time.sleep(0.1)
