from setuptools import setup, find_packages

# Read the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='yabai-manager',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'yabai-manager-cli=yabai_manager.yabai_manager_CLI:main',
        ],
    },
    install_requires=[
        "rumps",
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A CLI tool for managing Yabai.',
    long_description=long_description,
    long_description_content_type="text/markdown",
)