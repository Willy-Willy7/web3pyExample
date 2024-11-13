from web3_interaction import Web3Interaction

def main():
    web3_interaction = Web3Interaction()

    # Set a value in the smart contract
    tx_hash = web3_interaction.set_value(42)
    print(f'Transaction sent: {tx_hash}')

    # Get the value from the smart contract
    value = web3_interaction.get_value()
    print(f'Stored value: {value}')

if __name__ == "__main__":
    main()
