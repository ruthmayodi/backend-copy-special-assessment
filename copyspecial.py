#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Ruth Mayodi, ruthmayodi with the help of Howard Post"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    # new_list = [os.path.abspath(os.path.join(dirname, f))
    #     for f in (os.listdir(dirname))
    #     if re.findall(r'__(\w+)__', f)]
    new_list = []
    for f in os.listdir(dirname):
        special_file = re.findall(r'__(\w+)__', f)
        if special_file:
            new_list.append(os.path.abspath(os.path.join(dirname, f)))

    return new_list


def copy_to(path_list, dest_dir):
    """Given a list files, copies to a new directory."""
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)

    for path in path_list:
        # filename = os.path.basename(path)
        # current_path = os.path.dirname(path)
        # abs_path = os.path.join(current_path, dest_dir, filename)
       
        shutil.copy(path, dest_dir)
    return


def zip_to(path_list, dest_zip):
    """Given a list of files adds them to a zip"""
    print("Command I'm going to do:")
    for path in path_list:
    
        print('zip -j', dest_zip, path)

        subprocess.call(['zip', '-j', dest_zip, path])
    
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help= 'directory to search for files')
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)
    path_list = get_special_paths(ns.from_dir)
    if ns.todir:
        copy_to(get_special_paths(ns.from_dir), ns.todir)
    if ns.tozip:
        zip_to(path_list, ns.tozip)
    
    if not ns.todir and not ns.tozip:
        for path in path_list:
            print(path)


if __name__ == "__main__":
    main(sys.argv[1:])
