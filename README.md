# netlify-gsheet-url-shortner

A Url Shortner Generator which uses Google Sheets as Data EndPoint. 


## Synopsis

**Problem**:  This repsoitory demonstrate the creation of a Url Shortner with the help of Netlify with Google Sheets CSV End Point. This procedure is automated using Python.

**Solution**: The Solution is to covert Google Sheet into Netlify.toml redirect rules. When Netlify is deplyoed then these rules are available for redirection with all MIGHTY powers of Netlify echo system. I have used Python to solve this problem but Netlify fucntions would have been equally useful to solve this problem.


## Installation

- Create a Copy of Google Sheet Template
- Fork this Repo and update "google_sheet_url = None" in shortner.py file with your the url of your newly created Google Sheet template. 
- Delpy new site from Netlify and select your newly created Repo. Here, you need to enter "python shortner.py" as a command.
- New Your short Urls will be deoplyed automatically. Next time your add new urls to the google sheet then you need to (re)trigger your netlify site. You can also used Netlify webhooks for this purpose. 

## Contributions
Contributions are welcome. Please fork the repostiroy and submit a pull request.
Suggestions and comments are welcome.

## LICENSE
MIT 
