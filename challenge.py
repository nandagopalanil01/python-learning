#check whether any filenames appear more than ones 
files = ['report.csv', 'data.xlsx', 'summary.docx', 'report.csv', 'data.csv']
if len(files) != len(set(files)):
    print("Duplicate found!")
else:
    print("All files are unique")
