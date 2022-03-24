# Liferay CSE VETP (View Export Ticket Parser)

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/-Python-yellow?style=for-the-badge" alt="Python" /></a>
<a href="https://github.com/dianaseung/cse-ticket-csv-parse/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/dianaseung/cse-ticket-csv-parse"></a>
<a href="https://github.com/dianaseung/cse-ticket-csv-parse/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/dianaseung/cse-ticket-csv-parse"></a>

Python script to parse CSV exports from ZenDesk to prepare for import into Google Sheets for mandatory CSE Ticket Spreadsheet usage.
Requirements for use include having a proper ZenDesk view setup for proper CSV export. Work in Progress

## Recommended ZenDesk View Setup
(*Current configurations, subject to change as I figure out how best to automate importing updates*)


Recommended Conditions:
Tickets must meet all of these conditions to appear in the view:
-  Assignee is (Self)

Recommended formatting column for proper CSV export (in descending order):
- ID
- Priority
- Heat Score
- Subject
- Request date
- Latest update
- Latest updater type(agent/end user)

Recommended Group by: Status (Ascending)
Recommended Order by: Request date (Descending)


## Installation / Usage


### Prerequisites:
- Python 3.10
- PIP
- IDLE
- If using IDE such as VS Code, you can install Jupyter extension

### [Running Python on Windows](https://docs.python.org/3/faq/windows.html)
0. Open Command-Line CMD (win+R, 'cmd') and type 'py' to verify Python version.  Type exit() to exit Python interface.
1. Navigate to directory containing the python script in cmd.
2. Start the script with 
```
C:\Users\YourName\Desktop\> py cse-ticket-csv-parse/python.py
```

### Running Python on Linux systems
WIP


## Current Plan for Ticket Spreadsheet Workflow - Work on more automation in steps
(Setup custom ZenDesk view as detailed above)

1. Export CSV from All My Tickets view -> Download CSV from email
  - Point of improvement: IS possibly working on auto-generating CSV export for URL grab
2. Place CSV in folder with `parse_csv.py` 
  - Point of improvement: make it so that parse_csv.py will wildcard grab any *.csv files in folder to parse into formatted
3. Run `parse_csv.py`
  - Point of improvement: Possibly make .bat file instead to make it easier to run?
4. Open existing (Google Spreadsheet) Ticket Spreadsheet
5. Import
  - Current issues: Order of tickets change due to current ordering by Status.  This would override 
  - Possible solution: I may need to change the custom view to not group by Status, and list purely chronologically (ascending) to retain ticket order. 
  This would allow you to Import and Replace just the Status, dates (Requested, Updated, Due Date), Updater for previously existing tickets and retain Repro/Branch/Master/Jira/Hotfix columns in place.  For any new tickets, all columns would be auto-generated except Action Item (must manually update this one, sorry :) )
  - Potential issues with solution: [Need to investigate] Would filtering and sorting affect order for replacement? (is filter/sort a hard sort or a soft sort?)




## Next Steps

- Inquire into auto-generated CSV export 
- Consider best practice for importing new CSV to update ticket spreadsheet without overriding existing values I'd like to preserve
- (GET API for ZenDesk is not available) - not a viable solution
