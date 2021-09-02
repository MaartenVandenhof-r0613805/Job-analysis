## LinkedIn Job Analysis for Data Science
### TL;DR
This project collects job postings for the term "Data Science" and analyses them to get insights on what the main locations, requirements topics are.
This is still a work in progress.

### 1. Data Scraping
First the data is scraped from linkedin using the search term "Data Science", location "Belgium" and my personal login details, wich are stored in a config file on my local machine. This data is then stored in a json file and saved to the "data" folder.

### 2. Data Cleaning
After loading the data in a Jupyter notebook, the data is cleaned by first dropping all the rows with null values, then removing all the backspace characters ("\n") from all the columns and then selecting the specific city to set it as the location.

### 3. Data Pre-Processing
Here the data is prepared for analysis and NLP. The words are all set to lowercase, the language of the description is detected wherafter it is lemmanized.
After this the stop words are removed together with the punctuations and add experience level.
To end the data processing we create bigrams from the words that appear most frequently together.
![image](https://user-images.githubusercontent.com/28530143/131885368-0463096a-076e-4889-a820-f0499a59719f.png)


### 4. Analysis
Here we focus on 3 main categories: location, job type and experience level.
This is a snapshot of the results:
![image](https://user-images.githubusercontent.com/28530143/131885578-b8b6d9f3-7ecb-4817-9e79-f8e5de85ca08.png) { width: 200px; }
![image](https://user-images.githubusercontent.com/28530143/131885614-40139e12-f277-4bde-b8c7-5e152198f643.png) { width: 200px; }
![image](https://user-images.githubusercontent.com/28530143/131885644-2433980a-14a4-47d4-a84b-ac67367abf70.png) { width: 200px; }
