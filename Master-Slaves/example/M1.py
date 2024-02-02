
import machine, time
u1 = machine.UART(1, tx=13, rx=12) # master Rx 12 and 14

#sx = {'S1':12, 'S2':14} # slaves Tx input to master - check your wiring
sx = {'S1':14, 'S2':12} # slaves Tx input to master

def sim(s):
    global u1, sx

    # prepare to listen to slave s
    u1.deinit()
    u1 = machine.UART(1, tx=13, rx=sx[s]) # enable rx@master for the slave s

    tt = time.ticks_us()
    msg = f'{s} the ticks_us at M1 is {tt}'
    w = u1.write(msg) # master send to 2 rx lines
    u1.flush()
    if w == len(msg):
       print('Message sent from M1')
    else:
       print('Stop')
       return False

    # time.sleep(0.02) # a short wait

    # master read response
    cnt = 0
    while True:
       w = u1.read(256)
       if w:
          print('Message read@M1', w)
          break
       else: # do something else
          time.sleep(0.02)
          cnt += 1
          if cnt > 250: print('Timeout'); break # timeout cnt*0.02 (5 sec)

    return True

c = 0
while True:
   s = c%2
   if s == 0:
      w = sim('S1')
   else:
      w = sim('S2')
   if not w: break
   c += 1
#   time.sleep(1)

print('Simulation stop')


