"""Constants for Hemnet scraper"""

from enum import Enum


class HemnetItemType(str, Enum):
    """Hemnet property item types"""
    VILLA = "villa"
    RADHUS = "radhus"
    BOSTADSRATT = "bostadsratt"
    FRITIDSHUS = "fritidshus"
    TOMT = "tomt"
    GARD = "gard"
    OTHER = "other"


# Hemnet URLs mapping
HEMNET_URLS = {
    "listings": "https://www.hemnet.se/bostader",
    "sold": "https://www.hemnet.se/salda/bostader"
}
