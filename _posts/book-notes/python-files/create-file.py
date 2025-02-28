# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 12:17:08 2022

@author: vkumarpo
"""

# Python program to demonstrate
# creating a new file


# importing module
import os

# path of the current script
path = 'D:/Websites/test/python-files'

# Before creating
# dir_list = os.listdir(path)
# print("List of directories and files before creation:")
# print(dir_list)
# print()
# ----------------------------------
# Inputs
# ----------------------------------
booktitle='How to Not Die Alone, The Surprising Science That Will Help You Find Love'
booktitle_link_text='how-not-to-die-alone'
google_docs_link = "https://docs.google.com/document/d/e/2PACX-1vT0cWJYJnlaFkXTz69-ShEO_spG3UgQOJfACO_plO0HiySU8I5lwAoUVV9dartX61aGp_REIW4PBgW1/pub?embedded=true"


# ----------------------------------
# Main Code
# ----------------------------------
filename = '2022-07-02-'+ booktitle_link_text +'.md'

iframe_syntax = "<iframe src=\"" + google_docs_link +"\"  frameborder=\"0\" width=\"100%\" height=\"1500\" ></iframe>\n"
# Creates a new file
with open(filename, 'w') as fp:
	pass
	# To write data to new file uncomment
	fp.write("---\n")
	fp.write("layout: post\n")
	fp.write("title: \"" + booktitle + "\"\n")
	fp.write("author: \"Vijay Kumar Polimeru\"\n")
	fp.write("tags: Book-Notes\n")
	fp.write("permalink: /" + booktitle_link_text + "/\n")
	fp.write("comments: true\n")
	fp.write("---\n")
	fp.write("\n")
	fp.write("\n")
	fp.write("All other books notes are listed [here](/all-book-notes-google-play/)\n")
	fp.write("\n")
	fp.write(iframe_syntax)

# After creating
# dir_list = os.listdir(path)
# print("List of directories and files after creation:")
# print(dir_list)
