# MULTI-THREADED HTTP SERVER AND CLIENT

## Multi-threaded web server:
The web server should accept incoming connection requests. It then looks for the GET request and pick out the name of the requestedfile.
If the request is POST then it sends OK message and wait for the
uploaded file from the client.  a GET request from a real WWW
client may have several lines of optional information following the
GET. These optional lines, though, will be terminated by a blank line
(i.e., a line containing zero or more spaces, terminated by a ’\r\n’
(carriage return then line feed characters). The server should first
print out the received command as well as any optional lines following
it (and preceding the empty line).

## HTTP Web Client
The web client reads and parses a series of commands from an input file. The GET and POST commands are handled. The commands syntax is be as follows:

- GET file-name host-name (port-number)
- POST file-name host-name (port-number)

The port number is optional. If it is not specified, use the default HTTP port number, 80. In response to the specified operation (GET or POST),
the client opens a connection to an HTTP server on the specified host listening on the specified (or default) port number. The receiver displays the file and then store it in the local directory (i.e., the
directory from which the client or server program was run). The
client shuts down when reaching the end of the file.
