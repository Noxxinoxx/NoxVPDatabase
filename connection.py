import socket
import sys
import json





try: 
    sock = socket.socket();

except socket.error as err : 
    print(err)
    sys.exit();

port = 3001
address = "localhost"


json_data = {"data" : "datatest"}
json_data = json.dumps(json_data);
try: 
    sock.connect((address, port));
    sock.send(bytes(json_data, "utf-8"));
except socket.error as err: 
    print(err)

    sys.exit();


sock.close();

