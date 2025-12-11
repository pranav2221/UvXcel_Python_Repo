#Stroe the name of file in string variable 
log_file = "small.log"
#Declared variables to keep track for counting 
total_entries = 0
info_count = 0
warn_count = 0
errror_count = 0
first_timestamp = None
last_timestamp = None
#open file 
with open(log_file,'r') as file:
    # Traverse the file line by line 
    for line in file:
        # use line.strip() to remove extra spaces 
        line = line.strip()
        #If line is empty we will skip it 
        if line == "":
            continue
        #increse the total_entries count by 1 after every line 
        total_entries+=1
        #below line are increasing counts only if the condition get satisfied
        if "INFO" in line:
            info_count+=1
        elif "WARN" in line:
            warn_count+=1
        else:
            errror_count+=1
        #use line.split() it helps to break the log line into the pieces
        parts = line.split(" ")
        #it combines the date and time 
        timestamp = parts[0] + " " + parts[1]
        #we stroe frist occuring timestamp as firststamp
        if first_timestamp is None:
            first_timestamp = timestamp
        #increase the last_timestamp count untill we get the last timestamp
        last_timestamp = timestamp

# Finally we print the result in the form of summary
print("Total Entries: ",total_entries)
print("INFO: ",info_count)
print("WARN: ",warn_count)
print("ERROR: ",errror_count)
print("Time Range: ")
print(first_timestamp,"->",last_timestamp)
