import json
import jsonschema

schema = json.load(open("rhub-core/trade.schema.json"))

trade = json.load(open("rhub-core/sample_trade.json"))

jsonschema.validate(instance = trade, schema = schema)

print("passed")