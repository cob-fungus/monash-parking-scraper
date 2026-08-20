import requests
import csv
from datetime import datetime
import os

API_URL = "https://home.student.monash/public/parkingAvailability.json"
CSV_FILENAME = "monash_all_parking_availabilities.csv"

def fetch_and_save_data():
    file_exists = os.path.exists(CSV_FILENAME)
    
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status() 
        data = response.json()
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rows_processed = 0
        
        with open(CSV_FILENAME, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(["Timestamp", "Location", "Permits", "Spots_Available"])
            
            for row in data.get('Rows', []):
                location = row.get('TextDescription', 'Unknown Location')
                if not row.get('VacancyEnabled', False):
                    continue
                    
                vacant = row.get('Vacant', 'N/A')
                permits_list = row.get('Permits', [])
                permit_names = [p.get('Name', '') for p in permits_list]
                permit_string = " / ".join(permit_names) if permit_names else "None"
                
                writer.writerow([timestamp, location, permit_string, vacant])
                rows_processed += 1
                
        print(f"[{timestamp}] Successfully logged {rows_processed} parking zones.")
        
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_and_save_data()
