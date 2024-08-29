from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from urllib.parse import urljoin, urlparse

def is_valid_url(url):
    return url and url.startswith('http')

def get_links(driver, wait):
    try:
        links = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//a[@href]')))
        return [link.get_attribute('href') for link in links if link.get_attribute('href')]
    except (TimeoutException, StaleElementReferenceException):
        return []

def check_link(driver, wait, url):
    try:
        driver.get(url)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        if "404" in driver.title.lower() or "not found" in driver.title.lower():
            return 'Page not found'
        return None
    except WebDriverException as e:
        return str(e)

def check_links(base_url, max_pages=10):
    bad_links = []
    visited = set()
    to_visit = [base_url]

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        while to_visit and len(visited) < max_pages:
            current_url = to_visit.pop(0)
            if current_url in visited or not current_url.startswith(base_url):
                continue

            visited.add(current_url)
            print(f"Checking: {current_url}")

            error = check_link(driver, wait, current_url)
            if error:
                bad_links.append((current_url, current_url, error))
                continue

            new_links = get_links(driver, wait)
            for href in new_links:
                if is_valid_url(href) and href not in visited and href.startswith(base_url):
                    to_visit.append(href)

                if href not in visited:
                    error = check_link(driver, wait, href)
                    if error:
                        bad_links.append((current_url, href, error))

    finally:
        driver.quit()

    return bad_links

if __name__ == '__main__':
    website_url = input('Enter the website URL to check: ')
    bad_links = check_links(website_url)

    if bad_links:
        print('Bad links found:')
        for source_page, bad_link, error in bad_links:
            print(f'- {bad_link} (found on {source_page}) {error}')
    else:
        print('No bad links found.')
