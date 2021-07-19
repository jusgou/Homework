# Import dependencies
import os
import subprocess
import json
from dotenv import load_dotenv
import bit
import web3

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")


# # Import constants.py and necessary functions from bit and web3
from constants import *
 
mnemonic = "twelve enforce skin bag choice alcohol club organ item rebel enlist idle"
 
# # Create a function called `derive_wallets`

command = f'./derive  -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --format=json --coin={ETH} --numderive=3'
    
p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p.wait()

print(output)

# # Create a dictionary object called coins to store the output from `derive_wallets`.
# # parameterize coin in derive wallets function / create other coin dictionaries that stores the outputs of the subsequent calls (dictionary) (dictionary is currently a single call, add with for loop or some such)
# coins = json.loads(output)
# print(coins)

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
# def priv_key_to_account(# YOUR CODE HERE):
#     # YOUR CODE HERE
#     pass

# # Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
# def create_tx(# YOUR CODE HERE):
#     # YOUR CODE HERE
#     pass

# # Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
# def send_tx(# YOUR CODE HERE):
#     # YOUR CODE HERE
#     pass 