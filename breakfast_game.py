from breakfast_game.engine import Engine, Scene, Choice


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
        responses = ['You snuggle down with the nearest donkey',
                     '...'
                     'Ugh']

        path = Choice(possible_answers, responses).choice()
        if path == 1: return Intro()
        if path == 2: return Market()

class Market(Scene):

    pass

print('Welcome to Baconia!\n')
scene = Intro()
game = Engine(scene)
game.play()
