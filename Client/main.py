import connection;



def main():
    print("Welcome to NoxVPDatabase cli")
    print("____________________________")

    while True:
        command = input("Command : ");
        data = eval(input("Data: "));

        connection.send_command(str(command), data);

if __name__ == "__main__":
    main();

