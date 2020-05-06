from setuptools import setup
import yaml

with open("manifest.yml", "r") as f:
    version = yaml.safe_load(f).get("version")

setup(
    name="git_practice_xxx",
    version=version,
    author="Silviu Surcica",
    description=(
        "An demonstration of how to create, document, and publish "
        "to the cheese shop a5 pypi.org."
    ),
    license="BSD",
)
