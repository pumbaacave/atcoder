import bisect
class MyCalendar:
    def __init__(self):
        self.booked = {}
        
    def do_book(self, start, end):
        self.booked[start] = 1
        if end not in self.booked:
            self.booked[end] = -1


    @staticmethod
    def is_start_valid(booked_day, booked, day):
        day_idx = bisect.bisect_right(booked_day, day)
        if day_idx > 0 and  booked[booked_day[day_idx - 1]] == 1:
            return False
        else:
            return True

    @staticmethod
    def is_end_valid(booked_day, booked, day):
        day_idx = bisect.bisect_left(booked_day, day)
        if day_idx > 0 and  booked[booked_day[day_idx - 1]] == 1:
            return False
        else:
            return True

    def book(self, start: 'int', end: 'int') -> 'bool':
        booked = self.booked
        booked_day = sorted(booked.keys())
        end_idx = bisect.bisect_left(booked_day, end)
        if end_idx == 0:
            self.do_book(start, end)
            return True
        if self.is_start_valid(booked_day, booked, start) and self.is_end_valid(booked_day, booked, end):
            self.do_book(start, end)
            return True
        else:
            return False

def test_book():
    c = MyCalendar()
    book_days = [[97,100],[33,51],[89,100],[83,100],[75,92],[76,95],[19,30],[53,63],[8,23],[18,37],[87,100],[83,100],[54,67],[35,48],[58,75],[70,89],[13,32],[44,63],[51,62],[2,15]]
    results = [True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True]
    for days, res in zip(book_days, results):
        assert res == c.book(*days), f"{days} Errs, expected {res}, {c.booked}"

def test_is_start_valid():
    booked = {1: 1}
    booked_day = [1]
    assert MyCalendar.is_start_valid(booked_day, booked, 2) == False

    booked = {1: -1}
    booked_day = [1]
    assert MyCalendar.is_start_valid(booked_day, booked, 2) == True
