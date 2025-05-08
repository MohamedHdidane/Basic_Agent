from mythic_container.MythicCommandBase import *
from mythic_container.MythicRPC import *

class LsCommand(CommandBase):
    cmd = "ls"
    needs_admin = False
    help_cmd = "ls"
    description = "List directory contents on the target Ubuntu system"
    version = 1
    author = "@its_a_feature_"
    attack_mapping = ["T1083"]
    attributes = CommandAttributes(suggested_command=True)

    async def create_go_tasking(self, taskData: PTTaskMessageAllData) -> PTTaskCreateTaskingMessageResponse:
        response = PTTaskCreateTaskingMessageResponse(TaskID=taskData.Task.ID, Success=True)
        await SendMythicRPCArtifactCreate(MythicRPCArtifactCreateMessage(
            TaskID=taskData.Task.ID,
            ArtifactMessage="ls",
            BaseArtifactType="Process Create"
        ))
        response.DisplayParams = "ls"
        return response

    async def process_response(self, task: PTTaskMessageAllData, response: any) -> PTTaskProcessResponseMessageResponse:
        resp = PTTaskProcessResponseMessageResponse(TaskID=task.Task.ID, Success=True)
        await SendMythicRPCResponseCreate(MythicRPCResponseCreateMessage(
            TaskID=task.Task.ID,
            Response=response
        ))
        return resp