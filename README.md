# simple_NOAA

Welcome to simple_NOAA, a Python package for accessing weather data from the National Oceanic and Atmospheric Administration (NOAA) through their API. The package includes a dataframe of station metadata, which can be used to request weather data based on location and time.

# Dependencies
- import pandas
- import request
- from shapely.geometry import Point, Polygon
# Usage
The package includes the following functionalities:

- stations_frame: A dataframe of station data from NOAA, this enables stations_in_region
- stations_in_region(lat, lon, num_closest, radius): Returns a list of the num_closest stations within radius kilometers of the point created by lat and lon, enables searching 
- yearly_request(search_type, station_list, year1, year2): Returns a dataframe of global-summary-of-the-year datasets for the requested stations
- monthly_request(search_type, station_list, year1, year2): Returns a dataframe of global-summary-of-the-month datasets for the requested stations
- daily_request(search_type, station_list, year1, year2): Returns a dataframe of daily-summaries datasets for the requested stations
Examples and testing of the package's functionality can be found in the testing.ipynb file.

# Contribution
If you're interested in contributing to the development of the library, please reach out to me at devinrshaw@gmail.com. We welcome bug reports and feature requests.

# License
This package is released under a open-source license. Please refer to the license file for any restrictions on its use.

# Contact
Creator: devinrshaw@gmail.com

# References
Metadata on NOAA stations: https://www.ncei.noaa.gov/access/homr/reports/mshr
NOAA dataset API user documentation: https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation
NOAA datasets explained: https://www.ncdc.noaa.gov/cdo-web/datasets
Explanation of dataset labels: https://www.ncei.noaa.gov/pub/data/metadata/documents/
# FAQs
- What is the package's main purpose?

simple_NOAA is a Python package that provides an easy-to-use interface for accessing weather data from the National Oceanic and Atmospheric Administration (NOAA) through their API.

- What kind of weather data can I request?

You can request global-summary-of-the-year, global-summary-of-the-month, and daily-summaries datasets for specific stations.

- How do I find the stations I want to request data for?

You can use the stations_in_region function to find stations within a certain radius of a given latitude and longitude. Alternatively you can create you own functions using the dataframe staions_frame upon simple_NOAA creation.

- Is there a limit on how much data I can request?

The NOAA API has usage limits, please refer to their API documentation for more information.
Please let me know if you have any other question.
