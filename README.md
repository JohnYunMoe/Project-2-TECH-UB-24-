# NYUAD Major Course Scraper

## Project Summary

This project is a **Python-based web scraper** designed to extract and display course information for different majors offered at NYU Abu Dhabi (NYUAD). The program retrieves the course details directly from NYUAD's official undergraduate major pages, providing users with a list of course sections and their corresponding course names. Additionally, it offers an **interactive command-line interface** that allows users to mark the course sections they have completed, making it useful for students tracking their academic progress.

The tool demonstrates a simple yet powerful way to scrape structured data from web pages, process it, and present it in a user-friendly format. With minimal setup, users can quickly gather and interact with the academic information for any major offered at NYUAD.

## Methods to Gather Data

The project utilizes the following key methods and libraries to gather and process data from the web:

### 1. **Web Scraping with `requests` and `BeautifulSoup`**
   - We use the `requests` library to send an HTTP GET request to the official NYUAD undergraduate majors and minors page.
   - The `BeautifulSoup` library from `bs4` is then employed to parse the retrieved HTML content. This allows us to locate specific HTML elements such as tables and rows (`<tbody>`, `<tr>`, `<td>`) that contain the desired course data.
   - The data is extracted by navigating the HTML structure, focusing on relevant tags where course information is stored. The scraper handles cases where multiple courses are listed in a single table cell, splitting and formatting them properly.

### 2. **Data Formatting with `textwrap`**
   - After extracting the course information, we use Python’s `textwrap` module to format the text neatly. This ensures that long lists of course names fit well in the terminal output by wrapping lines to a specified width (60 characters in this case).

### 3. **Interactive Checklist with `prompt_toolkit`**
   - To make the program more interactive, the `prompt_toolkit` library is used to create a checkbox dialog in the terminal. Users can select which course sections they have completed from the list provided by the scraper.
   - The selections are then displayed, allowing users to track which sections they have already finished.

## Usage

The tool is simple to use and provides a terminal-based interface to interact with. Users are prompted to input their major, and the program will automatically generate the URL corresponding to that major’s course page, retrieve the course sections, and display them interactively. Users can then select which sections they have completed via a checkbox system.

### Running the Project
1. Clone the repository.
2. Install the necessary packages(in Requirements.txt):
   ```bash
   pip install requests beautifulsoup4 prompt_toolkit
3. Run the script 
   ```bash 
   python main.py
