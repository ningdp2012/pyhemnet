# PyHemnet

[![PyPI version](https://badge.fury.io/py/pyhemnet.svg)](https://pypi.org/project/pyhemnet/)
[![Python versions](https://img.shields.io/pypi/pyversions/pyhemnet.svg)](https://pypi.org/project/pyhemnet/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/pypi/dm/pyhemnet)](https://pypi.org/project/pyhemnet/)

A Python library for accessing Hemnet.se property data. Extract property sales information including prices, locations, sizes, and detailed property characteristics.

## Features

- 🏠 **Hemnet Data Access**: Access property sales data from Hemnet.se
  - Get summary statistics on properties for sale and sold properties
  - Extract detailed information including prices, location, size, broker, and more
  - Filter by location and property types
  - Support for multiple property types (villa, radhus, bostadsrätt, etc.)

- 🚀 Easy-to-use Python API
- 💻 Object-oriented design with clean interfaces

## Installation

Install from PyPI:

```bash
pip install pyhemnet
```

Or install from source:

```bash
git clone https://github.com/ningdp2012/pyhemnet.git
cd pyhemnet
pip install -e .
```

## Quick Start

```python
from pyhemnet import HemnetScraper, HemnetItemType

# Create a scraper instance
scraper = HemnetScraper()

# Get summary statistics
listing_count, sold_count = scraper.get_summary(location_id="17744")
print(f"Properties for sale: {listing_count}")
print(f"Sold properties: {sold_count}")

# Get detailed sold properties
homes = scraper.get_sold(
    location_id="17744",
    item_types=[HemnetItemType.VILLA, HemnetItemType.RADHUS]
)

for home in homes:
    print(f"{home['address']} - {home['final_price']} SEK")
```

## Usage

### Initialize the Scraper

```python
from pyhemnet import HemnetScraper, HemnetItemType

scraper = HemnetScraper()
```

### Get Summary Statistics

Get counts of properties for sale and sold:

```python
# Get summary for a specific location
listing_count, sold_count = scraper.get_summary(location_id="17744")
print(f"For sale: {listing_count}, Sold: {sold_count}")

# Filter by property types
listing_count, sold_count = scraper.get_summary(
    location_id="17744",
    item_types=[HemnetItemType.VILLA]
)
```

### Get Sold Properties

Retrieve detailed information about sold properties:

```python
homes = scraper.get_sold(
    location_id="17744",
    item_types=[HemnetItemType.VILLA, HemnetItemType.RADHUS]
)

for home in homes:
    print(f"Address: {home['address']}")
    print(f"Final price: {home['final_price']} SEK")
    print(f"Asking price: {home['asking_price']} SEK")
    print(f"Living area: {home['living_area']}")
    print(f"Sold date: {home['sold_at']}")
    print("---")
```

### Get Current Listings

Get properties currently for sale:

```python
listings = scraper.get_listings(
    location_id="17744",
    item_types=[HemnetItemType.BOSTADSRATT]
)

for listing in listings:
    print(f"Address: {listing['address']}")
    print(f"Price: {listing['asking_price']} SEK")
    print(f"Published: {listing['published_at']}")
```

### Property Types

Use the `HemnetItemType` enum or strings:

```python
# Using enum (recommended)
item_types = [HemnetItemType.VILLA, HemnetItemType.RADHUS]

# Using strings
item_types = ["villa", "radhus"]
```

Available types:
- `VILLA` - Detached houses
- `RADHUS` - Townhouses
- `BOSTADSRATT` - Condominiums
- `FRITIDSHUS` - Vacation homes
- `TOMT` - Land plots
- `GARD` - Farms
- `OTHER` - Other property types

## Data Structure

### Sold Property Data

Each sold property dictionary contains:

```python
{
    'id': str,              # Hemnet ID
    'listing_id': str,      # Listing identifier
    'address': str,         # Street address
    'location': str,        # Location description
    'housing_type': str,    # Type of housing (Villa, Radhus, etc.)
    'rooms': int,           # Number of rooms
    'living_area': str,     # Living area with units
    'land_area': str,       # Land area with units
    'asking_price': int,    # Initial asking price in SEK
    'final_price': int,     # Final sold price in SEK
    'price_change': str,    # Price change information
    'sold_at': str,         # Sale date (YYYY-MM-DD format)
    'broker': str,          # Broker agency name
    'labels': list,         # List of property labels/tags
}
```

### Current Listing Data

Each listing dictionary contains:

```python
{
    'id': str,                      # Hemnet ID
    'address': str,                 # Street address
    'location': str,                # Location description
    'housing_type': str,            # Type of housing
    'rooms': int,                   # Number of rooms
    'living_area': str,             # Living area with units
    'land_area': str,               # Land area with units
    'asking_price': int,            # Asking price in SEK
    'published_at': str,            # Publication date (YYYY-MM-DD)
    'removed_before_showing': bool, # Removed before showing
    'new_construction': bool,       # New construction flag
    'broker_name': str,             # Broker name
    'broker_agent': str,            # Broker agency name
    'labels': list,                 # List of property labels/tags
    'description': str,             # Property description
}
```

## Finding Location IDs

To find Hemnet location IDs:

1. Go to [Hemnet.se](https://www.hemnet.se)
2. Search for your desired location
3. Look at the URL - it contains `location_ids[]=XXXXX`
4. Use that ID in your code

Example: For Stockholm `https://www.hemnet.se/bostader?location_ids[]=17744`, use `location_id="17744"`

## Requirements

- Python 3.10+
- cloudscraper >= 1.2.71
- beautifulsoup4 >= 4.12.0
- requests >= 2.31.0

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This package is created for exploring python and web technologies and learning purposes only. It is **not intended for production use** or commercial applications.

- This is an unofficial package and is not affiliated with or endorsed by Hemnet AB
- Always respect website terms of service and robots.txt directives
- Web scraping may be subject to legal restrictions in your jurisdiction
- Use at your own risk and responsibility
