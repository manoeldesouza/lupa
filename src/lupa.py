
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import request
import sys

headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.$'
}


def main():
    if len(sys.argv) != 5:
        usage()
        exit()

    arguments = sys.argv
    page = get_url(arguments[1])
    soup = get_soup(page, arguments[2], arguments[3], arguments[4])

    for each in soup:
        print(each.text)


def get_url(url):

    request_data = urllib.request.Request(url, headers=headers)

    try:
        response_data = urllib.request.urlopen(request_data)
    except:
        print("Bad URL")
        usage()
        exit()
    else:
        page_data = response_data.read()

        return page_data


def get_soup(page, tag, element, value):

    page_soup = BeautifulSoup(page, 'html.parser')
    if page_soup:
        result = page_soup.find_all(tag, {element: value})
        return result


def usage():
    print("lupa <url> <TAG> <element> <value>")
    print("Example:")
    print("lupa http://www.cbc.ca h3 class headline")


if __name__ == "__main__":
    main()
 