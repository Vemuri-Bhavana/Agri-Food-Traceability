#
# Copyright Soramitsu Co., Ltd. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
#

from iroha import Iroha, IrohaCrypto
from iroha import primitive_pb2
import commons

admin = commons.new_user('admin@test')
alice = commons.new_user('alice@test')
bob = commons.new_user('bob@test')
iroha = Iroha(admin['id'])


@commons.hex
def genesis_tx():
    test_permissions = [primitive_pb2.can_transfer, primitive_pb2.can_receive]
    genesis_commands = commons.genesis_block(admin, alice, test_permissions)
    genesis_commands.extend([
        iroha.command('CreateAccount', account_name='bob', domain_id='test',
                      public_key=IrohaCrypto.derive_public_key(bob['key'])),
        iroha.command('CreateAsset', asset_name='coin', domain_id='test', precision=2),
        iroha.command('AddAssetQuantity', asset_id='coin#test', amount='90.00'),
        iroha.command('TransferAsset',
                      src_account_id=admin['id'],
                      dest_account_id=alice['id'],
                      asset_id='coin#test',
                      description='init top up',
                      amount='90.00')
    ])
    tx = iroha.transaction(genesis_commands)
    IrohaCrypto.sign_transaction(tx, admin['key'])
    return tx


@commons.hex
def transfer_asset_tx():
    tx = iroha.transaction([
        iroha.command('TransferAsset',
                      src_account_id=alice['id'],
                      dest_account_id=bob['id'],
                      asset_id='coin#test',
                      description='transfer to Bob',
                      amount='60.00')
    ], creator_account=alice['id'])
    IrohaCrypto.sign_transaction(tx, alice['key'])
    return tx
