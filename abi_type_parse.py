#!/usr/bin/env python

method_inputs = {
    "name": "advancedOrder",
    "type": "tuple",
    "components": [
        {
            "name": "parameters",
            "type": "tuple",
            "components": [
                {"name": "offerer", "type": "address", "internalType": "address"},
                {"name": "zone", "type": "address", "internalType": "address"},
                {
                    "name": "offer",
                    "type": "tuple[]",
                    "components": [
                        {
                            "name": "itemType",
                            "type": "uint8",
                            "internalType": "enum ItemType",
                        },
                        {"name": "token", "type": "address", "internalType": "address"},
                        {
                            "name": "identifierOrCriteria",
                            "type": "uint256",
                            "internalType": "uint256",
                        },
                        {
                            "name": "startAmount",
                            "type": "uint256",
                            "internalType": "uint256",
                        },
                        {
                            "name": "endAmount",
                            "type": "uint256",
                            "internalType": "uint256",
                        },
                    ],
                    "internalType": "struct OfferItem[]",
                },
                {
                    "name": "consideration",
                    "type": "tuple[]",
                    "components": [
                        {
                            "name": "itemType",
                            "type": "uint8",
                            "internalType": "enum ItemType",
                        },
                        {"name": "token", "type": "address", "internalType": "address"},
                        {
                            "name": "identifierOrCriteria",
                            "type": "uint256",
                            "internalType": "uint256",
                        },
                        {
                            "name": "startAmount",
                            "type": "uint256",
                            "internalType": "uint256",
                        },
                        {
                            "name": "endAmount",
                            "type": "uint256",
                            "internalType": "uint256",
                        },
                        {
                            "name": "recipient",
                            "type": "address",
                            "internalType": "address payable",
                        },
                    ],
                    "internalType": "struct ConsiderationItem[]",
                },
                {
                    "name": "orderType",
                    "type": "uint8",
                    "internalType": "enum OrderType",
                },
                {"name": "startTime", "type": "uint256", "internalType": "uint256"},
                {"name": "endTime", "type": "uint256", "internalType": "uint256"},
                {"name": "zoneHash", "type": "bytes32", "internalType": "bytes32"},
                {"name": "salt", "type": "uint256", "internalType": "uint256"},
                {"name": "conduitKey", "type": "bytes32", "internalType": "bytes32"},
                {
                    "name": "totalOriginalConsiderationItems",
                    "type": "uint256",
                    "internalType": "uint256",
                },
            ],
            "internalType": "struct OrderParameters",
        },
        {"name": "numerator", "type": "uint120", "internalType": "uint120"},
        {"name": "denominator", "type": "uint120", "internalType": "uint120"},
        {"name": "signature", "type": "bytes", "internalType": "bytes"},
        {"name": "extraData", "type": "bytes", "internalType": "bytes"},
    ],
    "internalType": "struct AdvancedOrder",
}


def parse_method_input(mi):
    if mi["type"] == "tuple[]":
        return [tuple([parse_method_input(c) for c in mi["components"]])]
    elif mi["type"] == "tuple":
        return tuple([parse_method_input(c) for c in mi["components"]])
    elif mi["type"].endswith("]"):
        return [mi["type"][:-2]]
    else:
        return mi["type"]


print(parse_method_input(method_inputs))
