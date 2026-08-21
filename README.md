# monash-parking-scraper
First GitHub project be me trying to download Monash University's parking vacancies data into a CSV 

Monash University hosts a JSON of the parking vacancies of every Monash carpark that contains parking sensors (e.g. all the major ones); the JSON is updated every 2 minutes and is available publicly from the following URL:
https://home.student.monash/public/parkingAvailability.json

The web-scraping script ``scraper.py`` is requested by ``scrape.yml`` on GitHub Actions, every 5 minutes, to run and thereby collect that Monash data into ``monash_all_parking_availabilities.csv``.

I'm using this first GitHub project of mine to learn how to use GitHub. For this end, basically all scripts were vibe-coded using Gemini and in setting up this repo I have just done everything as instructed by the Gemini assistant side panel. Have mercy on me. Everyone may enjoy using the ``monash_all_parking_availabilities.csv`` data as they please and lawfully, since I expect the CSV to continue collecting parking data for the foreseeable future, having started accumulating data on 21/08/2026.
