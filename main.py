import requests 
from bs4 import BeautifulSoup

def get_major_url(major): 
    base_url = "https://nyuad.nyu.edu/en/academics/undergraduate/majors-and-minors/"
    major_formatted = major.replace(" ", "-").lower() + "-major/courses.html"
    full_url = base_url + major_formatted
    print(full_url)
    return full_url


user_major = input("Enter your major: ")
url = get_major_url(user_major)
response = requests.get(url)

if response.status_code == 200: 
    print("request was successful")
else: 
    print("something went wrong")


