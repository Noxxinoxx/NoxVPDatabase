#DBWriter is ment to handle all the database interactions.
#this means it needs to both take in data and give out data.
#also handle the file that the database should talk to.
#I will call the files clusters and each cluster will designed.
import sys
import os
import json


class DBWriter: 
    def __init__(self):
        self.database_path = "../Database/";
        self.cluster = "";
        self.schema = None;

    def set_cluster(self, cluster_name) :
        self.cluster = cluster_name
        if not self.is_cluster_defined(self.cluster):
            self.cluster = "";
            return None;
        else:
            return self.cluster;


    def get_cluster(self):
        if not self.is_cluster_defined(self.cluster):
            return None;
        
        #get the cluster that is defined
        return self.read_file(self.cluster);
            
    def read_file(self, filename): #can only read from the database. 
        fd = open(self.database_path + filename, "r");
        
        try:
            return json.loads(fd.read());
        except json.JSONDecodeError as err: 
            print(err);
            return [];

    def write_file(self, filename, data): 
        fd = open(self.database_path + filename, "w");
        
        json_data_as_str = json.dumps(data);

        fd.write(json_data_as_str);

        return True;

        

    def is_cluster_defined(self, cluster_name): #returns None if not defined or the full path if defined.
        if(os.path.isfile(self.database_path + cluster_name)):
            return True;
        else :
            return False;
            

    def update_cluster(self, id, data) :
        if not self.is_cluster_defined(self.cluster) : 
            return None;

        cluster_data = self.read_file(self.cluster) ;

        for obj in cluster_data:
            if obj["id"] == id :
                #update this obj.
                obj["data"].clear();
                obj["data"].append(data);
                self.write_file(self.cluster, cluster_data);
                return obj;
        return None;

    def create_cluster(self, data): 
        if self.is_cluster_defined(data[0]):
            self.set_cluster("");
            return None;
         
        file = open(self.database_path + data[0], "w");

        file.write("[]");

        self.set_cluster(data[0]);

        return True;

    def add_cluster(self, data):
        if not self.is_cluster_defined(self.cluster): 
            return None;
       
        new_id = self.get_last_id() + 1;

        json_data = {"id" : new_id, "data" : data};

        self.append_file(json_data);
        
    def get_last_id(self):
        
        cluster_data = self.get_cluster();
         
        if(len(cluster_data) == 0 or cluster_data[-1]["id"] == None):
            return 0;
        else : 
            return cluster_data[-1]["id"];
    

    def append_file(self, data): 
        cluster_data = self.read_file(self.cluster) ;

        cluster_data.append(data)

        self.write_file(self.cluster, cluster_data);
    

    def get_item_from_id(self, id):
    
        cluster_data = self.get_cluster();

        for item in cluster_data: 
            if(item["id"] == id):
                return item;

        return None;

    def remove_item(self, id):
        #will remove an item with id.
        
        if not self.is_cluster_defined(self.cluster):
            return None;

        cluster_data = self.get_cluster();

        item = self.get_item_from_id(id);
        
        if(item == None):
            return None;

        cluster_data.remove(item);

        updated_cluster = self.move_id_in_cluster(cluster_data);

        self.write_file(self.cluster, updated_cluster);
    
    def move_id_in_cluster(self,current_cluster_data): 
        #this will update all other ids when an cluster item is removed.
        #takes current_cluster_data so I dont need to append twise.
        #I will use recount for this I think.
        
        return self.recount_algo(current_cluster_data);
        
    
    def recount_algo(self, cluster_data):
        #this will recount the hole cluster if an primary key is removed aka id.
        
        id = 1;
        
        for item in cluster_data:
            item["id"] = id;
            id += 1;

        return cluster_data;


    def delete_cluster(self):
        if not self.is_cluster_defined(self.cluster):
            return None;

        os.remove(self.database_path + self.cluster);

        return True;



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
            return self.db_writer.set_cluster(incomming_data["argc"][0])
        elif(command == "Update"):
            return self.db_writer.update_cluster(incomming_data["argc"][0], incomming_data["argc"][1]);
        elif(command == "Create"):
            return self.db_writer.create_cluster(incomming_data["argc"]);
        elif(command == "Add"):
            return self.db_writer.add_cluster(incomming_data["argc"]);
        elif(command == "Remove"):
            return self.db_writer.remove_item(incomming_data["argc"][0]);
        elif(command == "Delete"):
            return self.db_writer.delete_cluster();
        else:
            print("Not a command in the the database.");

#mabye define own schemas but that will mabye undermind the hole project tobe easy and dynmic.
class Schema:
    def __init__(self):
        self.define = None;
