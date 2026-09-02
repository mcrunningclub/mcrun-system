# McRace Cross Referencing

This is a simple spreadsheet + Google Apps Script project to check the membership status of everyone who signed up to McRace with the McRun member discount.

!!! info "Important"
    This code was only used for the McRace 2026 registrations.

## How it works

It uses the list of members from the current master list, including their latest membership payment date. A membership is typically valid for one calendar year, so members are indidated as "Expired" if their payment date is over a year before the date of the race.

!!! warning "Please note"
    The code includes some parts that are hard coded, including the date of the race and the columns where certain information is found in each spreadsheet. **Please update as necessary or it might not work as expected.**

Registrants are cross-referenced using the email they used to register for McRace. If a match isn't found, their first and last name is used (not case sensitive). If a matching name is found, the differing email is recorded.

## Interpreting the results

The names and emails of everyone who was checked are saved in the spreadsheet, as well as a note(s) indicating the result. The spreadsheet is conditionally formatted to easily group the types of results.

- **Not a member** (red) - This person's email and name were not found **<u>OR</u>** Someone with this email/name registered but a payment was never recorded
- **Expired member** (yellow) - Someone with this email/name registered and paid in the past, but more than a year before the race
- **Active member** (green) - Someone with this email/name registered and paid less than a year before the race

!!! danger "Please manually double check the results"
    - The script will miss people who register with a different name and different email, e.g. Jessica Smith "jessica.smith@mcgill.ca" and Jess Smith "jessicasmith@gmail.com".
    - If two people have the same name, they may get mixed up!
    - The payment dates may not be accurate as they rely on a different script.