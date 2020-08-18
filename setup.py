import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
        name='autocog',
        version='0.1.0',
        author='Rob Wagner',
        author_email='rob.wagner@outlook.com',
        license='License :: OSI Approved :: MIT License',
        description='A group of scripts and tools built for quickly prototyping or starting discord.py projects.',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/robertwayne/autocog',
        packages=setuptools.find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3.9',
            'Operating System :: OS Independent',
            'Typing :: Typed',
            'Topic :: Communications :: Chat',
            'Intended Audience :: Developers',
            'Development Status :: 4 - Beta',
        ],
        python_requires='>=3.8',
        install_requires=[
        ]
)
