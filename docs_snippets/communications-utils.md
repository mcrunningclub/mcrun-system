### Utils.gs

- *function* [`getUserTimeZone_()`](#getusertimezone_)
- *function* [`getCurrentUserEmail_()`](#getcurrentuseremail_)
- *function* [`escapeData_(str)`](#escapedata_str)
- *function* [`findRowByEmail_(targetEmail)`](#findrowbyemail_targetemail)
- *function* [`toCamelCase_(str)`](#tocamelcase_str)
- *function* [`cacheBlobToStore()`](#cacheblobtostore)
- *function* [`cacheBlobToProperties_(fileId, blobName)`](#cacheblobtoproperties_fileid-blobname)
- *function* [`getBlobFromProperties_(blobName)`](#getblobfromproperties_blobname)

#### getUserTimeZone_()

Gets time zone of the script

Returns:

- (string) - Time zone

#### getCurrentUserEmail_()

Gets email address of the current user

Returns:

- (string) - The user's email's address, or a blank string if address can't be accessed

#### escapeData_(str)

Escape cell data to make JSON safe.

Params:

- `str` (string) - to escape JSON special characters from

Returns:

- (string) - escaped string

#### findRowByEmail_(targetEmail)

Find row in Literals sheet that has the given email

Params:

- `targetEmail` (string) - Email address to find

Returns:

- (integer) - Row in Literals sheet (1-indexed), or 0 if email not found

#### toCamelCase_(str)

Replaces snake case string with camel case string

Params:

- `str` (string) - String in snake case, e.g. hello_world

Returns:

- (string) - Input converted to camel case, e.g. helloWorld

#### cacheBlobToStore()

Stores email header, linktree logo, strava logo, and run map images in script properties

#### cacheBlobToProperties_(fileId, blobName)

Stores given Google Drive file in script properties under given name

Gets blob from file, outputs encoded string in console. Need to manually add
to script properties.

Params:

- `fileId` (string) - ID of file to store
- `blobName` (string) - Name of property to store encoded file under

#### getBlobFromProperties_(blobName)

Fetches and decodes image blob from script properties using given name

Throws error if not found.

Params:

- `blobName` (string) - Name of property that stores the image

Returns:

- (Image) - Blob decoded as png

