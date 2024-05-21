import requests
import psycopg2
import json

# PostgreSQL database connection settings
DB_HOST = "localhost"
DB_NAME = "flight_data"
DB_USER = "my_user"
DB_PASSWORD = "password"

# FlightRadar API endpoint
url = "https://flightradar243.p.rapidapi.com/v1/flights/most-tracked"

headers = {
    "X-RapidAPI-Key": "79a1b32ed1mshac16a51ba8187b1p162d29jsn2549136b9466",
    "X-RapidAPI-Host": "flightradar243.p.rapidapi.com"
}

try:
    # Retrieve data from API
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
    data = response.json()

    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Create a table to store the flight data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flights_schema.flights (
            id SERIAL PRIMARY KEY,
            flight_id VARCHAR(255),
            flight VARCHAR(255),
            callsign VARCHAR(255),
            clicks INTEGER,
            from_iata VARCHAR(255),
            from_city VARCHAR(255),
            to_iata VARCHAR(255),
            to_city VARCHAR(255),
            aircraft_model VARCHAR(255),
            aircraft_type VARCHAR(255)
        )
    """)

    # Insert data into the table
    if "data" in data and "data" in data["data"]:
        flights = data["data"]["data"]
        for flight in flights:
            cursor.execute("""
                INSERT INTO flights_schema.flights (flight_id, flight, callsign, clicks, from_iata, from_city, to_iata, to_city, aircraft_model, aircraft_type)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                flight["flight_id"],
                flight["flight"],
                flight["callsign"],
                flight["clicks"],
                flight["from_iata"],
                flight["from_city"],
                flight["to_iata"],
                flight["to_city"],
                flight["model"],
                flight["type"]
            ))
        print("Data loaded successfully into PostgreSQL.")
    else:
        print("No flight data found in the API response.")

    # Commit changes and close the connection
    conn.commit()
except (requests.exceptions.RequestException, psycopg2.Error) as e:
    print(f"Error: {e}")
finally:
    if conn is not None:
        conn.close()
