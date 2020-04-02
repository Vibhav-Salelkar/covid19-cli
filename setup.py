from setuptools import setup


setup(
    name='covid19',
    version='0.1.0',
    packages=['covid19'],
    entry_points={
        'console_scripts': [
            'covid19 = covid19.__main__:main'
        ]
    },
    python_requires='>=3',
    install_requires=[
        'requests>=2.23',
        'argparse>=1.4'
    ],

    # metadata
    author="Ankush Patil",
    author_email="aspraz2658@gmail.com",
    description="This is an Example Package",
    keywords="covid19 covid19-india coronavirus cli python",
    url="https://ankush.tech/projects/covid19-cli",
    project_urls={
        "Source Code": "http://github.com/asprazz/covid19-cli",
        "Issues": "http://github.com/asprazz/covid19-cli/issues",
        "Documentation": "https://ankush.tech/projects/covid19-cli/docs/",
    },
    classifiers=[
        "License :: MIT License"
    ]
)