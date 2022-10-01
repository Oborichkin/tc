import setuptools

setuptools.setup(
    name="tc",
    packages=setuptools.find_packages(),
    version="0.1.0",
    description="JetBrains TeamCity CLI",
    author="Pavel Oborin",
    author_email="oborin.p@gmail.com",
    url="https://github.com/Oborichkin/tc",
    python_requires=">=3.6",
    install_requires=["requests", "click", "pydantic", "pendulum", "typer[all]"],
    entry_points={"console_scripts": ["teamcity=tc.cli:app"]},
)
