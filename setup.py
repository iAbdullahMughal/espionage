import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
version = "0.0.1"

packages = [
    "espionage",
    "espionage.modules",
    "espionage.modules.extra",
    "espionage.modules.whois",
]
package_data = {
    'domaintrails': [
        'README.html',
        'LICENSE.txt',
    ]
}
# https://github.com/iAbdullahMughal/espionage
entry_points = {
    'console_scripts': [
        'espionage=espionage.main:main',
    ],
}

setuptools.setup(
    name="espionage",
    version=version,
    author="Muhammad Abdullah",
    author_email="iamabdullahmughal@gmail.com",
    description="Espionage is open source intelligence gathering tool. This tool collect information "
                "related to domain. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iAbdullahMughal/espionage",
    project_urls={
        "Bug Tracker": "https://github.com/iAbdullahMughal/espionage/issues",
    },
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