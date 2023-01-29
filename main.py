import pandas as pd 
import requests 
import io
from shapely.geometry import Point, Polygon



#automatically will load the metadata from website into emhsr_lite.txt file
def emshr_load():  
  url = 'https://www.ncei.noaa.gov/access/homr/file/emshr_lite.txt'
  r = requests.get(url, allow_redirects=True)
  open('emshr_lite.txt', 'wb').write(r.content)


  
def emshr_parser():  
  df = {}
  rep = 0

  emshr_load()

  with open('emshr_lite.txt', 'r') as file:
    for line in file:
      if rep == 0:
        columns = line.split()
        for column in columns:
          df[column] = []

      elif rep == 1:
        rep += 1
        continue

      
      else:
        df['NCDC'].append(line[0:8])
        df['BEG_DT'].append(line[9:17])
        df['END_DT'].append(line[18:26])
        df['COOP'].append(line[27:33])
        df['WBAN'].append(line[34:39])
        df['ICAO'].append(line[40:44])
        df['FAA'].append(line[45:50])
        df['NWSLI'].append(line[51:56])
        df['WMO'].append(line[57:62])
        df['TRANS'].append(line[63:73])
        df['GHCND'].append(line[74:85])
        df['STATION_NAME'].append(line[86:186])
        df['CC'].append(line[187:189])
        df['CTRY_NAME'].append(line[190:225])
        df['ST'].append(line[226:228])
        df['COUNTY'].append(line[229:264])
        df['CD'].append(line[265:267])
        df['UTC'].append(line[268:271])
        df['LAT_DEC'].append(line[272:281])
        df['LON_DEC'].append(line[282:292])
        df['LOC_PREC'].append(line[293:303])
        df['LAT_DMS'].append(line[304:317])
        df['LON_DMS'].append(line[318:332])
        df['EL_GR_FT'].append(line[333:341])
        df['EL_GR_M'].append(line[342:350])
        df['EL_AP_FT'].append(line[351:359])
        df['EL_AP_M'].append(line[360:368])
        df['TYPE'].append(line[369:466])
        df['RELOCATION'].append(line[470:500])
        df['GHCNMLT'].append(line[501:512])
        df['IGRA'].append(line[513:524])
        df['HPD'].append(line[525:536])
        
      rep += 1
    df = pd.DataFrame(df)
  return df


  


class simple_noaa:

  def __init__(self):
    self.stations_frame = emshr_parser()


  def stations_in_radius(self,lat,lon,num_closest,radius):
    
    closest_station_list = []
    
    location = Point(lat,lon)
    radius_center = location.centroid

    
    
    for i in range(len(self.stations_frame)):
    
      
      station_id = self.stations_frame.loc[i,'GHCND']
      station_coordinate_lat = self.stations_frame.loc[i,'LAT_DEC']
      station_coordinate_lon = self.stations_frame.loc[i,'LON_DEC']


      if station_coordinate_lat.strip() == '' or station_coordinate_lon.strip() == '' or station_id.strip() == '':
        continue
    
      try:
        #station_coordinate_lat = float(station_coordinate_lat)
        station_coordinate_lon = float(station_coordinate_lon)

      except:
        continue
  
      station_coordinate = (station_coordinate_lat, station_coordinate_lon)
      station_coordinate = Point(station_coordinate)

      if station_coordinate.distance(radius_center) < (radius/111.32): #input radius in kilometers changes to degrees of distance
        closest_station_list.append((station_id, station_coordinate.distance(radius_center)))
    

    closest_station_list.sort(key=lambda closest_station_list: closest_station_list[1])
    closest_station_list = closest_station_list[:num_closest]
    
  
    return [x[0] for x in closest_station_list]



  def api_request(search_type, station_list,year1,year2):

    request_stations = ','.join(station_list)
    header = {'token': 'SXCObXMuhoovZxrVZpurQqmsHdvJWyUJ'}
    r = requests.get(f'https://www.ncei.noaa.gov/access/services/data/v1?dataset={search_type}&stations={request_stations}&&startDate={year1}-01-01T00:00:00z&&endDate={year2}-01-01&format=csv', headers=header)
    
    if r.status_code != 200:
      print(r.status_code)
      print(r.text)
    
    add_df = pd.read_csv(io.StringIO(r.text))

      #code to add the rows to the new dataframe to return 
    return add_df