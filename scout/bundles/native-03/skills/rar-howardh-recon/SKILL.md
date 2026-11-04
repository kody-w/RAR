---
name: "rar-howardh-recon"
description: "URL intelligence scanner. Point it at any URL to get a full recon report: tech stack, security headers, API schema, performance, SSL, redirects. Every scan produces an HTML report that auto-opens. action=scan for full recon, action=api for API focus, action=security for security audit, action=compare for side-by-side, action=history for past scans."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/recon_agent", "rar_sha256": "3d26f7412310635f9b35e26a324ecfdb1af86ea26b0069e753d95a76d4c9d089", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Howard Hoy", "tags": ["recon", "url", "security", "api", "scanner", "headers", "ssl", "tech-stack"]}
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
