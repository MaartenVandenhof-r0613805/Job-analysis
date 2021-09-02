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
![image](https://user-images.githubusercontent.com/28530143/131886114-936f4f41-3aa4-4624-a535-865450828a8b.png)
![image](https://user-images.githubusercontent.com/28530143/131886173-4fbcc66a-e06f-415a-9989-77185a5812cd.png)
![image](https://user-images.githubusercontent.com/28530143/131886203-f5877aa5-2383-46b1-9393-eb9725f3f750.png)

We can also look at the technologies required for eacht job category: \n
![image](https://user-images.githubusercontent.com/28530143/131886578-c3991b7e-417b-44dd-9b1f-473fe062d4b3.png)
![image](https://user-images.githubusercontent.com/28530143/131886608-4e895561-74e3-4ee8-8b74-8462efc04593.png)
![image](https://user-images.githubusercontent.com/28530143/131886635-8751d11e-4bc2-4099-b655-2b8dab6cca23.png)
