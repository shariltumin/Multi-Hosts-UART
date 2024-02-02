
import machine, time
u2 = machine.UART(2, tx=17, rx=16) # slave
pid = b'S1'

def sim():
    global u2

    # all slave read their rx
    while True:
       w = u2.read(256)
       if w:
          print('Message read@S1', w)
          break
       else: # do something else
          time.sleep(0.02)
    if bytes(w[:2]) == pid: # if address to me
#       u2.deinit()  # no need
#       u2 = machine.UART(2, tx=17, rx=16) # enable tx@slave
       tt = time.ticks_us()
       msg = f'M1 the ticks_us at S1 is {tt}'
       w = u2.write(msg) # slave S1 reply to master M1
       u2.flush()
       if w == len(msg):
          print('Message sent from S1')
       else:
          print('Stop')
          return False
    return True

while True:
   w = sim()
   if not w: break
   time.sleep(1)

print('Simulation stop')


