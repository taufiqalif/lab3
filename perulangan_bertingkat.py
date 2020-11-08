#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 22:34:05 2020

@author: taufiq
"""
baris = 10
kolom = baris
for i in range(baris):
    for j in range(kolom):
        tambahkan = i+j
        print("{0:>5}".format(tambahkan), end="")
    print()
