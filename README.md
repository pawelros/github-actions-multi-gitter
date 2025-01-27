# github-actions-multi-gitter
Recipes and SDK for GitHub Actions housekeeping

Example usage: `multi-gitter run "uv run recipes/update_runs_on.py --worfklow-filename pr_checks.yaml --job build 'my-runner'" -O my-org -m "Commit message" -B branch-name

## Recipes

- [Update job.runs-on](#update-jobruns-on)

### `Update job.runs-on`

Updates `runs-on` value for matching workflow job(s)

example usage
```
uv run recipes/update_runs_on.py --worfklow-filename pr_checks.yaml --job build 'my-runner'
```

supported flags:
- `--workflow-filename` match workflow file name, i.e. `pr_checks.yaml`
- `--job` match job id i.e. `build`
