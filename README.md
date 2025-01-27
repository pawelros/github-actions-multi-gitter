# github-actions-multi-gitter
Recipes and SDK for GitHub Actions housekeeping

Example usage: `multi-gitter run "uv run recipes/update_runs_on.py --worfklow-filename pr_checks.yaml --job build 'my-runner'" -O my-org -m "Commit message" -B branch-name

### Recipes
| file name | description | supported flags | example usage |
|---|---|---|---|
| `update_runs_on.py` | Updates `job.runs-on` | `--workflow-filename` `--job` | `uv run recipes/update_runs_on.py --worfklow-filename pr_checks.yaml --job build 'my-runner'` |
