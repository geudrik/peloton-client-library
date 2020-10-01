import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='peloton',
    version='0.0.2',
    packages=['peloton'],
    description='A Python library for Peloton data.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Pat Litke (geudrik)",
    author_email="please_use_github_issues@nowhere.com",
    license='MIT License',
    url="https://github.com/geudrik/peloton-client-library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires='>=3.6',
    package_data={
    },
    exclude_package_data={},
    include_package_data=True,
)
