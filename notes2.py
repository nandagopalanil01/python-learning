#useing loops to go through values and aggregate data like summing, counting, or averaging
scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total += score
    print("Current Total:", total)
print("Final Total:", total)

#Using for loops to trasform data like cleaning data before processing

files = [" Report.csv ", "DATA.csv ", " final.TXT"] #inconsistant casing & unnecessary spacing
for file in files:
    file = file.strip().lower().replace(".txt", ".csv")
    print(f"processing {file}")