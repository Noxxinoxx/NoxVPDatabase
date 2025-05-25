import socket
import sys
import json
import time


def send_command(Command,data):
        
    try: 
        sock = socket.socket();

    except socket.error as err : 
        print(err)
        sys.exit();

    port = 3001
    address = "localhost"


    json_data = {"command" : Command, "argc" : data}
    json_data = json.dumps(json_data);
    try: 
        sock.connect((address, port));
        sock.send(bytes(json_data, "utf-8"));
    except socket.error as err: 
        print(err)

        sys.exit();


    sock.close();


send_command("Set", ["test.json"])
time.sleep(2)
send_command("Get", ["test.json"])
time.sleep(2)
send_command("Update", [0, {"Name" : "Anders", "Age" : 20}]);
time.sleep(2)
send_command("Create", ["test_cluster.json"]);
time.sleep(2)
send_command("Add", [{"Name" : "ABnders", "Age" : 20}])




