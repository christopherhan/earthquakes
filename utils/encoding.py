import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(round(obj, 2))
        return json.JSONEncoder.default(self, obj)
