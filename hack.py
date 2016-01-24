class Hackathon(object):
    def __init__(self):
        self.hack_count = 0
        self.expos = set()

    def add_expo(self, expo):
        if not isinstance(expo, Expo):
            raise TypeError('Argument is not of type Expo.')
            return False
        self.expos.add(expo)
        return True


class Expo(object):
    def __init__(self, hackathon):
        self.hack_count = 0
        self.hackathon = hackathon
        self.hacks = set()
        self.routes = dict()
        return

    def add_hack(self, hack):
        if not isinstance(hack, Hack):
            raise TypeError('Argument is not of type Hack.')
            return False
        # Add to master list
        self.hacks.add(hack)
        # Add to route dictionary
        if not hack.route in self.routes.keys():
            self.routes[hack.route] = set()
        self.routes[hack.route].add(hack)
        # Increment this expo and the hackathon's hack count
        self.hack_count += 1
        self.hackathon.hack_count += 1
        # Point the hack to this expo
        hack.expo = self
        return True

    def remove_hack(self, hack):
        if hack not in self.hacks:
            raise AttributeError('Hack not found in this expo.')
            return False
        self.hacks.remove(hack)
        return True


class Hack(object):
    def __init__(self, name, url, sponsor_list, route):
        self.name = name
        self.url = url
        self.sponsor_list = sponsor_list.split(',')
        self.route = route
        self.expo = None
        return
