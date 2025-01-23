import csv

def filter_countries():
    # Step 1: Open the CSV file and read the data using DictReader
    try:
        with open('OneDayInternational.csv', mode='r') as file:
            reader = csv.DictReader(file)
            
            # Step 2: Create a set to store unique country names
            countries = set()
            
            # Step 3: Loop through each row and add the country (from 'Versus' column) to the set
            for row in reader:
                countries.add(row['Versus'])
            
            # Step 4: Sort the countries alphabetically
            sorted_countries = sorted(countries)
            
            # Step 5: Display the sorted countries
            print("Countries Sachin has played against (Alphabetical Order):")
            for country in sorted_countries:
                print(country)
                
    except FileNotFoundError:
        print("The file 'OneDayInternational.csv' was not found.")
        
# Call the function to filter and display countries
filter_countries()
