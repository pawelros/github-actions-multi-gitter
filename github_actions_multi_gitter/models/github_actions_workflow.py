from typing import List, Dict, Optional

class GitHubActionsWorkflow:
    def __init__(self, name: str, on: Dict[str, List[str]], jobs: Dict[str, Dict]):
        self.name = name
        self.on = on
        self.jobs = jobs

    def __repr__(self):
        return f"GitHubActionsWorkflow(name={self.name}, on={self.on}, jobs={self.jobs})"

    @staticmethod
    def from_dict(data: Dict) -> 'GitHubActionsWorkflow':
        jobs = {name: Job.from_dict(job) for name, job in data['jobs'].items()}
        return GitHubActionsWorkflow(name=data['name'], on=data['on'], jobs=jobs)

class Job:
    def __init__(self, name: str, runs_on: str, steps: List[Dict[str, str]]):
        self.name = name
        self.runs_on = runs_on
        self.steps = steps

    def __repr__(self):
        return f"Job(name={self.name}, runs_on={self.runs_on}, steps={self.steps})"

    @staticmethod
    def from_dict(data: Dict) -> 'Job':
        steps = [Step.from_dict(step) for step in data['steps']]
        return Job(name=data['name'], runs_on=data['runs_on'], steps=steps)

class Step:
    def __init__(self, name: str, uses: Optional[str] = None, run: Optional[str] = None):
        self.name = name
        self.uses = uses
        self.run = run

    def __repr__(self):
        return f"Step(name={self.name}, uses={self.uses}, run={self.run})"

    @staticmethod
    def from_dict(data: Dict) -> 'Step':
        return Step(name=data['name'], uses=data.get('uses'), run=data.get('run'))