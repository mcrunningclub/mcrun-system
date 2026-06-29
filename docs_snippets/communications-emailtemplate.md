### Email Template.gs

- *function* [`saveDraftAsHtml()`](#savedraftashtml)
- *function* [`generateHtmlFromDraft_(subjectLine)`](#generatehtmlfromdraftsubjectline)
- *function* [`getTemplateFromDraft_(subjectLine)`](#gettemplatefromdraftsubjectline)
- *function* [`subjectFilter_(subjectLine)`](#subjectfiltersubjectline)
- *function* [`fillInTemplate(template, data)`](#fillintemplatetemplate-data)

#### saveDraftAsHtml()

User function to execute `generateHtmlFromDraft_`.

Must updated subject line as needed.


#### generateHtmlFromDraft_(subjectLine)

Generate html version of email found in draft using its subject line.

Saves html under {draft subject}-{datetime}-html in Google Drive.

Params:

- `subjectLine` (string) - Subject line of target draft.


#### getTemplateFromDraft_(subjectLine)

Get a Gmail draft message by matching the subject line.

Params:

- `subjectLine` (string) - to search for draft message

Returns:

- (object) - containing the subject, plain and html message body and attachments

#### subjectFilter_(subjectLine)

Filter draft objects with the matching subject line message by matching the subject line.

Params:

- `subject` (string) - Line to search for draft message

Returns:

- (object) - Gmail Draft object

#### fillInTemplate(template, data)

Fill template string with data object and add current year.

Params:

- `template` (string) - string containing {{}} markers which are replaced with data
- `data` (object) - object used to replace {{}} markers

Returns:

- (object) - JSON-formatted message replaced with data

