import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = "0.0.4"

packages = [
    "espionage",
    "espionage.console",
    "espionage.modules.osint",
    "espionage.modules.parser",
]
package_data = {
    'espionage': [
        'README.md',
        'LICENSE',
    ]
}
entry_points = {
    'console_scripts': [
        'espionage=espionage.main:main',
    ],
}


def read_requirements():
    try:
        with open("requirements.txt", 'r', encoding='UTF-8') as file_handle:
            return file_handle.read().splitlines()
    except FileNotFoundError:
        return ["requests~=2.26.0", "beautifulsoup4~=4.10.0", "lxml", "rich~=10.16.1", "setuptools~=57.0.0"]


requirements = read_requirements()

setuptools.setup(
    name="espionage",
    version=VERSION,
    author="Muhammad Abdullah",
    author_email="iamabdullahmughal@gmail.com",
    description="A basic python based tool for domain ℹ️ information gathering. I am working 💻 on"
                " collecting information related to domain whois, history, dns records, web"
                " technologies and records from web. Feel free to drop a suggestion 💡",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iAbdullahMughal/espionage",
    project_urls={
        "Bug Tracker": "https://github.com/iAbdullahMughal/espionage/issues",
    },
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=packages,
    package_data=package_data,
    entry_points=entry_points,
    python_requires=">=3.6",
)
