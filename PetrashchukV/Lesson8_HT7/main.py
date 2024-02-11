from library import read_domains, match_authors_list, read_author_dates, read_csv, write_to_file

# Task 2
domains = read_domains("domains.txt")
print("Domains:", domains)

# Task 3
authors_list = match_authors_list("authors.txt")
print('Authors list: \n', '\n'.join(authors_list))


# Task 4
author_dates = read_author_dates("authors.txt")
print('Author dates:')
for author in author_dates:
    print(author['date'])

# Task 5
csv_data = read_csv("example.csv")
print("CSV Data:", csv_data)

write_to_file("modified_example.csv", csv_data)

