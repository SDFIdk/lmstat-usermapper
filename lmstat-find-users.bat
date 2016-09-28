@echo off

@rem Get licence info from the server, get matching email addresses, and display to the user.
@rem Early versions by mahvi@gst.dk, recent versions by halpe@sdfe.dk

@rem --- USER VARIABLES ---

@rem License server
set LICSERVER=10.34.129.186

@rem License type to get email addresses for
set LICTYPE="ARC/INFO"

@rem List of usernames and emails
set USERLIST=lmstat-userlist.txt

@rem Output files
set LICOUTPUT=lmstat.txt
set USEROUTPUT=lmstat-current-users.txt

@rem --- END USER VARIABLES --- DO NOT EDIT BELOW THIS LINE ---

@rem We want to make sure we execute script from its own directory
set ORIGDIR=%CD%
cd %~dp0

@rem TODO: Check existence of user file and warn if not found

call lmutil lmstat -a -c @%LICSERVER% > "%TMP%\%LICOUTPUT%"
call python.exe lmstat-users.py %LICTYPE% "%TMP%\%LICOUTPUT%" "%USERLIST%" > "%TMP%\%USEROUTPUT%"
start %TMP%\%LICOUTPUT%
start %TMP%\%USEROUTPUT%

@rem Return user to original directory
cd "%ORIGDIR%"
