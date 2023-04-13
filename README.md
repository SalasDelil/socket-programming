# socket-programming

Socket programming is a way to enable two-way communication between a server
and a client through the internet. In this assignment, a client will interact with a
server over TCP sockets, and it is going to be implemented using Python
programming language.

Transmission Control Protocol (TCP) Sockets
We are going to create a socket object using socket.socket(), specifying the socket
type as socket.SOCK_STREAM. When we do that, the default protocol that’s used
is the Transmission Control Protocol (TCP).
Why should you use TCP?

Is reliable: Packets dropped in the network are detected and retransmitted by the
sender.
Has in-order data delivery: Data is read by our application in the order it was
written by the sender.
In contrast, User Datagram Protocol (UDP) sockets created with
socket.SOCK_DGRAM aren’t reliable, and data read by the receiver can be out-of-
order from the sender’s writes.
