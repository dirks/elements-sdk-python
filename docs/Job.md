# Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**startable** | **bool** |  | [readonly] 
**webhook_url** | **str, none_type** |  | [readonly] 
**name** | **str** |  | 
**subtasks** | [**[SubtaskReference]**](SubtaskReference.md) |  | [optional] 
**schedules** | [**[ScheduleReference]**](ScheduleReference.md) |  | [optional] 
**allow_users** | [**[ElementsUserReference]**](ElementsUserReference.md) |  | [optional] 
**allow_groups** | [**[ElementsGroupReference]**](ElementsGroupReference.md) |  | [optional] 
**variable_definitions** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**media_roots** | **[int]** |  | [optional] 
**special_type** | **int, none_type** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**allow_others_to_start** | **bool** |  | [optional] 
**allow_client_to_start** | **bool** |  | [optional] 
**show_as_button** | **bool** |  | [optional] 
**input_type** | **str, none_type** |  | [optional] 
**hook** | **str, none_type** |  | [optional] 
**webhook_secret** | **str, none_type** |  | [optional] 
**security_context** | **int, none_type** |  | [optional] 
**part_of_workflow_for** | **int, none_type** |  | [optional] 

[[Back to Model list]](../README.md#models) [[Back to API list]](../README.md#api-endpoints) [[Back to README]](../README.md)


