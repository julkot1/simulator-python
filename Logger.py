class Logger:
    def __init__(self):
        self.logs = []

    def append(self, log):
        if len(self.logs) == 20:
            self.logs = []
        self.logs.append(log)

