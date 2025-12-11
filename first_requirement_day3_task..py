log_file = "small.log"   # Your log file name

total_entries = 0
info_count = 0
warn_count = 0
error_count = 0

first_timestamp = None
last_timestamp = None

# Reading the log file line by line
with open(log_file, "r") as file:
    for line in file:
        line = line.strip()           # Remove unwanted spaces
        if not line:                  # Skip empty lines
            continue

        total_entries += 1            # Counting total lines (entries)

        # --- CATEGORY COUNTING ---
        if "INFO" in line:
            info_count += 1
        elif "WARN" in line:
            warn_count += 1
        elif "ERROR" in line:
            error_count += 1

        # --- TIME RANGE EXTRACTION ---
        parts = line.split(" ")       # Break line into pieces
        timestamp = parts[0] + " " + parts[1]   # Example: "2025-12-09 15:34:22"

        if first_timestamp is None:
            first_timestamp = timestamp   # Set first timestamp only once
      
        last_timestamp = timestamp        # Keep updating last timestamp

# --- PRINT SUMMARY ---
print("Total entries:", total_entries)
print("INFO:", info_count)
print("WARN:", warn_count)
print("ERROR:", error_count)
print()
print("Time Range:")
print(first_timestamp, "→", last_timestamp)
