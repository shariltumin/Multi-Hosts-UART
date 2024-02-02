
In this configuration we have a master and two or more slaves. The master acts as a scheduler and dispatcher of data packets to and from the slaves. The master and the slaves use UART for communication.

You must not connect two or more Tx ports together. This will not work as they will interfere with each other and all we will get is noise.

Let us label our master node as M and the two slave nodes as V and W. The transmit ports of the UART are labelled as Tx and the receive ports are labelled as Rx:

1. master - TxM, RxM
2. slave1 - TxV, RxV
3. slave2 - TxW, RxW

We use no external components. We only use connecting wires.

How to connect is described below (only applies to esp32 board):

```
       Master             Slave 1             Slave 2

    TxM(GPIO13)-------->RxV(GPIO16)-------->RxW(GPIO16)
    RxM1(GPIO12)<-------TxV(GPIO17)
    RxM2(GPIO14)<---------------------------TxW(GPIO17)
       GND------------------GND----------------GND

```

The master node transmitter TxM is connected to both RxV and RxW of the slaves. The slave transmitters are connected to two different ports on the server; TxV is connected to RxM1 and TxW is connected to RxM2. No two transmitter lines are connected together.

Signal on TxM will be seen at RxV and RxW at the same time. RxM1 will only see the signal from slave1 and RxM2 will only see the signal from slave2.

All communication is initiated by the master. When the master wants to talk to slave1, it sets the UART Rx to listen on GPIO12 (RxM1), it will then only listen to TxV. A slave will not write to its Tx ports unless instructed to do so by the master.

We can have as many slave nodes as we like. However, each GPIO pin is rated at 40mA for an ESP32. There is a limit to how many Rx lines a Tx can drive. Each slave needs one GPIO.

There are three scripts in the examples, M1.py, S1.py and S2.py. Connect three boards as described above, and don't forget the common ground. Run M1 on the master node, S1 on the first slave node and S2 on the second slave. These are just simple examples. You can modify this script for more complicated projects. Remember that all packets must pass through M1. There is no direct UART path between the slave nodes.


