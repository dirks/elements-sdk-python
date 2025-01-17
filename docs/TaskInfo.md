# TaskInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**display_name** | **str** |  | [readonly] 
**kwargs** | **{str: (str, none_type)}** |  | 
**progress** | [**TaskProgress**](TaskProgress.md) |  | 
**log_path** | **str** |  | [readonly] 
**started** | **datetime** |  | [readonly] 
**subtask** | [**Subtask**](Subtask.md) |  | [optional] 
**worker** | [**StorageNodeMini**](StorageNodeMini.md) |  | [optional] 
**user** | [**ElementsUserMini**](ElementsUserMini.md) |  | [optional] 
**workstation** | [**Workstation**](Workstation.md) |  | [optional] 
**finished** | **datetime, none_type** |  | [optional] [readonly] 
**name** | **str, none_type** |  | [optional] 
**task_name** | **str, none_type** |  | [optional] 
**worker_name** | **str, none_type** |  | [optional] 
**queue** | **str, none_type** |  | [optional] 
**state** | **int** |  | [optional] 
**state_text** | **str, none_type** |  | [optional] 
**job_instance** | **str, none_type** |  | [optional] 
**exception** | **str, none_type** |  | [optional] 
**traceback** | **str, none_type** |  | [optional] 
**schedule** | **int, none_type** |  | [optional] 

[[Back to Model list]](../README.md#models) [[Back to API list]](../README.md#api-endpoints) [[Back to README]](../README.md)


