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

from azure.core import AsyncPipelineClient
from msrest import Serializer, Deserializer

from ._configuration_async import TextAnalyticsClientConfiguration
from .operations_async import TextAnalyticsClientOperationsMixin
from .. import models


class TextAnalyticsClient(TextAnalyticsClientOperationsMixin):
    """The Text Analytics API is a suite of text analytics web services built with best-in-class Microsoft machine learning algorithms. The API can be used to analyze unstructured text for tasks such as sentiment analysis, key phrase extraction and language detection. No training data is needed to use this API; just bring your text data. This API uses advanced natural language processing techniques to deliver best in class predictions. Further documentation can be found in https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview


    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param endpoint: Supported Cognitive Services endpoints (protocol and
     hostname, for example: https://westus.api.cognitive.microsoft.com).
    :type endpoint: str
    """

    def __init__(
            self, credentials, endpoint, **kwargs):

        base_url = '{Endpoint}/text/analytics/v3.0'
        self._config = TextAnalyticsClientConfiguration(credentials, endpoint, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = 'v3.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
