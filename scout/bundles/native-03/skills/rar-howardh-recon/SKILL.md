---
name: "rar-howardh-recon"
description: "URL intelligence scanner. Point it at any URL to get a full recon report: tech stack, security headers, API schema, performance, SSL, redirects. Every scan produces an HTML report that auto-opens. action=scan for full recon, action=api for API focus, action=security for security audit, action=compare for side-by-side, action=history for past scans."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/recon_agent", "rar_sha256": "7c13e82c07ce373aba2729caccfeab00ae44e5c80ef46c8de34e4798361f6f06", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "recon_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@howardh/recon:021e59962545c90f24154f2e0ce7cf6868f02dc7313b39fa469d3617db51f320", "kind": "skill"}, "version": "1.0.1", "author": "Howard Hoy", "tags": ["recon", "url", "security", "api", "scanner", "headers", "ssl", "tech-stack"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@howardh/recon_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `recon_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `recon_agent.py` and embedded as the fenced Python below (sha256 7c13e82c07ce373a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `recon_agent.py` first:

```bash
python3 recon_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 recon_agent.py   # or on stdin
python3 recon_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
