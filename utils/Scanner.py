import time

from threading import Thread

from mcstatus import JavaServer, BedrockServer
from mcstatus.status_response import JavaStatusResponse


class Scanner:
    def __init__(self, java: bool, port: int) -> None:
        self.java = java
        self.port = port
        self.threads = []

    def start(self, startRange: tuple[int, int, int, int], endRange: tuple[int, int, int, int]):
        for i in range(startRange[0], endRange[0] + 1):
            for j in range(startRange[1], endRange[1] + 1):
                for k in range(startRange[2], endRange[2] + 1):
                    for l in range(startRange[3], endRange[3] + 1):
                        ip = f"{i}.{j}.{k}.{l}"

                        thread = Thread(target=self.scan, args=(ip, self.port))
                        self.threads.append(thread)
                        thread.start()
                        time.sleep(0.1)

        for thread in self.threads:
            thread.join()

    def scan(self, ip: str, port: int):
        try:
            if self.java:
                server = JavaServer.lookup(ip, port)
                status: JavaStatusResponse = server.status()
                print(
                    f"Server Ip: {ip}:{port}"
                    f"\nMotd: {status.motd.raw['text']}"
                    f"\nVersion: {status.version.name}"
                    f"\nPlayers {status.players.online}/{status.players.max}")
            else:
                server = BedrockServer.lookup(ip, port)
                status: JavaStatusResponse = server.status()
                print(
                    f"Server Ip: {ip}:{port}"
                    f"\nMotd: {status.motd.raw}"
                    f"\nVersion: {status.version.name}"
                    f"\nPlayers {status.players.online}/{status.players.max}")
        except Exception:
            print(f"No server at {ip}:{port}")

