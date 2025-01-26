import os
import sys
import httpx
from colorama import Fore, init
# this is chatgpt lol!!
# kys if you say im a skid


init(autoreset=True)

# Define color codes for better readability
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
white = Fore.WHITE
reset = Fore.RESET

proxy_urls = [
'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
'https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
'https://api.openproxylist.xyz/http.txt',
'https://api.proxyscrape.com/v2/?request=displayproxies',
'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
'http://worm.rip/http.txt',
'https://proxyspace.pro/http.txt',
'https://multiproxy.org/txt_all/proxy.txt',
'https://proxy-spider.com/api/proxies.example.txt',
]  
     # Name of the file to store the downloaded proxies
proxy_file_name = "proxy.txt"


def main():
    """
    Main function to download and save proxies
    """

    # Check if the proxy file already exists
    if os.path.isfile(proxy_file_name):
        print(f"{red}File {proxy_file_name} already exists!{reset}")
        print(f"{yellow}Downloading a new {proxy_file_name}...{reset}")
        # Clear the console screen (Windows: 'cls', Linux/Mac: 'clear')
        #os.system('cls' if os.name == 'nt' else 'clear')
        # Remove the existing file
        os.remove(proxy_file_name)

    # Open the proxy file in append mode (to add new proxies without overwriting)
    with open(proxy_file_name, 'a') as proxy_file:
        for proxy_url in proxy_urls:
            try:
                # Download the proxy list from the URL
                response = httpx.get(proxy_url)
                proxy_data = response.text

                # Write the downloaded proxy data to the file
                proxy_file.write(proxy_data)

                # Print a success message with the downloaded URL
                print(f"-> Fetched {green}{proxy_url}{reset}")
            except httpx.HTTPError as error:
                print(f"[!] Error downloading from {proxy_url}: {error}")

    # Count the total number of proxies saved in the file
    with open(proxy_file_name, 'r') as proxy_file:
        total_proxies = sum(1 for line in proxy_file)

    print(f"\n{white}{yellow}{total_proxies}{white} {green}Proxies saved to {proxy_file_name}{reset}.")


if __name__ == "__main__":
    try:
        main()
    except IndexError:
        print("An error occurred. Please check the code and try again.")
        sys.exit(1)