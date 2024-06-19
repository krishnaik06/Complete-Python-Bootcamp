from logger import logging

def add(a,b):
    logging.debug("The addition operation is taking place")
    return a+b

logging.debug("The addition function is called")
add(10,15)