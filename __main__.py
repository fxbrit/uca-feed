from bs4 import BeautifulSoup
import requests
import os

def __main():
    url = "https://ungoogled-software.github.io/ungoogled-chromium-binaries/releases/archlinux/"
    filename = os.getcwd()+os.sep+"version.txt"
    if not os.path.isfile(filename):
        f= open(filename,"w+")
        f.write("0.0.0.0-0")
        f.close
    f = open(filename, "r", encoding="utf-8")
    current = f.read()
    f.close()
    r=requests.get(url, timeout=50)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.content, "html.parser")
    versions = soup.findAll("a")
    # fourth <a> contains latest release
    last_ver = str(versions[3])
    begin = last_ver.find(">")
    end = last_ver.find("</a>")
    ver = last_ver[begin+1:end]
    if ver != str(current):
        print("NEW: binaries for version "+ver+" are available at "+url+ver)
        f = open(filename, "w", encoding="utf-8")
        f.write(ver)
        f.close()
    else:
        print("no updated binary version available since "+current)

if __name__ == "__main__":
    __main()