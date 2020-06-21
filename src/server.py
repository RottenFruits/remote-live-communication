import sys
from pythonosc import dispatcher
from pythonosc import osc_server
import live

args = sys.argv

def play_stop_handler(unused_addr, args, value):
    try:
        print(args, value)
        if value == 1:
            set.play(reset = True)
        else:
            set.stop()
    except ValueError: pass

if __name__ == "__main__":
    set = live.Set()
    ip = str(args[1]) 
    port = int(args[2])
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/play-stop", play_stop_handler, "Play-Stop")
    server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()