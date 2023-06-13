from setuptools import setup, find_packages

setup(
    name="analyze-snowflake-monitoring",
    version="0.2.0",
    description="Meltano project file bundle of Matatika datasets for monitoring Snowflake",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/snowflake-monitoring/*.yml",
            "analyze/channels/*.yml",
            "pipelines/*.yml",
            "datastores/*.yml"
        ]
    },
)
