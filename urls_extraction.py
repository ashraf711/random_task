import re

# Function to extract URLs from a given text file and save them into a new file
def extract_urls(input_file_path, output_file_path):
    # Regular expression pattern for matching URLs
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    
    try:
        # Open the input file and read its contents
        with open(input_file_path, 'r') as file:
            file_contents = file.read()
            
            # Find all URLs using the regular expression pattern
            urls = re.findall(url_pattern, file_contents)
            
            # Open (or create) the output file and write the URLs to it
            with open(output_file_path, 'w') as output_file:
                for url in urls:
                    output_file.write(url + '\n')
                    
        print(f"URLs have been successfully extracted and saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


input_file_path = 'random.txt' # Replace with the path to your input file
output_file_path = 'extracted_urls.txt' # The path where you want to save the URLs

# Call the function
extract_urls(input_file_path, output_file_path)
