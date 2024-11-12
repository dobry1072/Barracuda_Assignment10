# Name: Heitor Previatti, Dobry Shaw
# email: previahc@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:    11/14/2024
# Course #/Section: 4010/001
# Semester/Year:   2/2024
# Brief Description of the assignment: The task is to create a Python project that retrieves data 
# from a public API, formats and displays the data in a user-friendly way, and saves it to a CSV file.
# Brief Description of what this module does:  creates Digimon class that get, fetch, and display the 
# digimon data, and save it as a CSV file 

# Citations: Stack Overflow                                                                                                                                
# Anything else that's relevant:

# import_api.py

import requests
import json
import csv

class DigimonAPI:
    '''
    A class to interact with Digimon data acquired through API (JSON)
    Get, fetch, and display the digimon data, and save it as a CSV file
    '''
    def __init__(self, api_url='https://digimon-api.vercel.app/api/digimon'):  
        '''
        Initializes the DigimonAPI class with the specific API URL
        @api_url String:  the url for Digimon API
        '''
        self.api_url = api_url
        self.digimon_data = []
        
    def fetch_data(self):
        '''
        Build and submit a request to the API server, then parse the results and store them
        '''        
        response = requests.get(self.api_url)
        self.digimon_data = response.json()
                    
    def display_data(self):
        '''
        Display a summary of the fetched data in a friendly readable format
        Shows number of digimon, and prints 10 of them and their levels
        '''
        dig_total = len(self.digimon_data)
        print("Total Digimon Found:", dig_total)
        
        for digimon in self.digimon_data[:10]:
            print("Name:", digimon['name'], ", Level:", digimon['level'])
    
    def save_to_csv(self, filename="digimon_data.csv"):
        '''
        Convert JSON data to CSV and save it to a file
        @filename String: the name of the CSV file
        '''
        fieldnames = ["name", "img", "level"]

        with open(filename,'w', newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for digimon in self.digimon_data:
                writer.writerow(digimon)
        
        print("Data saved to",filename, "successfully")

    def print_csv(self, filename="digimon_data.csv"):
        '''
        Reads and displays the contents of the CSV file
        @filename String: the name of the CSV file
        '''
        print_csv = input("Would you like to see the CSV content? Enter 'yes': ").strip().lower()
        
        if print_csv == 'yes':
            with open(filename,'r') as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    print(row)
        else:
            print("Ok, no CSV content will be displayed")

        