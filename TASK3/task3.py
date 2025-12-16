from concurrent.futures import ProcessPoolExecutor

def analyze_log_file(log_file):
    total_entries = 0
    info_count = 0
    warn_count = 0
    error_count = 0

    first_timestamp = None
    last_timestamp = None

    # List index = hour (1–24), value = error count
    errors_per_hour = [0] * 25   # index 0 unused

    with open(log_file, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            total_entries += 1

            if "INFO" in line:
                info_count += 1
            elif "WARN" in line:
                warn_count += 1
            elif "ERROR" in line:
                error_count += 1

                # Extract hour using split
                parts = line.split(" ")
                time_part = parts[1]        # HH:MM:SS
                hour = int(time_part.split(":")[0])

                # Convert 0–23 → 1–24 format
                hour = hour + 1
                errors_per_hour[hour] += 1

            # Timestamp extraction
            parts = line.split(" ")
            timestamp = parts[0] + " " + parts[1]

            if first_timestamp is None:
                first_timestamp = timestamp
            last_timestamp = timestamp

    return {
        "file": log_file,
        "total": total_entries,
        "info": info_count,
        "warn": warn_count,
        "error": error_count,
        "start": first_timestamp,
        "end": last_timestamp,
        "errors_per_hour": errors_per_hour
    }


if __name__ == "__main__":

    log_files = ["small.log", "medium.log", "large.log"]

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(analyze_log_file, log_files)

    for result in results:
        print("\n==============================")
        print("File:", result["file"])
        print("Total Entries:", result["total"])
        print("INFO:", result["info"])
        print("WARN:", result["warn"])
        print("ERROR:", result["error"])
        print("Time Range:")
        print(result["start"], "→", result["end"])

        print("\nErrors per Hour (1–24):")
        for hour in range(1, 25):
            if result["errors_per_hour"][hour] > 0:
                print(f"Hour {hour}: {result['errors_per_hour'][hour]}")
