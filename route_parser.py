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

# Sponsor prize counts
expo_1_sponsor_prize_counts = {}
expo_2_sponsor_prize_counts = {}


# Metadata column numbers (0 is the first column)
# Defaults are consistent with most (BUT NOT ALL) DevPost export formats
COL_NUM_OF = COLUMN_NUMBERS = {
    SUBMISSION_TITLE: 0,
    SUBMISSION_URL: 1,
    SPONSOR_LIST: 8,
    CUSTOM_CATEGORY: 7
}
# Number of table spots
NUMBER_OF_TABLE_SPOTS = 150
# [Assumes two expos]

OUTPUT_FILE_NAME = 'output.csv'

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
        # Add table nunextmber and expo columns to the first row
        first_row = (csv_iterator)
        first_row.append('Expo')
        first_row.append('Table')

        for row in csv_iterator:
            route_name = row[COL_NUM_OF.CUSTOM_CATEGORY]
            # Create array if key doesn't exist
            if not route_name in dict:
                dict[route_name] = []
                expo_1[route_name] = []
                expo_2[route_name] = []
            # Map row by route and add
            dict[route_name].append({
                project: row[COL_NUM_OF.SUBMISSION_TITLE],
                sponsor: row[COL_NUM_OF.SPONSOR_LIST],
                category: row[COL_NUM_OF.CUSTOM_CATEGORY],
                link: row[COL_NUM_OF.SUBMISSION_URL]
                })

        # Split in half by route
        for route in dict.keys():
            A, B = split_list(dict[route])
            expo_1[route] = A
            expo_2[route] = B


        # Sponsor prize sorting
        # for route in expo_2.keys():
        #     for hack in expo_2[route]:
        #         for sponsor_prize in hack[SPONSOR_PRIZE_COLUMN_NUMBER].split(','):
        #             if not sponsor_prize in expo_1_sponsor_prize_counts:
        #                 expo_1_sponsor_prize_counts[sponsor_prize] = 0
        #             expo_1_sponsor_prize_counts[sponsor_prize] += 1
        # for route in expo_2.keys():
        #     for hack in expo_2[route]:
        #         for sponsor_prize in hack[SPONSOR_PRIZE_COLUMN_NUMBER].split(','):
        #             if not sponsor_prize in expo_2_sponsor_prize_counts:
        #                 expo_2_sponsor_prize_counts[sponsor_prize] = 0
        #             expo_2_sponsor_prize_counts[sponsor_prize] += 1

        # for sponsor_prize in expo_1_sponsor_prize_counts:
        #     if expo_1_sponsor_prize_counts[sponsor_prize] > expo_2_sponsor_prize_counts[sponsor_prize] + SPONSOR_PRIZE_SIZE_THRESHOLD

        ##### EXPO AND TABLE NUMBER GENERATION #####

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


# Write to output file
output_file = open(OUTPUT_FILE_NAME)
with output_file as outputcsv:
    writer = csv.writer(outputcsv)
    writer.writerow(['expo', 'table', 'project', 'sponsors', 'link', 'category'])
    for route in expo_1:
        for hack in expo_1[route]:
            writer.writerow([1, hack])

# Generate judge sheets
# For each expo, each judge has 15 hacks
# NUMBER_OF_HACKS_PER_JUDGE



print expo_1['Android']
