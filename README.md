# ABS-2006_AMC1-POC

Welcome to the ABS-2006_AMC1-POC. This proof of concept (POC) is designed to allow users to retrieve ABS transactions and total available principal funds based on user input.

This tool assumes that CSV files are downloaded and imported in folder called 'enhancedLoanLevelData', while certificate statements are located in folder 'certificateStatements'. CSV files and PDF files can be downloaded from https://bit.ly/ABS-2006_AMC1-POC. Folders must be with the same directory with the py files.

Limitations:
1.	In the interest of time and complexity, I decided to read only the enhanced loan level data CSV files.
2. The system will generate SQL table for one (1) CSV file. This will limit the encompassed dates during the analysis of the user but this will reduce memory usage.
3. Generated SQL table will represent only transactions distributed within a singular month. This is to make sure that total values will align with the corresponding certificate of that month.
For example, if user chooses Mar 2012, only the enhanced loan level data from Mar 2012 will be uploaded to the SQL database. Likewise, only the certificate distributed from Mar 2012 will be opened.

Design:
1.	The user will be requested to input year (e.g. ‘2012’) and month (e.g. ‘Mar’).
2.	Based on the input year, ‘Principal Funds Available’ in tabular form will be printed in user console.
3.	Corresponding certificate statement (in PDF form) from input year and month will be opened for user’s comparison of values.
4.	A status log report will be generated.
