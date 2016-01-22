import sys
import csv

# Parse command_line arguments
file_list = sys.argv[1:]
csv_file_list = []

# Master dictionary of submissions by route
dict = {}

# Final expo collections
expo_1 = {}
expo_2 = {}


# Route column num
ROUTE_COLUMN_NUMBER = 5
# Number of table spots
NUMBER_OF_TABLE_SPOTS = 150
# [Assumes two expos]

# Utility to split route hack lists
def split_list(a_list):
    half = len(a_list)/2
    return a_list[:half], a_list[half:]



##### Begin flow #####

# Inspect files
for name in file_list:
    if not name.endswith('.csv'):
        print("File \"%s\" is not in csv format." % name)
        exit(1)
    csv_file_list.append(name)

# Parse
for csv_file in csv_file_list:
    with open(csv_file, "rU") as csvfile:
        # Delimeter and quotechar are optional
        csv_iterator = csv.reader(csvfile)
        # Add table number and expo columns to the first row
        first_row = next(csv_iterator)
        first_row.append('Expo')
        first_row.append('Table')

        for row in csv_iterator:
            route_name = row[ROUTE_COLUMN_NUMBER]
            # Create array if key doesn't exist
            if not route_name in dict:
                dict[route_name] = []
                expo_1[route_name] = []
                expo_2[route_name] = []
            # Map row by route and add
            dict[route_name].append(row)

        # Split in half by route
        for route in dict.keys():
            A, B = split_list(dict[route])
            expo_1[route] = A
            expo_2[route] = B

        # Generate expo and table numbers for each entry
        expo_1_table_counter = 1
        expo_2_table_counter = 1
        for route in expo_1.keys():
            for hack in expo_1[route]:
                # Expo number
                hack.append(1)
                # Assign table numbers
                hack.append(expo_1_table_counter)
                expo_1_table_counter += 1
        for route in expo_2.keys():
            for hack in expo_2[route]:
                # Expo number
                hack.append(2)
                # Assign table numbers
                hack.append(expo_2_table_counter)
                expo_2_table_counter += 1

# Generate judge sheets
# For each expo, each judge has 15 hacks
# NUMBER_OF_HACKS_PER_JUDGE



print expo_1['Android']
