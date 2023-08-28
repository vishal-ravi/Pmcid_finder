import requests
import xml.etree.ElementTree as ET

# Replace with your actual API key
api_key = "7c13496fb6f075b0cf97f52998b5f92a9108"

# Base URL for PubMed API
base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# PMID of the article you want to find the PMCID for
pmid = "21458665"  # Replace with the actual PMID

# Construct the API request URL to fetch article metadata
api_url = f"{base_url}/efetch.fcgi?db=pubmed&retmode=xml&id={pmid}&api_key={api_key}"

# Make the API request
response = requests.get(api_url)

if response.status_code == 200:
    xml_content = response.text
    root = ET.fromstring(xml_content)
    
    # Find the PMCID if available
    pmcid_element = root.find(".//ArticleId[@IdType='pmc']")
    
    if pmcid_element is not None:
        pmcid = pmcid_element.text
        print(f"PMID: {pmid} has PMCID: {pmcid}")
    else:
        print(f"PMID: {pmid} does not have a PMCID.")
else:
    print(f"Error: {response.status_code} - {response.text}")
