# Sitemap URL and Last Modified Date Fetcher

This script automates the process of extracting URLs and their last modified dates from XML sitemaps, including handling nested sitemaps. The extracted data is saved to a CSV file, making it easy to analyze and use for SEO or content management purposes.

## Requirements

- Python 3.x
- `requests` library

## Setup

First, ensure you have Python 3 installed. Then, install the required `requests` library using pip:

```bash
pip install requests
```

## How to Use

1. Edit the script to include the sitemaps you wish to process by modifying the `initial_sitemap_urls` list:

   ```python
   initial_sitemap_urls = [
       'https://example.com/sitemap.xml',
       # Add additional sitemap URLs here
   ]
   ```

2. Run the script from your terminal:

   ```bash
   python3 path/to/script.py
   ```

3. The script will produce a `urls.csv` file in the same directory, containing the URLs and their last modified dates.

## Output File

The output `urls.csv` will have two columns:
- **URL**: The webpage URL found in the sitemap.
- **Last Modified Date**: The date the webpage was last modified, as reported in the sitemap. If this information is not provided in the sitemap, "Not available" will be recorded.

## Contributing

Contributions to improve the script are welcome. Please feel free to fork the repository, make changes, and submit a pull request.
