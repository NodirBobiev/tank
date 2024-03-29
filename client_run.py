from client.client import get_game_state, get_game_state_stream, post_random_tank_event, post_tank_event

while True:
    c = input()
    if c == "0":
        get_game_state()
    if c == "1":
        try:
            get_game_state_stream()
        except KeyboardInterrupt:
            pass
    if c == "2":
        post_random_tank_event()
    
    if c == "3":
        while True:
            c = input()
            if c == "exit":
                break
            for i in range(10000):
                post_tank_event(int(c))