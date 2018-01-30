class Engine(object):
    def __init__(self, scene):
        self.scene = scene
        self.opening_scene = scene
        self.locations = {}

    def play(self):
        current_scene = self.scene

        while True:
            new_scene = current_scene.enter()
            if new_scene:
                current_scene = new_scene
            else:
                current_scene = self.opening_scene

    def unlock_location(self, name, scene):

        self.locations.update({name, scene})


class Scene(object):

    def enter(self):
        print("This scene hasn't been written yet\n")
        return None


class Player(object):

    def __init__(self):
        pass


class LocationSelector(object):

    def __init__(self, game):
        self.locations = game.locations

    def choose_location(self):
        print('Where would you like to go next?\n')
        while True:

            for i, loc in enumerate(self.locations.keys()):
                print("%d: %s" % (i+1, loc))

            answer = input("> ")

            #if answer not in list()


class Choice(object):
    def __init__(self, possible_answers, responses):
        self.possible_answers = possible_answers
        self.responses = responses

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