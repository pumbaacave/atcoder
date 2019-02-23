import bisect
class MyCalendar:
    """
    keep mapping of start_day and end_day
    booked[start_day] = 1
    booked[end_day] = -1
    when new booking comes
    1. booked[new_start_day - 1] != 1
    2. streaming total of booked[new_start_day:new_end_day] will never exceed 2
    """
    def __init__(self):
        self.booked = {}
        
    def do_book(self, start, end):
        self.booked[start] = 1
        if end not in self.booked:
            self.booked[end] = -1


    @staticmethod
    def is_bookable(booked_day, booked, start, end):
        start_idx = bisect.bisect_right(booked_day, start)
        end_idx = bisect.bisect_left(booked_day, end)
        if start_idx > 0 and  booked[booked_day[start_idx - 1]] == 1:
            return False
        else:
            total = 1
            for e in booked_day[start_idx:end_idx]:
                total += booked[e]
                if total > 1:
                    return False

        return True
        
    def book(self, start: 'int', end: 'int') -> 'bool':
        booked = self.booked
        booked_day = sorted(booked.keys())
        end_idx = bisect.bisect_left(booked_day, end)
        if end_idx == 0:
            self.do_book(start, end)
            return True
        if self.is_bookable(booked_day, booked, start, end):
            self.do_book(start, end)
            return True
        else:
            return False

class MyCalendar1(object):
    def __init__(self):
        self.book_list = []

    def book(self, start, end):
        book_list = self.book_list
        start_idx = bisect.bisect_left(book_list, (start, end))
        not_overlap_former = start_idx == 0 or start_idx > 0 and start >= book_list[start_idx - 1][1]
        not_overlap_latter = start_idx == len(book_list) or start_idx < len(book_list) and end <= book_list[start_idx][0]
        # print(f"start_idx: {start_idx}")
        # print(f"former: {not_overlap_former}")
        # print(f"latter: {not_overlap_latter}")
        if not_overlap_former and not_overlap_latter:
            book_list.insert(start_idx, (start, end))
            return True
        else:
            return False

def test_book():
    c = MyCalendar1()

    book_days = [[97,100],[33,51],[89,100],[83,100],[75,92],[76,95],[19,30],[53,63],[8,23],[18,37],[87,100],[83,100],[54,67],[35,48],[58,75],[70,89],[13,32],[44,63],[51,62],[2,15]]
    results = [True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True]
    for days, res in zip(book_days, results):
        assert res == c.book(*days), f"{days} Errs, expected {res}, {c.book_list}"

