import httpx, random, string, binascii, os, uuid; from concurrent.futures import ThreadPoolExecutor; from itertools import cycle; from colorama import Fore, init 
init(autoreset=True)

def GetProxies():
    with open("proxies.txt", "r") as temp_file:
        proxies = [line.rstrip("\n") for line in temp_file]
    return proxies
proxies = GetProxies()
proxy_pool = cycle(proxies)
def GetProxy():
    proxy = next(proxy_pool)
    if len(proxy.split(":")) == 4:
        splitted = proxy.split(":")
        return f"http://{splitted[2]}:{splitted[3]}@{splitted[0]}:{splitted[1]}"
    else:
        return f'http://{proxy}'

def register():
    while True:
        try:
            ll = "".join(random.choice(string.ascii_lowercase + string.digits) for i in range(8))
            Email=f"{ll}@outlook.com"
            Username=f"{ll}"
            client = httpx.Client(headers = {"authority": "www.guilded.gg","method": "POST", "path": "/api/users?type=email", "scheme": "https", "accept": "application/json, text/javascript, */*; q=0.01", "accept-encoding": "gzip, deflate, br","accept-language": "en-GB,en-US;q=0.9,en;q=0.8", "content-type": "application/json", "guilded-client-id": f"{uuid.uuid1()}","guilded-device-id": str(binascii.b2a_hex(os.urandom(64)).decode("utf-8")), "guilded-device-type": "desktop", "guilded-stag": "c4740afd3f3e4d63d365d826139de166", "origin": "https://www.guilded.gg", "referer": "https://www.guilded.gg/","sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36", "x-requested-with": "XMLHttpRequest", "dnt": "1","Sec-Ch-Ua": '" Not;A Brand";v="99", '"Google Chrome;v=97"', '"Chromium"';v=97',"Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "macOS" } ,proxies=GetProxy())
            RegisterReq=client.post("https://www.guilded.gg/api/users?type=email", json={"email": Email,"fullName": "clipssender ot","name": Username,"password": "github.com/clipssender",})
            if RegisterReq.status_code==200:
                Hmac=RegisterReq.cookies["hmac_signed_session"]
                print(f"{Fore.GREEN}Created Account: {Hmac}:{Email}:{Username}{Fore.RESET}")
                with open("Accounts.txt", "a+") as tk:
                    tk.write(f"{Email}:qpwo12!0-94-23_#$_#$@:{Hmac}\n")
            else:
                print(RegisterReq.json())
                register()
        except Exception as error:
            print(error)
            register()
if __name__=="__main__":
    init()
    threadAmount = input(f"{Fore.BLUE}Number of threads -> {Fore.RESET}")
    threadAmount = 1 if threadAmount == "" else int(threadAmount)
    threads = []
    with ThreadPoolExecutor(max_workers=threadAmount) as guilded: 
        for x in range(threadAmount):
            guilded.submit(register)
