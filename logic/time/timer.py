import time

class Timer:
    def __init__(self):
        self.start_time: float = -1
        self.last_tick: float = -1
        self.delta_time: float = -1
    
    def start(self):
        self.start_time = get_current_time()
        self.last_tick = self.start_time
        self.delta_time = 0.0

    def tick(self):
        current_time = get_current_time()
        self.delta_time = current_time - self.last_tick
        self.last_tick = current_time
        return self.delta_time
    
    def get_real_delta_time(self):
        return get_current_time() - self.last_tick

    def get_elapsed_time(self):
        return get_current_time() - self.start_time
    
    def get_delta_time(self):
        return self.delta_time


def get_current_time():
    return time.time()
