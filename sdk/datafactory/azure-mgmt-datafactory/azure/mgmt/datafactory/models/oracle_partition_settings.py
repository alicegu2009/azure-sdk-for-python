# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OraclePartitionSettings(Model):
    """The settings that will be leveraged for Oracle source partitioning.

    :param partition_names: Names of the physical partitions of Oracle table.
    :type partition_names: object
    :param partition_column_name: The name of the column in integer type that
     will be used for proceeding range partitioning. Type: string (or
     Expression with resultType string).
    :type partition_column_name: object
    :param partition_upper_bound: The maximum value of column specified in
     partitionColumnName that will be used for proceeding range partitioning.
     Type: string (or Expression with resultType string).
    :type partition_upper_bound: object
    :param partition_lower_bound: The minimum value of column specified in
     partitionColumnName that will be used for proceeding range partitioning.
     Type: string (or Expression with resultType string).
    :type partition_lower_bound: object
    """

    _attribute_map = {
        'partition_names': {'key': 'partitionNames', 'type': 'object'},
        'partition_column_name': {'key': 'partitionColumnName', 'type': 'object'},
        'partition_upper_bound': {'key': 'partitionUpperBound', 'type': 'object'},
        'partition_lower_bound': {'key': 'partitionLowerBound', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(OraclePartitionSettings, self).__init__(**kwargs)
        self.partition_names = kwargs.get('partition_names', None)
        self.partition_column_name = kwargs.get('partition_column_name', None)
        self.partition_upper_bound = kwargs.get('partition_upper_bound', None)
        self.partition_lower_bound = kwargs.get('partition_lower_bound', None)