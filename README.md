# lmstat-usermapper

A tool to display a list of email addresses of the active users of the given licence type.

It uses the tool `lmutil.exe`, together with the `lmstat-find-users.bat` and `lmstat-users.py` included here.


## Setup
Create a file `lmstat-userlist.txt` with a list of usernames and emails. One "`username<tab>email`" per line.

Make sure `lmutil.exe` is in the same directory as the files.

Edit the file `lmstat-find-users.bat`, and change line 9 to point to your licence server (`LICSERVER`). You don't need to edit anything else.

If you want to check for a different licence type than ARC/INFO, edit the `LICTYPE` variable in `lmstat-find-users.bat`.


## Usage
Double-click `lmstat-find-users.bat`.

It will open two text files. One displays a list of email addresses of the users currently using a licence (repeated if they have more than one). The other file displays the complete output from lmutil.

Checked-out licences will display as ACTIVATED LICENSE(S) followed by computer name. The Python script could be extended to lookup those too, but currently it doesn't.
