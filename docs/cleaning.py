import csv

input_file = "gesture_dataset.csv"
output_file = "gesture_dataset_clean.csv"

expected_cols = 43  
clean_rows = []

with open(input_file, "r", newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader, start=1):
        
        if not row:
            print(f"Skipping empty row {i}")
            continue
        
        if len(row) != expected_cols:
            print(f"Skipping row {i}: expected {expected_cols} columns, got {len(row)}")
            continue
        
        try:
            [float(x) for x in row[1:]]
            clean_rows.append(row)
        except ValueError:
            print(f"Skipping row {i}: contains non-numeric feature values")
            continue

with open(output_file, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(clean_rows)

print(f"Cleaning complete. Clean dataset saved as: {output_file}")
print(f"Total clean rows: {len(clean_rows)}")


