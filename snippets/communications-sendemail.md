### Send Email.gs
- [`sendWelcomeEmailInRow(row)`](#sendwelcomeemailinrowrow) → Sends a welcome email to the member in a row
- [`sendWelcomeEmail(memberInformation)`](#sendwelcomeemailmemberinformation) → Sends a personalized welcome email using member info
- [`sendUpdatedPass(member)`] → Sends an updated digital pass email  
- [`quickPassUpdate(row)`] → Creates a new pass and sends updated pass email

---

#### sendWelcomeEmailInRow(row)

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

#### sendWelcomeEmail(memberInformation)

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