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
    "name": "@borg/recon_agent",
    "version": "1.0.0",
    "display_name": "Recon",
    "description": "URL intelligence scanner — point it at any URL for a full recon report: tech stack, security headers, API schema, SSL, performance. Every scan produces an auto-opening HTML report.",
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