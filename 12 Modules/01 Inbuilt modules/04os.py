import os

print(os.getcwd()) # Returns the current working directory
print(os.listdir('.')) # Lists all files and directories in the current directory
print(os.path.exists('example.txt')) # Checks if a file or directory exists
print(os.path.join('folder', 'file.txt')) # Joins two paths
print(os.path.isfile('example.txt')) # Checks if a path is a file
print(os.path.isdir('folder')) # Checks if a path is a directory