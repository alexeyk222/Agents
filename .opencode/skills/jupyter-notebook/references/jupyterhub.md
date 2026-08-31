# JupyterHub operations

Read this reference only for a live JupyterHub task. Notebook creation and local validation
do not require Hub access.

## Boundaries

JupyterHub's API controls Hub users and servers. A user's Jupyter Server exposes separate
contents, sessions, and kernels APIs. Do not treat these surfaces as interchangeable or
guess deployment-specific URLs.

Classify the requested operation:

- `network-read`: identify the token owner or inspect server state. Name the target host and
  requested data before the first live request.
- `external-write`: start or stop a server, create/revoke a token, share a server, upload a
  notebook, or execute code remotely. Obtain explicit confirmation immediately before the
  mutation.

The bundled `jupyterhub_api.py` supports only identity/status reads and start/stop mutations.
For file upload, remote execution, sharing, administration, or deployment configuration,
inspect the Hub version, enabled APIs, base URL, authenticator, spawner, and required scopes
before designing additional automation.

## Credentials and transport

- Read the Hub URL from `JUPYTERHUB_URL` and the token from `JUPYTERHUB_API_TOKEN`.
- Never echo a token, put it in command arguments, store it in a notebook, or commit it.
- Use a short-lived token with the minimum scopes required by the operation.
- Require HTTPS except for an explicitly approved localhost development Hub.
- Do not follow cross-origin redirects while sending an authorization header.
- A failed authorization check does not justify requesting a broader token automatically.

## Helper examples

Inspect the request without contacting the Hub:

```bash
python3 .opencode/skills/jupyter-notebook/scripts/jupyterhub_api.py \
  --hub-url https://hub.example.org --dry-run whoami
```

Read the current token identity:

```bash
python3 .opencode/skills/jupyter-notebook/scripts/jupyterhub_api.py whoami
```

Inspect one user's server model:

```bash
python3 .opencode/skills/jupyter-notebook/scripts/jupyterhub_api.py \
  user-status --user alice
```

After explicit approval, start the default server:

```bash
python3 .opencode/skills/jupyter-notebook/scripts/jupyterhub_api.py \
  --confirm-mutation start-server --user alice
```

## Validate the result

- Check the HTTP status and returned server state.
- Treat `202 Accepted` as pending, not completed; poll only when the user asked to wait.
- Do not claim a notebook ran merely because its server started.
- Record the Hub URL, operation, timestamp, and non-secret response summary when provenance
  matters.

Authoritative references:

- JupyterHub REST API: https://jupyterhub.readthedocs.io/en/stable/reference/rest-api.html
- JupyterHub server sharing and scoped-token guidance:
  https://jupyterhub.readthedocs.io/en/stable/tutorial/sharing.html
