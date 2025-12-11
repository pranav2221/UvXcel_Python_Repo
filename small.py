log_file = "small.log"
total_entries = 0
info_count = 0
warn_count = 0
errror_count = 0
first_timestamp = None
last_timestamp = None

with open(log_file,'r') as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue
        total_entries+=1
        if "INFO" in line:
            info_count+=1
        elif "WARN" in line:
            warn_count+=1
        else:
            errror_count+=1

        parts = line.split(" ")
        timestamp = parts[0] + " " + parts[1]
        if first_timestamp is None:
            first_timestamp = timestamp
        last_timestamp = timestamp

print("Total Entries: ",total_entries)
print("INFO: ",info_count)
print("WARN: ",warn_count)
print("ERROR: ",errror_count)
print("Time Range: ")
print(first_timestamp,"->",last_timestamp)


