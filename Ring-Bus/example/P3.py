
import machine, time
u2 = machine.UART(2, baudrate=921600, tx=17, rx=16) #

pid = b'P3'

def sim():
    global u2

    # all read their rx
    cnt = 0
    while True:
       #msg = u2.readline()
       #msg = u2.read(256)
       data = u2.read()
       if data:
#          print('Message read@P3', msg)
          break
       else: # do something else
          time.sleep(0.02)
          cnt += 1
          if cnt > 250: print('Timeout'); return True # timeout cnt*0.02 (5 sec)
    for msg in data.split(b'\n'):
       if msg:
          mid = bytes(msg[:2])
          print('IDENT:', mid, pid, mid[0])
          if mid != pid:
             if chr(mid[0]) == 'P':   # Valid header
                w = u2.write(msg+b'\n') # forward the message
                u2.flush()
                #time.sleep(0.2)
          else:
             print('My MSG:', msg)
    tt = time.ticks_us()
    msg = f'P3 the ticks_us at P3 was {tt}\n' # new message
    w = u2.write(msg) # 
    u2.flush()
    #time.sleep(0.2)
    return True # next round

# start off
msg = f'P3 Hello!!\n'
w = u2.write(msg)
u2.flush()

while True:
   w = sim()
   if not w: break
   time.sleep(1)

print('Simulation stop')

