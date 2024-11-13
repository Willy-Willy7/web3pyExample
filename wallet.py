from web3 import Web3

class Wallet:
    def __init__(self, private_key):
        self.w3 = Web3()
        self.private_key = private_key
        self.address = self.w3.eth.account.from_key(private_key).address

    def get_balance(self):
        return self.w3.eth.get_balance(self.address)
