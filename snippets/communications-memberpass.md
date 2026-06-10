### Member Pass.gs

- [`createPassFile(passInfo)`](#createpassfilepassinfo) → Generates a digital membership pass using Google Slides
- [`createNewPass(row)`] → Regenerates pass using sheet row data  
- [`testRuntime()`] → Benchmarks pass generation runtime  
- [`generateQrUrl_(memberID)`] → Generates QR code URL  
- [`getImage_(url)`] → Fetches image from URL  
- [`loadImageBytes_(id)`] → Loads Drive file as base64  
- [`testQRGenerator_()`] → Tests QR code generation and storage


#### createPassFile(passInfo)

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