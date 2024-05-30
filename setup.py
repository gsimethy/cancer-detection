from setuptools import setup,find_packages

PROJECT_NAME='Cancer detection'
REPO_NAME='CANCER-DETECTION'
USER_NAME='gary'
USER_EMAIL='gary.sim93@gmail.com'


setup(
    name=PROJECT_NAME,
    version='0.0.1',
    author=USER_NAME,
    author_email=USER_EMAIL,
    package_dir={"": "src"},
    packages=find_packages(where="src")
)

