

class Engine(object):
    def __init__(self, flask=False):
        self.scene = None
        self.locations = []
        self.items = []
        self.flask = flask
        self.i = None
        self.o = None
        self.w = None

    def game_input(self):
        if self.flask:
            self.w.put('Waiting')
            input_str = ''
            while input_str == '':
                input_str = self.i.get()
        else:
            input_str = input("> ")
        return input_str

    def game_output(self, output_str):
        if self.flask:
            self.o.put(output_str)
        else:
            print(output_str)

    def play(self, opening_scene, i, o, w):
        self.i = i
        self.o = o
        self.w = w
        current_scene = opening_scene

        while True:
            new_scene = current_scene.enter()
            if new_scene:
                current_scene = new_scene
            else:
                current_scene = opening_scene

    def unlock_location(self, location):

        if location not in self.locations:
            self.locations.append(location)

    def lock_location(self, location):

        self.locations.remove(location)

    def clear_locations(self):

        self.locations = []

    def obtain_item(self, item):

        self.items.append(item)

    def remove_item(self, item):

        self.items.remove(item)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Scene(object):

    def __init__(self, game=None):
        if game:
            self.game_output = game.game_output
        else:
            self.game_output = print

    def enter(self):
        self.game_output("This scene hasn't been written yet\n")
        return None


class Location(Scene):

    def __init__(self, name, game, visible=1):
        Scene.__init__(self, game)
        self.name = name
        self.visible = visible


class Player(object):

    def __init__(self):
        pass


class Selector(object):

    def __init__(self, option_dict, response_dict, error_response):
        self.option_dict = option_dict
        self.response_dict = response_dict
        self.error_response = error_response

    def choice(self, game):

        while True:
            for key, val in self.option_dict.items():
                game.game_output("%d: %s" % (key, val))

            answer = int(game.game_input())

            if answer not in self.option_dict:
                game.game_output(self.error_response)
                continue

            game.game_output(self.response_dict[answer])
            return answer


class LocationSelector(Selector):

    def __init__(self, game):
        self.locations = game.locations
        self.location_dict = {i + 1: j.name for i, j in enumerate(self.locations)}
        self.error_response = 'You can''t go there yet'
        Selector.__init__(self, self.location_dict, self.location_dict, self.error_response)

    def choose_location(self, game):
        game.game_output('Where would you like to go next?\n')
        next_location = self.choice(game) - 1
        return self.locations[next_location]


class Choice(Selector):
    def __init__(self, possible_answers, responses, error_response):
        answer_dict = {i + 1: j for i, j in enumerate(possible_answers)}
        response_dict = {i + 1: j for i, j in enumerate(responses)}
        Selector.__init__(self, answer_dict, response_dict, error_response)
