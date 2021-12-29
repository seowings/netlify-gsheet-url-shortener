#!/usr/bin/env python
# -*- coding: utf-8 -*- #

"""
netlify-gsheet-url-shortner
A Python based Url Shortener using Netlity and Google Sheets.

MIT License
Copyright (c) 2021 SeoWings www.seowings.org
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# IMPORTS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

import os
import csv
import urllib.request


# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# FUNCTIONS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

def write_index_html(noindex=True, nofollow=True):
    """
    Write Index.html file to be dispalyed as main entry point of redirect subdomain.
    """
    
    index = "noindex" if noindex else "index"
    follow = "nofollow" if nofollow else "follow"

    html_str = f"""
    <html>
    <head>
        <meta name="robots" content="{index},{follow}">
    </head>
    <body>
        Welcome to Google Sheet URL Shortener
    </body>
    </html>
    """

    html_file = open("index.html", "w")
    html_file.write(html_str)
    html_file.close()


def gsheet_to_netlify_toml(google_sheet_url = None):
    """
    Main function to generate netlify.toml file.
    This function download Google Sheets as CSV file and fetch the data.
    """

    if google_sheet_url:
        response = urllib.request.urlopen(google_sheet_url)
        lines = [l.decode("utf-8") for l in response.readlines()]
        gsheet_data = csv.reader(lines)

        rules = []
        for data in gsheet_data:
            if "https://" in data[0] and len(data) == 3:
                rules.append(
                    [
                        f"[[redirects]]\n",
                        f'from = "{data[1].strip()}"\n',
                        f'to = "{data[0].strip()}"\n',
                        f'code = {data[2].strip()}\n',
                        "\n",
                    ]
                )
        
        path = "netlify.toml"
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(["".join(rule) for rule in rules])


if __name__ == "__main__":
    
    google_sheet_url = None # replace if you do not want to specify it via netlify environment variables
    
    if not google_sheet_url:
        google_sheet_url = os.environ.get('gsheet_url')
            
    write_index_html(noindex=False, nofollow=False)
    gsheet_to_netlify_toml(google_sheet_url)
