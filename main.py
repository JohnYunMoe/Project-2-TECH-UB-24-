import requests
from bs4 import BeautifulSoup
from prompt_toolkit.shortcuts import checkboxlist_dialog
import textwrap  

def get_major_url(major):
    base_url = "https://nyuad.nyu.edu/en/academics/undergraduate/majors-and-minors/"
    major_formatted = major.replace(" ", "-").lower() + "-major/courses.html"
    print(base_url + major_formatted)
    return base_url + major_formatted

def scrape_major_sections(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tbody = soup.find('tbody')
        table_rows = tbody.find_all('tr')

        sections_with_courses = []  # store all the sections with courses names

        for tr in table_rows:
            header = tr.find('td').text
            courses = []
            for td in tr.find_all('td')[1:]:
                courses.extend(td.text.split(';'))

            # join all the courses with a newline character so that they are displayed one per line
            courses_text = "\n".join(course.strip() for course in courses)

            # here we wrap the courses text to 60 characters per line so that it fits in the terminal
            wrapped_courses_text = textwrap.fill(courses_text, width=60)

            #append the header and wrapped courses text to the list
            sections_with_courses.append(f"{header.strip()}:\n{wrapped_courses_text}")

        return sections_with_courses
    else:
        print("Failed to get response from the server")
        return []

def interactive_checklist(sections):
    # list of tuples with index and section name
    checklist_items = [(i, section) for i, section in enumerate(sections)]
    
    result = checkboxlist_dialog(
        title="Select Completed Sections",
        text="Mark the sections you have completed:",
        values=checklist_items
    ).run()

    if result:
        print("\nYou have completed the following sections:")
        for i in result:
            print(f"✔ {sections[i]}")

    else:
        print("\nNo sections were marked as completed.")

def main():
    user_major = input("Enter your major: ")
    url = get_major_url(user_major)
    sections = scrape_major_sections(url)

    if sections:
        interactive_checklist(sections)

if __name__ == "__main__":
    main()
