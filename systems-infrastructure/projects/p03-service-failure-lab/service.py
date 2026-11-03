#!/usr/bin/env python3
"""P03: small loopback-only service for authorized fault-injection labs."""
import argparse
import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def load_config(path: Path) -> str:
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot load configuration: {type(exc).__name__}") from exc
    message = config.get("message") if isinstance(config, dict) else None
    if not isinstance(message, str) or not (0 < len(message) <= 100):
        raise ValueError("Configuration requires string 'message' with length 1..100")
    return message


def main(argv=None):
    parser = argparse.ArgumentParser(description="Local-only service lab, never production")
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args(argv)
    if not 0 <= args.port <= 65535:
        parser.error("port must be between 0 and 65535")
    try:
        message = load_config(args.config)
    except ValueError as exc:
        print(f"CONFIG_ERROR: {exc}", file=sys.stderr)
        return 2

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path != "/health":
                self.send_error(404)
                return
            body = json.dumps({"status": "ok", "message": message}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, format, *values):
            # Intentionally no client identifiers or request details in logs.
            return

    try:
        with ThreadingHTTPServer(("127.0.0.1", args.port), Handler) as server:
            print(f"READY http://127.0.0.1:{server.server_address[1]}/health", flush=True)
            server.serve_forever(poll_interval=0.1)
    except OSError as exc:
        print(f"BIND_ERROR: {type(exc).__name__}", file=sys.stderr)
        return 3
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
