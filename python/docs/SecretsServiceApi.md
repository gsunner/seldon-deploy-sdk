# seldon_deploy_sdk.SecretsServiceApi

All URIs are relative to *http://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secrets_service_create_gcs_bucket_secret**](SecretsServiceApi.md#secrets_service_create_gcs_bucket_secret) | **POST** /secrets/{namespace}/bucket/gcs/{remote} | Creates a GCS bucket secret according to specified parameters.
[**secrets_service_create_rclone_bucket_secret**](SecretsServiceApi.md#secrets_service_create_rclone_bucket_secret) | **POST** /secrets/{namespace}/bucket/rclone/{remote} | Creates a generic rclone bucket secret according to specified parameters.
[**secrets_service_create_registry_secret**](SecretsServiceApi.md#secrets_service_create_registry_secret) | **POST** /secrets/{namespace}/registry/{name} | Creates a registry secret according to specified parameters.
[**secrets_service_create_s3_bucket_secret**](SecretsServiceApi.md#secrets_service_create_s3_bucket_secret) | **POST** /secrets/{namespace}/bucket/s3/{remote} | Creates a S3 bucket secret according to specified parameters.
[**secrets_service_delete_secret**](SecretsServiceApi.md#secrets_service_delete_secret) | **DELETE** /secrets/{namespace}/{secretType}/{name} | Deletes the specified secret.
[**secrets_service_list_secrets**](SecretsServiceApi.md#secrets_service_list_secrets) | **GET** /secrets/{namespace}/{secretType} | Lists the names and metadata of secrets used by Seldon Deploy.


# **secrets_service_create_gcs_bucket_secret**
> V1CreateGCSBucketSecretResponse secrets_service_create_gcs_bucket_secret(namespace, remote, body)

Creates a GCS bucket secret according to specified parameters.

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_sdk
from seldon_deploy_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = seldon_deploy_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = seldon_deploy_sdk.SecretsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace to create secret in.
remote = 'remote_example' # str | The name of the remote to create, can be lowercase characters or numbers up to 10 characters long. The created secret will be named {remote}-bucket.
body = NULL # object | The GCS account credentials to populate the secret. See documentation for how to generate this.

try:
    # Creates a GCS bucket secret according to specified parameters.
    api_response = api_instance.secrets_service_create_gcs_bucket_secret(namespace, remote, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsServiceApi->secrets_service_create_gcs_bucket_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace to create secret in. | 
 **remote** | **str**| The name of the remote to create, can be lowercase characters or numbers up to 10 characters long. The created secret will be named {remote}-bucket. | 
 **body** | **object**| The GCS account credentials to populate the secret. See documentation for how to generate this. | 

### Return type

[**V1CreateGCSBucketSecretResponse**](V1CreateGCSBucketSecretResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_create_rclone_bucket_secret**
> V1CreateRcloneBucketSecretResponse secrets_service_create_rclone_bucket_secret(namespace, remote, body)

Creates a generic rclone bucket secret according to specified parameters.

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_sdk
from seldon_deploy_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = seldon_deploy_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = seldon_deploy_sdk.SecretsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace to create secret in.
remote = 'remote_example' # str | The name of the remote to create, can be lowercase characters or numbers up to 10 characters long. The created secret will be named {remote}-bucket.
body = seldon_deploy_sdk.V1RcloneConfig() # V1RcloneConfig | The rclone key value pairs.

try:
    # Creates a generic rclone bucket secret according to specified parameters.
    api_response = api_instance.secrets_service_create_rclone_bucket_secret(namespace, remote, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsServiceApi->secrets_service_create_rclone_bucket_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace to create secret in. | 
 **remote** | **str**| The name of the remote to create, can be lowercase characters or numbers up to 10 characters long. The created secret will be named {remote}-bucket. | 
 **body** | [**V1RcloneConfig**](V1RcloneConfig.md)| The rclone key value pairs. | 

### Return type

[**V1CreateRcloneBucketSecretResponse**](V1CreateRcloneBucketSecretResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_create_registry_secret**
> V1CreateRegistrySecretResponse secrets_service_create_registry_secret(namespace, name, body)

Creates a registry secret according to specified parameters.

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_sdk
from seldon_deploy_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = seldon_deploy_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = seldon_deploy_sdk.SecretsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace to create secret in.
name = 'name_example' # str | The name of the secret to create.
body = NULL # object | The raw json docker credentials config.

try:
    # Creates a registry secret according to specified parameters.
    api_response = api_instance.secrets_service_create_registry_secret(namespace, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsServiceApi->secrets_service_create_registry_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace to create secret in. | 
 **name** | **str**| The name of the secret to create. | 
 **body** | **object**| The raw json docker credentials config. | 

### Return type

[**V1CreateRegistrySecretResponse**](V1CreateRegistrySecretResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_create_s3_bucket_secret**
> V1CreateS3BucketSecretResponse secrets_service_create_s3_bucket_secret(namespace, remote, body)

Creates a S3 bucket secret according to specified parameters.

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_sdk
from seldon_deploy_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = seldon_deploy_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = seldon_deploy_sdk.SecretsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace to create secret in.
remote = 'remote_example' # str | The name of the remote to create, can be lowercase characters or numbers up to 10 characters long. The created secret will be named {remote}-bucket.
body = seldon_deploy_sdk.V1S3Credentials() # V1S3Credentials | The S3 account credentials to populate the secret. See documentation for how to generate these.

try:
    # Creates a S3 bucket secret according to specified parameters.
    api_response = api_instance.secrets_service_create_s3_bucket_secret(namespace, remote, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsServiceApi->secrets_service_create_s3_bucket_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace to create secret in. | 
 **remote** | **str**| The name of the remote to create, can be lowercase characters or numbers up to 10 characters long. The created secret will be named {remote}-bucket. | 
 **body** | [**V1S3Credentials**](V1S3Credentials.md)| The S3 account credentials to populate the secret. See documentation for how to generate these. | 

### Return type

[**V1CreateS3BucketSecretResponse**](V1CreateS3BucketSecretResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_delete_secret**
> V1DeleteSecretResponse secrets_service_delete_secret(namespace, secret_type, name)

Deletes the specified secret.

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_sdk
from seldon_deploy_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = seldon_deploy_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = seldon_deploy_sdk.SecretsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace to delete secret from.
secret_type = 'secret_type_example' # str | The secret type of the secret to be deleted, can be one of (`bucket`, `registry`).
name = 'name_example' # str | The name of the secret to delete.

try:
    # Deletes the specified secret.
    api_response = api_instance.secrets_service_delete_secret(namespace, secret_type, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsServiceApi->secrets_service_delete_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace to delete secret from. | 
 **secret_type** | **str**| The secret type of the secret to be deleted, can be one of (&#x60;bucket&#x60;, &#x60;registry&#x60;). | 
 **name** | **str**| The name of the secret to delete. | 

### Return type

[**V1DeleteSecretResponse**](V1DeleteSecretResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_list_secrets**
> V1ListSecretsResponse secrets_service_list_secrets(namespace, secret_type)

Lists the names and metadata of secrets used by Seldon Deploy.

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_sdk
from seldon_deploy_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = seldon_deploy_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = seldon_deploy_sdk.SecretsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace to list secrets in.
secret_type = 'secret_type_example' # str | The secret type, can be one of (`bucket`, `registry`) or `all` to list all secrets used by Seldon Deploy.

try:
    # Lists the names and metadata of secrets used by Seldon Deploy.
    api_response = api_instance.secrets_service_list_secrets(namespace, secret_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsServiceApi->secrets_service_list_secrets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace to list secrets in. | 
 **secret_type** | **str**| The secret type, can be one of (&#x60;bucket&#x60;, &#x60;registry&#x60;) or &#x60;all&#x60; to list all secrets used by Seldon Deploy. | 

### Return type

[**V1ListSecretsResponse**](V1ListSecretsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

