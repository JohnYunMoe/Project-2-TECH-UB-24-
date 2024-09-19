# Ethical Considerations for Web Scraping

This project involves web scraping to gather course listings based on user input for their major at NYU Abu Dhabi. It is important to recognize the ethical responsibilities associated with web scraping, as improper techniques can lead to violations of a website’s terms of service, as well as potential disruption of services or unauthorized access to private information. Below are the ethical considerations taken into account for this project, along with the measures implemented to address them.

## Purpose of Data Collection

The purpose of this project is to generate URLs for specific NYU Abu Dhabi course listing pages based on the user’s major. The data is collected for **educational and research purposes only** and is used solely to demonstrate how web scraping can retrieve publicly available information. The project does **not** store or analyze personal user data or sensitive information.

## Data Sources and `robots.txt`

The data is collected from the NYU Abu Dhabi public website:
- [https://nyuad.nyu.edu/](https://nyuad.nyu.edu/)

## Collection Practices

This project adheres to responsible scraping practices, which include:
1. **Rate Limiting**: No excessive scraping is performed to avoid placing undue load on the website's servers.
2. **Avoiding Protected Content**: The project does not attempt to scrape password-protected, paywalled, or otherwise restricted pages.
3. **Respecting Terms of Service**: The project does not scrape sites that prohibit scraping in their terms of service or restrict it via `robots.txt`.

## Data Handling and Privacy

- **No Personal Identifiable Information (PII)**: This project does not collect or process any personal user data, such as names, email addresses, or IP addresses. The scraping activity is limited to gathering publicly available course information.
  
- **Data Security**: Should any data be collected in the future, appropriate measures will be taken to ensure that it is securely stored. Any data that may be collected for educational purposes will be excluded from version control by adding it to `.gitignore` to prevent public exposure. Currently, no data is stored locally.

## Data Usage

The data collected through this project is solely for **educational and research purposes**. It is used to demonstrate the functionality of web scraping in a controlled, responsible manner. No commercial use of the data is intended, and all scraping activities are aligned with the guidelines provided by the website.

If the website owner requests that scraping cease or modifies the terms to prohibit it, this project will be updated to comply with those requests.

---

This project aims to balance the technical capabilities of web scraping with ethical responsibility and respect for the data owners’ rights. All scraping activities are conducted in a manner that minimizes harm, respects privacy, and follows legal and ethical guidelines.
