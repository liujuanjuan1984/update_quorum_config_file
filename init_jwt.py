"""
旧版的 jwt 不再支持，需要重新生成 jwt token。

pip install quorum_fullnode_py --upgrade

python3 init_jwt.py <local_fullnode_api_port>

"""

import sys

from quorum_fullnode_py import FullNode

args = sys.argv[1:]
if args:
    port = int(args[0])  # 62716
else:
    raise ValueError("python3 init_jwt.py <local_fullnode_api_port>")
bot = FullNode(port=port)

# create chain jwt for local_msi
payload = {"role": "chain", "name": "local_msi"}
resp = bot.api.create_token(**payload)
print(resp.get("token"))
