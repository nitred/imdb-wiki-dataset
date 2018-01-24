# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test modules."""


def test_init(hello_world):
    """Run a test."""
    import imdb_wiki_dataset

    # Test __init__
    assert hasattr(imdb_wiki_dataset, '__version__')

    # Test pytest fixtures
    assert(hello_world == "Hello World!")
