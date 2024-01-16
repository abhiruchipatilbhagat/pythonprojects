import requests
from bs4 import BeautifulSoup

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=&txtLocation=&cboWorkExp1=9'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all job listings on the page
    job_listings = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # Extract information from each job listing
    for job in job_listings:
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.strip()
        posted_days_ago = job.find('span', class_='sim-posted').text.strip()

        # Print job details
        print(f"Company Name: {company_name}")
        print(f"Skills: {skills}")
        print(f"Posted: {posted_days_ago}")
        print("\n---\n")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
