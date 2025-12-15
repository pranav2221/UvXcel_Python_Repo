log_file = "small.log"
search_term = input("Enter the word you want to search: ")
search_term = search_term.lower()
print("\nMacthing log entries are: ")
with open(log_file,"r") as file:
    for line in file:
        line = line.strip()
        if search_term in line.lower():
            print(line)