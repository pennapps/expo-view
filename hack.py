import csv


class Hackathon(object):
    def __init__(self):
        self.hack_count = 0
        self.expos = set()
        self.hacks = set()
        # Maps routes to hacks
        self.routes = dict()
        # Judge codes for expo judges
        self.judge_codes = []
        self.judge_map = dict()

    def set_judge_codes(self, codes):
        self.judge_codes = codes
        for person in codes:
            judge_map[person] = 0
        return True

    def add_expo(self, expo):
        if not isinstance(expo, Expo):
            raise TypeError('Argument is not of type Expo.')
            return False
        self.expos.add(expo)
        return True

    def add_hack(self, hack):
        # Add to hack set and route dictionary
        self.hacks.add(hack)
        if not hack.route in self.routes.keys():
            self.routes[hack.route] = set()
        self.routes[hack.route].add(hack)
        return True

    def write_to_csv(self, output_filename, hacks_per_judge=17):
        with open(output_filename, 'wb') as outputcsv:
            writer = csv.writer(outputcsv)
            # Write top column
            writer.writerow(['expo', 'table', 'project', 'sponsors', 'link', 'route'])
            # Loop through hacks by route so everything is together
            current_judge_code_index = 0
            current_judge_code = self.judge_codes[0]
            for expo in self.expos:
                table_number_counter = 0
                for route in expo.routes.keys():
                    for hack in expo.routes[route]:
                        # Go to next judge code if necessary
                        if table_number_counter % hacks_per_judge == 0:
                            current_judge_code_index += 1
                            if (current_judge_code_index == len(self.judge_codes)):
                                raise AttributeError('Insufficient number of judges. Terminating output write.')
                                return False
                            current_judge_code = self.judge_codes[current_judge_code_index]
                        table_number_counter += 1
                        # Write to output file
                        writer.writerow([
                            expo.number,
                            table_number_counter,
                            hack.name,
                            hack.sponsor_list_raw,
                            hack.url,
                            hack.route,
                            current_judge_code
                        ])
        return True


class Expo(object):
    def __init__(self, hackathon, max_size=100):
        self.hack_count = 0
        self.number = len(hackathon.expos) + 1
        self.hackathon = hackathon
        self.max_size = max_size
        self.hacks = set()
        self.routes = dict()
        return

    def add_hack(self, hack):
        if not isinstance(hack, Hack):
            raise TypeError('Argument is not of type Hack.')
            return False
        # Make sure we haven't exceeded the number of hacks per expo
        if len(self.hacks) >= self.max_size:
            raise AttributeError('Expo maximum size exceeded.')
            return False
        if hack in self.hacks:
            return False
        # Add to master list
        self.hacks.add(hack)
        # Add to route dictionary
        if not hack.route in self.routes.keys():
            self.routes[hack.route] = set()
        self.routes[hack.route].add(hack)
        # Add expo number based on number of expos in hackathon
        self.hack_count += 1
        self.hackathon.hack_count += 1
        # Point the hack to this expo
        hack.expo = self
        # Add to hackathon
        self.hackathon.add_hack(hack)
        return True

    def add_hacks_by_list(self, hack_list):
        for hack in hack_list:
            if not self.add_hack(hack):
                return False
        return True

    def remove_hack(self, hack):
        if hack not in self.hacks:
            raise AttributeError('Hack not found in this expo.')
            return False
        self.hacks.remove(hack)
        self.routes[hack.route].remove(hack)
        self.hack_count -= 1
        return True


class Hack(object):
    def __init__(self, name, url, sponsor_list, route, hackathon):
        self.name = name
        self.url = url
        self.sponsor_list_raw = sponsor_list
        self.sponsor_list = sponsor_list.split(',')
        self.route = route
        self.expo = None
        self.hackathon = hackathon
        hackathon.hacks.add(self)
