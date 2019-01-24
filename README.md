Install https://www.controlplaneapp.com/

Setup a new context called "lock screen" and one called "unlock screen"

Add the evidence sources called "Sleep/Wake Event" and "Screen Lock/Unlock"

Add a rule that sets the context to "Unlock screen" when screen lock is "unlocked"
Add a rule that sets the context to "Lock screen" when screen lock is "locked"
Add a rule that sets the context to "Unlock screen" when system is going to "Wake"
Add a rule that sets the context to "Lock screen" when system is going to "Sleep"

Add a Action that runs the "login.sh" script on "unlock screen" context
Add a Action that runs the "logout.sh" script on "lock screen" context
