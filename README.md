# Website Link Checker

This Python script checks for broken links on a given website using Selenium WebDriver.

## Features

- Crawls through a specified website
- Checks for broken links (404 errors, connection issues, etc.)
- Handles dynamic content using Selenium
- Respects the website's structure (doesn't check external links)

## Requirements

- Python 3.6+
- Selenium WebDriver
- Chrome browser

## Installation

1. Clone this repository or download the source code.
2. Install the required packages:

```
pip install -r requirements.txt
```

3. Make sure you have Chrome browser installed on your system.

## Usage

Run the script using Python:

```
python website_link_checker.py
```

When prompted, enter the URL of the website you want to check.

## Output

The script will print the URLs it's checking in real-time. After completion, it will display a list of bad links found, including:
- The problematic URL
- The page where the link was found
- The error message associated with the link

## License

MIT License

Copyright (c) 2024 Tatsu Ikeda

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