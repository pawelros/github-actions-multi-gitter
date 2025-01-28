import yaml
from github_actions_multi_gitter.models.github_actions_workflow import GitHubActionsWorkflow


def parse_workflow(yaml_content: str) -> GitHubActionsWorkflow:
    data = yaml.safe_load(yaml_content)
    return GitHubActionsWorkflow.from_dict(data)
