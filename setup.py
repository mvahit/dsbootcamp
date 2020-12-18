import setuptools

setuptools.setup(name="dsbootcamp",
                 version="0.0.22",
                 license="MIT",
                 author="Vahit Keskin",
                 author_mail="m.vahitkeskin@gmail.com",
                 description="Data Science Tools Package",
                 url="https://github.com/mvahit/dsbootcamp",
                 keywords=["data science", "machine learning", "bootcamp"],
                 classifiers=[
                     "Development Status :: 4 - Beta",
                     "License :: OSI Approved :: MIT License",
                     "Programming Language :: Python",
                     "Programming Language :: Python :: 2.7",
                     "Programming Language :: Python :: 3.5",
                     "Topic :: Scientific/Engineering",
                 ],

                 packages=setuptools.find_packages()
                 # install_requires=["numpy", "scipy", "pandas"]

                 )


