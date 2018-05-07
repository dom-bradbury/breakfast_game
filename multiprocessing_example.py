from multiprocessing import Process, Queue, Pipe
from time import sleep


def game_engine(i, o, conn):
    while True:
        #print('Game is running')
        #print('Game is producing output for the web server')
        game_output = 'Here is some output for the web server'
        conn.send(game_output)
        more_game_output = 'Do you have any input for me web server?'
        conn.send(more_game_output)
        while conn.poll() is False:
            #print('Game is waiting for input from the web_server')
            sleep(1)
        even_more_game_output = 'Thanks for the following output web server: ' + conn.recv()
        conn.send(even_more_game_output)


def web_server(i, o, conn):
    while True:
        if conn.poll():
            print(conn.recv())
            print('SLEEPING')
            sleep(1)
        server_input = 'Yes, I have some input, here it is'
        conn.send(server_input)

if __name__ == '__main__':
    i = Queue()
    o = Queue()
    parent, child = Pipe()
    p = Process(target=game_engine, args=(i, o, child))
    q = Process(target=web_server, args=(i, o, parent))

    p.start()
    q.start()
