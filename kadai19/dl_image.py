from urllib.request import urlopen


def download_file(url, file_path):
    with urlopen(url) as res, open(file_path, "wb") as wfo:
        wfo.write(res.read())


if __name__ == "__main__":
    url = "https://www.teu.ac.jp/common/images/teulogo_ja_201216.png"
    download_file(url, "data/tutlogo.png")
