from setuptools import setup, find_packages

setup(
    name='snowflakePOC',  # Replace with your package name
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'snowflake-connector-python',  # Snowflake connection
        'pandas',                      # Data manipulation
        'matplotlib',                  # Data visualization
        'scikit-learn',                # Machine learning
    ],
    package_data={' snowflakePOC': ['config.json']},  # Include config.json in the package
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'perform_analysis= snowflakePOC.performAnalysis:main',
            'upload_data=snowflakePOC.uploadData:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
