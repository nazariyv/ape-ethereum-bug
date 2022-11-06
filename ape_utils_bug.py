#!/usr/bin/env python
from typing import Union, Tuple, List


# * This is parse_type from ape.utils v0.5.4
# * It has a bug
def parse_type(output_type: str) -> Union[str, Tuple, List]:
    if not output_type.startswith("("):
        return output_type

    # Strip off first opening parens
    output_type = output_type[1:]
    found_types: List[Union[str, Tuple, List]] = []

    while output_type:
        if output_type.startswith(")"):
            result = tuple(found_types)
            if "[" in output_type:
                return [result]

            return result

        elif output_type[0] == "(" and ")" in output_type:
            # A tuple within the tuple
            end_index = output_type.index(")") + 1
            found_type = parse_type(output_type[:end_index])
            output_type = output_type[end_index:]

            if output_type.startswith("[") and "]" in output_type:
                end_array_index = output_type.index("]") + 1
                found_type = [found_type]
                output_type = output_type[end_array_index:].lstrip(",")

        else:
            found_type = output_type.split(",")[0].rstrip(")")
            end_index = len(found_type) + 1
            output_type = output_type[end_index:]

        if isinstance(found_type, str) and "[" in found_type and ")" in found_type:
            parts = found_type.split(")")
            found_type = parts[0]
            output_type = f"){parts[1]}"

        if found_type:
            found_types.append(found_type)

    return tuple(found_types)


value_that_causes_the_bug = "((address,address,(uint8,address,uint256,uint256,uint256)[],(uint8,address,uint256,uint256,uint256,address)[],uint8,uint256,uint256,bytes32,uint256,bytes32,uint256),uint120,uint120,bytes,bytes)"
# * do not use this, purely to see this type in a friendly format
human_friendly_format = """(
    (
        address,
        address,
        (uint8,address,uint256,uint256,uint256)[],
        (uint8,address,uint256,uint256,uint256,address)[],
        uint8,
        uint256,
        uint256
        bytes32,
        uint256,
        bytes32,
        uint256
    ),
    uint120,
    uint120,
    bytes,
    bytes
)"""

# print(parse_type(value_that_causes_the_bug))

# this is what parse type produces for that string
what_parse_type_produces = (
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

if not (what_parse_type_produces == parse_type(value_that_causes_the_bug)):
    err = "parse_type does not produce the claimed output"
    raise Exception(err)

# * as you can see the tuple starting with 'address' should not be places inside of
# * the list. This implies that the bug is somehwere where parse_type determines to
# * make a list
what_parse_type_should_produce = (
    (
        "address",
        "address",
        [("uint8", "address", "uint256", "uint256", "uint256")],
        [("uint8", "address", "uint256", "uint256", "uint256", "address")],
        "uint8",
        "uint256",
        "uint256",
        "bytes32",
        "uint256",
        "bytes32",
        "uint256",
    ),
    "uint120",
    "uint120",
    "bytes",
    "bytes",
)

# (
#     ('address', 'address',
#      [('uint8', 'address', 'uint256', 'uint256', 'uint256')],
#      [('uint8', 'address', 'uint256', 'uint256', 'uint256', 'address')],
#      'uint8', 'uint256', 'uint256', 'bytes32', 'uint256', 'bytes32', 'uint256'
#      ),
#     'uint120', 'uint120', 'bytes', 'bytes'
# )

# if what_parse_type_should_produce != parse_type(human_friendly_format):
#     err = "parse_type does not produce the expected output"
#     raise Exception(err)

# * This problem reminds me of: https://leetcode.com/problems/valid-parentheses/
# * Where you need to return true if parentheses are properly constructed
# * Stack data structure is very useful here in tracking where you saw the opening
# * braces.

# to produce:
# (('address', 'address', [('foo', 'bar')], [('baz', 'bee')]),
#  'uint120',
#  'uint120',
#  'bytes32',
#  'bytes32')
# you need:
# tuple([tuple(['address', 'address', [tuple(['foo', 'bar'])], [tuple(['baz', 'bee'])]]), 'uint120', 'uint120', 'bytes32', 'bytes32'])

# to produce
human_friendly_format = """(
    (
        address,
        address,
        [(uint8,address,uint256,uint256,uint256)],
        [(uint8,address,uint256,uint256,uint256,address)],
        uint8,
        uint256,
        uint256
        bytes32,
        uint256,
        bytes32,
        uint256
    ),
    uint120,
    uint120,
    bytes,
    bytes
)"""
# you need:

# tuple(
#     [tuple(
#             ['address',
#              'address',
#              [tuple(
#                  ['uint8',
#                   'address',
#                   'uint256',
#                   'uint256',
#                   'uint256']
#                  )
#              ],
#              [tuple(
#                  ['uint8',
#                   'address',
#                   'uint256',
#                   'uint256',
#                   'uint256',
#                   'address']
#                  )
#             ],
#              'uint8',
#              'uint256',
#              'uint256',
#              'bytes32',
#              'uint256',
#              'bytes32',
#              'uint256'
#             ]
#           ),
#      'uint120',
#      'uint120',
#      'bytes',
#      'bytes'
#     ]
# )
