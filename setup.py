# -*- coding: utf-8 -*-

from distutils.core import setup 
import py2exe 
 
setup(name="CleanLogSalesforce",
 version="1.0",
 description="Limpia el log de Salesforce",
 author="SGH",
 author_email="sergiogonzalezhidalgo@gmail.com",
 url="",
 license="",
 scripts=["main.py"],
 console=["main.py"],
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)