import csv
from pathlib import Path

from main.health.models import FitbitDailyActivity
from main.utility.functions import LoggingService


log = LoggingService()


class FitbitCSVImporter:
    def __init__(self):
        self.read_csv()

    def read_csv(self):
        filename = "/home/linux/fitbit_export_20230125.csv"
        if Path(filename).exists():
            log.debug(f"File path exists: {filename}")
            FitbitDailyActivity.objects.all().delete()
            log.debug("ProjectDetail deleted!")

            with open(file=filename, encoding="utf-8", mode="r") as csvf:
                try:
                    csv_dict = list(csv.DictReader(csvf))
                    log.debug(csv_dict)
                    objs = [
                        FitbitDailyActivity(
                            date=row["Date"],
                            calories_burned=int(row["Calories Burned"].replace(",", "")),
                            steps=int(row["Steps"].replace(",", "")),
                            distance=float(row["Distance"].replace(",", "")),
                            floors=int(row["Floors"].replace(",", "")),
                            minutes_sedentary=int(row["Minutes Sedentary"].replace(",", "")),
                            minutes_lightly_active=int(row["Minutes Lightly Active"].replace(",", "")),
                            minutes_fairly_active=int(row["Minutes Fairly Active"].replace(",", "")),
                            minutes_very_active=int(row["Minutes Very Active"].replace(",", "")),
                            activity_calories=int(row["Activity Calories"].replace(",", "")),
                        )
                            for row in csv_dict if isinstance(row, dict)
                    ]
                    FitbitDailyActivity.objects.bulk_create(objs)
                    log.info("Data inserted.")

                except Exception as e:
                    print(e)
