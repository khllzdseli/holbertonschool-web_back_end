#!/usr/bin/env python3
"""
Simple helper function for pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing start index and end index
    for the given pagination parameters
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
