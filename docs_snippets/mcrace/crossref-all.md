- *constant* [`REGISTRATIONS`](#registrations)
- *constant* [`MEMBERSHIPS`](#memberships)
- *function* [`getRegistrations()`](#getregistrations)
- *function* [`getMembers()`](#getmembers)
- *function* [`crossReference()`](#crossreference)
- *function* [`onOpen()`](#onopen)

#### REGISTRATIONS

Spreadsheet with McRace Fillout registrations. Has fields URL and SHEET_NAME.

#### MEMBERSHIPS

McRun membership spreadsheet. Has fields URL and SHEET_NAME.

#### getRegistrations()

Gets the first name, last name, email, and claimed membership 
status from registrations. Converts name to lowercase.

In the form: [[jane, doe, email@gmail.com, Not yet], ...]


#### getMembers()

Gets the first name, last name, email, and payment date from 
memberships. 

In the form: [[Jane, Doe, email@gmail.com, 2026-05-01], ...]


#### crossReference()

Check whether every registration that claims to be a mcrun member
is in the membership list and what their membership status is.

Saves results in this spreadsheet in format:
email | firstname | lastname | membership status

!! Assumes no duplicates in membership list.

#### onOpen()

Creates user menu upon opening sheet

