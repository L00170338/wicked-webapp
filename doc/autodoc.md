


Auto Documentation
============

Document automation (also known as document assembly or document management) 
is the design of systems and workflows that assist in the creation of electronic 
documents. These include logic-based systems that use segments of pre-existing 
text and/or data to assemble a new document. This process is increasingly used 
within certain industries to assemble legal documents, contracts and letters. 
Document automation systems can also be used to automate all conditional text, 
variable text, and data contained within a set of documents.

Automation systems allow companies to minimize data entry, reduce the time spent 
proofreading, and reduce the risks associated with human error. Additional benefits 
include: time and financial savings due to decreased paper handling, document loading, 
storage, distribution, postage/shipping, faxes, telephone, labor and waste. *

To generate the documentation of Django code the sphinx utility is used.
 
* Install sphinx by typing `pip install sphinx`
* Create the `doc` folder in you project
* Create and run `python` virtual environment
* Run `sphinx-quickstart` and answer the questions.
* 4x files will be created in doc folder
* Modify `config.py` as below
* Run `make html`
* The code will be documented
 
~~~python
import os
import sys
import django

sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'book'  # ,config,members'#,'members'
django.setup()

project = 'Wicked-Adventure'
copyright = '2022, Wednesday'
author = 'Wednesday'
~~~

The steps above demonstrate the code documentation creation of Wicked-Adventures project.
These are part of `publishdocs.yml` workflow and can be slightly differ.
To deploy the code to the server mkdocs and `GitHub` pages are used in this project.
These steps are also as part of `publishdocs.yml` workflow which means the documentation
is beeing generated automaticaly and publoshed to `GitHub` pages. Also, please see `mkdocs.yml`
file in the root folder of the Project. These describes the layout of documentation. The documentatio
is build and pushed to gh-branch in the same `repo` where the Project lives. Its important 
to make that branch as GitHub page.

~~~
site_name: Wicked Adventures
site_url: https://devopslecturer.github.io/awpgdip2022/
repo_name: GitHub
docs_dir: doc/
nav:
    - Home: index.md
    - AutoDocs: autodoc.md
    - Back-end-testing: back-end-testing.md
    - Code: code.md
    - DAST: dast.md
    - Deployment: deployment.md
    - Installation: installation.md
    - Front-end-testing: front-end-testing.md
    - Monitoring: monitoring.md
    - SAST: sast.md
theme: readthedocs
~~~


*Note1: The first paragpah is taken from Wikipedia*

*Note2: The steps described in this document may require verification.*
 
This page is created by L00169827


