"""
Workspace manager.

Responsible for provisioning and tearing down workspace containers
(workspace_<project_id>) via the workspace-runner worker. This service
delegates actual Docker operations to the workspace-runner; it does not
execute workspace commands directly.
"""


class WorkspaceManager:
    # TODO: implement workspace provisioning via workspace-runner events
    pass
