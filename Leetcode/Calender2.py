import bisect
from collections import defaultdict
class MyCalendarTwo:

    def __init__(self):
        self.booked = defaultdict(int)
        
    def do_book(self, start, end):
        self.booked[start] += 1
        self.booked[end] -= 1


    @staticmethod
    def is_bookable(booked_day, booked, start, end):
        start_idx = bisect.bisect_right(booked_day, start)
        end_idx = bisect.bisect_left(booked_day, end)
        total = 0
        for e in booked_day[:end_idx]:
            total += booked[e]
            # print(f"{e}: {total}")
            if e >=  booked_day[max(start_idx-1, 0)] and total >= 2:
                return False

        return True
        
    def book(self, start: 'int', end: 'int') -> 'bool':
        booked = self.booked
        booked_day = sorted(booked.keys())
        # print(booked_day)
        # print(booked)
        end_idx = bisect.bisect_left(booked_day, end)
        if end_idx == 0 or self.is_bookable(booked_day, booked, start, end):
            self.do_book(start, end)
            return True
        else:
            return False

class MyCalendarTwo2:

    def __init__(self):
        self.records= []

    def book(self, start: 'int', end: 'int') -> 'bool':
        records = self.records
        if not records:
            records.append((start, 1))
            records.append((end, -1))
            return True

        bisect.insort(records, (start, 1))
        bisect.insort(records, (end, -1))
        total = 0
        for r in records:
            total += r[1]
            if total >= 3:
                records.remove((start, 1))
                records.remove((end, -1))
                return False
        return True



def test_book():
    c = MyCalendarTwo2()
    book_days = [[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]
    true = True
    false = False
    results = [true,true,true,true,false,false,true,false,false,false]
    for days, res in zip(book_days, results):
        assert res == c.book(*days), f"{days} Errs, expected {res}, {c.records}"
    # c.booked.clear()
    c.records.clear()
    book_days = [[26,35],[26,32],[25,32],[18,26],[40,45],[19,26],[48,50],[1,6],[46,50],[11,18]]
    results = [true,true,false,true,true,true,true,true,true,true]
    for days, res in zip(book_days, results):
        assert res == c.book(*days), f"{days} Errs, expected {res}, {c.records}"
