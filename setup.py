# -*- coding: utf-8 -*-

from distutils.core import setup 
import py2exe 
 
setup(name="CleanLogSalesforce",
 version="1.5",
 description="Limpia el log de Salesforce",
 author="SGH",
 author_email="sergiogonzalezhidalgo@gmail.com",
 url="",
 license="",
 scripts=["CleanSalesforceLog.py"],
 console=["CleanSalesforceLog.py"],
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)