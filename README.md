# Real-Time Bus Data Extraction & Interactive Filtering with Python | Web Scraping & Streamlit Integration

### Techniques Employed
Web Scraping using Selenium, Python, Postgres SQL, Streamlit <br>

### Business Use Cases:
The solution can be applied to various business scenarios including:
- Travel Aggregators: Providing real-time bus schedules and seat availability for customers.
- Market Analysis: Analyzing travel patterns and preferences for market research.
- Customer Service: Enhancing user experience by offering customized travel options based on data insights.
- Competitor Analysis: Comparing pricing and service levels with competitors <br>

### Approach:
1. Data Scraping: Use Selenium to automate the extraction of Redbus data including routes, schedules, prices, and seat availability.

2. Data Storage: Store the scraped data in a SQL database.

3. Streamlit Application Data Analysis/Filtering: Develop a Streamlit application to display and filter the scraped data.
 
### File definition

-selinium_redbus_links_scrapping : This file contains code to scrape 10 Government State Bus Transport data from Redbus website

- busdetails: This file contains extracting bus details from each route links using Selenium and XPath to filter the data. Perform the data extraction atmost 2 hours before the day ends. Post 12 a.m some of the bus route details won't be updated in the redbus website for some hours.

- PythonPostgresSQLconnector : This file contains the code to tranfer the data from csv file to PostgresSQL in localhost.

- digibus_sqlapp: Use of SQL queries to retrieve and filter data based on user inputs. Use Streamlit to allow users to interact with and filter the data through
the application.

- digibus_app : Use Streamlit to allow users to interact with and filter the data through the structured data in csv file.