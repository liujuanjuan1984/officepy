import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="officy",
    version="0.0.3",
    author="liujuanjuan1984",
    author_email="qiaoanlu@163.com",
    description="common python code for office use. like dir,file,etc.",
    keywords=["office"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liujuanjuan1984/officy",
    project_urls={
        "Github Repo": "https://github.com/liujuanjuan1984/officy",
        "Bug Tracker": "https://github.com/liujuanjuan1984/officy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=["tests"]),
    python_requires=">=3.6",
    install_requires=[],
)
