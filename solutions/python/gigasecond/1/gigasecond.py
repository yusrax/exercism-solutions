from datetime import datetime, timedelta
"""Gigaesecond"""
def add(moment):
    """Add a gigasecond to a given date"""
    return moment + timedelta(seconds=1000000000)
