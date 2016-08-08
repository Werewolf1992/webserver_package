from setuptools import setup

setup(
    name = "webserver",
    packages = ["webserver"],
    version = "1.0.0",
    description = "TNT task",
    author = "Michal",
    author_email = "mark@diveintomark.org",
    url = "https://github.com/Werewolf1992/webserver_package.git",
    download_url = "https://github.com/Werewolf1992/webserver_package.git",
    keywords = ["server", "web", "python"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        ],
    long_description = """\
Created using python 3.6
""",
    entry_points = {
                       'console_scripts': [
                           'webserver = websever.MichalWebServer:main'
                       ]
                   },
    )