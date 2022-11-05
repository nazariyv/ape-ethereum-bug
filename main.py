#!/usr/bin/env python
from pathlib import Path
from ape_ethereum.ecosystem import Ethereum

# * This is the actual part of the transaction taken from Etherscan.
# * We are interested in the first (tuple,uint120,uin120,bytes,bytes) part
# * The section with the values only relates to that part
# Function: fulfillAdvancedOrder((tuple,uint120,uint120,bytes,bytes), (uint256,uint8,uint256,uint256,bytes32[])[], bytes32, address)
# #	Name	Type	Data
# 0	advancedOrder.parameters	tuple	0x985DE337b99DD0a6Fb1c4169D37A9e40cc5a2316,0x004C00500000aD104D7DBd00e3ae0A5C00560C00,1,0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2,0,422700000000000000,422700000000000000,4,0xEf0182dc0574cd5874494a120750FD222FdB909a,93746800504734318969635817595067014524856428941470735176047083875732562066213,1,1,0x985DE337b99DD0a6Fb1c4169D37A9e40cc5a2316,1,0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2,0,10567500000000000,10567500000000000,0x0000a26b00c1F0DF003000390027140000fAa719,1,0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2,0,21135000000000000,21135000000000000,0x2B5964447005f661D13637CBDFFFCe600708138f,2,1662416648,1662459829,0x0000000000000000000000000000000000000000000000000000000000000000,85017582433403444,0x0000007b02230091a7ed01230072f7006a004d60a8d4e71d599b8104250f0000,3
# 0	advancedOrder.numerator	uint120	1
# 0	advancedOrder.denominator	uint120	1
# 0	advancedOrder.signature	bytes	0xc4bf5d286bcbd3a2cce00d7431cce8499841475fb9cc52eba8bba27922af249f7c1b49321e391f21ec8256d8ca2abf090af0fd6e371697feca277000785199511c
# 0	advancedOrder.extraData	bytes	0x

value = (
    (
        "0x985de337b99dd0a6fb1c4169d37a9e40cc5a2316",
        "0x004c00500000ad104d7dbd00e3ae0a5c00560c00",
        (
            (
                1,
                "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
                0,
                422700000000000000,
                422700000000000000,
            ),
        ),
        (
            (
                4,
                "0xef0182dc0574cd5874494a120750fd222fdb909a",
                93746800504734318969635817595067014524856428941470735176047083875732562066213,
                1,
                1,
                "0x985de337b99dd0a6fb1c4169d37a9e40cc5a2316",
            ),
            (
                1,
                "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
                0,
                10567500000000000,
                10567500000000000,
                "0x0000a26b00c1f0df003000390027140000faa719",
            ),
            (
                1,
                "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
                0,
                21135000000000000,
                21135000000000000,
                "0x2b5964447005f661d13637cbdfffce600708138f",
            ),
        ),
        2,
        1662416648,
        1662459829,
        b"\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00",
        85017582433403444,
        b"\\x00\\x00\\x00{\\x02#\\x00\\x91\\xa7\\xed\\x01#\\x00r\\xf7\\x00j\\x00M`\\xa8\\xd4\\xe7\\x1dY\\x9b\\x81\\x04%\\x0f\\x00\\x00",
        3,
    ),
    1,
    1,
    b"\\xc4\\xbf](k\\xcb\\xd3\\xa2\\xcc\\xe0\\rt1\\xcc\\xe8I\\x98AG_\\xb9\\xccR\\xeb\\xa8\\xbb\\xa2y\"\\xaf$\\x9f|\\x1bI2\\x1e9\\x1f!\\xec\\x82V\\xd8\\xca*\\xbf\\t\\n\\xf0\\xfdn7\\x16\\x97\\xfe\\xca\\'p\\x00xQ\\x99Q\\x1c",
    b"",
)

# * now these are the types that ape formats to. This is **NOT** reflective of the
# * actual transaction value from the top. It also does not coincide with the above
# * value. This must mean that the bug is in the part that produces the below parsed
# * types.
output_type = (
    [("address", "address", ("uint8", "address", "uint256", "uint256", "uint256"))],
    [("uint8", "address", "uint256", "uint256", "uint256", "address")],
    "uint8",
    "uint256",
    "uint256",
    "bytes32",
    "uint256",
    "bytes32",
    "uint256",
    "uint120",
    "uint120",
    "bytes",
    "bytes",
)

ethereum = Ethereum(
    data_folder=Path("/home/shredder/.ape/ethereum"),
    request_header={"User-Agent": "Ape/0.5.3 (Python/3.10.6 final)"},
)
ethereum.decode_primitive_value(value, output_type)
