# Client - Server Ping Program

## Problem Definition

Our team was tasked with writing a client <-> server ping program. The client should send 10 messages to the server and receive a corresponding message back. It must also calculate the Round Trip Time (RTT) it took between the client to the server and back. This should be implemented using UDP as its Transport layer protocol. Any message that exceeds one (1) second is considered lost and a "Timed out" message should be shown.

![Client Server Ping Diagram](./img/client-server-ping-diagram.png)
