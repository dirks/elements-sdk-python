# StorageNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**backend** | [**Backend**](Backend.md) |  | 
**interfaces** | [**[Interface]**](Interface.md) |  | [readonly] 
**is_log_aggregator** | **bool** |  | [readonly] 
**name** | **str** |  | [optional] 
**address** | **str** | For communication between nodes only | [optional] 
**address_override** | **str, none_type** | Enforces mounting from a specific address/hostname instead of the available interfaces | [optional] 
**type** | **int** |  | [optional] 
**ipmi** | **int** |  | [optional] 
**status** | [**StorageNodeStatus**](StorageNodeStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#models) [[Back to API list]](../README.md#api-endpoints) [[Back to README]](../README.md)


