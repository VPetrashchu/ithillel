from library import read_domains, read_surnames, read_author_dates, read_csv, write_to_file

#Task 2
domains = read_domains("domains.txt")
print("Domains:", domains)

#Task3
surnames = read_surnames("authors.txt")
print("Surnames:", surnames)

#Task4
author_dates = read_author_dates("authors.txt")
print("Author dates:", author_dates)

#Task5
csv_data = read_csv("example.csv")
print("CSV Data:", csv_data)

write_to_file("modified_example.csv", csv_data)


