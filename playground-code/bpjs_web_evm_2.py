from web3 import Web3
import inspect

infura_url = "https://rpc-mumbai.maticvigil.com"

web3 = Web3(Web3.HTTPProvider(infura_url))

contract_address = "0x0499fcD8Aa4A23c26a4a0e625194B102d4ABA2dF"

topics = ['0x844e4fccb87d6d1843733397bf5d41ce3551716260f6e90263dbbed3bda32f4f']
from_block = 40275908
to_block = 40276268

contract_abi = [
  {
    "Inputs": [],
    "StateMutability": "Payable",
    "Type": "Constructor"
  },
  {
    "Anonymous": False,
    "Inputs": [
      {
        "Indexed": False,
        "InternalType": "String",
        "Name": "Context",
        "Type": "String"
      }
    ],
    "Name": "Added",
    "Type": "Event"
  },
  {
    "Inputs": [
      {
        "InternalType": "String",
        "Name": "Context",
        "Type": "String"
      }
    ],
    "Name": "Add",
    "Outputs": [],
    "StateMutability": "Nonpayable",
    "Type": "Function"
  },
  {
    "Inputs": [],
    "Name": "Owner",
    "Outputs": [
      {
        "InternalType": "Address Payable",
        "Name": "",
        "Type": "Address"
      }
    ],
    "StateMutability": "View",
    "Type": "Function"
  }
]

event_filter = {
    'address': contract_address,
    'topics': topics,
    'fromBlock': from_block,
    'toBlock': to_block
}
event_logs = web3.eth.get_logs(event_filter)

for log in event_logs:
    print(log)

