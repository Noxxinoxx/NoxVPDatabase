import socket
from DB import CommandHandler
from DB import DBWriter

#This is the main obj for the connection between the database and the client.
class DatabaseServer: 
    def __init__(self, address, port) :
        self.socket = socket.socket();
        self.port = port;
        self.address = address;
        #create a new database writer.
        self.db_writer = DBWriter();
        self.command_handler = CommandHandler();
        self.socket.bind((self.address, self.port));

    def start_connection(self): 
        self.socket.listen(5); 
        while True: 
            
            c,addr = self.socket.accept();


            #database writer.
            
            #data will be in the for of a string.
            data = c.recv(1024).decode(); 
            
            #print("Command : " + data + " Result: " + str(self.command_handler.handler(data)));
            #print("cluster : " + self.command_handler.db_writer.cluster);
            
            result = str(self.command_handler.handler(data));

            c.sendall(result.encode());

            c.close();
    

