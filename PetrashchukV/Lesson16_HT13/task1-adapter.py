import json
import csv


class JSONtoCSVAdapter:
    @staticmethod
    def json_to_csv(json_data, example_csv):
        with open(json_data, 'r') as example_json:
            data = json.load(example_json)

        with open(example_csv, 'w', newline='') as example_csv:
            writer = csv.DictWriter(example_csv, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def csv_to_json(example_csv, json_data):
        with open(example_csv, 'r') as example_csv:
            reader = csv.DictReader(example_csv)
            data = [row for row in reader]

        with open(json_data, 'w') as example_json:
            json.dump(data, example_json, indent=4)


JSONtoCSVAdapter.json_to_csv('example_json.json', 'example1.csv')
JSONtoCSVAdapter.csv_to_json('example_csv.csv', 'output.json')
