from setuptools import setup, find_packages

setup(
    name="analyze-example",
    version="0.1.0",
    description="Meltano project file bundle of Matatika datasets for monitoring Snowflake",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/snowflake-monitoring/*.yml",
            "analyze/channels/*.yml"
        ]
    },
)
