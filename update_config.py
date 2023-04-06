"""
由于 jwt api 更改，config 文件模板也更改了。
这个脚本用于更新 config 文件。
"""

import logging
import os
import sys

import toml

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def update_config(config: dict):
    """config:旧版本的 config 数据更新为新版本的"""
    new = config.copy()
    new["jwt"] = {
        "Key": config["jwtkey"],
        "Chain": {"Normal": [], "Revoke": []},
        "Node": {},
    }
    for k, v in new["jwttokenmap"].items():
        if k.startswith("allow-"):
            group_id = k.strip("allow-")
            new["jwt"]["Node"][group_id] = {
                "Normal": [{"Remark": k, "Token": v}],
                "Revoke": [],
            }
        else:
            new["jwt"]["Chain"]["Normal"] = {"Remark": k, "Token": v}

    if "jwtkey" in new:
        del new["jwtkey"]
    if "jwttokenmap" in new:
        del new["jwttokenmap"]
    return new


def main(target_dir: str):
    """target_dir: 已更新了 quorum 版本的 fullnode 的 config 所在的目录。"""

    # 搜索 toml 文件
    config_files = []
    for root, paths, names in os.walk(target_dir):
        for name in names:
            if name.endswith("options.toml"):
                config_file = os.path.join(root, name)
                config_files.append(config_file)
                logger.info(f"find config file: {config_file}")

    # 更新 toml 文件
    for config_file in config_files:
        with open(config_file, "r") as f:
            config = toml.load(f)

        backup = config_file + ".bak"
        with open(backup, "w") as f:
            toml.dump(config, f)

        new = update_config(config)
        with open(config_file, "w") as f:
            toml.dump(new, f)


if __name__ == "__main__":
    logger.info("please update quorum binary and stop fullnode before update")
    args = sys.argv[1:]
    if args:
        target_dir = args[0]  # "./running_quorum"
        main(target_dir)
    else:
        raise ValueError(
            "please input target_dir `python3 update_config.py <target_dir>`"
        )
