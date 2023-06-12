import csv

# Read in the CSV files
with open(r"C:/Users/surya/OneDrive/Documents/Programs/She values/DATA/FreshHR-Data - Sheet1.csv",encoding='utf-8') as unfiltered_data,\
open(r"C:/Users/surya/OneDrive/Documents/Programs/She values/DATA/Indian-Male-Names.csv",encoding='latin-1') as male_names,\
open(r"C:/Users/surya/OneDrive/Documents/Programs/She values/DATA/Output.csv",'w', newline='',encoding='utf-8') as output:
    # Create CSV reader and writer objects
    raw_data_reader = csv.reader(unfiltered_data)
    elements_reader = csv.reader(male_names)
    output_writer = csv.writer(output)

    # Extract the elements to remove into a set
    elements_to_remove = set()
    for row in elements_reader:
        elements_to_remove.add(row[0].lower())
    
    # Filter the raw data and write the remaining rows to the output file
    for row in raw_data_reader:
        if row[0].lower() not in elements_to_remove:
            output_writer.writerow(row)

