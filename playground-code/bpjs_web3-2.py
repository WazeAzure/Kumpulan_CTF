from web3 import Web3

# URL dari Polygon Mumbai RPC
#rpc_url = "https://rpc-mumbai.matic.today"
#rpc_url = "https://mainnet.infura.io/v3/e3735c324e9a46088354ae7702814e5e"
rpc_url = "https://rpc-mumbai.maticvigil.com"

# Alamat kontrak dan ABI yang Anda berikan
contract_address = "0xCE69Ea4901b51d0E24981be690010E48E1C6336c"
contract_abi = [
   {
       "inputs": [],
       "name": "getFlag",
       "outputs": [{"internalType": "string", "name": "", "type": "string"}],
       "stateMutability": "view",
       "type": "function"
   }
]

# Inisialisasi web3
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Buat instance kontrak
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Panggil fungsi GetFlag()
try:
   flag = contract.functions.getFlag().call()
   print("Flag:", flag)
except Exception as e:
   print("Error:", e)

