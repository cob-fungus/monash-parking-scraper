# monash-parking-scraper
First GitHub project be me trying to download Monash University's parking vacancies data into a CSV 

Monash University hosts a JSON of the parking vacancies of every Monash carpark that contains parking sensors (e.g. all the major ones); the JSON is updated every 2 minutes and is available publicly from the following URL:
https://home.student.monash/public/parkingAvailability.json

The web-scraping script ``scraper.py`` is run every 6 minutes by [cron-job.org](https://cron-job.org/en/) using ``scrape.yml`` on GitHub Actions to run and thereby collect that Monash data into ``monash_all_parking_availabilities.csv``.

I'm using this first GitHub project of mine to learn how to use GitHub. For this end, basically all scripts were written using Gemini under my invigilation, and in setting up this repo I have just done everything as instructed by the Gemini assistant side panel. Have mercy on me. Everyone may enjoy using the ``monash_all_parking_availabilities.csv`` data as they please and lawfully, since I expect the CSV to continue collecting parking data for the foreseeable future, having started accumulating data on 21/08/2026.

29/08/2026 Okay, I'll probably be hitting file size limits in five months; I'll get back to it in a few weeks, when I'll:
- analyse all data series;
- limit the carparks whose active data series are being collected to only N1 (all permits) and other blue- or red-permit carparks;
- store the data in a wide format, because the data is expected to be very dense, rather than sparse, due to few series' being toggled within any given year; and
- perhaps make a GitHub webpage displaying whether it is predicted that there would be parking spots one hour in the future based on historical trends (and to display interactively the data from ``monash_all_parking_availabilities.csv`` which may be split into monthly files).
