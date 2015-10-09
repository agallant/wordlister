#!/usr/bin/env python

"""
Generate a common word list based on web content.
"""

from bs4 import BeautifulSoup
import sys
import urllib.request

# Default websites to get words from
WEBSITES = {
    'en': 'https://news.google.com/?hl=en'
}


def main():
  args = sys.argv[1:]  # TODO parse args to allow for other options
  response = urllib.request.urlopen(WEBSITES['en'])
  html = response.read()
  soup = BeautifulSoup(html, 'html.parser')
  print(soup.prettify())


if __name__ == "__main__":
  main()
