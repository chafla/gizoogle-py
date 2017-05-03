"""
Retrieve a gizoogled string. Mostly adapted from a library written in ruby.
Optimized for python3.
"""
import re
import bs4
from urllib import parse
import requests
import argparse


def translate_string(text):
    params = {"translatetext": text}
    url = "http://www.gizoogle.net/textilizer.php"
    resp = requests.post(url, data=params)
    # the html returned is in poor form normally.
    soup_input = re.sub("/name=translatetext[^>]*>/", 'name="translatetext" >', resp.text)
    soup = bs4.BeautifulSoup(soup_input, "lxml")
    giz = soup.find_all(text=True)
    giz_text = giz[39]  # Hacky, but consistent.
    giz_text = giz_text.strip("\n")
    return giz_text


def translate_site(dest_url):
    params = {"search": dest_url}
    return "http://www.gizoogle.net/tranzizzle.php?{}".format(parse.urlencode(params))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make some text a bit more gangster.")
    parser.add_argument("--text", "-t", help="Process text through textilizer.")
    parser.add_argument("--link", "-l", help="Gizoogle a website.")

    args = parser.parse_args()

    if args.text is not None:
        print(translate_string(args.text))
    elif args.link is not None:
        print(translate_site(args.link))
