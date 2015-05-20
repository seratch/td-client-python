#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

from tdclient._model import Model

class BulkImport(Model):
    """Bulk-import session on Treasure Data Service
    """

    def __init__(self, client, name=None, database=None, table=None, status=None, upload_frozen=None, job_id=None, valid_records=None, error_records=None, valid_parts=None, error_parts=None, **kwargs):
        super(BulkImport, self).__init__(client)
        self._name = name
        self._database = database
        self._table = table
        self._status = status
        self._upload_frozen = upload_frozen
        self._job_id = job_id
        self._valid_records = valid_records
        self._error_records = error_records
        self._valid_parts = valid_parts
        self._error_parts = error_parts

    @property
    def name(self):
        """
        Returns: name of the bulk import session
        """
        return self._name

    @property
    def database(self):
        """
        Returns: database name in a string which the bulk import session is working on
        """
        return self._database

    @property
    def table(self):
        """
        Returns: table name in a string which the bulk import session is working on
        """
        return self._table

    @property
    def status(self):
        """
        Returns: status of the bulk import session in a string
        """
        return self._status

    @property
    def job_id(self):
        """
        TODO: add docstring
        """
        return self._job_id

    @property
    def valid_records(self):
        """
        TODO: add docstring
        """
        return self._valid_records

    @property
    def error_records(self):
        """
        TODO: add docstring
        """
        return self._error_records

    @property
    def valid_parts(self):
        """
        TODO: add docstring
        """
        return self._valid_parts

    @property
    def error_parts(self):
        """
        TODO: add docstring
        """
        return self._error_parts

    @property
    def upload_frozen(self):
        """
        TODO: add docstring
        """
        return self._upload_frozen

    def error_record_items(self):
        """
        TODO: add docstring
        """
        for record in self._client.bulk_import_error_records(self.name):
            yield record

    def upload_part(self, part_name, bytes_or_stream, size):
        """Upload a part to bulk import session

        Params:
            part_name (str): name of a part of the bulk import session
            bytes_or_stream (file-like): a file-like object contains the part
            size (int): the size of the part
        """
        return self._client.bulk_import_upload_part(self.name, part_name, bytes_or_stream, size)

    def upload_file(self, part_name, format, file):
        """Upload a part to Bulk Import session, from an existing file on filesystem.

        Params:
            part_name (str): name of a part of the bulk import session
            format (str): format of data type (e.g. "msgpack", "json")
            file (str or file-like): a name of a file, or a file-like object contains the data
        """
        return self._client.bulk_import_upload_file(self.name, part_name, format, file)
