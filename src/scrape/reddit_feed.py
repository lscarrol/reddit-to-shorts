import requests
import xml.etree.ElementTree as ET
from io import StringIO

def parse_feed(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code ==  200:
        # Parse the XML content
        tree = ET.parse(StringIO(response.text))
        root = tree.getroot()
        
        # Define the namespace map for namespaces used in the XML
        ns = {'atom': 'http://www.w3.org/2005/Atom', 'media': 'http://search.yahoo.com/mrss/'}
        
        # Iterate over each entry in the feed
        for entry in root.findall('atom:entry', ns):
            # Extract the author's name
            author_name = entry.find('atom:author/atom:name', ns).text
            
            # Extract the title
            title = entry.find('atom:title', ns).text
            
            print(f"Title: {title}")
            print("---")
    else:
        print(f"Failed to retrieve the feed. Status code: {response.status_code}")

# Use the provided URL
url = "https://www.reddit.com/r/TikTokCringe/.rss"
parse_feed(url)
