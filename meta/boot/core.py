#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pathlib
import yaml
path_DB = pathlib.Path(__file__).parent.absolute()
print(path_DB)
print(("Metaprogramming", argv[1]))

intro = """
Hello there!
The database has been booted, but it is not yet functional."""
print(intro)

inputprompt = """
To show some interactivity from the database,
please provide something to echo:  """

response = input(inputprompt)
print("Echo: %s" % str(response))

