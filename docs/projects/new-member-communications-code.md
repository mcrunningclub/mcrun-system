# New Member Communications

Automates the process of sending welcome emails and digital passes to new members of the McGill Students Running Club. This Google Apps Script project integrates with Google Sheets, Gmail, and Google Drive to streamline member onboarding and communication.

## Features
- Automatically sends a personalized welcome email to new members.
- Generates and attaches a digital membership pass (with QR code) for each member.
- Logs email and pass delivery status in a Google Sheet.
- Supports updating and resending digital passes.
- Uses Gmail drafts and HTML templates for flexible email content.

## Main Functions
```javascript linenums="1"
  // Sends a welcome email to the member in the specified row of the sheet.
  sendWelcomeEmailInRow(row);

  // Sends a personalized welcome email to a new member using their information.
  sendWelcomeEmail_(memberInformation);

  // Generates a digital pass for a member and returns a download link.
  createPassFile_(passInfo);

  // Updates member status, creates a new pass, and sends an updated pass email.
  updateAndSendPass(statusObj, isLogged);

  // Logs email or pass status to the sheet.
  logMessage_(message, sheet, row);
```

## Example Usage

### Send Welcome Email to New Member
```javascript
// Send welcome email to the last row (newest member)
sendWelcomeEmailInRow();
```

### Generate and Send Updated Pass
```javascript
// Update member status and send new pass for row 5
updateAndSendPass({
  email: 'member@email.com',
  feeStatus: 'Paid',
  // ...other member info
});
```

### Create a Digital Pass for a Member
```javascript
const passUrl = createPassFile_({
  firstName: 'Jane',
  lastName: 'Doe',
  memberId: '12345',
  // ...other info
});
Logger.log(passUrl);
```

## Requirements
- Google Workspace (Gmail, Google Sheets, Google Drive)
- Script must be run from the club's Google account for full functionality

## License
Apache 2.0
