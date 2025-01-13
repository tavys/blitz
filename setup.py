from setuptools import setup, find_packages

setup(
    name="solana-trading-trends",
    version="1.0.0",
    description="Analyze trending narratives and market trends on Solana.",
    author="Your Name",
    author_email="your_email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "requests",
        "pandas",
        "numpy",
        "matplotlib",
        "pytest",
        "textblob",
    ],
    entry_points={
        "console_scripts": [
            "solana-trends=main:main",
        ],
    },
)