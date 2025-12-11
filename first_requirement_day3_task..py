# Store the file name in the variable as a string 
file_name = "small.log"   
#Define variables to track the counters for different purpose
total_entries = 0
info_count = 0
warn_count = 0
error_count = 0
#open the file using open from python and keep it only in reading mode
file = open(file_name, "r")
#now iterate through the file using loop 
for line in file:
    #remove spaces in line using strip() function from python
    line = line.strip()
    #check if line is empty then skip that line
    if line == "":
        continue
    #increse the total count 
    total_entries += 1

    # Check log level using simple condition
    if " INFO " in line:
        info_count += 1
    elif " WARN " in line:
        warn_count += 1
    elif " ERROR " in line:
        error_count += 1

file.close()

#finally print the output
print("Total entries:", total_entries)
print("INFO:", info_count)
print("WARN:", warn_count)
print("ERROR:", error_count)


# Day 4 code to write code for second requirement 
