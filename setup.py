from setuptools import setup, find_packages

setup(
    name='pipelogger',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        "google-cloud-bigquery>=3.11.0",
        "google-cloud-storage"
    ],
    entry_points={
    },
    author='Romboost',
    author_email='dcajiao@romboost.com',
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Romboost-Repo/PipeLogger',
    license='MIT',
)
