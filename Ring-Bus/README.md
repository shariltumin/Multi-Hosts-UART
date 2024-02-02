
In this configuration, we are connecting UART devices in a ring. Say we have three devices, A, B, and C. The UART transmit output terminals are labelled TxA, TxB, and TxC. The UART receive input terminals are labelled RxA, RxB, and RxC.

We will refer to these devices as nodes.

Connecting these nodes into a ring will look like this:

     TxA-->RxB, TxB-->RxC, TxC-->RxA
     Gnd--GA--GB--GC (common ground)

Suppose node B writes something to its TxB, then the data appears at node C's RxC. Node C reads the data from RxC and can forward it to the next device in the ring, which is node A, by writing the data to its TxC. Node A will read the data from its UART input port RxA. Node A in turn will write the data to its TxA where node B can read from its RxB, completing the circular data path.

In order to prevent the endless circulation of data, each packet is prefixed with a two-byte identifier, e.g. A1, B1 and C1. A message packet 'Hello from B' will then look like b'B1Hello from B'. Such a packet will travel the whole length of the ring. A node will forward all packets that are not labelled with its node identifier. For example, the packet b'B1Hello form B' will be forwarded by node C with node identifier C1. A packet will not be forwarded if the label is equal to the node identifier. The packet b'B1Hello form B' will not be forwarded at node B with node identifier B1.

We can have as many nodes in our ring as we like. However, it only takes one non-functioning node to break the whole chain of nodes. For it to work, every node needs to be up and running, pushing packets through the ring.

There are three scripts in the examples, P1.py, P2.py and P3.py. Connect three boards as described above, and don't forget the common ground. Run P1 on the first board, P2 on the second and P3 on the third. These are just simple examples. You can modify this script for more complicated projects. Remember that all boards must be powered up and processing UART data whenever there is data.

The message packet is a text string ending with a newline. For other packet formats you will need a different processing.


