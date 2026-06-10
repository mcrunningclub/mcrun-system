### Member Info.gs
- [`getUserTimeZone_()`](#getusertimezone_) → Returns user's timezone
- [`GET_LITERAL_SHEET()`](#get_literal_sheet) → Returns the "Literals" sheet object
- [`GET_PAYMENT_LOG_SHEET()`](#get_payment_log_sheet) → Returns the "Payment Logs" sheet object  
- [`getCurrentUserEmail_()`] → Returns active user email  
- [`getDraftBySubject_(subject)`] → Returns Gmail draft by subject  
- [`getDraftById_(id)`] → Returns Gmail draft by ID  
- [`createNewMemberCommunications(memberObj)`] → Full new member onboarding pipeline  
- [`appendNewValues_(memberObj, sheet)`] → Appends new member to Literals sheet  
- [`triggerUpdateAndSendPass(row)`] → Updates pass from Payment Logs  
- [`updateAndSendPass(statusObj, isLogged)`] → Updates pass and sends email  
- [`logPaymentStatus_(status)`] → Appends payment log entry  
- [`findRowByEmail_(email)`] → Finds row index by email  
- [`logMessage_(message, sheet, row)`] → Logs status message in sheet
  
---

#### getUserTimeZone_()

Returns the user's timezone from script settings.

```js
const tz = getUserTimeZone();
```

**Output:** String (timezone)

---

#### GET_LITERAL_SHEET()

Returns the "Literals" sheet, or opens by ID if not found.

```js
const sheet = GET_LITERAL_SHEET();
```

**Output:** Google Sheet object

---

#### GET_PAYMENT_LOG_SHEET()

Returns the "Payment Logs" sheet, or opens by ID if not found.

```js
const sheet = GET_PAYMENT_LOG_SHEET();
```

**Output:** Google Sheet object