## LinkedIn Job Analysis for Data Science
### TL;DR
This project collects job postings for the term "Data Science" and analyses them to get insights on what the main locations, requirements topics are.
This is still a work in progress.

### 1. Data Scraping
First the data is scraped from linkedin using the search term "Data Science", location "Belgium" and my personal login details, wich are stored in a config file on my local machine. This data is then stored in a json file and saved to the "data" folder.

### 2. Data Cleaning
After loading the data in a Jupyter notebook, the data is cleaned by first dropping all the rows with null values, then removing all the backspace characters ("\n") from all the columns and then selecting the specific city to set it as the location.

### 3. Data Pre-Processing
Here the data is tokenized
