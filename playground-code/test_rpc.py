from web3 import Web3

contract_addr = "0xe1e604bf82D018D790AdEAB911E7445336aA6e73"
rpc_url = "https://rpc.sepolia.org"

web3 = Web3(Web3.HTTPProvider(rpc_url))

contract_abi = [
    {
        "contant": True,
        "inputs": [],
        "name": "print",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

contract = web3.eth.contract(address=contract_addr, abi=contract_abi)

print(contract.functions.print().call())
