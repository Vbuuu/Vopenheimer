from utils.Scanner import Scanner


def main():
    serverType = input("Do you want to scan for (B)edrock or (J)ava server?: \n")
    addrRange = input("Enter in the IP range (e.g. 1.1.1.1-2.2.2.2): \n").split("-")
    port = int(input(f"Enter in the port (e.g. {25565 if serverType == 'J' else 19132}): \n"))

    startRange = addrRange[0].split(".")
    endRange = addrRange[1].split(".")

    # make list(str) to list(int)
    startRange = [int(x) for x in startRange]
    endRange = [int(x) for x in endRange]

    startRange = (startRange[0], startRange[1], startRange[2], startRange[3])
    endRange = (endRange[0], endRange[1], endRange[2], endRange[3])

    scanner = Scanner(serverType == "J", port)
    scanner.start(startRange, endRange)


if __name__ == "__main__":
    main()
