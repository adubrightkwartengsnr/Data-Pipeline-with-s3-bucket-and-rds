# import necessary libraries
import requests
import pandas as pd

# create a function to scrape the data
def scrape_data():
    # api endpoint
    endpoint = "https://flightradar243.p.rapidapi.com/v1/flights/most-tracked"

    token = "bearer-token"
    # set the headers
    headers = {
    "X-RapidAPI-Key": "79a1b32ed1mshac16a51ba8187b1p162d29jsn2549136b9466",
    "X-RapidAPI-Host": "flightradar243.p.rapidapi.com"
      }
    
    # Send a get request to the URL
    response = requests.get(endpoint,headers=headers)
    try:
        if response.status_code == 200:
            print("successfuly connected")
            print(response.status_code)
            # parse response as json
            data = response.json()
            return data

        else:
            print("Connection unsuccessful")
            print(response.status_code)
        
    except Exception as e:
        print(e)


# store the return data
json_data = scrape_data()

# check the structure of the json data
print(json_data)

if json_data and 'data' in json_data:
    flight_data = json_data['data']['data']

# convert data to pandas dataframe
df = pd.json_normalize(flight_data)
print(df)

# save the data to a csv file

df.to_csv('flight_data.csv', index=False)