# -*- coding: utf-8 -*-
"""
A script to parse a license output file, and return a list of email addresses
of the active users of the given type.

DEV LOG:
 4 Mar 2014: Created script with lookup of user names, halpe@gst.dk
 8 Jan 2015: mahvi@gst.dk
30 Aug 2016: reading additional command line input, translating output to English, halpe@sdfe.dk
"""

import sys, string

lictype = "ARC/INFO"
if len(sys.argv) > 1:
    lictype = sys.argv[1]

licencefile = "./lmstat.txt"
if len(sys.argv) > 2:
    licencefile = sys.argv[2]

gstuserfile = "./lmstat-userlist.txt"
if len(sys.argv) > 3:
    gstuserfile = sys.argv[3]

inarcusers = False
# currentusers = []
allusers = []
mailaddresses = []
missing = []

# read all usernames
f = open(gstuserfile, 'r')
for line in f:
    if len(line.strip()) > 0:  # skip empty lines
        allusers.append(line.split())
# print allusers

# read current users
f = open(licencefile, 'r')
line = f.readline()

while line.find(lictype) == -1:
    line = f.readline()

for i in range(5):
    line = f.readline()  # read forward to first relevant line
    
while(len(line.strip())>0):
    l = line.strip().split()
    # currentusers.append(l[0])
    found = False
    for a in allusers:
        if l[0].lower() == a[0]:
            mailaddresses.append(a[1])
            found = True
    if not found:
        if line[0].islower():
            missing.append(l[0])
        else:
            l2 = line.split("-")
            name = line[:l2[0].rfind(" ")]
            missing.append(name)
    line = f.readline()
    
# print "\nMAIL ADDRESSES FOUND:"
for m in mailaddresses:
    print m

print

# print "\nUSERS NOT FOUND:"
for u in missing:
    print u
    
if missing:
    print
    print "Any usernames with unknown email address can be looked up in Windows under Explorer -> Network -> Search Active Directory.\nConsider adding them to {}, so they're available in the future.".format(gstuserfile)
