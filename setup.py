from setuptools import setup, find_packages

setup(
    name="eventcollector",
    version="1.0",
    author="Neil Williams",
    author_email="neil@reddit.com",
    packages=find_packages(),
    install_requires=[
        "pyramid",
        "sysv_ipc",
        "boto",
        "baseplate",
    ],
    tests_require=[
        "mock",
    ],
    entry_points={
        "paste.app_factory": [
            "main = events.collector:make_app",
        ],
    },
)
