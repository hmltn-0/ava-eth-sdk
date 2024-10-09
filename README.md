This is my submission to the Permissionless Hackathon, 2024. I learned a lot doing this. It was my first hackathon. My project may not fulfill the challenge description perfectly, but it was what I was capable of pulling off in 36 hours. Since it is not a robust tool, I will actually just use this README to explain what I learned, as a way of organizing what I did during this hackathon.

First of all, I am still working on fully understanding what Ava Protocol does. I understand that it is essentially "running on Eigenlayer" as an "AVS". I did not have enough time to study this. I assume Eigenlayer has servers in some kind of network. I do not fully understand what Eigenlayer really does, though. It mentions "restaking", amongst other things.

What I do know is that Ava Protocol basically wrote a Protobuf protocol. And that protocol does not actually look that complex. I will walk through what it says:

---------
As Protobuf has presumably had different versions, with different syntaxes, it starts with a version declaration (like declaring which version of HTML youäre using):
```
syntax = "proto3";
```

```
package aggregator;
```

This may not be essential, but may be useful when generating Python code from this .proto file. I'm not sure.

```
option go_package = "./avsproto";
```

If you are not using Go, I am pretty sure you do not need this.

``` 
import "google/protobuf/timestamp.proto";
import "google/protobuf/wrappers.proto";
``` 

These are classes from the Protobuf library. Basically, the normal way to interact with a Protobuf protocol is by using "gRPC", which stands for "Google Remote Procedure Calls". Remote procedure calls are just a way of sending executable commands onto some other computer (i.e. over the internet, in this case). 

So if you were to try to interact with this protocol using gRPC directly, you can use a command line tool like `grpcurl` (installable with `brew`, if you are on Mac). You can see what "services" a grpc server offers, with a command like:

`grpcurl -plaintext localhost:50051 list`

Ava has an RPC URL. The mainnet - where transactions are real and happen - is `aggregator.avaprotocol.org:2206`. The testnet - where you can practice running commands, without using real money, is `aggregator-holesky.avaprotocol.org:2206`. Essentially, the first part of that string is a hostname, I believe, and the number at the end is the port of a server you are connecting to. As far as I know, your machine finds the remote machine with these urls, using DNS resolution, just like with HTTP requests. On the test network, you use the Sepolia Ethereum currency, on the Sepolia network. (This is the standard way to test anything to do with Ethereum, at the moment.)

So to actually see the available services, we use the above command with the actual URL:

`grpcurl -plaintext aggregator.avaprotocol.org:2206 list`

which returns this:

```aggregator.Aggregator
grpc.reflection.v1.ServerReflection
grpc.reflection.v1alpha.ServerReflection
```

"Reflection", I believe, is more like for getting information about the server; whereas `aggregator.Aggregator` is the actual endpoint where you send commands. We list the methods inside the `Aggregator` service:

``` > grpcurl -plaintext aggregator.avaprotocol.org:2206 list aggregator.Aggregator

aggregator.Aggregator.CancelTask
aggregator.Aggregator.CreateTask
aggregator.Aggregator.DeleteTask
aggregator.Aggregator.GetKey
aggregator.Aggregator.GetNonce
aggregator.Aggregator.GetSmartAccountAddress
aggregator.Aggregator.GetTask
aggregator.Aggregator.ListTasks
aggregator.Aggregator.Ping
aggregator.Aggregator.SyncTasks
aggregator.Aggregator.UpdateChecks
```

These are basically the core methods of the Ava API, and this is why I said above that interacting with Ava "isn't actually that complicated". All of the above methods are focused around the same functionality: creating "*tasks*". We can inspect each service with the `describe` command:

```
 > grpcurl -plaintext aggregator.avaprotocol.org:2206 describe aggregator.Aggregator.CreateTask

aggregator.Aggregator.CreateTask is a method:
rpc CreateTask ( .aggregator.CreateTaskReq ) returns ( .aggregator.CreateTaskResp );
```

This says that the method `CreateTask` takes "`.aggregator.CreateTaskReq` as input, and return an object of type `CreateTaskResp` as output. Naturally, "Req" stands for "Request", and "Resp" for "Response". Later, we will see how to construct the Request object properly.

`CreateTaskReq` is apparently a valid keyword in this protocol, and we can indeed get information about it as well:


```
 > grpcurl -plaintext aggregator.avaprotocol.org:2206 describe aggregator.CreateTaskReq

aggregator.CreateTaskReq is a message:
message CreateTaskReq {
  .aggregator.TaskType task_type = 1;
  .aggregator.TaskAction action = 2;
  .aggregator.TaskTrigger trigger = 3;
  int64 start_at = 4;
  int64 expired_at = 5;
  string memo = 6;
}
```

Protobuf compresses messages to be sent over the internet into a very tiny form; often, parameters are communicated via integer codes, rather than string names. The `task_type = 1` in the message definition indicates that task_type is field number 1 in the CreateTaskReq message. This numbering is used internally by Protocol Buffers for serialization and doesn't affect how you construct your request. You do not need to use the number 1 in your request. Instead, you use the field name `task_type` and set its value to one of the allowed enum values defined in `.aggregator.TaskType.`

In light of the above schema for a CreateTask request, we can try to define a request in `.json`:

```

{
  "task_type": "ETHTransferTask",
  "action": {
    "eth_transfer": {
      "destination": "destination_address_here",
      "amount": "1000000000000000000"
    }
  },
  "trigger": {
    "trigger_type": "TimeTrigger",
    "schedule": {
      "fixed": [1633036800]
    }
  },
  "start_at": 1633036800,
  "expired_at": 1635724800,
  "memo": "Test task"
}



```

Recall that we can always figure out what we need to pass as arguments to the field with the `describe` command:

```
> grpcurl -plaintext aggregator.avaprotocol.org:2206 describe aggregator.TaskType

aggregator.TaskType is an enum:
enum TaskType {
  ETHTransferTask = 0;
  ContractExecutionTask = 1;
}

 > grpcurl -plaintext aggregator.avaprotocol.org:2206 describe aggregator.TaskAction

aggregator.TaskAction is a message:
message TaskAction {
  .aggregator.ETHTransfer eth_transfer = 1;
  .aggregator.ContractExecution contract_execution = 2;
}

 > grpcurl -plaintext aggregator.avaprotocol.org:2206 describe aggregator.TaskTrigger

aggregator.TaskTrigger is a message:
message TaskTrigger {
  .aggregator.TriggerType trigger_type = 1;
  .aggregator.TimeCondition schedule = 2;
  .aggregator.ContractQueryCondition contract_query = 3;
  .aggregator.ExpressionCondition expression = 4;
}

> grpcurl -plaintext aggregator.avaprotocol.org:2206 describe aggregator.TriggerType

aggregator.TriggerType is an enum:
enum TriggerType {
  TimeTrigger = 0;
  ContractQueryTrigger = 1;
  ExpressionTrigger = 2;
}

 > grpcurl -plaintext aggregator.avaprotocol.org:2206 describe aggregator.TimeCondition

aggregator.TimeCondition is a message:
message TimeCondition {
  repeated int64 fixed = 1;
  string cron = 2;
}

 > grpcurl -plaintext aggregator.avaprotocol.org:2206 describe aggregator.ContractQueryCondition

aggregator.ContractQueryCondition is a message:
message ContractQueryCondition {
  string contract_address = 1;
  string callmsg = 2;
}

 > grpcurl -plaintext aggregator.avaprotocol.org:2206 describe aggregator.ExpressionCondition

aggregator.ExpressionCondition is a message:
message ExpressionCondition {
  string expression = 1;
}

```

So we see what values we may choose for each of the above fields.

Now, we may begin actually making calls to this gRPC server, like so:


```> grpcurl -plaintext aggregator.avaprotocol.org:2206 aggregator.Aggregator/CreateTask

ERROR:
  Code: Unknown
  Message: missing auth header
```

Now we observe that we must authenticate in order to be able to send messages.

The Ava protocol documentation explains the authentication process [here](https://avaprotocol.org/docs/ethereum/develop/api-reference).


> # Authentication
> 
> To start interacting with our protocol for task management, the process consists of two steps:
> 
> Given a wallet address, exchange it for an auth token. This auth token allows you to perform task management for that wallet.
> For any request that requires authentication, include this auth token in request metadata.
> ## 1. Exchange an auth token
> 
> Call the GetKey method with the following data:
> 
> owner: your wallet address
> expired_at: the epoch time when your key will expire
> signature: sign a message in the format key request for `${wallet_address} expired at ${expired_at}`
> The response will include a key that can be set in the metadata of subsequent requests. The token will expire at the expired_at epoch.
> 
> You can refer to this example code for guidance on how to generate the signature.
> 
> ## 2. Making a gRPC Request
> 
> After obtaining the auth token, for any request that requires authentication, set the authkey: ${your-key-from-above} header in the request.
> 
> Since an account needs to send an auth key generated from the signature above, no one else will be able to view your data, ensuring that your task and parameter data remain private.
> 



Basically, we have to have our Ethereum (or Sepolia) address on hand, and generate a "signature", and then we use the `GetKey` method to get an authentication token.

You can do the above using the `web3´ library in Python.

If you already have a wallet, it's up to you to track down the address. For example, I have the Metamask add-on on my Firefox browser, so I can just copy and paste that info here. My wallet address isn't a secret, so I'll use mine in this demo:

`0x73F378fa22Ef3eCd54bdfe9fDA723a4B421e96AF`

In the course of this project, I learned something interesting: your wallet address is actually the same number across different networks. I also learned more about how addresses actually work.

You do not need to use the Ethereum network to create a wallet address. You do not tap into some special algorithm running on the blockchain. You can actually generate a wallet address yourself using a cryptographic function. Without going into details of how it works, this is what you would do in Python (if you haven't installed `web3`, do so using `pip`):

```python

from web3 import Web3
from eth_account import Account

```

Once you `pip install web3`, you already get the module `eth_account`, so you don't need to pip install that one separately.

The `Account` class provides extremely convenient methods for creating Ethereum wallets and doing basic functions with them. For example:


```python

# Get your private key. For example. mine was in my Metamask Firefox add-on. I went to My Account, clicked on Account Details, then pressed the button Show Private Key.
myprivatekey = "XXXXXXXXXXXXXXX"
myaccount = Account.from_key(myprivatekey)

```

When you do this, cryptographic methods will actually generate the other info about your Ethereum wallet. For example, `Account` now knows my public address:


```python

>>> myaccount = Account.from_key(myprivatekey)
>>> myaccount.address
'0x73F378fa22Ef3eCd54bdfe9fDA723a4B421e96AF'

```

This is my actual Ethereum wallet address. Basically, the address is generated from the private key deterministically (actually, the private key generates a public key, and the public key is used to generate an address), but you cannot recover the private key from the address.

Now I will save that info as an environmental variable in my shell:

```
 > MYETHADDRESS="0x73F378fa22Ef3eCd54bdfe9fDA723a4B421e96AF"
```

Here is how you generate the signature using the Python `web3` module. I saved this as a file called `gensig.py` and can verify it works:


```python


import os
import datetime
from web3 import Web3
from eth_account.messages import encode_defunct
from eth_account import Account

# Import the environmental variable
private_key = os.getenv('ETHPRIVATEKEY')

wallet_address = Account.from_key(private_key).address

# Get the current time and add one hour
current_time = datetime.datetime.now()
one_hour_later = current_time + datetime.timedelta(hours=1)

# Convert to timestamp
timestamp_one_hour_later = int(one_hour_later.timestamp())

message_text = f'key request for {wallet_address} expired at {timestamp_one_hour_later}'

message = encode_defunct(text=message_text)
w3 = Web3()
signed_message = w3.eth.account.sign_message(message, private_key=private_key)
signature = signed_message.signature.hex()

# Print the signature so we can capture it in the shell
print("WALLET ADDRESS:")
print(wallet_address)
print("SIGNATURE:")
print(signature)
print("TIMESTAMP:")
print(timestamp_one_hour_later)




```



For example, here's such a signature I just generated:

`b06280363608e81849f6d2f7eb4c58382598f2ab217224e3d65ee4126bc89f19502f1838284ce4983cd0d1b496d1d6112e45a3d9d73b60658cb56652d1c317881c`

Now we can get our Ava authentication token!

We just have to be careful at the CLI to pass the variables properly and not make any mistake with double quotes or variable expansion. Also, you must add '0x' to the beginning of the signature.


Here is a demo of me doing this and it working:

```zsh

(venv)  > grpcurl -plaintext -d @ aggregator.avaprotocol.org:2206 aggregator.Aggregator/GetKey <<EOM
{
  "owner": "$add",
  "expired_at": $tm,
  "signature": "0x$sig"
}
EOM

{
  "key": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBdmFQcm90b2NvbCIsInN1YiI6IjB4NzNGMzc4ZmEyMkVmM2VDZDU0YmRmZTlmREE3MjNhNEI0MjFlOTZBRiIsImV4cCI6MTcyODQ0NDYyOH0.XWffiZVKamwV5R3if2zpofYR_XJw0BEDZsK2wq8wnz8"
}

```

Now that I have authenticated, I can begin sending actual task creation messages.



For example:

```zsh

(venv)  > authtoken="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBdmFQcm90b2NvbCIsInN1YiI6IjB4NzNGMzc4ZmEyMkVmM2VDZDU0YmRmZTlmREE3MjNhNEI0MjFlOTZBRiIsImV4cCI6MTcyODQ0NDYyOH0.XWffiZVKamwV5R3if2zpofYR_XJw0BEDZsK2wq8wnz8"
(venv)  > grpcurl -plaintext -H "authkey: $authtoken" -d '{}' aggregator.avaprotocol.org:2206 aggregator.Aggregator/ListTasks

{}



```


I have no current tasks, which is true.


The next thing we need to do to start doing actual transactions, is we need to use a wallet that actually has tokens in it. So we will now use my Sepolia wallet instead.

I will now start from the top and write out a bunch of methods we have used so far in this explanation. Also, at this point, it will become easier to switch to Python.

So we are going to generate Python code from the `.proto` file, and then we can use the same methods in Python instead of with `grpcurl` from the cli.

Here goes.

1. We download the `avs.proto` file from here: https://github.com/AvaProtocol/EigenLayer-AVS/blob/main/protobuf/avs.proto

2. Launch a venv for Python: `python3 -m venv venv`. Activate it: `source venv/bin/activate`. Install needed packages: `pip3 install web3 protobuf grpcio grpcio-tools`.

3. The version of `protoc` bundled with `grpcio-tools` is an older version. Download a newer one, from the official website (latest releases: https://github.com/protocolbuffers/protobuf/releases), or even just homebrew: `brew install protoc`. Ensure it is version 28.2 with `protoc --version`.

4. Use those tools to generate Python code from the `avs.proto` file. Go into the same directory as it and do: `protoc --python_out=. avs.proto` and `python3 -m grpc_tools.protoc --python_out_grpc=. avs.proto`. For reasons I don't fully understand, this generates Python code in the form of classes that you can then import from other Python files. For some reason, I needed to modify one line of code, though. In `avs_pb2_grpc.py`, change the import statement from absolute to relative: from `import avs_pb2 as avs__pb2` to `from . import avs_pb2 as avs__pb2`. This is some quirk I didn't have time to figure out.

3. Open a Python file, say, `ava.py`. We can begin to define much of what we previously did from the CLI, as Python methods. Here we go:






----------




Basically, my intention was to create an SDK in Python for the above, but part of me feels like I simply did not have enough time to explore what kinds of functionalities are possible using the above protocol. Still, perhaps we can sketch out some ideas.

In order to do things like create tasks, one parameter you must pass a value to is `owner_address`.












-----------

There are only two task types supported in the protocol: `ETHTransferTask`, and `ContractExecutionTask`. The former is for transfering Ethereum on the Ethereum network, and the latter is for interacting in various ways with smart contracts (also on the Ethereum network).

As you can see, constructing a task basically just requires you declare:

- a `task_type` (money transaction or smart contract)
- an `action` (depending on the task type, this could be a transfer)



aggregator.avaprotocol.org:2206',
        'testnet_endpoint': 'aggregator-holesky.avaprotocol.org:2206',

you could install the Python package `grpcio` with `pip`, and do something like:






----------





- [Proto file](https://github.com/AvaProtocol/EigenLayer-AVS/blob/main/protobuf/avs.proto)

- [GitHub](https://github.com/AvaProtocol/EigenLayer-AVS)