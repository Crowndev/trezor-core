from trezor.messages import wire_types
from micropython import const

# source: https://github.com/stellar/go/blob/master/xdr/Stellar-transaction.x
op_codes = {
    'StellarAccountMergeOp': const(8),
    'StellarAllowTrustOp': const(7),
    'StellarBumpSequenceOp': const(11),
    'StellarChangeTrustOp': const(6),
    'StellarCreateAccountOp': const(0),
    'StellarCreatePassiveOfferOp': const(4),
    'StellarManageDataOp': const(10),
    'StellarManageOfferOp': const(3),
    'StellarPathPaymentOp': const(2),
    'StellarPaymentOp': const(1),
    'StellarSetOptionsOp': const(5),
}

op_wire_types = [
    wire_types.StellarAccountMergeOp,
    wire_types.StellarAllowTrustOp,
    wire_types.StellarBumpSequenceOp,
    wire_types.StellarChangeTrustOp,
    wire_types.StellarCreateAccountOp,
    wire_types.StellarCreatePassiveOfferOp,
    wire_types.StellarManageDataOp,
    wire_types.StellarManageOfferOp,
    wire_types.StellarPathPaymentOp,
    wire_types.StellarPaymentOp,
    wire_types.StellarSetOptionsOp,
]

ASSET_TYPE_CREDIT_ALPHANUM4 = const(1)
ASSET_TYPE_CREDIT_ALPHANUM12 = const(2)


def get_op_code(msg) -> int:
    if msg.__qualname__ not in op_codes:
        raise ValueError('Stellar: op code unknown')
    return op_codes[msg.__qualname__]
