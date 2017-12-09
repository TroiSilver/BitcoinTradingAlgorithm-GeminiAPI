import random

class nonce:


    def generate_nonce(length):
        """Generate pseudorandom number."""
        return ''.join([str(random.randint(0, 9)) for i in range(length)])