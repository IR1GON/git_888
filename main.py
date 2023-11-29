import requests
import csv
import time

def get_iss_position():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    if response.status_code == 200:
        data = response.json()
        timestamp = data['timestamp']
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        return timestamp, latitude, longitude
    else:
        print("Failed to fetch ISS position")
        return None, None, None

def write_to_csv(file_path, data):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(data)

if __name__ == "__main__":
    csv_file = 'iss_positions.csv'

    while True:
        timestamp, latitude, longitude = get_iss_position()
        if timestamp and latitude and longitude:
            data_to_write = [timestamp, latitude, longitude]
            write_to_csv(csv_file, data_to_write)
            print(f"Position recorded: Timestamp - {timestamp}, Latitude - {latitude}, Longitude - {longitude}")
        time.sleep(5)
