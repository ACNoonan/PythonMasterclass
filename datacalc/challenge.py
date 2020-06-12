# Display information on the four clocks (time(), perf_counter(), Monotonic(),
# process_time().
#   Use doc's from get_clock_info() function to work out how to call each one
import time

# print(time.get_clock_info('time'))
# print(time.get_clock_info('perf_counter'))
# print(time.get_clock_info('monotonic'))
# print(time.get_clock_info('process_time'))

print(time.time())
print(time.perf_counter())
print(time.monotonic())
print(time.process_time())
