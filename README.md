# Infinite Scroll Web Scraper

## Overview
A specialized web scraper built to handle websites with infinite scrolling functionality. This project specifically targets fintech startup information from Fintastico, demonstrating automated scrolling, data extraction, and multi-format export capabilities.

![image](https://github.com/user-attachments/assets/8fa58198-665f-4476-8028-a9fe921cc964)

## Key Features

### 1. Infinite Scroll Handling
- Automated scroll simulation using Selenium
- Dynamic page height detection
- Intelligent scroll termination
- Configurable scroll pause timing

### 2. Modular Operation Modes
The scraper operates in three distinct modes:
- **Extract Mode**: Processes previously saved page source
- **Scrape Mode**: Performs live web scraping
- **Combined Mode**: Both extracts and scrapes

### 3. Data Processing
- BeautifulSoup4 for HTML parsing
- Structured data extraction:
  - Company titles
  - Website links
  - Company descriptions
- Multi-format export (Excel & JSON)

## Technical Implementation

### Core Dependencies
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
```

### How It Works

#### 1. Infinite Scroll Handling
```python
while True:
    driver.execute_script('window.scrollBy(0,2000)')
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    if(new_height == last_height):
        break
    last_height = new_height
```

#### 2. Data Extraction
```python
data = []
soup = BeautifulSoup(page_source, features="lxml")
items = soup.findAll("a", class_="card")

for item in items:
    item_out = {
        'Title': item.find("h4").text,
        'Link': item.attrs['href'],
        'Description': item.find("p").text
    }
    data.append(item_out)
```

## Getting Started

### Prerequisites
```bash
pip install selenium beautifulsoup4 pandas openpyxl
```

### Chrome WebDriver Setup
1. Download ChromeDriver matching your Chrome version
2. Add to system PATH or specify path in code

### Configuration
```python
path_to_file = "your/path/here/"
url = "https://www.fintastico.com/fintech-uk/"
mode = "extract"  # Options: "extract", "scrape", or "" for both
```

### Running the Scraper
```bash
python fintech_scraper.py
```

## Output Formats

### 1. Excel Output (startups.xlsx)
- Structured spreadsheet format
- Easy to read and analyze
- Compatible with data analysis tools

### 2. JSON Output (startups.json)
- Machine-readable format
- Ideal for API integration
- Preserves data structure

## Key Technical Features

### 1. Robust Scroll Detection
- Monitors page height changes
- Prevents infinite loops
- Ensures complete data capture

### 2. Error Handling
- Graceful scroll termination
- File operation safety checks
- Encoding management (UTF-8)

### 3. Memory Efficiency
- Incremental data collection
- Optimized page source storage
- Efficient DOM parsing

## Potential Applications
1. Market Research
2. Competitor Analysis
3. Investment Research
4. Startup Discovery
5. FinTech Industry Analysis

## Future Improvements
1. Add proxy support
2. Implement retry mechanisms
3. Add data validation
4. Include rate limiting
5. Add more export formats
6. Implement concurrent scraping

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/infinite-scroll-scraper

# Install required packages
pip install -r requirements.txt

# Run the scraper
python fintech_scraper.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgments
- Selenium Documentation
- BeautifulSoup4 Documentation
- Fintastico for the data source

---
*Note: Please ensure compliance with the website's terms of service and robots.txt when using this scraper.*
