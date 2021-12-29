# netlify-gsheet-url-shortener

A Url Shortner Generator which uses Google Sheets as Data EndPoint. 


## Synopsis

**Problem**:  This repository demonstrates the creation of a Url Shortner with the help of Netlify with Google Sheets CSV End Point. This procedure is automated using Python.

**Solution**: The Solution is to covert Google Sheet into Netlify.toml redirect rules. When Netlify is deployed then these rules are available for redirection with all MIGHTY powers of the Netlify echo system. I have used Python to solve this problem but Netlify functions would have been equally useful to solve this problem.


## Installation

- Create a Copy of the Google Sheet Template
- Fork this Repo and update "google_sheet_url = None" in the shortner.py file with the URL of your newly created Google Sheet template. Alternatively, you can also create a "gsheet_url" environmental variable in NEtlify Site.
- Delpy a new site from Netlify and select your newly created Repo. Here, you need to enter "python shortner.py" as a command.
- New Your short URLs will be deployed automatically. Next time you add new URLs to the google sheet then you need to (re)trigger your netlify site. You can also use Netlify webhooks for this purpose. 

## Contributions
Contributions are welcome. Please fork the repository and submit a pull request.
Suggestions and comments are welcome.

## LICENSE
MIT 
