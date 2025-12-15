# Store file name
log_file = "small.log"

# Counters
total_entries = 0
info_count = 0
warn_count = 0
error_count = 0

first_timestamp = None
last_timestamp = None

# Error count per hour using LIST
# Index 0 → hour 1
# Index 23 → hour 24
errors_per_hour = [0] * 24    # Creates 24 zeros


# Open file
with open(log_file, "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue

        total_entries += 1

        # Category counting
        if "INFO" in line:
            info_count += 1
        elif "WARN" in line:
            warn_count += 1
        elif "ERROR" in line:
            error_count += 1

            # ---- ERROR PER HOUR LOGIC (List method) ----
            parts = line.split(" ")   # Split log line
            time_part = parts[1]      # Example: "15:34:22"
            hour = int(time_part[0:2])   # Extract hour → 0–23

            # Convert 0–23 hour → 1–24 hour
            hour_index = hour          # Example: 0 → index 0 but means hour 1
            errors_per_hour[hour_index] += 1


        # Timestamp handling
        parts = line.split(" ")
        timestamp = parts[0] + " " + parts[1]

        if first_timestamp is None:
            first_timestamp = timestamp

        last_timestamp = timestamp


# ------------------------------
# PRINT SUMMARY
# ------------------------------
print("Total Entries:", total_entries)
print("INFO:", info_count)
print("WARN:", warn_count)
print("ERROR:", error_count)

print("\nTime Range:")
print(first_timestamp, "→", last_timestamp)

print("\nErrors Per Hour (1–24):")
for i in range(24):
    print(f"Hour {i+1}: {errors_per_hour[i]}")
