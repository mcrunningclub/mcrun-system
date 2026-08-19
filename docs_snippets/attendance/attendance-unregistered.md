### Unregistered.gs

- *function* [`getAllUnregisteredMembers_()`](#getallunregisteredmembers_)
- *function* [`getUnregisteredMembersInRow_(row)`](#getunregisteredmembersinrow_row)
- *function* [`getUnregisteredFromList_(attendees, memberMap)`](#getunregisteredfromlist_attendees-membermap)
- *function* [`formatName_(name)`](#formatname_name)
- *function* [`reverseName_(name)`](#reversename_name)
- *function* [`formatAndSortMemberMap_(memberMap, searchKeyIndex, emailIndex)`](#formatandsortmembermap_membermap-searchkeyindex-emailindex)
- *function* [`swapAndFormatNames_(names)`](#swapandformatnames_names)
- *function* [`getMemberMap_()`](#getmembermap_)

#### getAllUnregisteredMembers_()

Finds attendees who are unregistered members for all rows in the attendance sheet.

#### getUnregisteredMembersInRow_(row)

Find attendees in a specific row of the attendance sheet who are unregistered members.
Sets unregistered members in the "Not Found" column. List of members found in `Members` sheet.

Params:

- `row` (number) - *Optional* The row number in the attendance sheet (1-indexed).
                               Defaults to the last row in the sheet.

#### getUnregisteredFromList_(attendees, memberMap)

Finds unregistered attendees in the given list by comparing against the member map.

Params:

- `attendees` (string[]) - All attendees of the head run (sorted).
- `memberMap` (string[][]) - All search keys of registered members (sorted) and emails.

Returns:

- (Object) - An object containing registered and unregistered attendees.
                   { registered: string[], unregistered: string[] }

#### formatName_(name)

Formats a name by removing whitespace, stripping accents, and capitalizing names.

Params:

- `name` (string) - The name to format.

Returns:

- (string) - The formatted name.

#### reverseName_(name)

Reverses the order of a name to `LastName, FirstName` format.

Params:

- `name` (string) - The name to reverse.

Returns:

- (string) - The reversed name.

#### formatAndSortMemberMap_(memberMap, searchKeyIndex, emailIndex)

Formats and sorts all entries in the member map by search key.
Removes whitespace, hyphens, and accents, and capitalizes names.

Params:

- `memberMap` (string[][]) - Array of search keys and their emails.
- `searchKeyIndex` (number) - The index of the search key in the member map.
- `emailIndex` (number) - The index of the email in the member map.

Returns:

- (string[][]) - A sorted array of formatted names and emails.

Example:

```js
// Sample Script ➜ Format, then sort names.
const rawData = [["Francine de-Blé", "francine.de-ble@mail.com"],
                 ["BOb-Burger belChEr ", "bob.belcher@mail.com"]];
const result = formatAndSortMemberMap_(rawData);
Logger.log(result)  // [["Bob Burger Belcher", "bob.belcher@mail.com"],
                        [ "Francine De ble", "francine.de-ble@mail.com"]]
```

#### swapAndFormatNames_(names)

Formats and sorts an array of names, swapping last and first names.
Removes whitespace, apostrophes, and accents, and capitalizes names.

Params:

- `names` (string[]) - Array of names to format.

Returns:

- (string[]) - A sorted array of formatted names.

Example:

```javascript
// Sample Script ➜ Format, swap first and last name, then sort.
const rawNames = ["BOb-Burger bulChEr ", "Francine de-Blé"];
const result = swapAndFormatName_(rawNames);
Logger.log(result)  // ["Bulcher, Bob Burger", "De ble, Francine"]
```

#### getMemberMap_()

Retrieves the member map from the `Members` sheet.
Combines member search keys and emails, filtering out empty rows.

Returns:

- (string[][]) - An array of member search keys and emails.

