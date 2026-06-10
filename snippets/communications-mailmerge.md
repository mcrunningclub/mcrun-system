### Mail Merge.gs
- [`inlineImage()`](#inlineimage) → Example: send email with inline images
- [`saveDraftAsHtml()`](#savedraftashtml) → Saves HTML of a Gmail draft to Drive
- [`generateHtmlFromDraft(subjectLine)`](#generatehtmlfromdraftsubjectline) → Generates and saves HTML version of an email draft
- [`cacheBlobToStore()`] → Wrapper to cache Drive images  
- [`cacheBlobToProperties_(fileId, blobName)`] → Stores Drive image as base64 in Script Properties  
- [`getBlobFromProperties_(blobKey)`] → Retrieves cached image blob  
- [`testRuntime()`] → Benchmarks email send runtime  
- [`sendEmail_(memberInformation)`] → Sends email from Gmail draft  
- [`getGmailTemplateFromDrafts(subjectLine)`] → Retrieves draft template and inline images  
- [`subjectFilter_(subjectLine)`] → Filters drafts by subject  
- [`fillInTemplateFromObject_(template, data)`] → Replaces `{{placeholders}}`  
- [`escapeData_(str)`] → Escapes special characters for safe JSON parsing
---

#### inlineImage()

Sends an example email with inline images to demonstrate image embedding.

```js
inlineImage();
```

**Output:** None (sends test email)

---

#### saveDraftAsHtml()

Saves the HTML content of a Gmail draft (by subject) as a file in Drive.

```js
saveDraftAsHtml();
```

**Output:** None

---

#### generateHtmlFromDraft(subjectLine)

Generates and saves the HTML version of an email draft found by subject.

```js
generateHtmlFromDraft("Here's your post-run report! 🙌");
```

| Name        | Type   | Description         |
|-------------|--------|---------------------|
| subjectLine | String | Subject of draft    |

**Output:** None (file created in Drive)