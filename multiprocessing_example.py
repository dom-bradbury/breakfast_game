from multiprocessing import Process, Queue
from time import sleep


def game_engine(i, o):
    while True:
        #print('Game is running')
        #print('Game is producing output for the web server')
        game_output = 'Here is some output for the web server'
        o.put(game_output)
        more_game_output = 'Do you have any input for me web server?'
        o.put(more_game_output)
        while i.empty():
            #print('Game is waiting for input from the web_server')
            sleep(1)
        even_more_game_output = 'Thanks for the following output web server: ' + i.get()
        o.put(even_more_game_output)


def web_server(i, o):
    while True:
        if o.empty() is False:
            print(o.get())
            print('SLEEPING')
            sleep(1)
        server_input = 'Yes, I have some input, here it is'
        i.put(server_input)

if __name__ == '__main__':
    i = Queue()
    o = Queue()
    p = Process(target=game_engine, args=(i, o,))
    q = Process(target=web_server, args=(i, o,))

    p.start()
    q.start()
