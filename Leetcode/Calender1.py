from loguru import logger
from bisect import bisect_right, bisect_left
class MyCalendar:

    def __init__(self):
        self.booking = []
        self.book_map = {}

    def book(self, start: 'int', end: 'int') -> 'bool':
        booking = self.booking
        book_map = self.book_map
        start_idx = bisect_right(booking, start)
        end_idx = bisect_left(booking, end)
        logger.debug(end_idx)

        def no_former_bookings():
            return end_idx == 0

        def interval_confict():
            print("start_ids", start_idx)
            if start_idx - 1 >= 0 and book_map[start_idx - 1] == 1:
                return True
            print("end_idx - 1", end_idx - 1)
            if end_idx - 1 >= 0 and book_map[end_idx - 1] == 1:
                print("ENTER")
                return True
            return False

        def do_book():
            # create booking
            booking.insert(start_idx, start)
            book_map[start] = 1 # start_day
            end_idx = bisect_right(booking, end)
            booking.insert(end_idx, end)
            book_map[end] = -1 # end_day

        if no_former_bookings:
            do_book()
            return True

        if interval_confict():
            return False
        else:
            do_book()
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
def test_calender():
    c = MyCalendar()
    assert c.book(37, 50) == True, "First Booking Fail"
    print(c.booking, c.book_map)
    assert c.book(33, 50) == False, "Second Booking Fail"
    print(c.booking, c.book_map)
    assert c.book(4, 17) == True, "Third Booking Fail"
