# onibunkr
✨ bunkrr.su album scraper and downloader. ✌️

<h1 align="center">oniBunkr</h1> 

<div align="center">
<a href="https://github.com/topics/html"><img alt="PYTHON" src="https://img.shields.io/badge/PYTHON%20-%23E34F26.svg?&style=for-the-badge"/></a>
<br>
<br>
<a href="https://github.com/oniyevski/onibunkr"><img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103"></a>
<a href="https://github.com/oniyevski/onibunkr"><img src="https://img.shields.io/badge/Built%20by-developers%20%3C%2F%3E-0059b3"></a>
<a href="https://github.com/oniyevski/onibunkr"><img src="https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=yellow"></a>
<a href="https://github.com/oniyevski"><img src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg?v=103"></a>
<a href="https://github.com/oniyevski/onibunkr/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?v=103"></a>
<br>
<br>
<a href="https://github.com/oniyevski/onibunkr/graphs/contributors"><img src="https://img.shields.io/github/contributors/oniyevski/onibunkr?color=brightgreen"></a>
<a href="https://github.com/oniyevski/onibunkr/stargazers"><img src="https://img.shields.io/github/stars/oniyevski/onibunkr?color=0059b3"></a>
<a href="https://github.com/oniyevski/onibunkr/network/members"><img src="https://img.shields.io/github/forks/oniyevski/onibunkr?color=yellow"></a>
<a href="https://github.com/oniyevski/onibunkr/issues"><img src="https://img.shields.io/github/issues/oniyevski/onibunkr?color=0059b3"></a>
<a href="ühttps://github.com/oniyevski/onibunkr/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed-raw/oniyevski/onibunkr?color=yellow"></a>
<a href="https://github.com/oniyevski/onibunkr/pulls"><img src="https://img.shields.io/github/issues-pr/oniyevski/onibunkr?color=brightgreen"></a>
<a href="https://github.com/oniyevski/onibunkr/pulls?q=is%3Apr+is%3Aclosed"><img src="https://img.shields.io/github/issues-pr-closed-raw/oniyevski/onibunkr?color=0059b3"></a> 

</div>
<br>

```terminal
positional arguments:
  bunkr_url             Any "bunkr" album link.
  album_name            Specify here the name under which the album is saved when it is saved on your computer.

optional arguments:
  -h, --help            show this help message and exit
  -d {y,n,yes,no}, --download {y,n,yes,no}
                        Should album contents be downloaded to the computer? (default: no)
  -t TIMEOUT, --timeout TIMEOUT
                        Limit the download and album browsing speed with this argument if connections time out.
                        (default: 1)
  -dn DOWNLOAD_NAME, --download_name DOWNLOAD_NAME
                        Albums are normally downloaded to the browser with the same name as on the site, but you can
                        change the name of the downloaded files to a fixed value. For example: "onibunkr file" the
                        files will now be named "onibunkr file 0, onibunkr file 1". (default: bunkr_file_name)
  -v, --version         show program's version number and exit
```
<br>
<br>

## 📌 REQUIRED

Python Version > 3.6  [i recommend](https://www.python.org/downloads/release/python-386/).

<br>
  ## HOW TO USE IT? 👷 

**1.** Download [this](https://github.com/oniyevski/onibunkr) repository.

**2.** Install the required modules.

```terminal
pip install -r requirements.txt
```

**3.** Let's run the project, for example:.

```terminal
python main.py https://bunkrr.su/a/vs...E7 "Album 1" -d y -dn "ONIYEVSKI BUNKR" -t 2
```
