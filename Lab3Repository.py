def write_name_to_file():
    try:
        file_name = "data.txt"  
        your_name = input("Enter your name: ")

        with open(file_name, 'w') as file:
            file.write(f"Name: {your_name}")

        print(f"File '{file_name}' created successfully with your name.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to write the text file
write_name_to_file()


