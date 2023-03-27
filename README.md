# RawDataReplay
Simple client-A side program that connects to a remote server using a TCP socket and sends a log file's contents to the server.

## Usage
Run it with the command python client.py `<ip_address> <port> <log_file>`. 

`python replay-raw-data.py localhost 9004 log.txt`

Replace `<ip_address>` with the IP address of the server, `<port>` with the port number of the server, and `<log_file>` with the path to the log file you want to send to the server.
