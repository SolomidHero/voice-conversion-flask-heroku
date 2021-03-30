# openapi_client.VcApi

All URIs are relative to *https://vc-pytorch.herokuapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_file_get**](VcApi.md#upload_file_get) | **GET** / | Load main page
[**upload_file_post**](VcApi.md#upload_file_post) | **POST** / | Upload source and target


# **upload_file_get**
> str upload_file_get()

Load main page

Upload source and target audio files for voice conversion

### Example

```python
import time
import openapi_client
from openapi_client.api import vc_api
from pprint import pprint
# Defining the host is optional and defaults to https://vc-pytorch.herokuapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://vc-pytorch.herokuapp.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = vc_api.VcApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Load main page
        api_response = api_instance.upload_file_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VcApi->upload_file_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_post**
> ApiResponse upload_file_post()

Upload source and target

### Example

```python
import time
import openapi_client
from openapi_client.api import vc_api
from openapi_client.model.api_response import ApiResponse
from openapi_client.model.read_stream import ReadStream
from pprint import pprint
# Defining the host is optional and defaults to https://vc-pytorch.herokuapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://vc-pytorch.herokuapp.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = vc_api.VcApi(api_client)
    source =  # ReadStream | target file to upload (optional)
    target =  # ReadStream | target file to upload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload source and target
        api_response = api_instance.upload_file_post(source=source, target=target)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VcApi->upload_file_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | [**ReadStream**](ReadStream.md)| target file to upload | [optional]
 **target** | [**ReadStream**](ReadStream.md)| target file to upload | [optional]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

