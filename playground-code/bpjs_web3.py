from web3 import Web3
import inspect

infura_url = "https://rpc-mumbai.matic.today"

web3 = Web3(Web3.HTTPProvider(infura_url))

contract_address = "0xCE69Ea4901b51d0E24981be690010E48E1C6336c"
contract_abi = [
  {
    "inputs": [],
    "name": "participate",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]
contract = web3.eth.contract(contract_address, abi=contract_abi)
result = contract.functions.participate().call()

print(result)
