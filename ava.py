import grpc
import datetime
from web3 import Web3
from eth_account import Account
from eth_account.messages import encode_defunct
import avs_pb2
import avs_pb2_grpc
import os

class AvaClient:
    def __init__(self, private_key, network='holesky', auth_token_expiration_minutes=60):
        # Store the private key securely
        self.private_key = private_key
        self.wallet_address = Account.from_key(private_key).address

        # Set the network endpoint based on the network choice
        if network == 'mainnet':
            endpoint = 'aggregator.avaprotocol.org:2206'
        elif network == 'holesky':
            endpoint = 'aggregator-holesky.avaprotocol.org:2206'  # Replace with actual testnet endpoint if different
        else:
            raise ValueError("Invalid network specified. Choose 'mainnet' or 'holesky'.")

        # Establish an insecure gRPC channel
        # credentials = grpc.ssl_channel_credentials()
        self.channel = grpc.insecure_channel(endpoint)
        self.stub = avs_pb2_grpc.AggregatorStub(self.channel)  # Used to make RPC calls to the server

        # Initialize auth_key and metadata
        self.auth_key = None
        # self.metadata = None

        # Authenticate and get auth token
        self.get_auth_token(expiration_minutes=auth_token_expiration_minutes)

    def generate_timestamp(self, minutes=60):
        # Get the current UTC time and add 'minutes' minutes
        current_time = datetime.datetime.utcnow()
        expiration_time = current_time + datetime.timedelta(minutes=minutes)
        # Convert to UNIX timestamp
        timestamp = int(expiration_time.timestamp())
        return timestamp

    def generate_signature(self, message_text):
        # Sign the message using the private key
        message = encode_defunct(text=message_text)
        signed_message = Account.sign_message(message, private_key=self.private_key)
        signature = signed_message.signature.hex()
        # the signature doesnt have the 0x prefix but the ava protocol will return an error if it doesnt have one
        return "0x" + signature

    def get_auth_token(self, expiration_minutes=60):
        # Generate expiration timestamp
        expired_at = self.generate_timestamp(minutes=expiration_minutes)

        # Create the message to sign
        message_text = f'key request for {self.wallet_address} expired at {expired_at}'

        # Generate signature
        signature = self.generate_signature(message_text)

        # Prepare the GetKey request
        get_key_request = avs_pb2.GetKeyReq(
            owner=self.wallet_address,
            expired_at=expired_at,
            signature=signature
        )

        # Make the GetKey RPC call
        try:
            key_response = self.stub.GetKey(get_key_request)
            self.auth_key = key_response.key
            self.metadata = [('authkey', self.auth_key)]
            print('Authentication successful.')
        except grpc.RpcError as e:
            print(f'Authentication failed: {e.details()}')
            raise

    def get_nonce(self):
        # Prepare the NonceRequest
        nonce_request = avs_pb2.NonceRequest(owner=self.wallet_address)
        # Make the GetNonce RPC call
        try:
            nonce_response = self.stub.GetNonce(nonce_request, metadata=self.metadata)
            print(f"Nonce: {nonce_response.nonce}")
            return nonce_response.nonce
        except grpc.RpcError as e:
            print(f'GetNonce failed: {e.details()}')
            raise

    def create_task(self, task_request):
        # Make the CreateTask RPC call
        try:
            create_task_response = self.stub.CreateTask(task_request, metadata=self.metadata)
            print(f'Task created with ID: {create_task_response.id}')
            return create_task_response.id
        except grpc.RpcError as e:
            print(f'CreateTask failed: {e.details()}')
            raise

    def close(self):
        # Close the gRPC channel
        self.channel.close()
