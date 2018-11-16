# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.


import time

print("time()        :", time.get_clock_info('time'))
print("perf_counter():", time.get_clock_info('perf_counter'))
print("monotonic()   :", time.get_clock_info('monotonic'))
print("process_time():", time.get_clock_info('process_time'))



# Example

# import time
#
# print("The epoch on this system starts at :"+ time.strftime('%c',time.gmtime(0)))
#
# print("The current timezone is {0} with an offset of {1}".format(time.tzname[0],time.timezone))
#
# if time.daylight != 0:
#     print("\t DayLight saving time is in effect for this location")
#     print("\t The DST timezone is"+ time.tzname[1])
#
# print("Local time is:" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("UTC time is:" + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))