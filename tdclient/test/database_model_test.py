#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

try:
    from unittest import mock
except ImportError:
    import mock

from tdclient import model
from tdclient.test.test_helper import *

def setup_function(function):
    unset_environ()

def test_database():
    client = mock.MagicMock()
    database = model.Database(client, "sample_datasets", tables=["nasdaq", "www_access"], count=12345, created_at="created_at", updated_at="updated_at", org_name="org_name", permission="administrator")
    assert database.org_name == "org_name"
    assert database.permission == "administrator"
    assert database.count == 12345
    assert database.name == "sample_datasets"
    assert database.tables() == ["nasdaq", "www_access"]
    assert database.created_at == "created_at"
    assert database.updated_at == "updated_at"

def test_database_update_tables():
    client = mock.MagicMock()
    client.tables = mock.MagicMock(return_value=[
        model.Table(client, "sample_datasets", "foo", "type", "schema", "count"),
        model.Table(client, "sample_datasets", "bar", "type", "schema", "count"),
        model.Table(client, "sample_datasets", "baz", "type", "schema", "count"),
    ])
    database = model.Database(client, "sample_datasets", tables=None, count=12345, created_at="created_at", updated_at="updated_at", org_name="org_name", permission="administrator")
    tables = database.tables()
    assert [ table.name for table in tables ] == ["foo", "bar", "baz"]
    client.tables.assert_called_with("sample_datasets")