import sys
import csv
from hack import Hackathon, Expo, Hack

# Parse command_line arguments
file_list = sys.argv[1:]
csv_file_list = []


# Metadata column numbers (0 is the first column)
# Defaults are consistent with most (BUT NOT ALL) DevPost export formats
COL_NUM_OF = COLUMN_NUMBERS = {
    'SUBMISSION_TITLE': 0,
    'SUBMISSION_URL': 1,
    'SPONSOR_LIST': 8,
    'ROUTE': 7
}
# Number of table spots
HACKS_PER_EXPO_MAX = 200
HACKS_PER_JUDGE = 17
# [Assumes two expos]

OUTPUT_FILE_NAME = 'output.csv'


def split_list(a_list):
    # Utility to split route hack lists
    half = len(a_list)/2
    return a_list[:half], a_list[half:]

##### Begin flow #####

# Inspect files
for name in file_list:
    if not name.endswith('.csv'):
        print("File \"%s\" is not in csv format." % name)
        exit(1)
    csv_file_list.append(name)

# Instantiate PennApps!
pennapps = Hackathon()

# Instantiate expos
expo_1 = Expo(pennapps, HACKS_PER_EXPO_MAX)
expo_2 = Expo(pennapps, HACKS_PER_EXPO_MAX)
pennapps.add_expo(expo_1)
pennapps.add_expo(expo_2)

# Set judge codes
pennapps.judge_codes = ['judge_code']

# Parse and create results
for csv_file in csv_file_list:
    with open(csv_file, "rU") as csvfile:
        # Delimeter and quotechar are optional
        csv_iterator = csv.reader(csvfile)
        # Get first row columns
        first_row = (csv_iterator)

        for row in csv_iterator:
            new_hack = Hack(name=row[COL_NUM_OF['SUBMISSION_TITLE']],
                            url=row[COL_NUM_OF['SUBMISSION_URL']],
                            sponsor_list=row[COL_NUM_OF['SPONSOR_LIST']],
                            route=row[COL_NUM_OF['ROUTE']],
                            hackathon=pennapps
                            )
            pennapps.add_hack(new_hack)

        # Split by route
        for route in pennapps.routes.keys():
            A, B = split_list(list(pennapps.routes[route]))
            expo_1.add_hacks_by_list(A)
            expo_2.add_hacks_by_list(B)

pennapps.write_to_csv('output.csv', HACKS_PER_JUDGE)
