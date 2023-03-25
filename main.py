import requests,time,random,argparse,socket,asyncio
from fake_useragent import UserAgent




class Run:
    def __init__(self):
        self.ua = UserAgent().random
        self.check_connection()
        self.check_arguments()
        self.check_wordlist()

    def check_connection(self):
        try:
            socket.create_connection(('www.google.com', 80))
        except OSError:
            print("No internet connection, program is exiting ...")
            exit()

    def check_arguments(self):
        parser = argparse.ArgumentParser(description="Read Commands and works ... ")
        parser.add_argument('-u', metavar='--url', help="Enter target URL ", type=str, required=True)
        parser.add_argument('-w', metavar='--wordlist', help="Enter the wordlist file name", type=str, required=True)
        self.args = parser.parse_args()

    def check_wordlist(self):
        try:
            with open(self.args.w, "r") as f:
                self.dirs = f.read().splitlines()
        except FileNotFoundError as F:
            print(f"Error in File {F}")
            exit()

    async def run(self):
        for dirb in self.dirs:
            headers = {"user-agent": self.ua}
            url = f"{self.args.u}/{dirb}"
            try:
                req = requests.get(url, headers=headers, timeout=10)
                if req.status_code == 200:
                    print(f"Dir is found {url} {req.status_code}")

                    time.sleep(random.uniform(1.5, 2.5))
                elif req.status_code == 302:
                    print(f"Dir needs permission {url} {req.status_code}")
                    time.sleep(random.uniform(1.5, 2.5))
                elif req.status_code == 404:
                    print(f"Dir is not found {url} {req.status_code}")
                    time.sleep(random.uniform(1.5, 2.5))
                else:
                    print(f"Dir {url} {req.status_code}")

            
            except requests.exceptions.ConnectionError:
                print(f"Connection timeout for {url}")
                continue
            except requests.exceptions.ConnectionError:
                print(f"Could not connect to {url}")
                continue


async def main():
    run = Run()
    await run.run()


if __name__ == "__main__":
    asyncio.run(main())
