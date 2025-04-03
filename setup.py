# setup.py
from setuptools import setup, find_packages

setup(
    name="real_time_abuse_detection",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "tweepy",
        "transformers",
        "flask",
        "streamlit",
        "pandas",
        "python-dotenv",
        "schedule"
    ],
    entry_points={
        'console_scripts': [
            'abuse-detector=run:main',  # Enables command line execution
        ]
    },
    author="Naveena Paleti",
    description="Real-time abuse detection system for X (Twitter) using Regex + BERT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.8',
)
