import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

from postgre_sql_config import *
from queries import *

def take_screenshot(driver, record, results_found):
    transaction_status = "OK"
    current_date = datetime.now().strftime("%Y%m%d")
    person_id, _, _, _ = record
    file_name = f"{current_date}_{person_id}.png"
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    WebDriverWait(driver, 2)
     
    driver.save_screenshot(file_name)
    q2 = save_results_query(record,results_found,transaction_status)
    insert(q2['query'],q2['params'])
    print(f"Screenshot saved as: {file_name}")

def extract_number(text):
    match = re.search(r'Lookup Results:\s*(\d+)\s*Found', text)
    return int(match.group(1)) if match else None

def perform_search(driver,records):
    
    if records is not None:
    
        for record in records:
            
            _, person_name, address, country = record
            
            address = address if address is not None else 'None'
            country = country if country is not None else 'None'
            
            transaction_status = ""
            
            try:
                
                name_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "ctl00_MainContent_txtLastName"))
                )
                address_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "ctl00_MainContent_txtAddress"))
                )
                city_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "ctl00_MainContent_ddlCountry"))
                )

                name_field.send_keys(person_name)
                address_field.send_keys(address)
                city_field.send_keys(country)
            
                search_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "ctl00_MainContent_btnSearch"))
                )
                search_button.click()

                results_count = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "ctl00_MainContent_lblResults"))
                )
                
        
                all_text = results_count.text.strip()
                results_found = extract_number(all_text)
            
                
                if results_found > 0:
                    take_screenshot(driver, record, results_found)
                
                else:
                    results_found = 0
                    if address or country is None:
                        transaction_status = 'Información incompleta' 
                    
                    else:
                        transaction_status = 'NOK'
                    
                    q2 = save_results_query(record,results_found,transaction_status)
                    insert(q2['query'],q2['params'])
                

            except Exception as e:
                print(f"Error during the search process: {e}")
        
        driver.quit()        


def main():
    
    while True:
        try:
            option = int(input("Enter:\n1. to run the bot\n2. to delete processed data\n3. to exit\n=> "))
            if option in [1, 2, 3]:
                if option == 1:
                    print("Running bot...")
                    q1 = records_query()
                    records = select(q1['query'],q1['params'])
                    print(f"{len(records)}: data points will be processed")
                    driver = webdriver.Chrome()
                    
                    try:
                        driver.get("https://sanctionssearch.ofac.treas.gov/")
                        perform_search(driver,records)
                        q3 = results_user8329()
                        processed = select(q3['query'],q3['params'])
                        print(f"{len(processed)}: data points were processed")
                    
                    except Exception as e:
                        print(f"Error opening the page or initializing the browser: {e}")
                        
                    finally:
                        driver.quit()
    
                elif option == 2:
                    print("Deleting processed data...")
                    q4 = delete_results_user8329()
                    delete(q4['query'],q4['params'])
                    
                elif option == 3:
                    print("Exiting the program...")
                    exit()
            
            else:
                print("Invalid option. Please enter 1, 2, or 3.")
        
        except ValueError:
            print("Invalid input. Only integers are allowed.")

if __name__ == "__main__":
    main()