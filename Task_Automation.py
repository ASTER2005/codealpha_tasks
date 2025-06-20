import os  
import shutil  
import re  
import requests  

def move_jpg_files():  
    """Moves all .jpg files from a folder to a new folder."""  
    source = input("Enter source folder path: ")  
    destination = input("Enter destination folder path: ")  

    if not os.path.exists(destination):  
        os.makedirs(destination)  

    moved_files = 0  
    for file in os.listdir(source):  
        if file.lower().endswith(".jpg"):  
            shutil.move(os.path.join(source, file), destination)  
            moved_files += 1  

    print(f"Moved {moved_files} JPG files successfully!")  

def extract_emails():  
    """Extracts all emails from a text file and saves them."""  
    input_file = input("Enter the text file path: ")  
    output_file = input("Where to save extracted emails? ")  

    with open(input_file, "r") as file:  
        text = file.read()  

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)  

    with open(output_file, "w") as file:  
        for email in emails:  
            file.write(email + "\n")  

    print(f"Extracted {len(emails)} emails and saved to {output_file}!")  

def scrape_webpage_title():  
    """Scrapes the title of a webpage and saves it."""  
    url = input("Enter the webpage URL: ")  
    output_file = input("Where to save the title? ")  

    try:  
        response = requests.get(url)  
        if response.status_code == 200:  
            title = response.text.split("<title>")[1].split("</title>")[0]  
            with open(output_file, "w") as file:  
                file.write(title)  
            print(f"Title saved: '{title}'")  
        else:  
            print("Failed to fetch the webpage.")  
    except Exception as e:  
        print(f"Error: {e}")  

def main():  
    print("\n=== Python Automation Tool ===")  
    print("1. Move all JPG files to a folder")  
    print("2. Extract emails from a text file")  
    print("3. Scrape a webpage title")  
    print("4. Exit")  

    while True:  
        choice = input("\nChoose an option (1-4): ")  

        if choice == "1":  
            move_jpg_files()  
        elif choice == "2":  
            extract_emails()  
        elif choice == "3":  
            scrape_webpage_title()  
        elif choice == "4":  
            print("Exiting...")  
            break  
        else:  
            print("Invalid choice. Try again!")  

if __name__ == "__main__":  
    main()  