#DBWriter is ment to handle all the database interactions.
#this means it needs to both take in data and give out data.
#also handle the file that the database should talk to.
#I will call the files clusters and each cluster will designed.
import sys
import os
import json


class DBWriter: 
    def __init__(self):
        self.database_path = "./Database/";
        self.cluster = "";
        self.schema = None;

    def set_cluster(self, cluster_name) :
        self.cluster = cluster_name
        if self.is_cluster_defined():
            self.cluster = "";
            return None;
        else:
            return self.cluster;


    def get_cluster(self):
        if self.is_cluster_defined():
            return None;
        
        #get the cluster that is defined
        return self.read_file(self.cluster);
            
    def read_file(self, filename): #can only read from the database. 
        fd = open(self.database_path + filename);

        try:
            return json.loads(fd);
        except json.JSONDecodeError as err: 
            print(err);
            return None;

    def is_cluster_defined(self): #returns None if not defined or the full path if defined.
        if(os.path.isfile(self.database_path + self.cluster)):
            return True;
        else :
            return False;
            



class CommandHandler:
    def __init__(self):
        self.db_writer = DBWriter();

    #will handle the data that is incomming will have a {command : !command, argc : !args}; 
    def handler(self,incomming_data):
        
        incomming_data = json.loads(incomming_data)

        command = incomming_data["command"];



        if(command == "Get"):
           return self.db_writer.get_cluster() 

        elif(command == "Set"):
            return self.db_writer.set
        elif(command == "Update"):


        else:
            print("Not a command in the the database.");

#mabye define own schemas but that will mabye undermind the hole project tobe easy and dynmic.
class Schema:
    def __init__(self):
        self.define = None;
