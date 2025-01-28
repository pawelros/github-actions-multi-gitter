# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "argparse",
#     "pyyaml",
# ]
# ///
import argparse
import yaml
from github_actions_multi_gitter.models.github_actions_workflow import GitHubActionsWorkflow
from github_actions_multi_gitter.github_actions_workflow_parser import parse_workflow

parser = argparse.ArgumentParser(
                    prog='GitHub Actions Multi-Gitter',
                    description='Update runs-on in GitHub Actions workflow',
                    epilog='Text at the bottom of help')

parser.add_argument('-r', '--recipe', help='Name of the recipe. One of [update-run-on]', required=True) 
parser.add_argument('-w', '--worfklow-filename', help='The name of the workflow file to match, i.e. build.yaml') 
parser.add_argument('-j', '--job', help='The job id to match, i.e build')
parser.add_argument('--new-runs-on', help='A new value for runs-on')

args = parser.parse_args()

