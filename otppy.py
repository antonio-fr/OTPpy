

import hmac_OTP
import time
import base64
import struct

class OTP:
	def __init__(self, secret, hashalg="sha1", digits=6):
		self._secret = secret
		self.hashalg = hashalg
		self.digits = digits
	
	def HOTP(self, counter, digits=None):
		if digits==None:
			digits=self.digits 
		count_byts = struct.pack('>Q', counter)
		h=hmac_OTP.new(self._secret, count_byts, self.hashalg)
		hmac_digest = h.digest()
		return self.Truncate(hmac_digest,digits)
	
	def TOTP(self, window=30, digits=None):
		if digits==None:
			digits=self.digits
		prestime = long(time.time())
		C = prestime // window
		rema_sec = (C+1)*window - prestime
		return self.HOTP(C, digits), rema_sec
	
	def Truncate(self, hmac_digest, digits):
		assert digits<9
		iob = ord(hmac_digest[-1])& 15
		token_base = struct.unpack('>I', hmac_digest[iob:iob + 4])[0] & 2147483647
		token = token_base % 10**digits
		fmt = '{:0'+chr(digits+48)+'d}'
		return fmt.format(token)

def fromb32(secret_base32, hashalg="sha1", digits=6):
	secret = base64.b32decode(secret_base32, True)
	return OTP(secret, hashalg, digits)


if __name__ == "__main__":
	otp0 = fromb32("MFRGGZDFMZTWQ2LK")
	assert otp0.HOTP(2) == "816065"
	assert otp0.HOTP(int(time.time())//30) == otp0.TOTP()[0]
	
	
	# RFC4226 Appendix D Test Values
	seed_sha1 = "12345678901234567890"
	otp1 = OTP(seed_sha1)
	assert otp1.HOTP(2)=="359152"
	assert otp1.HOTP(5)=="254676"
	assert otp1.HOTP(8)=="399871"
	
	
	# RFC6238 Appendix B Test Vectors
	seed_sha256 =   seed_sha1+"123456789012"
	seed_sha512 = 3*seed_sha1+"1234"
	otp256 = OTP(seed_sha256, "sha256", 8 )
	otp512 = OTP(seed_sha512, "sha512", 8 )
	
	timetest = 59
	C = long(timetest) // 30
	assert otp1.HOTP(C, 8)=="94287082"
	
	timetest = 1234567890
	C = long(timetest) // 30
	assert otp1.HOTP(C, 8)=="89005924"
	assert otp1.HOTP(C   )==  "005924"
	assert otp256.HOTP(C )=="91819424"
	assert otp512.HOTP(C )=="93441116"
	
	timetest = 2000000000
	C = long(timetest) // 30
	assert otp1.HOTP(C, 8)=="69279037"
	assert otp256.HOTP(C )=="90698825"
	assert otp512.HOTP(C )=="38618901"
	
	print "Test Passed"

