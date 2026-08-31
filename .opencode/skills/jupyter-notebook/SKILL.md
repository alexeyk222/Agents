---
name: jupyter-notebook
description: Create, edit, validate, and hand off reproducible Jupyter notebooks, including notebooks intended for JupyterHub. Use for `.ipynb` artifacts, experiments, tutorials, notebook execution checks, or explicitly requested JupyterHub API operations. Do not use for unrelated Python scripts.
license: Apache-2.0
metadata:
  source: https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook
  upstream-skill: jupyter-notebook
  adapted-for: OpenAgents Control OpenCode project
  runtime: Python 3.10+ for helpers; authorized Hub URL and API token for live operations
---

# Jupyter Notebook and JupyterHub

> Adaptation notice: this project-local derivative adds OpenCode paths, JupyterHub
> safety boundaries, and a minimal Hub API helper to the upstream OpenAI skill.

Create notebooks that are understandable, reproducible, and safe to hand off. Treat
local notebook authoring and live JupyterHub operations as separate modes.

## Choose the mode

- `artifact`: create, edit, or validate an `.ipynb` file locally. This is the default.
- `hub-read`: inspect the authenticated Hub identity or a user's server state.
- `hub-mutate`: start or stop a JupyterHub server. This changes an external system.

For `artifact`, choose `experiment` for exploratory or hypothesis-driven work and
`tutorial` for an instructional walkthrough. Preserve the existing notebook's intent
when editing.

For `hub-read` or `hub-mutate`, read
[`references/jupyterhub.md`](references/jupyterhub.md) before making a live request.
Do not infer that a request to edit a notebook authorizes access to a remote Hub.

## Artifact workflow

1. Identify the objective, audience, inputs, expected outputs, and validation target.
2. Scaffold new notebooks with the bundled helper rather than hand-writing notebook JSON:

   ```bash
   python3 .opencode/skills/jupyter-notebook/scripts/new_notebook.py \
     --kind experiment \
     --title "Compare prompt variants" \
     --out output/jupyter-notebook/compare-prompt-variants.ipynb
   ```

3. Keep setup, parameters, data loading, computation, results, and interpretation in
   distinct cells. Do not place credentials in cells, outputs, metadata, or committed files.
4. Read the relevant pattern:
   - experiments: [`references/experiment-patterns.md`](references/experiment-patterns.md)
   - tutorials: [`references/tutorial-patterns.md`](references/tutorial-patterns.md)
5. For raw JSON edits, first read
   [`references/notebook-structure.md`](references/notebook-structure.md).
6. Execute top-to-bottom when the required runtime and data are available. Otherwise
   report the exact missing kernel, package, credential, or data source.
7. Apply [`references/quality-checklist.md`](references/quality-checklist.md) before delivery.

## JupyterHub workflow

Use the bundled helper for the small supported Hub-control surface:

```bash
python3 .opencode/skills/jupyter-notebook/scripts/jupyterhub_api.py --help
```

The helper supports identity lookup, user/server status, and explicit start/stop
operations. It intentionally does not guess deployment-specific spawn options or automate
Jupyter Server contents and kernel APIs.

Required environment variables for a live request:

- `JUPYTERHUB_URL`: the trusted Hub base URL.
- `JUPYTERHUB_API_TOKEN`: a scoped API token.

Never print, persist, or embed the token. Prefer HTTPS and the minimum JupyterHub scopes.
Before a live read, name the target Hub and requested data. Immediately before a server
start or stop, obtain explicit user confirmation; the helper additionally requires
`--confirm-mutation`.

## Files and outputs

- Templates: `assets/experiment-template.ipynb` and `assets/tutorial-template.ipynb`.
- Scaffold helper: `scripts/new_notebook.py`.
- Hub helper: `scripts/jupyterhub_api.py`.
- Put disposable work in `.tmp/jupyter-runs/<task-slug>/`.
- Put final notebooks at the user's requested path, or under `output/jupyter-notebook/`
  when no path is specified.
- Do not overwrite an existing notebook unless the user asked for an edit or overwrite.

## Dependencies

The scaffold and Hub helpers use only the Python standard library. Install optional
Jupyter runtime packages only when execution is required and after obtaining approval:

```bash
uv pip install jupyterlab nbformat nbclient ipykernel
```
