class Request:
    def __init__(self,start,end,weight):
        self.start=start
        self.end=end
        self.weight=weight

    def __str__(self):
        return f'request: {self.start},{self.end}'

def Interval_Scheduling(Requests):
    Requests.sort(key=lambda r:r.start)
    