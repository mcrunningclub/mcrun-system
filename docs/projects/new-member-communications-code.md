---
authors:
    - andrey
date: 2025-06-11
links:
    - start/faq.md
---

# McRUN New Member Communications

---

## About

**McRUN New Member Communications** is a Google Apps Script project that automates onboarding for new members of the McGill Students Running Club.

It generates and sends personalized welcome emails and digital membership passes, integrating with Google Sheets, Gmail, and Google Slides to streamline communications and record-keeping.

**Purpose**

- Automatically generate and send a welcome email with a digital pass to new registered members.
- Log communications and membership information for club administrators.
- Provide a seamless, professional onboarding experience for all new club members.

### Files

- **Github Repo:** [mcrun-new-member-communications](https://github.com/mcrunningclub/mcrun-new-member-communications)
- **Google Sheets:** [New Member Communications Sheet](https://docs.google.com/spreadsheets/d/1PrKth6f81Dx52bB3oPX1t55US-GnNRGve-TN4rU9Wlo/edit?usp=sharing)
- **Apps Script Project:** [McRUN New Member Communications Apps Script](https://script.google.com/home/projects) _(Accessible via Extensions > Apps Script in the Google Sheet)_

### Key Features

- Sends personalized welcome emails with inline images and digital pass attachment.
- Generates digital membership passes from Google Slides template, including QR code.
- Caches and reuses email templates and Drive blobs for efficiency.
- Logs outgoing emails and member info for compliance and reporting.
- Supports importing and processing from other club systems via Sheets.
- Customizable HTML email templates.
- Robust error and status logging for every communication.

### Tools Used

- Google Apps Script (JavaScript/HTML)
- Google Sheets (Literals, Payment Logs, etc.)
- Gmail API (send personalized HTML emails, inline images)
- Google Slides API (generate custom digital passes)
- Google Drive (store digital passes)
- Apps Script Triggers (manual, event-based)


---

## Function Docs

This section is divided by project file (alphabetical order).  
Each file lists its functions and provides a detailed reference for each.

> **Note:** Only a selection of functions may be shown below due to search result limits.  
> [See all code/functions in GitHub](https://github.com/mcrunningclub/mcrun-new-member-communications/search?q=function)

<br>
<!-- 
    🔴 Member Info.gs
-->

### # <big> Member Info.gs </big>
- [`getUserTimeZone()`](#getusertimezone) → Returns user's timezone
- [`GET_LITERAL_SHEET()`](#get_literal_sheet) → Returns the "Literals" sheet object
- [`GET_PAYMENT_LOG_SHEET()`](#get_payment_log_sheet) → Returns the "Payment Logs" sheet object

---

#### ## <big> getUserTimeZone() </big>

Returns the user's timezone from script settings.

```js
const tz = getUserTimeZone();
```

**Output:** String (timezone)

---

#### ## <big> GET_LITERAL_SHEET() </big>

Returns the "Literals" sheet, or opens by ID if not found.

```js
const sheet = GET_LITERAL_SHEET();
```

**Output:** Google Sheet object

---

#### ## <big> GET_PAYMENT_LOG_SHEET() </big>

Returns the "Payment Logs" sheet, or opens by ID if not found.

```js
const sheet = GET_PAYMENT_LOG_SHEET();
```

**Output:** Google Sheet object

---

<br>
<!-- 
    🔴 Member Pass.gs
-->

### # <big> Member Pass.gs </big>
- [`createPassFile(passInfo)`](#createpassfilepassinfo) → Generates a digital membership pass using Google Slides

---

#### ## <big> createPassFile(passInfo) </big>

Generates a digital pass file for a member using a Google Slides template, fills in info, generates QR code, and returns the download link.

```js
const passUrl = createPassFile({
  firstName: "Alice",
  lastName: "Smith",
  memberId: "MC1234",
  // ...other fields
});
```

| Name     | Type   | Description                |
|----------|--------|----------------------------|
| passInfo | Object | Member data (name, ID, etc)|

**Output:** String (download link for pass PNG)

**Pitfalls:** Template and folder IDs must be correct and accessible.

---

<br>
<!-- 
    🔴 Send Email.gs
-->

### # <big> Send Email.gs </big>
- [`sendWelcomeEmailInRow(row)`](#sendwelcomeemailinrowrow) → Sends a welcome email to the member in a row
- [`sendWelcomeEmail(memberInformation)`](#sendwelcomeemailmemberinformation) → Sends a personalized welcome email using member info

---

#### ## <big> sendWelcomeEmailInRow(row) </big>

Sends a welcome email to the member in the specified row of the "Literals" sheet. Logs status.

```js
sendWelcomeEmailInRow(14);
```

| Name | Type    | Description                 |
|------|---------|-----------------------------|
| row  | Integer | Row to target (default: last row) |

**Output:** None (logs status in sheet)

**Pitfalls:** Must be run as the club account.

---

#### ## <big> sendWelcomeEmail(memberInformation) </big>

Sends a personalized welcome email to a new member using their information and a template.

```js
sendWelcomeEmail({
  firstName: "Alice",
  passUrl: "https://drive.google.com/...",
  email: "alice@example.com"
});
```

| Name              | Type   | Description                    |
|-------------------|--------|--------------------------------|
| memberInformation | Object | Includes firstName, passUrl, email, etc. |

**Output:** String (status message)

---

<br>
<!-- 
    🔴 Mail Merge.gs
-->

### # <big> Mail Merge.gs </big>
- [`inlineImage()`](#inlineimage) → Example: send email with inline images
- [`saveDraftAsHtml()`](#savedraftashtml) → Saves HTML of a Gmail draft to Drive
- [`generateHtmlFromDraft(subjectLine)`](#generatehtmlfromdraftsubjectline) → Generates and saves HTML version of an email draft

---

#### ## <big> inlineImage() </big>

Sends an example email with inline images to demonstrate image embedding.

```js
inlineImage();
```

**Output:** None (sends test email)

---

#### ## <big> saveDraftAsHtml() </big>

Saves the HTML content of a Gmail draft (by subject) as a file in Drive.

```js
saveDraftAsHtml();
```

**Output:** None

---

#### ## <big> generateHtmlFromDraft(subjectLine) </big>

Generates and saves the HTML version of an email draft found by subject.

```js
generateHtmlFromDraft("Here's your post-run report! 🙌");
```

| Name        | Type   | Description         |
|-------------|--------|---------------------|
| subjectLine | String | Subject of draft    |

**Output:** None (file created in Drive)

---

## Triggers

### Types of Triggers

- **Manual triggers:**  
  - Most functions are designed to be invoked when a new member is added, or by admin action via Apps Script.
- **Event-based triggers:**  
  - Can be set up to run when new rows are added (e.g., via onChange in a connected membership sheet).
- **Time-based triggers:**  
  - Not present by default, but possible for scheduled reminders or follow-ups if extended.

**Purpose:**  
- Automate sending of welcome emails and pass generation for each new member registration.

---

## Troubleshooting & FAQ

| Issue/Error | Likely Cause | Solution |
|-------------|--------------|----------|
| "Wrong email. Please try using the club's account" | Script not run as mcrunningclub@ssmu.ca | Use the club account to send emails |
| "Expected X for newMemberValues.length..." | Sheet column mismatch | Ensure header and data columns match |
| "Blob not found" | Script property missing or not cached | Run cacheBlobToStore or check Drive file access |
| "Template/Drive ID not found" | File/folder IDs incorrect | Double-check and update IDs in the code |
| Email not received | Spam filter, wrong address | Check recipient address and Gmail spam folder |

---

## See Also

- [mcrun-membership-list](https://github.com/mcrunningclub/mcrun-membership-list) — Membership roster automation
- [mcrace-code](https://github.com/mcrunningclub/mcrace-code) — McRUN Race registration management
- [Google Apps Script Triggers](https://developers.google.com/apps-script/guides/triggers)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [McRUN Club GitHub](https://github.com/mcrunningclub)

---

_Last updated: 2025-06-12_