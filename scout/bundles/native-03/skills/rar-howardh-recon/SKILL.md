---
name: "rar-howardh-recon"
description: "URL intelligence scanner. Point it at any URL to get a full recon report: tech stack, security headers, API schema, performance, SSL, redirects. Every scan produces an HTML report that auto-opens. action=scan for full recon, action=api for API focus, action=security for security audit, action=compare for side-by-side, action=history for past scans."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/recon_agent", "rar_sha256": "3d26f7412310635f9b35e26a324ecfdb1af86ea26b0069e753d95a76d4c9d089", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Howard Hoy", "tags": ["recon", "url", "security", "api", "scanner", "headers", "ssl", "tech-stack"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@howardh/recon_agent`. The original RAPP
agent is preserved byte-for-byte in `recon_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Recon — "Every URL has a story. I read it first." — Made by HOLO

URL intelligence scanner. Point it at any URL and get a full recon report:tech stack, security
headers, API schema, performance, SSL certificate, redirects. Every scan
produces a self-contained HTML report that auto-opens in your browser.

## 5 Usage Examples

1. "Recon https://api.github.com"
   → Recon action=scan, url="https://api.github.com"
   → Full scan: headers, tech stack, security, performance, SSL

2. "What API does this endpoint expose?"
   → Recon action=api, url="https://api.stripe.com/v1/charges"
   → API focus: response schema, auth detection, pagination, content type

3. "Check security headers on my site"
   → Recon action=security, url="https://mysite.com"
   → Security audit: present/missing headers, SSL cert, CORS, CSP grades

4. "Compare these two APIs"
   → Recon action=compare, url="https://api.openai.com", url2="https://api.anthropic.com"
   → Side-by-side comparison report

5. "Show my past recon scans"
   → Recon action=history
   → Lists all past scan reports

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "scan = full recon; api = API schema/auth/pagination focus; security = security headers/SSL audit; compare = two URLs side-by-side; history = list past scans",
      "enum": [
        "scan",
        "api",
        "security",
        "compare",
        "history"
      ],
      "type": "string"
    },
    "url": {
      "description": "The URL to scan",
      "type": "string"
    },
    "url2": {
      "description": "Second URL for compare action",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `recon_agent.py` and embedded as the fenced Python below (sha256 3d26f7412310635f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `recon_agent.py` first:

```bash
python3 recon_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 recon_agent.py   # or on stdin
python3 recon_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@howardh/recon_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/recon_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@howardh/recon_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Recon — "Every URL has a story. I read it first." — Made by HOLO

URL intelligence scanner. Point it at any URL and get a full recon report:tech stack, security
headers, API schema, performance, SSL certificate, redirects. Every scan
produces a self-contained HTML report that auto-opens in your browser.

## 5 Usage Examples

1. "Recon https://api.github.com"
   → Recon action=scan, url="https://api.github.com"
   → Full scan: headers, tech stack, security, performance, SSL

2. "What API does this endpoint expose?"
   → Recon action=api, url="https://api.stripe.com/v1/charges"
   → API focus: response schema, auth detection, pagination, content type

3. "Check security headers on my site"
   → Recon action=security, url="https://mysite.com"
   → Security audit: present/missing headers, SSL cert, CORS, CSP grades

4. "Compare these two APIs"
   → Recon action=compare, url="https://api.openai.com", url2="https://api.anthropic.com"
   → Side-by-side comparison report

5. "Show my past recon scans"
   → Recon action=history
   → Lists all past scan reports
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@howardh/recon_agent",
    "version": "1.0.1",
    "display_name": "Recon",
    "description": "Scans any URL and produces an auto-opening HTML recon report covering tech stack, security headers, SSL, performance, and API schema.",
    "author": "Howard Hoy",
    "tags": ["recon", "url", "security", "api", "scanner", "headers", "ssl", "tech-stack"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import json
import os
import re
import socket
import ssl
import time
import urllib.error
import urllib.request
import webbrowser
from datetime import datetime
from html import escape
from html.parser import HTMLParser

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    from basic_agent import BasicAgent


class _MetaParser(HTMLParser):
    """Extract meta tags, title, and script sources from HTML."""
    def __init__(self):
        super().__init__()
        self.title = ""
        self._in_title = False
        self.meta = {}
        self.scripts = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            name = a.get("name", a.get("property", "")).lower()
            content = a.get("content", "")
            if name and content:
                self.meta[name] = content
        elif tag == "script":
            src = a.get("src", "")
            if src:
                self.scripts.append(src)
        elif tag == "link":
            rel = a.get("rel", "")
            href = a.get("href", "")
            if href:
                self.links.append({"rel": rel, "href": href})

    def handle_data(self, data):
        if self._in_title:
            self.title += data

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False


class ReconAgent(BasicAgent):
    """Recon — 'Every URL has a story. I read it first.' — Made by HOLO"""

    def __init__(self):
        self.name = "Recon"
        self.metadata = {
            "name": self.name,
            "description": (
                "URL intelligence scanner. Point it at any URL to get a full recon "
                "report: tech stack, security headers, API schema, performance, SSL, "
                "redirects. Every scan produces an HTML report that auto-opens. "
                "action=scan for full recon, action=api for API focus, "
                "action=security for security audit, action=compare for side-by-side, "
                "action=history for past scans."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["scan", "api", "security", "compare", "history"],
                        "description": (
                            "scan = full recon; api = API schema/auth/pagination focus; "
                            "security = security headers/SSL audit; compare = two URLs side-by-side; "
                            "history = list past scans"
                        ),
                    },
                    "url": {
                        "type": "string",
                        "description": "The URL to scan",
                    },
                    "url2": {
                        "type": "string",
                        "description": "Second URL for compare action",
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__()
        self._data_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), ".brainstem_data", "recon"
        )
        self._out_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "deliverables"
        )

    # ------------------------------------------------------------------
    # Core scanner
    # ------------------------------------------------------------------
    def _fetch(self, url, timeout=10):
        """Fetch a URL and return structured results."""
        result = {
            "url": url,
            "timestamp": datetime.now().isoformat(),
            "status": None,
            "headers": {},
            "body_preview": "",
            "body_size": 0,
            "content_type": "",
            "response_time_ms": 0,
            "redirects": [],
            "error": None,
        }

        if not url.startswith(("http://", "https://")):
            url = "https://" + url
            result["url"] = url

        # Follow redirects manually to capture chain
        redirects = []
        current_url = url
        for _ in range(10):
            req = urllib.request.Request(current_url, headers={
                "User-Agent": "RAPP-Recon/1.0 (brainstem scanner)",
                "Accept": "application/json, text/html, */*",
            })
            start = time.time()
            try:
                resp = urllib.request.urlopen(req, timeout=timeout)
                result["response_time_ms"] = round((time.time() - start) * 1000)
                result["status"] = resp.status
                result["headers"] = {k.lower(): v for k, v in resp.getheaders()}
                result["content_type"] = result["headers"].get("content-type", "")
                body = resp.read(50000)
                result["body_size"] = len(body)
                try:
                    result["body_preview"] = body.decode("utf-8", errors="replace")[:5000]
                except Exception:
                    result["body_preview"] = str(body[:2000])
                break
            except urllib.error.HTTPError as e:
                result["response_time_ms"] = round((time.time() - start) * 1000)
                result["status"] = e.code
                result["headers"] = {k.lower(): v for k, v in e.headers.items()}
                result["content_type"] = result["headers"].get("content-type", "")
                try:
                    body = e.read(5000)
                    result["body_preview"] = body.decode("utf-8", errors="replace")
                except Exception:
                    pass
                break
            except urllib.error.URLError as e:
                result["error"] = str(e.reason)
                break
            except Exception as e:
                result["error"] = str(e)
                break

        result["redirects"] = redirects
        return result

    def _get_ssl_info(self, url):
        """Get SSL certificate information."""
        try:
            from urllib.parse import urlparse
            parsed = urlparse(url)
            hostname = parsed.hostname
            port = parsed.port or 443
            ctx = ssl.create_default_context()
            with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
                s.settimeout(5)
                s.connect((hostname, port))
                cert = s.getpeercert()
            return {
                "subject": dict(x[0] for x in cert.get("subject", ())),
                "issuer": dict(x[0] for x in cert.get("issuer", ())),
                "not_before": cert.get("notBefore", ""),
                "not_after": cert.get("notAfter", ""),
                "san": [x[1] for x in cert.get("subjectAltName", ())],
                "version": cert.get("version", ""),
            }
        except Exception as e:
            return {"error": str(e)}

    def _detect_tech(self, headers, body):
        """Detect technology stack from headers and body."""
        tech = []
        h = {k.lower(): v.lower() for k, v in headers.items()}
        server = h.get("server", "")
        powered = h.get("x-powered-by", "")

        if server:
            tech.append(("Server", server))
        if powered:
            tech.append(("Powered By", powered))
        if "x-aspnet-version" in h:
            tech.append(("ASP.NET", h["x-aspnet-version"]))
        if "x-drupal" in str(h):
            tech.append(("CMS", "Drupal"))
        if "wp-" in body.lower() or "wordpress" in body.lower():
            tech.append(("CMS", "WordPress"))
        if "next" in server or "_next" in body:
            tech.append(("Framework", "Next.js"))
        if "cloudflare" in server:
            tech.append(("CDN", "Cloudflare"))
        if "fastly" in h.get("via", ""):
            tech.append(("CDN", "Fastly"))
        if "akamai" in str(h):
            tech.append(("CDN", "Akamai"))
        if "x-amz" in str(h):
            tech.append(("Cloud", "AWS"))
        if "x-ms" in str(h) or "azure" in str(h):
            tech.append(("Cloud", "Azure"))
        if "x-goog" in str(h) or "gfe" in server:
            tech.append(("Cloud", "Google Cloud"))

        # Script-based detection
        script_tech = {
            "react": "React", "vue": "Vue.js", "angular": "Angular",
            "jquery": "jQuery", "bootstrap": "Bootstrap", "tailwind": "Tailwind",
            "gtag": "Google Analytics", "fbevents": "Facebook Pixel",
            "stripe": "Stripe", "intercom": "Intercom", "segment": "Segment",
        }
        body_lower = body.lower()
        for key, name in script_tech.items():
            if key in body_lower:
                tech.append(("Script", name))

        return tech

    def _analyze_security(self, headers, url):
        """Analyze security headers."""
        h = {k.lower(): v for k, v in headers.items()}
        checks = [
            ("strict-transport-security", "HSTS", "Forces HTTPS connections"),
            ("content-security-policy", "CSP", "Controls resource loading"),
            ("x-content-type-options", "X-Content-Type-Options", "Prevents MIME sniffing"),
            ("x-frame-options", "X-Frame-Options", "Prevents clickjacking"),
            ("x-xss-protection", "X-XSS-Protection", "XSS filter (legacy)"),
            ("referrer-policy", "Referrer-Policy", "Controls referrer info"),
            ("permissions-policy", "Permissions-Policy", "Controls browser features"),
            ("access-control-allow-origin", "CORS", "Cross-origin access control"),
        ]
        results = []
        for header, name, desc in checks:
            present = header in h
            value = h.get(header, "")
            results.append({
                "header": name,
                "present": present,
                "value": value[:100] if value else "",
                "description": desc,
            })
        # Grade
        present_count = sum(1 for r in results if r["present"])
        if present_count >= 7:
            grade = "A"
        elif present_count >= 5:
            grade = "B"
        elif present_count >= 3:
            grade = "C"
        elif present_count >= 1:
            grade = "D"
        else:
            grade = "F"
        return {"checks": results, "grade": grade, "present": present_count, "total": len(results)}

    def _analyze_api(self, result):
        """Analyze API-specific characteristics."""
        info = {
            "is_json": "json" in result.get("content_type", "").lower(),
            "auth_required": result.get("status") in (401, 403),
            "schema": None,
            "pagination": [],
            "rate_limit": {},
        }

        # Parse JSON schema
        if info["is_json"] and result.get("body_preview"):
            try:
                data = json.loads(result["body_preview"])
                info["schema"] = self._map_schema(data, depth=0)
            except (json.JSONDecodeError, ValueError):
                pass

        # Auth hints
        h = result.get("headers", {})
        auth_headers = [k for k in h if "auth" in k.lower() or "api-key" in k.lower() or "token" in k.lower()]
        if auth_headers:
            info["auth_hints"] = auth_headers

        # Rate limiting
        for k, v in h.items():
            kl = k.lower()
            if "ratelimit" in kl or "rate-limit" in kl or "retry" in kl:
                info["rate_limit"][k] = v

        # Pagination
        if "link" in h:
            info["pagination"].append(f"Link header: {h['link'][:100]}")
        body = result.get("body_preview", "")
        for pattern in ["next_page", "nextPage", "next_cursor", "offset", "page_token", "has_more"]:
            if pattern in body:
                info["pagination"].append(f"Found '{pattern}' in response body")

        return info

    def _map_schema(self, data, depth=0, max_depth=4):
        """Map JSON response to a type schema."""
        if depth > max_depth:
            return "..."
        if isinstance(data, dict):
            return {k: self._map_schema(v, depth + 1) for k, v in list(data.items())[:20]}
        elif isinstance(data, list):
            if data:
                return [self._map_schema(data[0], depth + 1)]
            return ["(empty)"]
        elif isinstance(data, bool):
            return "boolean"
        elif isinstance(data, int):
            return "integer"
        elif isinstance(data, float):
            return "number"
        elif isinstance(data, str):
            if len(data) > 50:
                return f"string({len(data)})"
            return f'"{data[:30]}"'
        elif data is None:
            return "null"
        return str(type(data).__name__)

    # ------------------------------------------------------------------
    # HTML Report Generator
    # ------------------------------------------------------------------
    def _render_report(self, title, sections):
        """Render an HTML report from sections."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        body_html = ""
        for sec in sections:
            body_html += f'<div class="section"><h2>{sec["title"]}</h2>{sec["content"]}</div>\n'

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Recon — {escape(title)}</title>
<style>
  body{{margin:0;padding:24px;font-family:'Segoe UI',system-ui,sans-serif;background:#f5f5f5;color:#24292f;max-width:900px;margin:0 auto}}
  h1{{font-size:22px;margin-bottom:4px}}
  .subtitle{{font-size:13px;color:#57606a;margin-bottom:20px}}
  .section{{background:#fff;border:1px solid #ddd;border-radius:12px;padding:16px 20px;margin-bottom:14px}}
  .section h2{{font-size:15px;color:#0969da;margin:0 0 10px}}
  table{{width:100%;border-collapse:collapse;font-size:13px}}
  th{{text-align:left;padding:6px 8px;border-bottom:2px solid #0969da;font-size:11px;text-transform:uppercase;color:#0969da}}
  td{{padding:5px 8px;border-bottom:1px solid #eee;vertical-align:top}}
  .pass{{color:#1a7f37;font-weight:700}}.fail{{color:#cf222e;font-weight:700}}
  .grade{{display:inline-block;font-size:28px;font-weight:700;width:48px;height:48px;line-height:48px;text-align:center;border-radius:12px;color:#fff}}
  .grade-A{{background:#1a7f37}}.grade-B{{background:#2da44e}}.grade-C{{background:#bf8700}}.grade-D{{background:#cf222e}}.grade-F{{background:#82071e}}
  .mono{{font-family:'Cascadia Code','Fira Code',monospace;font-size:12px;background:#f0f1f3;padding:2px 6px;border-radius:4px}}
  pre{{background:#f0f1f3;border:1px solid #ddd;border-radius:8px;padding:12px;font-size:12px;overflow-x:auto;line-height:1.5}}
  .tag{{display:inline-block;font-size:11px;padding:2px 8px;border-radius:10px;font-weight:600;margin:1px}}
  .tag-tech{{background:#dbeafe;color:#1e40af}}.tag-warn{{background:#fff3cd;color:#856404}}.tag-ok{{background:#d1fae5;color:#065f46}}
  .kv{{display:flex;gap:8px;padding:3px 0;border-bottom:1px solid #f0f0f0}}.kv .k{{font-weight:600;min-width:140px;color:#57606a;font-size:12px}}.kv .v{{font-size:12px;word-break:break-all}}
  .compare{{display:flex;gap:16px}}.compare .col{{flex:1}}
  .footer{{text-align:center;font-size:11px;color:#57606a;margin-top:20px;padding:12px;border-top:1px solid #ddd}}
</style>
</head>
<body>
<h1>🔍 Recon — {escape(title)}</h1>
<div class="subtitle">Scanned {timestamp} · Made by HOLO</div>
{body_html}
<div class="footer">Recon — URL Intelligence Scanner · Made by HOLO · RAPP Brainstem</div>
</body>
</html>"""

    def _kv(self, key, value):
        return f'<div class="kv"><div class="k">{escape(str(key))}</div><div class="v">{escape(str(value))}</div></div>'

    def _save_and_open(self, html, slug):
        os.makedirs(self._out_dir, exist_ok=True)
        slug = re.sub(r'[^a-z0-9]+', '-', slug.lower()).strip('-')[:40]
        path = os.path.join(self._out_dir, f"recon-{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        webbrowser.open(f"file://{os.path.abspath(path)}")

        # Save to history
        os.makedirs(self._data_dir, exist_ok=True)
        history_file = os.path.join(self._data_dir, "history.json")
        history = []
        if os.path.isfile(history_file):
            try:
                with open(history_file, "r") as f:
                    history = json.load(f)
            except (json.JSONDecodeError, OSError):
                pass
        history.append({"slug": slug, "path": path, "timestamp": datetime.now().isoformat()})
        with open(history_file, "w") as f:
            json.dump(history[-50:], f, indent=2)

        return path

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------
    def _action_scan(self, url="", **kwargs):
        if not url:
            return "Please provide a URL to scan. Example: `url=https://api.github.com`"

        result = self._fetch(url)
        if result["error"]:
            return f"❌ Failed to reach {url}: {result['error']}"

        ssl_info = self._get_ssl_info(url) if url.startswith("https") else {}
        tech = self._detect_tech(result["headers"], result.get("body_preview", ""))
        security = self._analyze_security(result["headers"], url)
        api_info = self._analyze_api(result)

        sections = []

        # Overview
        overview = f"""
        {self._kv("URL", result["url"])}
        {self._kv("Status", f'{result["status"]} {"✅" if result["status"] == 200 else "⚠️"}')}
        {self._kv("Content-Type", result["content_type"])}
        {self._kv("Response Time", f'{result["response_time_ms"]}ms')}
        {self._kv("Body Size", f'{result["body_size"]:,} bytes')}
        """
        sections.append({"title": "📊 Overview", "content": overview})

        # Tech Stack
        if tech:
            tech_html = "".join(f'<span class="tag tag-tech">{escape(cat)}: {escape(val)}</span> ' for cat, val in tech)
            sections.append({"title": "🔧 Tech Stack", "content": tech_html})

        # Security
        sec_rows = ""
        for check in security["checks"]:
            status = f'<span class="pass">✅ {escape(check["value"][:60])}</span>' if check["present"] else '<span class="fail">❌ Missing</span>'
            sec_rows += f'<tr><td><b>{escape(check["header"])}</b></td><td>{status}</td><td style="font-size:11px;color:#57606a">{escape(check["description"])}</td></tr>'
        grade_class = f'grade-{security["grade"]}'
        sec_html = f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:12px"><span class="grade {grade_class}">{security["grade"]}</span><span>{security["present"]}/{security["total"]} headers present</span></div>'
        sec_html += f'<table><tr><th>Header</th><th>Status</th><th>Purpose</th></tr>{sec_rows}</table>'
        sections.append({"title": "🛡️ Security Headers", "content": sec_html})

        # SSL
        if ssl_info and "error" not in ssl_info:
            ssl_html = f"""
            {self._kv("Issuer", ssl_info.get("issuer", {}).get("organizationName", "Unknown"))}
            {self._kv("Subject", ssl_info.get("subject", {}).get("commonName", "Unknown"))}
            {self._kv("Valid Until", ssl_info.get("not_after", "Unknown"))}
            {self._kv("SANs", ", ".join(ssl_info.get("san", [])[:5]))}
            """
            sections.append({"title": "🔒 SSL Certificate", "content": ssl_html})

        # API Analysis
        if api_info["is_json"]:
            api_html = ""
            if api_info.get("auth_required"):
                api_html += '<span class="tag tag-warn">🔑 Authentication Required</span> '
            if api_info.get("auth_hints"):
                api_html += f'<span class="tag tag-warn">Auth Headers: {", ".join(api_info["auth_hints"])}</span> '
            if api_info.get("rate_limit"):
                for k, v in api_info["rate_limit"].items():
                    api_html += f'{self._kv(k, v)}'
            if api_info.get("pagination"):
                api_html += "<br><b>Pagination:</b> " + ", ".join(api_info["pagination"])
            if api_info.get("schema"):
                api_html += f'<br><b>Response Schema:</b><pre>{escape(json.dumps(api_info["schema"], indent=2))}</pre>'
            sections.append({"title": "🔌 API Analysis", "content": api_html})

        # Headers
        header_html = "".join(self._kv(k, v) for k, v in sorted(result["headers"].items()))
        sections.append({"title": "📋 All Response Headers", "content": header_html})

        # Parse HTML if applicable
        if "html" in result.get("content_type", "").lower() and result.get("body_preview"):
            parser = _MetaParser()
            try:
                parser.feed(result["body_preview"])
            except Exception:
                pass
            if parser.title or parser.meta:
                seo_html = ""
                if parser.title:
                    seo_html += self._kv("Title", parser.title.strip())
                for key in ["description", "og:title", "og:description", "og:image", "twitter:card"]:
                    if key in parser.meta:
                        seo_html += self._kv(key, parser.meta[key])
                if parser.scripts:
                    seo_html += self._kv("Scripts", f"{len(parser.scripts)} external scripts")
                sections.append({"title": "🔍 SEO & Meta", "content": seo_html})

        from urllib.parse import urlparse
        host = urlparse(url).hostname or "scan"
        html = self._render_report(host, sections)
        path = self._save_and_open(html, host)

        return (
            f"## ✅ Recon Complete — {url}\n\n"
            f"**Status:** {result['status']} · **Time:** {result['response_time_ms']}ms · "
            f"**Security Grade:** {security['grade']} ({security['present']}/{security['total']})\n\n"
            f"**Report:** `{path}`\n\n"
            f"Opened in browser. — Made by HOLO"
        )

    def _action_api(self, url="", **kwargs):
        if not url:
            return "Please provide an API URL. Example: `url=https://api.github.com`"

        result = self._fetch(url)
        if result["error"]:
            return f"❌ Failed to reach {url}: {result['error']}"

        api_info = self._analyze_api(result)
        sections = []

        # Overview
        overview = f"""
        {self._kv("URL", result["url"])}
        {self._kv("Status", f'{result["status"]} {"✅" if result["status"] == 200 else "⚠️"}')}
        {self._kv("Content-Type", result["content_type"])}
        {self._kv("Response Time", f'{result["response_time_ms"]}ms')}
        {self._kv("Is JSON", "✅ Yes" if api_info["is_json"] else "❌ No")}
        """
        sections.append({"title": "📊 Endpoint Overview", "content": overview})

        # Auth
        auth_html = ""
        if api_info.get("auth_required"):
            auth_html += '<span class="tag tag-warn">🔑 Authentication Required (401/403)</span><br>'
        if api_info.get("auth_hints"):
            auth_html += "Auth-related headers: " + ", ".join(f'<span class="mono">{h}</span>' for h in api_info["auth_hints"])
        else:
            auth_html += '<span class="tag tag-ok">No auth required for this endpoint</span>'
        sections.append({"title": "🔑 Authentication", "content": auth_html})

        # Rate Limits
        if api_info.get("rate_limit"):
            rl_html = "".join(self._kv(k, v) for k, v in api_info["rate_limit"].items())
            sections.append({"title": "⏱️ Rate Limiting", "content": rl_html})

        # Pagination
        if api_info.get("pagination"):
            pag_html = "<ul>" + "".join(f"<li>{escape(p)}</li>" for p in api_info["pagination"]) + "</ul>"
            sections.append({"title": "📄 Pagination", "content": pag_html})

        # Schema
        if api_info.get("schema"):
            schema_html = f'<pre>{escape(json.dumps(api_info["schema"], indent=2))}</pre>'
            sections.append({"title": "📐 Response Schema", "content": schema_html})

        # Discovery
        disc_html = ""
        base_url = url.rstrip("/").rsplit("/", 1)[0] if "/" in url.split("//", 1)[-1] else url
        for path in ["/docs", "/swagger.json", "/openapi.json", "/api-docs", "/.well-known/openid-configuration"]:
            disc_html += f'<div class="kv"><div class="k"><span class="mono">{path}</span></div><div class="v">Try: <a href="{base_url}{path}" target="_blank">{base_url}{path}</a></div></div>'
        sections.append({"title": "🔎 API Discovery Links", "content": disc_html})

        from urllib.parse import urlparse
        host = urlparse(url).hostname or "api"
        html = self._render_report(f"API: {host}", sections)
        path = self._save_and_open(html, f"api-{host}")

        return (
            f"## ✅ API Recon Complete — {url}\n\n"
            f"**Status:** {result['status']} · **JSON:** {'Yes' if api_info['is_json'] else 'No'} · "
            f"**Auth Required:** {'Yes' if api_info.get('auth_required') else 'No'}\n\n"
            f"**Report:** `{path}`\n\nOpened in browser. — Made by HOLO"
        )

    def _action_security(self, url="", **kwargs):
        if not url:
            return "Please provide a URL to audit. Example: `url=https://mysite.com`"

        result = self._fetch(url)
        if result["error"]:
            return f"❌ Failed to reach {url}: {result['error']}"

        security = self._analyze_security(result["headers"], url)
        ssl_info = self._get_ssl_info(url) if url.startswith("https") else {}
        sections = []

        # Grade
        grade_class = f'grade-{security["grade"]}'
        grade_html = f'<div style="display:flex;align-items:center;gap:20px"><span class="grade {grade_class}" style="font-size:40px;width:64px;height:64px;line-height:64px">{security["grade"]}</span><div><b>{security["present"]}/{security["total"]}</b> security headers present<br><span style="font-size:12px;color:#57606a">A=7+ B=5-6 C=3-4 D=1-2 F=0</span></div></div>'
        sections.append({"title": "🏆 Security Grade", "content": grade_html})

        # Header checks
        sec_rows = ""
        for check in security["checks"]:
            if check["present"]:
                status = f'<span class="pass">✅ Present</span>'
                val = f'<br><span class="mono" style="font-size:11px">{escape(check["value"][:80])}</span>' if check["value"] else ""
            else:
                status = '<span class="fail">❌ Missing</span>'
                val = ""
            sec_rows += f'<tr><td><b>{escape(check["header"])}</b></td><td>{status}{val}</td><td style="font-size:11px;color:#57606a">{escape(check["description"])}</td></tr>'
        sections.append({"title": "🛡️ Security Headers", "content": f'<table><tr><th>Header</th><th>Status</th><th>Purpose</th></tr>{sec_rows}</table>'})

        # SSL
        if ssl_info and "error" not in ssl_info:
            ssl_html = f"""
            {self._kv("Issuer", ssl_info.get("issuer", {}).get("organizationName", "Unknown"))}
            {self._kv("Subject", ssl_info.get("subject", {}).get("commonName", "Unknown"))}
            {self._kv("Valid From", ssl_info.get("not_before", "Unknown"))}
            {self._kv("Valid Until", ssl_info.get("not_after", "Unknown"))}
            {self._kv("SANs", ", ".join(ssl_info.get("san", [])[:10]))}
            """
            sections.append({"title": "🔒 SSL Certificate", "content": ssl_html})
        elif not url.startswith("https"):
            sections.append({"title": "🔒 SSL", "content": '<span class="fail">❌ Not using HTTPS!</span>'})

        from urllib.parse import urlparse
        host = urlparse(url).hostname or "security"
        html = self._render_report(f"Security: {host}", sections)
        path = self._save_and_open(html, f"sec-{host}")

        return (
            f"## ✅ Security Audit Complete — {url}\n\n"
            f"**Grade: {security['grade']}** ({security['present']}/{security['total']} headers)\n\n"
            f"**Report:** `{path}`\n\nOpened in browser. — Made by HOLO"
        )

    def _action_compare(self, url="", url2="", **kwargs):
        if not url or not url2:
            return "Please provide two URLs. Example: `url=https://api.openai.com url2=https://api.anthropic.com`"

        r1 = self._fetch(url)
        r2 = self._fetch(url2)
        s1 = self._analyze_security(r1.get("headers", {}), url)
        s2 = self._analyze_security(r2.get("headers", {}), url2)

        def col(result, security):
            html = f"""
            {self._kv("Status", result.get("status", "Error"))}
            {self._kv("Response Time", f'{result.get("response_time_ms", "?")}ms')}
            {self._kv("Content-Type", result.get("content_type", "?"))}
            {self._kv("Body Size", f'{result.get("body_size", 0):,} bytes')}
            {self._kv("Security Grade", security["grade"])}
            {self._kv("Security Headers", f'{security["present"]}/{security["total"]}')}
            """
            return html

        sections = [{
            "title": "⚔️ Side-by-Side Comparison",
            "content": f'<div class="compare"><div class="col"><h3 style="color:#0969da">{escape(url)}</h3>{col(r1, s1)}</div><div class="col"><h3 style="color:#0969da">{escape(url2)}</h3>{col(r2, s2)}</div></div>'
        }]

        html = self._render_report(f"Compare", sections)
        path = self._save_and_open(html, "compare")

        return (
            f"## ✅ Comparison Complete\n\n"
            f"| | {url} | {url2} |\n|---|---|---|\n"
            f"| Status | {r1.get('status')} | {r2.get('status')} |\n"
            f"| Time | {r1.get('response_time_ms')}ms | {r2.get('response_time_ms')}ms |\n"
            f"| Security | {s1['grade']} | {s2['grade']} |\n\n"
            f"**Report:** `{path}`\n\nOpened in browser. — Made by HOLO"
        )

    def _action_history(self, **kwargs):
        history_file = os.path.join(self._data_dir, "history.json")
        if not os.path.isfile(history_file):
            return "No recon history yet. Run a scan first!"
        try:
            with open(history_file, "r") as f:
                history = json.load(f)
        except (json.JSONDecodeError, OSError):
            return "No recon history yet."

        lines = ["## 📜 Recon History — Made by HOLO\n"]
        for entry in reversed(history[-20:]):
            lines.append(f"- **{entry['slug']}** — {entry['timestamp'][:16]} — `{entry['path']}`")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Perform
    # ------------------------------------------------------------------
    def perform(self, action="scan", url="", url2="", **kwargs):
        dispatch = {
            "scan": self._action_scan,
            "api": self._action_api,
            "security": self._action_security,
            "compare": self._action_compare,
            "history": self._action_history,
        }
        handler = dispatch.get(action, self._action_scan)
        return handler(url=url, url2=url2)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
