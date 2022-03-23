# Liferay CSE VETP (View Export Ticket Parser)

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/-Python-yellow?style=for-the-badge" alt="Python" /></a>
<a href="https://github.com/dianaseung/cse-ticket-csv-parse/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/dianaseung/cse-ticket-csv-parse"></a>
<a href="https://github.com/dianaseung/cse-ticket-csv-parse/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/dianaseung/cse-ticket-csv-parse"></a>

Python script to parse CSV exports from ZenDesk to prepare for import into Google Sheets for mandatory CSE Ticket Spreadsheet usage.
Requirements for use include having a proper ZenDesk view setup for proper CSV export.

## Recommended ZenDesk View Setup
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
- If using IDE such as VS Code, you can install Jupyter

To use this in a Linux environment, you will need to:




## Next Steps

- Inquire into auto-generated CSV export 
- (GET API for ZenDesk is not available) - not a viable solution
