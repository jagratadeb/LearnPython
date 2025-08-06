import time

print(time.time()) # Returns the current time in seconds since the epoch
print(time.localtime()) # Returns the current local time as a struct_time object
print(time.asctime()) # Converts a struct_time object to a string
print(time.sleep(2)) # Pauses the program for 2 seconds
print(time.strftime("%Y-%m-%d %H:%M:%S")) # Formats the current time as a string
print(time.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")) # Parses a string into a struct_time object
print(time.mktime(time.localtime())) # Converts a struct_time object to seconds since the epoch
print(time.perf_counter()) # Returns a float representing the time elapsed since a reference point,