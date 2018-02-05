from breakfast_game.engine import Engine, Scene, Choice, Location, LocationSelector


class Intro(Scene):

    def enter(self):
        print("INTRO\n"
              "You slowly wake up on a bed of hay in a stable\n"
              "You don't know who you are, where you are, or how you got there\n"
              "There is one thing you do know\n"
              "You are hungry, you need breakfast\n\n")
        print("What do you do next?\n")
        possible_answers = ['Go back to sleep',
                            'Stumble outside']
        responses = ['You snuggle down with the nearest donkey\n',
                     'You stumble out of the stable door into the blinding light of the day\n']
        error_response = '"I should really make a decision"\n'

        path = Choice(possible_answers, responses, error_response).choice()
        if path == 1: return Intro()
        if path == 2: return Market()
        print('iehdihwefiuhwiufeh')


class Market(Scene):

    def enter(self):
        print("Market")

        game.unlock_location(Butcher)
        game.unlock_location(Baker)
        game.unlock_location(Tavern)

        path = LocationSelector(game).choose_location()
        return path()


class Butcher(Location):
    name = 'Butcher'

    def __init__(self):
        Location.__init__(self, 'Butcher')


class Baker(Location):
    name = 'Baker'

    def __init__(self):
        Location.__init__(self, 'Baker')


class Tavern(Location):
    name = 'Tavern'

    def __init__(self):
        Location.__init__(self, 'Tavern')



print('Welcome to Baconia!\n')
scene = Intro()
game = Engine(scene)
game.play()
