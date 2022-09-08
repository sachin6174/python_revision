import json
from types import SimpleNamespace
# data=input()
data={"name": "John Smith", "hometown": {"name": "New York", "id": 123}}
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
print(x.name, x.hometown.name, x.hometown.id)

