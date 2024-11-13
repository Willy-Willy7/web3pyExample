from web3 import Web3
import json
from config import INFURA_URL, PRIVATE_KEY, CONTRACT_ADDRESS

class Web3Interaction:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(INFURA_URL))
        self.account = self.w3.eth.account.from_key(PRIVATE_KEY)
        self.contract = self.load_contract()

    def load_contract(self):
        with open('contract/SimpleStorage.json') as f:
            contract_json = json.load(f)
        return self.w3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_json['abi'])

    def set_value(self, value):
        nonce = self.w3.eth.getTransactionCount(self.account.address)
        tx = self.contract.functions.set(value).buildTransaction({
            'chainId': 1,  # Mainnet
            'gas': 2000000,
            'gasPrice': self.w3.toWei('50', 'gwei'),
            'nonce': nonce,
        })
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
        tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    def get_value(self):
        return self.contract.functions.get().call()
