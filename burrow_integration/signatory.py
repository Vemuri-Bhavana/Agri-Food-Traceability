import os
import binascii
from iroha import IrohaCrypto
from iroha import Iroha, IrohaGrpc
import sys
from Crypto.Hash import keccak
import integration_helpers

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

# Here is the information about the environment and admin account information:
IROHA_HOST_ADDR = os.getenv("IROHA_HOST_ADDR", "127.0.0.1")
IROHA_PORT = os.getenv("IROHA_PORT", "50051")
ADMIN_ACCOUNT_ID = os.getenv("ADMIN_ACCOUNT_ID", "admin@test")
ADMIN_PRIVATE_KEY = os.getenv(
    "ADMIN_PRIVATE_KEY",
    "f101537e319568c765b2cc89698325604991dca57b9716b58016b253506cab70",
)

iroha = Iroha(ADMIN_ACCOUNT_ID)
net = IrohaGrpc("{}:{}".format(IROHA_HOST_ADDR, IROHA_PORT))

test_private_key = IrohaCrypto.private_key()
test_public_key = IrohaCrypto.derive_public_key(test_private_key).decode("utf-8")


@integration_helpers.trace
def create_contract():
    bytecode = "608060405234801561001057600080fd5b5073a6abc17819738299b3b2c1ce46d55c74f04e290c6000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550610b2a806100746000396000f3fe608060405234801561001057600080fd5b506004361061004c5760003560e01c8063686493791461005157806369c11e5a146100815780637fcd1036146100b1578063d4e804ab146100e1575b600080fd5b61006b600480360381019061006691906106c6565b6100ff565b6040516100789190610881565b60405180910390f35b61009b60048036038101906100969190610685565b6102c6565b6040516100a89190610881565b60405180910390f35b6100cb60048036038101906100c691906106c6565b610432565b6040516100d89190610881565b60405180910390f35b6100e96105f9565b6040516100f69190610866565b60405180910390f35b6060600083836040516024016101169291906108c5565b6040516020818303038152906040527f68649379000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff19166020820180517bffffffffffffffffffffffffffffffffffffffffffffffffffffffff8381831617835250505050905060008060008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16836040516101dd9190610838565b600060405180830381855af49150503d8060008114610218576040519150601f19603f3d011682016040523d82523d6000602084013e61021d565b606091505b509150915081610262576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610259906108fc565b60405180910390fd5b84604051610270919061084f565b604051809103902086604051610286919061084f565b60405180910390207f8d72069943c3cc6e44b6fd24c5aec4ae9c76f6923336203dc824a6c8c12064f360405160405180910390a380935050505092915050565b60606000826040516024016102db91906108a3565b6040516020818303038152906040527f69c11e5a000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff19166020820180517bffffffffffffffffffffffffffffffffffffffffffffffffffffffff8381831617835250505050905060008060008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16836040516103a29190610838565b600060405180830381855af49150503d80600081146103dd576040519150601f19603f3d011682016040523d82523d6000602084013e6103e2565b606091505b509150915081610427576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161041e906108fc565b60405180910390fd5b809350505050919050565b6060600083836040516024016104499291906108c5565b6040516020818303038152906040527f7fcd1036000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff19166020820180517bffffffffffffffffffffffffffffffffffffffffffffffffffffffff8381831617835250505050905060008060008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16836040516105109190610838565b600060405180830381855af49150503d806000811461054b576040519150601f19603f3d011682016040523d82523d6000602084013e610550565b606091505b509150915081610595576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161058c906108fc565b60405180910390fd5b846040516105a3919061084f565b6040518091039020866040516105b9919061084f565b60405180910390207fdd72c73ca40ba5767d7ef6a5c4a8546d4c1a41675a83ebfe3b5054022955f15a60405160405180910390a380935050505092915050565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600061063061062b84610941565b61091c565b90508281526020810184848401111561064857600080fd5b6106538482856109f2565b509392505050565b600082601f83011261066c57600080fd5b813561067c84826020860161061d565b91505092915050565b60006020828403121561069757600080fd5b600082013567ffffffffffffffff8111156106b157600080fd5b6106bd8482850161065b565b91505092915050565b600080604083850312156106d957600080fd5b600083013567ffffffffffffffff8111156106f357600080fd5b6106ff8582860161065b565b925050602083013567ffffffffffffffff81111561071c57600080fd5b6107288582860161065b565b9150509250929050565b61073b816109c0565b82525050565b600061074c82610972565b6107568185610988565b9350610766818560208601610a01565b61076f81610a94565b840191505092915050565b600061078582610972565b61078f8185610999565b935061079f818560208601610a01565b80840191505092915050565b60006107b68261097d565b6107c081856109a4565b93506107d0818560208601610a01565b6107d981610a94565b840191505092915050565b60006107ef8261097d565b6107f981856109b5565b9350610809818560208601610a01565b80840191505092915050565b60006108226027836109a4565b915061082d82610aa5565b604082019050919050565b6000610844828461077a565b915081905092915050565b600061085b82846107e4565b915081905092915050565b600060208201905061087b6000830184610732565b92915050565b6000602082019050818103600083015261089b8184610741565b905092915050565b600060208201905081810360008301526108bd81846107ab565b905092915050565b600060408201905081810360008301526108df81856107ab565b905081810360208301526108f381846107ab565b90509392505050565b6000602082019050818103600083015261091581610815565b9050919050565b6000610926610937565b90506109328282610a34565b919050565b6000604051905090565b600067ffffffffffffffff82111561095c5761095b610a65565b5b61096582610a94565b9050602081019050919050565b600081519050919050565b600081519050919050565b600082825260208201905092915050565b600081905092915050565b600082825260208201905092915050565b600081905092915050565b60006109cb826109d2565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b82818337600083830152505050565b60005b83811015610a1f578082015181840152602081019050610a04565b83811115610a2e576000848401525b50505050565b610a3d82610a94565b810181811067ffffffffffffffff82111715610a5c57610a5b610a65565b5b80604052505050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b6000601f19601f8301169050919050565b7f4572726f722063616c6c696e67207365727669636520636f6e7472616374206660008201527f756e6374696f6e0000000000000000000000000000000000000000000000000060208201525056fea2646970667358221220f8144a64fd15258021b4eda9df297a58ecd23dd5e29851da33747cf64d0c8a1264736f6c63430008040033"
    """Bytecode was generated using remix editor  https://remix.ethereum.org/ from file signatory.sol. """
    tx = iroha.transaction(
        [iroha.command("CallEngine", caller=ADMIN_ACCOUNT_ID, input=bytecode)]
    )
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    net.send_tx(tx)
    hex_hash = binascii.hexlify(IrohaCrypto.hash(tx))
    for status in net.tx_status_stream(tx):
        print(status)
    return hex_hash


@integration_helpers.trace
def add_signatory(address):
    params = integration_helpers.get_first_four_bytes_of_keccak(
        b"addSignatory(string,string)"
    )
    no_of_param = 2
    for x in range(no_of_param):
        params = params + integration_helpers.left_padded_address_of_param(
            x, no_of_param
        )
    params = params + integration_helpers.argument_encoding(
        ADMIN_ACCOUNT_ID
    )  # account id
    params = params + integration_helpers.argument_encoding(
        test_public_key
    )  # public key
    tx = iroha.transaction(
        [
            iroha.command(
                "CallEngine", caller=ADMIN_ACCOUNT_ID, callee=address, input=params
            )
        ]
    )
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    response = net.send_tx(tx)
    for status in net.tx_status_stream(tx):
        print(status)
    hex_hash = binascii.hexlify(IrohaCrypto.hash(tx))
    return hex_hash


@integration_helpers.trace
def remove_signatory(address):
    params = integration_helpers.get_first_four_bytes_of_keccak(
        b"removeSignatory(string,string)"
    )
    no_of_param = 2
    for x in range(no_of_param):
        params = params + integration_helpers.left_padded_address_of_param(
            x, no_of_param
        )
    params = params + integration_helpers.argument_encoding(
        ADMIN_ACCOUNT_ID
    )  # account id
    params = params + integration_helpers.argument_encoding(
        test_public_key
    )  # public key
    tx = iroha.transaction(
        [
            iroha.command(
                "CallEngine", caller=ADMIN_ACCOUNT_ID, callee=address, input=params
            )
        ]
    )
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    response = net.send_tx(tx)
    for status in net.tx_status_stream(tx):
        print(status)
    hex_hash = binascii.hexlify(IrohaCrypto.hash(tx))
    return hex_hash


@integration_helpers.trace
def get_signatories(address):
    params = integration_helpers.get_first_four_bytes_of_keccak(b"getSignatories(string)")
    no_of_param = 1
    for x in range(no_of_param):
        params = params + integration_helpers.left_padded_address_of_param(
            x, no_of_param
        )
    params = params + integration_helpers.argument_encoding(
        ADMIN_ACCOUNT_ID
    )  # account id
    tx = iroha.transaction(
        [
            iroha.command(
                "CallEngine", caller=ADMIN_ACCOUNT_ID, callee=address, input=params
            )
        ]
    )
    IrohaCrypto.sign_transaction(tx, ADMIN_PRIVATE_KEY)
    response = net.send_tx(tx)
    for status in net.tx_status_stream(tx):
        print(status)
    hex_hash = binascii.hexlify(IrohaCrypto.hash(tx))
    return hex_hash


hash = create_contract()
address = integration_helpers.get_engine_receipts_address(hash)
add_signatory(address)
hash = get_signatories(address)
integration_helpers.get_engine_receipts_result(hash)
remove_signatory(address)
hash = get_signatories(address)
integration_helpers.get_engine_receipts_result(hash)
print("done")
