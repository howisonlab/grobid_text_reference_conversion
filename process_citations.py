import requests
import json

def process_citations(citations):
    # Grobid server URL (replace with the actual URL if different)
    url = "http://host.docker.internal:8070/api/processCitationList"

    # Prepare the data
    data = {
        "citations": citations
    }

    # Set the headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/x-bibtex"
    }

    try:
        # Send POST request to Grobid
        response = requests.post(url, data=data, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            result = response.text
            return result
        else:
            print(f"Error: Received status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":

    from pathlib import Path
    import sys
    
    citation_txt = Path(sys.argv[1]).read_text().split("\n\n")
    
    result = process_citations(citation_txt)
        
   # result = process_citations("Doe J. et al., A study of citation processing, Journal of Citations, 2023.")
    
    
    if result:
        print(result)
    else:
        print("Failed to process citations.")