#Decompiled by Deray Feat  Ahmad Riswanto
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('termux-setup-storage')
        os.system('cd /sdcard')
        os.system('clear')
        os.system('termux-setup-storage')

