### HTML-Extraction.gs

- *function* [`extractTagsFromProjectFile()`](#extracttagsfromprojectfile)
- *function* [`saveDraftAsHtml()`](#savedraftashtml)
- *function* [`generateHtmlFromDraft_(subjectLine)`](#generatehtmlfromdraft_subjectline)
- *function* [`getEmailTemplateFromDrafts_(subjectLine)`](#getemailtemplatefromdrafts_subjectline)
- *function* [`subjectFilter_(subjectLine)`](#subjectfilter_subjectline)
- *function* [`fillInEmailTemplate_(template, data)`](#fillinemailtemplate_template-data)

#### extractTagsFromProjectFile()

Extracts all literal tags from HTML file using regex.

Used to debug HTML file. Must change file name variable inside function before running.


#### saveDraftAsHtml()

Generate html version of email found in draft using its subject line.

Must updated subject line as needed.


#### generateHtmlFromDraft_(subjectLine)

Generate html version of email found in draft using its subject line.

Saves html under {draft subject}-{datetime}-html in Google Drive.

Params:

- `subjectLine` (string) - Subject line of target draft.


#### getEmailTemplateFromDrafts_(subjectLine)

Get a Gmail draft message by matching the subject line.

Params:

- `subjectLine` (string) - to search for draft message

Returns:

- (object) - containing the subject, plain and html message body and attachments

#### subjectFilter_(subjectLine)

Filter draft objects with the matching subject line message by matching the subject line.

Params:

- `subjectLine` (string) - to search for draft message

Returns:

- (object) - GmailDraft object

#### fillInEmailTemplate_(template, data)

Fill template string with data object and add current year.

Params:

- `template` (string) - string containing {{}} markers which are replaced with data
- `data` (object) - object used to replace {{}} markers

Returns:

- (object) - JSON-formatted message replaced with data

