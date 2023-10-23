class times:
    """The time class stores general information about a time.
"""
    def __init__(self, hour: int, minute: int, second: int):
        """Constructs a time object having the specified hour, minute, and second,
    and universal time in the format HH:MM:SS.
    :ivar __hour: hour of this time object
    :ivar __minute: minute of this time object
    :ivar __second: second of this time object
    :ivar __time: universal time of this time object in the format HH:MM:SS
    Args:
    hour (int): specified hour
    minute (int): specified minute
    second (int): specified second
    Raises:
    ValueError: indicates specified hour is less than 0 or greater than 24
    ValueError: indicates specified minute is less than 0 or greater than 60
    ValueError: indicates specified second is less than 0 or greater than 60
    """
        try: 
            if(hour < 0):
                raise ValueError("Hour may not be less than zero")
            
            elif(minute < 0):
                raise ValueError("Minute may not be less than zero")
            
            elif(second < 0):
                raise ValueError("Second may not be less than zero")
            
        except ValueError as e:
                exit(e)
        
        finally: 
            self.hour = hour
            self.minute = minute
            self.second = second


    def getHour(self):
        """Returns the hour of the calling time object.
    Returns:
    int: hour of the calling time object
    """
        return self.hour
    def setHour(self, hour: int):
        """Sets the hour of the calling time object to the specified hour and
    2
    recomputes the universal time of the calling time object.
    Args:
    hour (int): specified hour
    Raises:
    ValueError: indicates specified hour is less than 0 or greater than 24
    """
        try:
            if(hour < 0 or hour > 24):
                raise ValueError("Hour may not be less than 0 or greater than 24")
            
        except ValueError as e:
            exit (e)
        finally:
            self.hour = hour

    def getMinute(self):
        """Returns the minute of the calling time object.
    Returns:
    int: minute of the calling time object
    """
        return self.minute

    def setMinute(self, minute: int):
        """Sets the minute of the calling time object to the specified minute and
recomputes the universal time of the calling time object.
Args:
minute (int): specified minute
Raises:
ValueError: indicates specified minute is less than 0 or greater than 60
"""
        try:
            if(minute < 0 or minute > 60):
                raise ValueError("Hour may not be less than 0 or greater than 60")
            
        except ValueError as e:
            exit (e)
        finally:
            self.minute = minute

    def getSecond(self):
        """Returns the second of the calling time object.
Returns:
int: second of the calling time object
"""
        return self.second

    def setSecond(self, second: int):
        """Sets the second of the calling time object to the specified second and
recomputes the universal time of the calling time object.
Args:
second (int): specified second
3
Raises:
ValueError: indicates specified second is less than 0 or greater than 60
"""
        try:
            if(second < 0 or second > 60):
                raise ValueError("Hour may not be less than 0 or greater than 24")
            
        except ValueError as e:
            exit (e)
        finally:
            self.second = second
    def getTime(self):
        """Returns the universal time of the calling time object.
Returns:
str: universal time of the calling time object
"""
        return self.getTime
    def __str__(self):
        """Returns string representation of the calling time object.
Returns:
str: string representation of the calling time object
"""
        return f"time hour={self.hour} minute={self.minute} second={self.second}"
    def __eq__(self, other):
        """Tests if the calling time object is equal to the specified object.
Args:
other: the specified object
Returns:
Boolean: True if the calling time object is equal to the specified
object, else False
"""
        if other is not None:
            if isinstance(other,time):
                if other.hour == self.hour:
                    if self.minute == self.minute:
                        if self.second == self.second:

                            return True
                        return False


    @staticmethod
    def sort(data, first: int, last: int):
        """Sorts a list from smallest to largest using the insertion sort
algorithm bypassing the elements to the left of first and to the
right of last.
Args:
data: list to sort
first (int): list index at which the sort will begin
last (int): list index at which the sort will end
""" 
        i =len(data - first - 1)

        j = 0

        big = 0

        temp = 0

        while (i > 0):
            big = first

            j = first + 1

            while (j <= first + i):

                if (data[big] < data[j]):

                    big = j

                j += 1

            temp = data [first + i]

            data[first + i] = data[big]

            data[big] = temp

            i -= 1




             

    @staticmethod
    def search (a, first: int, last: int, target: int):
        """Searches part of a sorted list for a specified target starting at a[first]
and ending at a[last].
Args:
a (int): the list to search
first (int): the list index at which the search will start
last (int): the list index at which the search will end
target (int): the element to search for
Returns:
int: If target appears in the list, index of the, element
that contains target; else -1.
"""
        i = 0 

        found = False


        while ((i < last )and not found and(i + first < len(a))):
            if (a[i + first]==target):

                found = True
            else:
                i += 1

        if (found):
            return i + first
        else:
            return -1
