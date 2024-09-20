from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

from postgre_sql_config import *
from queries import *

def main():
    
    while True:
        try:
            option = int(input("Enter:\n1. to run the bot\n2. to delete processed data\n3. to exit\n=> "))
            if option in [1, 2, 3]:
                if option == 1:
                
                    print("Running bot...")
            
                elif option == 2:
                    print("Deleting processed data...")
                    
                elif option == 3:
                    print("Exiting the program...")
                    exit()
            
            else:
                print("Invalid option. Please enter 1, 2, or 3.")
        
        except ValueError:
            print("Invalid input. Only integers are allowed.")


if __name__ == "__main__":
    main()
    