import pytest
import etherscan.accounts as accounts
from etherscan.blocks import Blocks
from etherscan.proxies import Proxies
import re


with open("./not_commit/key.txt") as k:
    key = k.read()
    
address = '0x2a65aca4d5fc5b5c859090a6c34d164135398226'


def test_single_balance():
    api = accounts.Account(address=address, api_key=key)
    single_balance = '2705137562827380044250'
    assert api.get_balance() == single_balance

def test_block_reward():
    api_b = Blocks(api_key=key)
    block = '2165403'
    reward = '5314181600000000000'
    uncle_reward = '312500000000000000'
    response = api_b.get_block_reward(block)
    assert response['blockReward'] == reward
    assert response['uncleInclusionReward'] == uncle_reward

def test_get_trans_count():
    api_p = Proxies(api_key=key)
    address = '0x7896f0cea889964c00fb47fcddf89eab42eb9df8'
    p = re.compile('^[0-9]*$')
    count = api_p.get_transaction_count(address)
    assert p.match(str(int(count, 16)))


