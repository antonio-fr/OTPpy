#!/usr/bin/env python


import otppy

# Create OTP object (SHA1 and 6 digits), with secret seed from base32
ex_otp = otppy.fromb32("BLABLA2BLABLA234")
# Compute TOTP and gives also remaining time
totp = ex_otp.TOTP()

print "OTP Code :", totp[0]
print totp[1], "sec left"

