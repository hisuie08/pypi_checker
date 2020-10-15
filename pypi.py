import json
import os
import requests
PATH = os.path.dirname(os.path.abspath(__file__))

API_BASE_URL = "https://pypi.python.org/pypi/"

PACKAGE_LIST_PATH = f"{PATH}/registered_packages.json"


class Package:
    def __init__(self, rawJson: any):
        self.rawJson = rawJson
        self.info = self.rawJson["info"]
        self.author = str(self.info["author"])
        self.name = str(self.info["name"])
        self.description = str(self.info["description"])

    def dump(self):
        with open(f"{PATH}/{self.name}.json", "w", encoding="utf-8") as w:
            json.dump(self.rawJson, w, ensure_ascii=False)

    def releases(self):
        releases_list = list(self.rawJson["releases"].keys())
        return releases_list

    def latest(self):
        releases_list = self.releases()
        latest_ver = str(releases_list[-1])
        return latest_ver

    def register(self, version="latest"):
        if version == "latest":
            version = self.latest()
        else:
            if version in self.releases():
                version = version
            else:
                raise ValueError(f"Project version {version} was not found")
        if not os.path.exists(PACKAGE_LIST_PATH):
            with open(PACKAGE_LIST_PATH, "w", encoding="utf-8") as j:
                packages = dict({})
                json.dump(packages, j, ensure_ascii=False)
        with open(PACKAGE_LIST_PATH, encoding="utf-8") as j:
            packages = dict(json.loads(j.read()))
        with open(PACKAGE_LIST_PATH, "w", encoding="utf-8") as j:
            packages[self.name] = str(version)
            json.dump(packages, j, ensure_ascii=False)


def get_package(name: str):
    url = f"{API_BASE_URL}{name}/json"
    request = requests.get(url, headers={'content-type': 'application/json'})
    request.raise_for_status()
    package_json = request.json()
    return Package(package_json)


"""
Example:

>>> d_py = get_package("discord.py")
>>> print(d_py.name, d_py.latest(), f"made by {d_py.author}")

discord.py 1.5.0 made by Rapptz

"""
