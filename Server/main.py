
from server import DatabaseServer;


def main() :


    server = DatabaseServer("localhost", 3001);


    print("server is staring!");

    server.start_connection();

if __name__ == "__main__": 
  main();  
