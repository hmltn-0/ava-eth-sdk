

import grpc
import avs_pb2
from avs_pb2_grpc import AggregatorStub

from web3 import Web3
from eth_account import Account
from eth_account.messages import encode_defunct


import os

import datetime

import secrets


def main():
    # Establish a secure channel using SSL/TLS
    credentials = grpc.ssl_channel_credentials()
    channel = grpc.secure_channel('aggregator.avaprotocol.org:2206', credentials)
    
    # Create a stub (client)
    stub = AggregatorStub(channel)

    print(stub)

if __name__ == '__main__':
    main()
