# simple_NOAA

simple_NOAA object contains dataframe of station metadata 
to be used for requesting data from the NOAA API based on location and time


# dependacies
- pandas 
- io
- request
- from shapely.geometry import Point, Polygon


# usage
simple_noaa.stations_frame is a dataframe of station data from NOAA

simple_noaa.stations_in_region(self,lat,lon,num_closest,radius) 
- lat and lon are floats for latitude and longitude
- num_closest is int of how many stations we want
- radius is float input of how many decimals away stations will be requested  convert this to kilometers  
- returns a list of num_closest stations within radius of point created by lat and lon

simple_noaa.api_request(search_type, station_list,year1,year2)
- returns a dataframe of data for stations inputted

# examples / tests
- examples / testing of funcitonalities is included in testing.ipynb


# contribution
Contribution: Guidelines on how to contribute to the development of the library, including information on how to submit bug reports and feature requests.

# license
License: Information on the license under which the library is released, and any restrictions on its use.

# contact
creator: devinrshaw@gmail.com

# references

metadata on noaa stations https://www.ncei.noaa.gov/access/homr/reports/mshr

noaa dataset api use specified https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation

explanation of dataset lables https://www.ncei.noaa.gov/pub/data/metadata/documents/GSOYReadme.txt

# FAQs
FAQs: Frequently asked questions and their answers, for the most common issues or concerns about the library.
