---
name: "rar-howardh-recon"
description: "URL intelligence scanner. Point it at any URL to get a full recon report: tech stack, security headers, API schema, performance, SSL, redirects. Every scan produces an HTML report that auto-opens. action=scan for full recon, action=api for API focus, action=security for security audit, action=compare for side-by-side, action=history for past scans."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/recon_agent", "rar_sha256": "7c13e82c07ce373aba2729caccfeab00ae44e5c80ef46c8de34e4798361f6f06", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Howard Hoy", "tags": ["recon", "url", "security", "api", "scanner", "headers", "ssl", "tech-stack"]}
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
