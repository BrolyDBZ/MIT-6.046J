class Request:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'Request:{self.start},{self.end}'

    def Is_compatible(self, request):
        return request.start > self.end or request.end < self.start


'''This Algorithm give 0(n2) running time'''


def interval_scheduling(array):
    result = []
    while array:
        early_request = Request(0, float('inf'))
        for request in array:
            if early_request.end > request.end:
                early_request = request
        newarray = []
        result.append(early_request)
        for request in array:
            if request.start > early_request.end:
                newarray.append(request)
        array = newarray
    return result


'''This algorithm give 0(nlogn) running time with no extra space'''


def Interval_Scheduling(array):
    array.sort(key=lambda r: r.end)
    n = len(array)
    i = 0
    result = []
    while i < n:
        check = array[i]
        result.append(array[i])
        while i < n and not array[i].Is_compatible(check):
            i += 1
    return result
