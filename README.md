OTPpy
=====

OTP library for Python 2.x : HOTP and TOTP ( RFC4226 &amp; RFC6238 )
Easy to use OTP generator : counter-based or time-based

* Fully compatible with standards
* Can manage 4 to 8 digits
* Can manage SHA1, SHA256 or SHA512 hash functions (as in RFC6238)

Compatible with Google Authenticator (default settings)

Example :

    import otppy
    otp = otppy.fromb32("BASE32-SECRET-HERE")
    hotp = otp.HOTP(counter)
    print "HOTP Code :", hotp
    totp = otp.TOTP() < Return [TOTP, Remaining Time in seconds]
    print "TOTP Code :", totp[0]


## Using library

Copy "otppy.py" and "hmac_OTP.py" in your working directory.
run otppy.py to check if everything is OK ("Tests Passed").
"import otppy" in your python program.


Form more details: see code


Test vectors from standards included in otppy run when
running otppy.py alone (as main).



## GUI Example

A basic GUI for TOTP is provided. GUI uses Tk included in Python.
User have to edit "user.dat" file with his credentials:
CSV 1 line per service: ServiceName,Base32Seed,HashAlg,Digits

HashAlg is either : sha1, sha256 or sha512
Digits is mostly: 6 or 8
For Google Auth, use sha1 and 6 digits
See existing example file user.dat provided

just launch GUI.pyw
TOTPs are refreshed automatically.
Text is red when remaining time is below 5 seconds.




Licence :
----------
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
