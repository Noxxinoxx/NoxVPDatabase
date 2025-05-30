
from server import DatabaseServer;


def main() :


    server = DatabaseServer("0.0.0.0", 5000);


    print("server is staring!");

    server.start_connection();

if __name__ == "__main__": 
  main();  
