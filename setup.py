from distutils.core import setup


setup(
    name='django-campaign',
    version='0.1',
    description='Lightweight Political Campaign app for Django',
    author='Ben Spaulding',
    author_email='ben@benspaulding.us',
    url='https://github.com/benspaulding/django-campaign/',
    packages=[
        'campaign',
        'campaign.urls',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Content Management',
    ],
)
