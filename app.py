import requests
import xml.etree.ElementTree as ET
import re
import csv

# Define your initial array of sitemap URLs here
initial_sitemap_urls = [
    'https://www.1mg.com/sitemap.xml',
    # Add more initial sitemap URLs as needed
]

# Output CSV file where URLs and last modified dates will be stored
output_csv = 'urls.csv'

def namespace(element):
    """Extract namespace from an element."""
    m = re.match(r'\{.*\}', element.tag)
    return m.group(0) if m else ''

def process_sitemap(url):
    """Fetch and process a sitemap, recursively handling sitemap indexes."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors

        root = ET.fromstring(response.content)
        ns = namespace(root)  # Extract namespace correctly using re.match

        # Open the CSV file here to append rows for each URL found
        with open(output_csv, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            
            # Check if the sitemap is an index of other sitemaps
            if root.tag == f'{ns}sitemapindex':
                # Process each sitemap listed in the sitemap index
                for sitemap in root.findall(f'.//{ns}sitemap'):
                    sitemap_loc = sitemap.find(f'{ns}loc').text
                    process_sitemap(sitemap_loc)  # Recursive call
            elif root.tag == f'{ns}urlset':
                # Process and save URLs from the sitemap
                for url_element in root.findall(f'.//{ns}url'):
                    url = url_element.find(f'{ns}loc').text
                    lastmod_element = url_element.find(f'{ns}lastmod')
                    lastmod = lastmod_element.text if lastmod_element is not None else 'Not available'
                    csvwriter.writerow([url, lastmod])
                print(f'Appended URLs from {url} to {output_csv}')
    except requests.exceptions.RequestException as e:
        print(f'Failed to fetch or process {url}: {e}')

def main():
    # Ensure the output CSV file has headers before appending data
    with open(output_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["URL", "Last Modified Date"])
    
    for sitemap_url in initial_sitemap_urls:
        process_sitemap(sitemap_url)

if __name__ == '__main__':
    main()
