# Project Source Code Documentation

Each project has its own Google Sheet and associated Google Apps Scripts, and its own Github repo.

**Membership Code** manages the club membership ledger

**Attendance Code** records attendance at various events

**Points System Code** keeps track of members' points and sends emails accordingly


**McRace Code** contains stuff for our 5k race event

<br> 

## How to Read Function Documentation

Each function is documented using the following template (see image):

### Example:

**sendEmail(recipient, subject, body)**  
Sends an email message.

```js
MailApp.sendEmail(
  'recipient@example.com',
  'TPS reports',
  'Where are the TPS reports?',
);
```

| Name      | Type   | Description                              |
|-----------|--------|------------------------------------------|
| recipient | String | The addresses of the recipients          |
| subject   | String | The subject line                         |
| body      | String | The body of the email                    |

---
