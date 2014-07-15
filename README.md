OTPpy
=====

OTP library for Python 2.x : HOTP and TOTP ( RFC4226 &amp; RFC6238 )


Example :

import otppy
otp = otppy.fromb32("BASE32-SECRET-HERE")
hotp = otp.HOTP(counter)
print "HOTP Code :", hotp
totp = otp.TOTP() < Return [TOTP, Remaining Time in seconds]
print "TOTP Code :", totp[0]


Form more details , see code