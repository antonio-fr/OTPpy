"""HMAC (Keyed-Hashing for Message Authentication) Python module for OTPpy"""

trans_5C = "".join ([chr (x ^ 0x5C) for x in xrange(256)])
trans_36 = "".join ([chr (x ^ 0x36) for x in xrange(256)])

digest_size = None

class HMAC:
    blocksize = 64
    
    def __init__(self, key, msg = None, digestmod = None):
        """Create a new HMAC object.

        key:       key for the keyed hash object.
        msg:       Initial input for the hash, if provided.
        digestmod: A module hash type string
        """
        
        from hashlib import new as newhash
        if digestmod is None:
            digestmod = 'md5'
        self.outer = newhash(digestmod)
        self.inner = newhash(digestmod)
        self.digest_size = self.inner.digest_size
        
        
        blocksize = self.inner.block_size
        
        if len(key) > blocksize:
            key = self.newhash(digestmod).update(key).digest()
        
        key = key + chr(0) * (blocksize - len(key))
        self.outer.update(key.translate(trans_5C))
        self.inner.update(key.translate(trans_36))
        if msg is not None:
            self.update(msg)
    
    def update(self, msg):
        self.inner.update(msg)
    
    def _current(self):
        h = self.outer.copy()
        h.update(self.inner.digest())
        return h
    
    def digest(self):
        h = self._current()
        return h.digest()

def new(key, msg = None, digestmod = None):
    return HMAC(key, msg, digestmod)
