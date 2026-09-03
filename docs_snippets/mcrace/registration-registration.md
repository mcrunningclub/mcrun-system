### Registration.gs

- *function* [`getLastRowInReg_()`](#getlastrowinreg_)
- *function* [`onNewRegistration_({ newRow: row, member: memberArr })`](#onnewregistration_)
- *function* [`addNewRegistration_(registrationObj)`](#addnewregistration_registrationobj)
- *function* [`extractPaymentInfo_(memberArr)`](#extractpaymentinfo_memberarr)
- *function* [`extractFromSheet_(row)`](#extractfromsheet_row)

#### getLastRowInReg_()

Returns the last valid row in the `Registration` sheet.

Returns:

- (integer) - The last non-empty row in the `Registration` sheet.


#### onNewRegistration_({ newRow: row, member: memberArr }) {#onnewregistration_}

Processes a new registration by extracting payment information, verifying payment, 
and formatting the registration sheet.

Params:

- `this` (Object) - Input object with the following properties.
    - `this.newRow` (integer) - The new row added in the `Registration` sheet.
    - `this.member` (Object[]) - The formatted member values added in the `Registration` sheet.


#### addNewRegistration_(registrationObj)

Adds a new registration to the `Registration` sheet.

Formats the registration data and appends it to the sheet. Returns the new row and formatted member data.

Params:

- `registrationObj` (Object) - The registration data to add.

Returns:

- (Object) - An object containing the new row and formatted member data.


#### extractPaymentInfo_(memberArr)

Extracts payment information from a member array.

Params:

- `memberArr` (Object[]) - The array of member data.

Returns:

- (Member) - A Member object containing the payment information.


#### extractFromSheet_(row)

Extracts payment information using row number

Params:

- `row` (number) - Row to get information from

Returns:

- (Member) - A Member object containing the payment information.

