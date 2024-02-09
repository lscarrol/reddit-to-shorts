from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your ChromeDriver
CHROMEDRIVER_PATH = '/path/to/chromedriver'

def find_tiktok_links(url):
    # Initialize Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
    
    try:
        # Load the RSS feed URL
        driver.get(url)
        
        # Wait for the page to load
        WebDriverWait(driver,  10).until(EC.presence_of_element_located((By.TAG_NAME, "item")))
        
        # Find all item tags (each representing a post)
        items = driver.find_elements_by_tag_name("item")
        
        # Extract TikTok links from the descriptions
        tiktok_links = []
        for item in items:
            description = item.find_element_by_tag_name("description").text
            if "tiktok.com" in description:
                tiktok_links.append(description)
        
        return tiktok_links
    finally:
        driver.quit()

# Example usage:
rss_feed_url = 'https://www.reddit.com/r/example/new/.rss'
tiktok_links = find_tiktok_links(rss_feed_url)
for link in tiktok_links:
    print(link)
