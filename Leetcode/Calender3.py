class MyCalendarThree:

    def __init__(self):
        self.records= []

    def book(self, start: 'int', end: 'int') -> 'bool':
        records = self.records
        if not records:
            records.append((start, 1))
            records.append((end, -1))
            return 1

        bisect.insort(records, (start, 1))
        bisect.insort(records, (end, -1))
        total = 0
        max_booking = 0
        for r in records:
            total += r[1]
            max_booking = max(max_booking, total)
        return max_booking
