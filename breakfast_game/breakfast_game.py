from .engine import Engine, Scene, Choice, Location, LocationSelector, bcolors

'''
whole execution needs to loop within read_input

python breakfast_game.py

-- game=Game
-- p=process(game.play())
-- p.start()
        adds print output to html variable as it goes
        if reaches 'input', clears queue and go onto wait loop
        fetches input value from input queue

--app.run()
        when user inputs value, add to queue variable

'''


class Intro(Scene):

    def enter(self):
        self.game_output("INTRO\n"
                         "You slowly wake up on a bed of hay in a stable\n"
                         "You don't know who you are, where you are, or how you got there\n"
                         "There is one thing you do know\n"
                         "You are hungry, you need breakfast\n\n")
        self.game_output("What do you do next?\n")
        possible_answers = ['Go back to sleep',
                            'Stumble outside']
        responses = ['You snuggle down with the nearest donkey\n',
                     'You stumble out of the stable door into the blinding light of the day\n']
        error_response = '"I should really make a decision"\n'

        path = Choice(possible_answers, responses, error_response).choice(game)
        if path == 1: return Intro(game)
        if path == 2: return Market(game)


class Market(Scene):
    def enter(self):
        self.game_output("Market")

        game.unlock_location(Butcher)
        game.unlock_location(Baker)
        game.unlock_location(Tavern)

        path = LocationSelector(game).choose_location(game)
        return path()


class Butcher(Location):
    name = 'Butcher'

    def __init__(self):
        Location.__init__(self, 'Butcher', game)

    def enter(self):
        self.game_output(bcolors.OKGREEN + '"A customer! A customer! What a glorious day!"' + bcolors.ENDC)
        self.game_output('"Take a look at my fine sausages, they are they best in town"')
        self.game_output('What would you like?')

        possible_answers = ['Sausage',
                            'Bacon']
        responses = ['Ohh, good choice!\n',
                     'I recommend you cook it extra crispy\n']
        error_response = '"I should really make a decision"\n'

        meat_choice = Choice(possible_answers, responses, error_response).choice(game)
        meat = possible_answers[meat_choice-1]

        possible_answers = ['Apologise and leave',
                            'Steal the %s!' % meat]
        responses = ['Pfft, go eat breadcrumbs like a little pigeon you worthless wretch\n',
                     'GUARDS! GUARDS! He has stolen my %s!\n' % meat]
        error_response = '"I should really make a decision"\n'

        response = Choice(possible_answers, responses, error_response).choice(game)

        if response == 2:
            game.obtain_item(meat)

        return Market(game)


class Baker(Location):
    name = 'Baker'

    def __init__(self):
        Location.__init__(self, 'Baker', game)


class Tavern(Location):
    name = 'Tavern'

    def __init__(self):
        Location.__init__(self, 'Tavern', game)


def main(i,o,w):
    #game.game_output('Welcome to Baconia!\n')
    game.play(Intro(game), i, o, w)


game = Engine(flask=True)

if __name__ == '__main__':

    main()
