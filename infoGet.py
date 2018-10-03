#!/usr/bin/python
# -*- coding: utf-8 -*-
from gateAPI import GateIO

## 填写 apiKey APISECRET
apiKey = 'your api key'
secretKey = 'your api secret'
## address
btcAddress = 'your btc address'

## Provide constants

API_QUERY_URL = 'data.gateio.io'
API_TRADE_URL = 'api.gateio.io'

## Create a gate class instance

gate_query = GateIO(API_QUERY_URL, apiKey, secretKey)
gate_trade = GateIO(API_TRADE_URL, apiKey, secretKey)


# Trading Pairs
# print(gate_query.getKlineInfo('eth_b'))
print(gate_query.getKlineInfo('eth_usdt', 60, 1))