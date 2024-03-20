import csv

def add_row_to_csv(example_csv, row_data):
    with open(example_csv, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row_data)

def delete_row_from_csv(example_csv, row_index):
    rows = []
    with open(example_csv, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]

    print("Before deletion:", rows)

    rows.pop(row_index)

    print("After deletion:", rows)

    with open(example_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def test_add_row_to_csv():
    example_csv = 'test.csv'
    row_data = ['Doe', '40', 'Paris']
    add_row_to_csv(example_csv, row_data)
    with open(example_csv, 'r') as f:
        lines = f.readlines()
        assert lines[-1].strip() == ','.join(row_data)

def test_delete_row_from_csv():
    example_csv = 'test.csv'
    row_index = 0
    delete_row_from_csv(example_csv, row_index)
    with open(example_csv, 'r') as f:
        lines = f.readlines()
        assert len(lines) == 7  # Assuming there were 8 rows before deletion

test_add_row_to_csv()
test_delete_row_from_csv()