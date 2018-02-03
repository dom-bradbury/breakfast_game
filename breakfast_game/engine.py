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

    def __init__(self, option_dict, response_dict):
        self.option_dict = option_dict
        self.response_dict = response_dict

    def choice(self):

        while True:
            for key, val in self.option_dict.items():
                print("%d: %s" % (key, val))

            answer = int(input("> "))

            if answer not in self.option_dict:
                print(self.response_dict[0])
                continue

            print(self.response_dict[answer])
            return answer


class LocationSelector(object):

    def __init__(self, game):
        self.locations = game.locations

    def choose_location(self):
        print('Where would you like to go next?\n')
        while True:

            for location in self.locations:
                print("%d: %s" % (i+1, loc))

            answer = input("> ")

            #if answer not in list()


class Choice(Selector):
    def __init__(self, possible_answers, responses):
        answer_dict = {i + 1: j for i, j in enumerate(possible_answers)}
        response_dict = {i: j for i, j in enumerate(responses)}
        Selector.__init__(self,answer_dict,response_dict)

    def choice(self):

        answer_dict = {i + 1: j for i, j in enumerate(self.possible_answers)}
        response_dict = {i: j for i, j in enumerate(self.responses)}

        while True:
            print(answer_dict)
            for key, val in answer_dict.items():
                print("%d: %s" % (key, val))

            answer = int(input("> "))

            if answer not in answer_dict:
                print(response_dict[0])
                continue

            print(response_dict[answer])
            return answer