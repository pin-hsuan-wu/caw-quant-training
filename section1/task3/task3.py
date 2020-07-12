import etherscan.accounts as accounts
from etherscan.blocks import Blocks
from etherscan.contracts import Contract
from etherscan.proxies import Proxies
import etherscan.stats as stats
import etherscan.tokens as tokens
import etherscan.transactions as transactions
import json
from pandas.io.json import json_normalize
import pandas as pd


with open("./key.txt") as k:
    key = k.read()
    
address = '0x2a65aca4d5fc5b5c859090a6c34d164135398226'

#accounts
api = accounts.Account(address=address, api_key=key)

#get_balance
balance = api.get_balance()
print(balance)

#get_transaction_page
tran_page = api.get_transaction_page(page=1, offset=10)
t = json_normalize(tran_page)
print(t)

#get_all_transactions
trans = api.get_all_transactions(offset=10)

#get_transaction_page_erc20
trans_erc20 = api.get_transaction_page(erc20=True)
t_erc20 = json_normalize(trans_erc20)
print(t_erc20)

#get_blocks_mined_page
bl_mined_page = api.get_blocks_mined_page(page=1, offset=10)
bmp = json_normalize(bl_mined_page)
print(bmp)

#get_all_blocks_mined
blocks_mined = api.get_all_blocks_mined()

#get multiple balance
address = ['0xbb9bc244d798123fde783fcc1c72d3bb8c189413', '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a']
api = accounts.Account(address=address, api_key=key)
balances = api.get_balance_multiple()
print(balances)


#blocks
api_b = Blocks(api_key=key)
reward = api_b.get_block_reward(2165403)
r = json_normalize(reward)
print(r)
print(r['blockReward'])
uncle_r = json_normalize(r['uncles'][0])
print(uncle_r)


#contracts
address = '0x6e03d9cce9d60f3e9f2597e13cd4c54c55330cfd'
api_c = Contract(address=address, api_key=key)

#get_abi
abi = api_c.get_abi()
with open('abi.json', 'w') as fd: 
    fd.write(abi)
df_abi = pd.read_json('abi.json')
print(df_abi)

#get_sourcecode
sourcecode = api_c.get_sourcecode()
sc_norm = json_normalize(sourcecode)
df_sc = pd.DataFrame(sc_norm)
print(df_sc)


#proxies
api_p = Proxies(api_key=key)

#gas price
price = api_p.gas_price()
print(price)

#get block by number
bl = api_p.get_block_by_number(0x57b414)
bl_norm = json_normalize(bl)
bl_norm_trans = bl_norm['transactions'].apply(lambda x: json_normalize(x))
print(bl_norm)
print(bl_norm_trans[0])

#get block transaction count by number
tx_count = api_p.get_block_transaction_count_by_number(block_number='0x57b414')
print(int(tx_count, 16))

#get code
code = api_p.get_code('0x48f775efbe4f5ece6e0df2f7b5932df56823b990')
print(code)

#get most recent block
rblock = api_p.get_most_recent_block()
print(int(rblock, 16))

#get storage
value = api_p.get_storage_at('0x6e03d9cce9d60f3e9f2597e13cd4c54c55330cfd', 0x1)
print(value)

#get transaction by blocknumber index
transaction = api_p.get_transaction_by_blocknumber_index(block_number='0x57b414', index='0x2')
norm_transaction = json_normalize(transaction)
print(norm_transaction)

#get transaction by hash
TX_HASH = '0xb11f622f0f58d8648bd456d751329de27b402fbc974167cb468bbc260d966f57'
tran_by_hash = api_p.get_transaction_by_hash(tx_hash=TX_HASH)
norm_tran_by_hash = json_normalize(tran_by_hash)
print(norm_tran_by_hash)

#get transaction count
count = api_p.get_transaction_count('0x7896f0cea889964c00fb47fcddf89eab42eb9df8')
print(int(count, 16))

#get transaction receipt 
receipt = api_p.get_transaction_receipt('0x498abfd4aac86b970b54b6fea4fa32948a6838f33bedf6aae55eaf31c6acce94')
norm_receipt = json_normalize(receipt)
print(norm_receipt)

#get uncles by blocknumber index 0x210A9B
uncles = api_p.get_uncle_by_blocknumber_index(block_number='0x210A9B', index='0x1')
print(uncles['uncles']) 


#stats
api_s = stats.Stats(api_key=key)

#get ether last price
lastprice = api_s.get_ether_last_price()
print(lastprice)

#get total ether supply
total_supply = api_s.get_total_ether_supply()
print(total_supply)


#tokens
contract_address = '0x57d90b64a1a57749b0f932f1a3395792e12e7055'
api_t = tokens.Tokens(contract_address=contract_address, api_key=key)

#token balance
address = '0xe04f27eb70e025b78871a2ad7eabe85e61212761'
tb = api_t.get_token_balance(address=address)
print(tb)

#total supply of tokens
total_supply_t = api_t.get_total_supply()
print(total_supply_t)


#transactions
api_tran = transactions.Transactions(api_key=key)

#get status
TX_HASH = '0xb11f622f0f58d8648bd456d751329de27b402fbc974167cb468bbc260d966f57'
status = api_tran.get_status(tx_hash=TX_HASH)
print(status)

#receipt status
receipt_status = api_tran.get_tx_receipt_status(tx_hash=TX_HASH)
print(receipt_status)