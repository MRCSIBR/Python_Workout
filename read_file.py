# Open a file for reading
with open("data.txt", "r") as file:
  # Read the entire content into a string
  data = file.read()

# Process the data (e.g., split lines, extract information)

# Open the same file for writing (overwrites existing content)
with open("data.txt", "w") as file:
  # Write modified data back to the file
  file.write("This is the new content.")
