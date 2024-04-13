import csv

# Function to get field names from the user
def get_field_names():
    number_of_fields = int(input("How many fields would you like to enter? "))
    field_names = []
    for i in range(number_of_fields):
        field_name = input(f"Enter the name of the field {i + 1}: ")
        field_names.append(field_name)
    return field_names

# Function to add a record based on the field names
def add_record(field_names):
    record = {}
    for field in field_names:
        record[field] = input(f"Enter {field}: ")
    return record

# Function to save records to a CSV file
def save_records(filename, records, field_names):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(records)
    print(f"Data saved to {filename}.")

def main():
    field_names = get_field_names()  # Get the field names from the user
    records = []  # Initialize a list to store the records

    # Main loop to add records
    while True:
        record = add_record(field_names)
        records.append(record)
        continue_input = input("Add another record? (y/n): ")
        if continue_input.lower() != 'y':
            break

    # Save the collected data to a CSV file
    filename = input("Enter the filename to save as (with .csv extension): ")
    save_records(filename, records, field_names)

if __name__ == "__main__":
    main()
