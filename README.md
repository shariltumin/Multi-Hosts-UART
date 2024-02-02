
The UART is designed for host-to-host communication. Their Tx and Rx ports are crossed. One transmits, the other receives and vice versa.

Here we are experimenting with a multi-host UART. This means that we have more than two machines communicating via UART.

We do not use any external electronic components - all we use are the connecting wires.

I have found two ways of connecting three esp32 boards:

1. Master-Slaves
2. Ring-Bus

Here I provide descriptions and scripts so that others can try it for themselves. I have tried and with these simple examples the setups worked.

I hope this will be useful to those who need to configure a multi-host UART in their projects.

