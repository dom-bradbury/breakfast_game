class Engine(object):
    def __init__(self, scene):
        self.scene = scene
        self.opening_scene = scene
        self.locations = []

    def play(self):
        current_scene = self.scene

        while True:
            new_scene = current_scene.enter()
            if new_scene:
                current_scene = new_scene
            else:
                current_scene = self.opening_scene

    def unlock_location(self, location):

        self.locations.append(location)


class Scene(object):

    def enter(self):
        print("This scene hasn't been written yet\n")
        return None


class Location(Scene):

    def __init__(self, name, visible=1):
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

    def choice(self):

        while True:
            for key, val in self.option_dict.items():
                print("%d: %s" % (key, val))

            answer = int(input("> "))

            if answer not in self.option_dict:
                print(self.error_response)
                continue

            print(self.response_dict[answer])
            return answer


class LocationSelector(Selector):

    def __init__(self, game):
        self.locations = game.locations
        self.location_dict = {i + 1: j.name for i, j in enumerate(self.locations)}
        self.error_response = 'You can''t go there yet'
        Selector.__init__(self, self.location_dict, self.location_dict, self.error_response)

    def choose_location(self):
        print('Where would you like to go next?\n')
        next_location = self.choice() - 1
        return self.locations[next_location]


class Choice(Selector):
    def __init__(self, possible_answers, responses, error_response):
        answer_dict = {i + 1: j for i, j in enumerate(possible_answers)}
        response_dict = {i + 1: j for i, j in enumerate(responses)}
        Selector.__init__(self, answer_dict, response_dict, error_response)
