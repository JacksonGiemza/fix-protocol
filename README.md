# FIX Protocol Parser & Log Analyzer

A lightweight Python tool for parsing, translating, and analyzing FIX (Financial Information eXchange) protocol messages.

I'm using this project to explore the FIX protocol, understand common trading message flows, and provide tools for inspecting FIX session logs.

**Resources Used:**
- [FIX Repository](https://fixtrading.org/fix-repository/)
- [FIXimate](https://fiximate.fixtrading.org/)

## Overview

FIX messages are transmitted as sequences of `tag=value` fields separated by the SOH (`\x01`) delimiter.

A raw message such as:

```text
35=D|34=1080|49=TESTBUY1|56=TESTSELL1|11=12345|38=7000|40=1|54=1|55=MSFT
```

can be translated into a more readable representation:

```text
MsgType:      NewOrderSingle
MsgSeqNum:    1080
SenderCompID: TESTBUY1
TargetCompID: TESTSELL1
ClOrdID:      12345
OrderQty:     7000
OrdType:      Market
Side:         Buy
Symbol:       MSFT
```

The parser preserves both the original FIX tag/value and its human-readable interpretation:

```python
{
    "Side": {
        "tag": "54",
        "raw": "1",
        "value": "Buy"
    },
    "Symbol": {
        "tag": "55",
        "raw": "MSFT"
    }
}
```

## Goals

- Parse raw FIX messages
- Translate FIX tags into human-readable field names
- Translate enumerated values into their symbolic meanings
- Preserve original tag numbers and wire values
- Analyze FIX log files
- Identify common message types
- Reconstruct order lifecycles
- Analyze FIX session behavior
<!--
## Project Structure

```text
fix-parser/
├── data/
│   ├── fields.json
│   └── enums.json
├── src/
│   ├── parser.py
│   ├── translator.py
│   └── analyzer.py
├── samples/
│   └── sample.log
├── tests/
├── README.md
└── requirements.txt
```

## FIX Dictionary

FIX metadata is generated from the FIX 4.4 Repository.

### Fields

`fields.json` maps FIX tags to their definitions.

```json
{
    "54": {
        "Name": "Side",
        "Type": "char",
        "Description": "Side of order"
    }
}
```

### Enumerations

`enums.json` maps enumerated FIX values to their symbolic meanings.

```json
{
    "54": {
        "1": "Buy",
        "2": "Sell"
    },
    "40": {
        "1": "Market",
        "2": "Limit"
    }
}
```

## Usage

### Parse a Message

```python
# TODO: Add example
```

### Analyze a Log

```bash
# TODO: Add CLI example
```

## Supported FIX Version

Currently targeting:

```text
FIX 4.4
```

Support for additional FIX versions may be added later.

## Analysis Features

### Current

- [ ] Parse FIX fields
- [ ] Translate tag numbers
- [ ] Translate enumerated values
- [ ] Parse FIX log files

### Planned

- [ ] Group messages by message type
- [ ] Track message sequence numbers
- [ ] Detect sequence gaps
- [ ] Reconstruct order lifecycles
- [ ] Track New Order Single messages
- [ ] Track Execution Reports
- [ ] Track cancel requests
- [ ] Track cancel/replace requests
- [ ] Identify rejected orders
- [ ] Calculate order/fill statistics
- [ ] Validate FIX messages
- [ ] Validate BodyLength
- [ ] Validate CheckSum
- [ ] Support repeating groups

## Example Order Lifecycle

The analyzer will eventually reconstruct FIX messages into order lifecycles such as:

```text
NewOrderSingle
      │
      ▼
ExecutionReport
   [NEW]
      │
      ▼
ExecutionReport
[PARTIALLY_FILLED]
      │
      ▼
ExecutionReport
  [FILLED]
```

Example output:

```text
Order: 636730640278898634
Symbol: MSFT
Side: Buy
Quantity: 7000
Type: Market

Lifecycle:
  18:14:19.492  NewOrderSingle
  18:14:19.510  New
  18:14:19.521  PartiallyFilled
  18:14:19.536  Filled
```

## Future Development

The parser and translation components are intended to eventually serve as the foundation for a lightweight FIX engine.

Potential future components include:

- TCP initiator and acceptor
- FIX session state management
- Logon / Logout
- Heartbeats
- Test Requests
- Sequence number management
- Resend Requests
- Sequence Reset
- Persistent message storage
- Session recovery
- FIX message encoding
- Exchange simulator
- Fault injection and session testing

Conceptually:

```text
                    FIX Toolkit

                        │
             ┌──────────┴──────────┐
             │                     │
        Log Analyzer          FIX Engine
             │                     │
             │               Session Layer
             │                     │
             │                TCP Transport
             │                     │
             └──────────┬──────────┘
                        │
                  Parser / Encoder
                        │
                  FIX Dictionary
```

## Resources

- FIX Trading Community
- FIX 4.4 Specification
- FIX Repository
- FIXimate
- OnixS FIX 4.4 Dictionary
- QuickFIX

## Disclaimer

This project is for educational and research purposes. It is not intended for use in production trading systems.
