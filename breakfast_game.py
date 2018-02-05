from breakfast_game.engine import Engine, Scene, Choice, Location, LocationSelector, bcolors


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

    def enter(self):
        print(bcolors.OKGREEN + '"A customer! A customer! What a glorious day!"' + bcolors.ENDC)
        print('"Take a look at my fine sausages, they are they best in town"')
        print('What would you like?')

        possible_answers = ['Sausage',
                            'Bacon']
        responses = ['Ohh, good choice!\n',
                     'I recommend you cook it extra crispy\n']
        error_response = '"I should really make a decision"\n'

        meat_choice = Choice(possible_answers, responses, error_response).choice()
        meat = possible_answers[meat_choice-1]

        possible_answers = ['Apologise and leave',
                            'Steal the %s!' % meat]
        responses = ['Pfft, go eat breadcrumbs like a little pigeon you worthless wretch\n',
                     'GUARDS! GUARDS! He has stolen my %s!\n' % meat]
        error_response = '"I should really make a decision"\n'

        response = Choice(possible_answers, responses, error_response).choice()

        if response == 2:
            game.obtain_item(meat)

        return Market()


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
