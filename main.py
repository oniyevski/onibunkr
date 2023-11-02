import requests, time, os, argparse
from modules.advancedWrite import AdvancedWrite
from bs4 import BeautifulSoup
from colorama import init, Fore, Back
init()

aw = AdvancedWrite()
s = requests.session()
VERSION = "v1.1"
PROG = "onibunkr"


parser = argparse.ArgumentParser(description="You can learn how to use arguments and what they do here.", formatter_class=argparse.ArgumentDefaultsHelpFormatter, prog=PROG)
parser.add_argument("bunkr_url", help='Any "bunkr" album link.', type=str)
parser.add_argument("album_name", help='Specify here the name under which the album is saved when it is saved on your computer.', type=str)
parser.add_argument("-d", "--download", help="Should album contents be downloaded to the computer?", choices=["y", "n", "yes", "no"], default="no")
parser.add_argument("-t", "--timeout", help="Limit the download and album browsing speed with this argument if connections time out.", default=1, type=int)
parser.add_argument("-dn", "--download_name", help='Albums are normally downloaded to the browser with the same name as on the site, but you can change the name of the downloaded files to a fixed value. For example: "onibunkr file" the files will now be named "onibunkr file 0, onibunkr file 1".', default="bunkr_file_name", type=str)
parser.add_argument('-v', "--version", action='version', version=f'%(prog)s {VERSION}')
args = parser.parse_args()
config = vars(args)

os.system('cls' if os.name == 'nt' else 'clear')

logo = f"""
{Fore.LIGHTGREEN_EX}               _ __                __            
{Fore.LIGHTGREEN_EX}  ____  ____  (_) /_  __  ______  / /______
{Fore.LIGHTBLUE_EX} / __ \/ __ \/ / __ \/ / / / __ \/ //_/ ___/
{Fore.LIGHTBLUE_EX}/ /_/ / / / / / /_/ / /_/ / / / / ,< / /    
{Fore.LIGHTCYAN_EX}\____/_/ /_/_/_.___/\__,_/_/ /_/_/|_/_/     {Back.LIGHTCYAN_EX}{Fore.BLACK} {VERSION} {Fore.RESET}{Back.RESET}

{Fore.LIGHTCYAN_EX}                   developed by {Fore.LIGHTBLUE_EX}oniyevski{Fore.RESET} 
"""
print(logo)

try:
    albumCheck = s.get(config["bunkr_url"])
    albumCheckSource = BeautifulSoup(albumCheck.content, "html.parser")
    getAlbumCheckElement = albumCheckSource.find_all("select", attrs={"id":"filterDropdown"})
    if not getAlbumCheckElement:
        aw.warning("No such album was found on bunkr.")
        exit()
    album = s.get(config["bunkr_url"])
    albumSource = BeautifulSoup(album.content, "html.parser")
    getAllAlbumATag = albumSource.find_all("a", attrs={"class":"grid-images_box-link"})
    getAllAlbumATag.reverse()
    os.makedirs(os.path.join(".", "albums"), exist_ok=True)
    try:
        os.mkdir(os.path.join("albums", config["album_name"])) 
    except:
        aw.error(f'The album named "{config["album_name"]}" is already in the "albums" folder, so if you want to use a different album, try again with a different name.')
        exit()
    counter = 0
    for aTag in getAllAlbumATag:
        try:
            aTagHREF = f"https://bunkrr.su{aTag.get('href')}"
            albumItem = s.get(aTagHREF)
            albumItemSource = BeautifulSoup(albumItem.content, "html.parser")
            albumItemATag = albumItemSource.find("a", attrs={"class":"bg-blue-500"})
            if albumItemATag == None:
                albumItemATag = albumItemSource.find("a", attrs={"class": "rounded-[5px]"})
            f = open(f"albums\\{config['album_name']}\\urls.txt", "+a")
            f.write(albumItemATag.get("""href""")+"\n")
            f.close()
            mediaName = albumItemATag.get("""href""").split("/")[-1]
            if len(mediaName) > 70:
                mediaName = albumItemATag.get("""href""").split("/")[-1][:70] + "..."
            if config["download"] in ["yes", "y"]:
                aw.info(f'"{mediaName}" downloading...')
                response = requests.get(albumItemATag.get("""href"""))
                if response.status_code == 200:
                    if config["download_name"] == "bunkr_file_name":
                        downloadFileName = albumItemATag.get("""href""").split("/")[-1]
                    else:
                        downloadFileName = config["download_name"] + f" {counter}." + albumItemATag.get("""href""").split("/")[-1].split(".")[-1]
                        counter += 1
                    with open(f"albums\\{config['album_name']}\\" + downloadFileName, "wb") as file:
                        file.write(response.content)
            aw.success(f'"{mediaName}" saved.')
            time.sleep(config["timeout"]) 
        except Exception as e:
            aw.warning(f"{aTagHREF} album track could not be reached or downloaded. This might be because you are sending too many requests to the bunkr servers. You can try limiting the speed with the -timeout argument.")
            time.sleep(15)
except Exception as e:
    aw.error(str(e))