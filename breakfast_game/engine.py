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

        p_a_index = range(0, len(self.possible_answers))  # possible answer index list
        p_a_nums = list(map(str, range(1, len(self.possible_answers) + 1)))

        while True:

            for i in p_a_index:
                print("%d: %s" % (i + 1, self.possible_answers[i]))

            answer = input("> ")

            if answer not in self.possible_answers + p_a_nums:
                print(self.responses[-1])
                continue

            for i in p_a_index:

                if answer == self.possible_answers[i] or answer == p_a_nums[i]:
                    print(self.responses[i])
                    break

            return i + 1