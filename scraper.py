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
        
        as_of_time = data.get('AsOf', 'N/A')
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rows_processed = 0
        
        with open(CSV_FILENAME, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            
            # Added a 6th column for Vacancy_Enabled
            if not file_exists:
                writer.writerow(["Timestamp", "AsOf", "Location", "Permits", "Spots_Available", "Vacancy_Enabled"])
            
            for row in data.get('Rows', []):
                location = row.get('TextDescription', 'Unknown Location')
                
                # We no longer skip rows! We just capture their boolean status.
                vacancy_enabled = row.get('VacancyEnabled', False)
                vacant = row.get('Vacant', 'N/A')
                
                permits_list = row.get('Permits', [])
                permit_names = [p.get('Name', '') for p in permits_list]
                permit_string = " / ".join(permit_names) if permit_names else "None"
                
                # Write all 6 columns to the row
                writer.writerow([timestamp, as_of_time, location, permit_string, vacant, vacancy_enabled])
                rows_processed += 1
                
        print(f"[{timestamp}] Successfully logged {rows_processed} parking zones (As Of: {as_of_time}).")
        
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_and_save_data()
