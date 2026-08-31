from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener


SUCCESS_STATUSES = {200, 201, 202, 204}


class NoRedirectHandler(HTTPRedirectHandler):
    """Prevent an Authorization header from being forwarded through redirects."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[no-untyped-def]
        return None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Perform a small, safety-bounded set of JupyterHub REST API operations."
    )
    parser.add_argument(
        "--hub-url",
        default=os.environ.get("JUPYTERHUB_URL"),
        help="Hub base URL; defaults to JUPYTERHUB_URL.",
    )
    parser.add_argument(
        "--token-env",
        default="JUPYTERHUB_API_TOKEN",
        help="Name of the environment variable containing the API token.",
    )
    parser.add_argument("--timeout", type=float, default=30.0, help="Request timeout in seconds.")
    parser.add_argument(
        "--allow-http",
        action="store_true",
        help="Allow plain HTTP. Use only for an explicitly approved local development Hub.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the method and URL without reading a token or sending a request.",
    )
    parser.add_argument(
        "--confirm-mutation",
        action="store_true",
        help="Required for start-server and stop-server live requests.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("whoami", help="Return the model for the current token owner.")

    status_parser = subparsers.add_parser("user-status", help="Return one user's Hub model.")
    status_parser.add_argument("--user", required=True)

    for command in ("start-server", "stop-server"):
        command_parser = subparsers.add_parser(command)
        command_parser.add_argument("--user", required=True)
        command_parser.add_argument(
            "--server-name",
            default="",
            help="Named server. Omit for the default server.",
        )

    return parser.parse_args()


def validate_hub_url(raw_url: str | None, allow_http: bool) -> str:
    if not raw_url:
        raise SystemExit("Missing Hub URL: pass --hub-url or set JUPYTERHUB_URL.")

    url = raw_url.rstrip("/")
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise SystemExit("Hub URL must be an absolute http:// or https:// URL.")

    hostname = (parsed.hostname or "").lower()
    local_hosts = {"localhost", "127.0.0.1", "::1"}
    if parsed.scheme != "https" and not (allow_http and hostname in local_hosts):
        raise SystemExit(
            "Refusing to send a token over plain HTTP. Use HTTPS, or --allow-http for localhost."
        )
    return url


def server_path(user: str, server_name: str) -> str:
    encoded_user = quote(user, safe="")
    if server_name:
        return f"/hub/api/users/{encoded_user}/servers/{quote(server_name, safe='')}"
    return f"/hub/api/users/{encoded_user}/server"


def resolve_operation(args: argparse.Namespace) -> tuple[str, str, bytes | None, bool]:
    if args.command == "whoami":
        return "GET", "/hub/api/user", None, False
    if args.command == "user-status":
        return "GET", f"/hub/api/users/{quote(args.user, safe='')}", None, False
    if args.command == "start-server":
        return "POST", server_path(args.user, args.server_name), b"{}", True
    if args.command == "stop-server":
        return "DELETE", server_path(args.user, args.server_name), None, True
    raise SystemExit(f"Unsupported command: {args.command}")


def print_response(status: int, body: bytes) -> None:
    result: dict[str, Any] = {"status": status}
    if body:
        decoded = body.decode("utf-8", errors="replace")
        try:
            result["body"] = json.loads(decoded)
        except json.JSONDecodeError:
            result["body"] = decoded
    print(json.dumps(result, indent=2, ensure_ascii=False))


def main() -> None:
    args = parse_args()
    hub_url = validate_hub_url(args.hub_url, args.allow_http)
    method, path, data, mutation = resolve_operation(args)
    url = f"{hub_url}{path}"

    if args.dry_run:
        print(json.dumps({"method": method, "url": url, "mutation": mutation}, indent=2))
        return

    if mutation and not args.confirm_mutation:
        raise SystemExit("Mutation refused: repeat only after approval and add --confirm-mutation.")

    token = os.environ.get(args.token_env)
    if not token:
        raise SystemExit(f"Missing API token in environment variable {args.token_env}.")

    headers = {"Authorization": f"token {token}", "Accept": "application/json"}
    if data is not None:
        headers["Content-Type"] = "application/json"
    request = Request(url=url, method=method, headers=headers, data=data)
    opener = build_opener(NoRedirectHandler())

    try:
        with opener.open(request, timeout=args.timeout) as response:
            status = response.status
            body = response.read()
    except HTTPError as exc:
        body = exc.read()
        print_response(exc.code, body)
        raise SystemExit(1) from None
    except URLError as exc:
        print(f"Request failed: {exc.reason}", file=sys.stderr)
        raise SystemExit(1) from None

    print_response(status, body)
    if status not in SUCCESS_STATUSES:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
