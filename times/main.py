from times import *

def main():
# create a time object named t1 thats hour is 2, minute is 30, and seconds are 5.
    t1 = times("hour is 2","minute is 30", "second are 5")


# create a time object named t2 thats hour is 12, minute is 25, and seconds are 42.
    t2 = times("hour is 12", "minute is 25", "seconds are 42")

# create a time object named t3 thats hour is 1, minute is 20, and seconds are 22.
    t3 = times("hour is 1 ", "minute is 20", "seconds are 22")

# create a time object named t4 thats hour is 11, minute is 45, and seconds are 50.
    t4 = times("hour is 11","minute is 45", "seconds are 50 ")

# create a time object named t5 thats hour is 3, minute is 25, and seconds are 25.
    t5 = times("hour is  3", "minute is 25", "seconds are 25")
# display a string representation of t1
    print(t1)
# display a string representation of t2
    print(t2)
# display a string representation of t3
    print(t3)
# display a string representation of t4
    print(t4)
# display a string representation of t5
    print(t5)

# display the result of testing if t1 is equal to t5
    print("t1 equals t5?", t1.__eq__(t5))
# use getter and setter methods to make t1 the same time
# object as t5
    t1.setHour(t5.getHour())
# display the result of testing if t1 is equal to t5
    print("t1 equals t2?", t1.__eq__(t5))
# get the times of t1, t2, t3, t4, and t5
# and store them in a list named times
# display the times list
    times = ['02:30:05', '01:25:42', '1:20:22', '11:45:50', '03:25:25']
# sort the times list starting at index position 1 and ending at index position 3
def insertion_sort(order, start, end):
    n = len(order)

    for i in range(start, end):
        key = order[i]
        j = i - 1

        while j >= start and key < order[j]:
            order[j + 1] = order[j]
            j -= 1

        order[j + 1] = key

times = ['02:30:05', '01:25:42', '1:20:22', '11:45:50', '03:25:25']

insertion_sort(times, 1, 4)
        
# display the times list
print(times)
# sort the times list starting at index position 0 and ending at index position 4
def insertion_sort(order, start, end):
    n = len(order)

    for i in range(start, end):
        key = order[i]
        j = i - 1

        while j >= start and key < order[j]:
            order[j + 1] = order[j]
            j -= 1

        order[j + 1] = key

times = ['02:30:05', '01:25:42', '1:20:22', '11:45:50', '03:25:25']

insertion_sort(times, 0, 4)
# display the times list
print(times)
# search for t2's time in the times list starting at index position 0 and ending at index
# position 4
times = ['02:30:05', '01:25:42', '1:20:22', '11:45:50', '03:25:25']

t2 = '01:25:42'

start = 0 

end = 4

found_index = None

for i in range (start, end):
    if times[i] == t2:
        found_index = i 
        break

# search for t3's time in the times list starting at index position 0 and ending at index
# position 4
times = ['02:30:05', '01:25:42', '1:20:22', '11:45:50', '03:25:25']

t3 = '01:25:42'

start = 0 

end = 4

found_index = None

for i in range (start, end):
    if times[i] == t3:
        found_index = i 
        break
# search for t2's time in the times list starting at index position 1 and ending at index
# position 3
times = ['02:30:05', '01:25:42', '1:20:22', '11:45:50', '03:25:25']

t2 = '01:25:42'

start = 0 

end = 4

found_index = None

for i in range (start, end):
    if times[i] == t2:
        found_index = i 
        break
# search for t3's time in the times list starting at index position 1 and ending at index
# position 3
times = ['02:30:05', '01:25:42', '1:20:22', '11:45:50', '03:25:25']

t2 = '01:25:42'

start = 0 

end = 4

found_index = None

for i in range (start, end):
    if times[i] == t3:
        found_index = i 
        break