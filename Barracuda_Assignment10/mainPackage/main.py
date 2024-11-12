# Name: Heitor Previatti, Dobry Shaw
# email: previahc@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:    11/14/2024
# Course #/Section: 4010/001
# Semester/Year:   2/2024
# Brief Description of the assignment: The task is to create a Python project that retrieves data 
# from a public API, formats and displays the data in a user-friendly way, and saves it to a CSV file.
# Brief Description of what this module does: Initiates the DigimonAPI class in import_api.py 

# Citations: Stack Overflow                                                                                                                                
# Anything else that's relevant:

# main.py

from import_api_Package.import_api import *

if __name__ == "__main__":
    def main():
        '''
        'Main' function initializes the DigimonAPI class and all its functions.
        '''
        # Instantiates the DigimonAPI class 
        digimon_api = DigimonAPI()
        # Fetch the digimon data
        digimon_api.fetch_data()
        # Display digimon data
        digimon_api.display_data()
        # Creates CSV file
        digimon_api.save_to_csv()
        # Print CSV file content as desired
        digimon_api.print_csv()
    
    # Call main function
    main()