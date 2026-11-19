"""Browser: use this Mac's real, signed-in Edge or Chrome by what things are called, not where they are.

A RAPP agent file: drop it in a Brainstem's agents/ folder. It talks to the local browser bridge
(~/.rappter-chrome/runtime/rappter_chrome_mcp.py, from kody-w/rapp-copilot-in-chrome) and to nothing else.
The model only picks an action and fills plain words; this file does the rest.
Lesson paid by others: Playwright finds elements by role and visible text, which survives redesigns that break
pixel positions and class names.
"""
import json
import os
import subprocess

try:
    from agents.basic_agent import BasicAgent
except Exception:  # standalone use and tests
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            self.name, self.metadata = name, metadata or {}

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/browser",
    "version": "0.1.0",
    "display_name": "Browser",
    "description": "Open a page, read it, click or type by visible label in this Mac's signed-in browser.",
    "author": "kody-w",
    "tags": ["browser", "edge", "chrome"],
    "category": "integrations",
    "requires_env": [],
    "example_call": "Read my latest Google Voice calls.",
}

READ_JS = r"""
((about) => {
  // 2026-11-19: npr.org's <main> is just the radio player ("Play Live Radio"); a tiny main falls back to the whole page.
  let root = document.querySelector('main,[role=main],article') || document.body;
  if ((root.innerText || '').length < 400) root = document.body;
  // The tab title is what people mean by "the page title" (example.com's link lands on "Example Domains").
  const lines = ((document.title ? 'Page title: ' + document.title + '\n' : '') + (root.innerText || '')).split(/\n+/).map(l => l.trim()).filter(l => l && !/^(loading|loading\.\.\.|…)$/i.test(l));
  if (!about) return lines.join('\n').slice(0, 6000);
  const words = about.toLowerCase().split(/\W+/).filter(w => w.length > 2);
  const out = [];
  // A short matching line is usually a section heading ("Pinned", "Hours"): take the section under it, not 3 lines.
  lines.forEach((l, i) => { if (words.some(w => l.toLowerCase().includes(w))) out.push(lines.slice(Math.max(0, i - 1), i + (l.length <= 30 ? 16 : 3)).join(' | ')); });
  return (out.length ? out.slice(0, 25).join('\n') : 'nothing on the page mentions ' + about + '. Start of page:\n' + lines.slice(0, 40).join('\n')).slice(0, 6000);
})(%s)
"""

RECEIPTS = os.environ.get("BROWSER_RECEIPTS") or os.path.expanduser("~/.openrappter/receipts/browser.jsonl")


def receipt(action, url="", label="", result=""):
    """One line per browser step: what was done, where, and the start of what came back. Never typed text
    (it could be private); a record-kind exhaust rule keeps the folder (lungs keep never removes records)."""
    try:
        import time
        os.makedirs(os.path.dirname(RECEIPTS), exist_ok=True)
        rule = os.path.join(os.path.dirname(RECEIPTS), ".exhaust.json")
        if not os.path.exists(rule):
            with open(rule, "w") as f:
                json.dump({"schema": "rapp-exhaust/1", "kind": "record"}, f)
        with open(RECEIPTS, "a") as f:
            f.write(json.dumps({"at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "action": action,
                                "url": url, "label": label, "result": (result or "")[:160]}) + "\n")
    except OSError:
        pass   # a receipt must never break the job


RESULTS_JS = r"""
(() => {
  const a = [...document.querySelectorAll('a.result__a, h2 a, h3 a')].filter(x => x.href && x.innerText.trim().length > 8);
  return a.slice(0, 8).map((x, i) => (i + 1) + '. ' + x.innerText.trim() + ' | ' + x.href).join('\n') || 'no results';
})()
"""

LAST_TAB = os.environ.get("BROWSER_LAST_TAB") or os.path.expanduser("~/.openrappter/receipts/last-tab")


def remember_tab(tab):
    try:
        with open(LAST_TAB, "w") as f:
            f.write(str(tab))
    except OSError:
        pass


def last_tab():
    try:
        return int(open(LAST_TAB).read().strip())
    except (OSError, ValueError):
        return None


RUNTIME = os.path.expanduser("~/.rappter-chrome/runtime/rappter_chrome_mcp.py")
NEVER = ("pay", "buy", "purchase", "checkout", "order", "delete", "remove", "password", "signin", "login", "logon",
         "allow", "approve", "confirm", "accept", "agree", "authorize", "authorise", "grant", "sendmoney", "transfer",
         "subscribe", "unsubscribe")


def refused(label):
    """Owner-only buttons. Letters only, so 'Sign-in', 'Log in' and 'Signin' all match (tests found the gap 2026-11-19).
    Over-cautious on purpose: a harmless 'Remove filter' is refused too; the owner can do that one."""
    flat = "".join(ch for ch in (label or "").lower() if ch.isalpha())
    return any(w in flat for w in NEVER)

FIND_JS = r"""
((want, act, text, submit) => {
  const lab = e => ((e.getAttribute('aria-label') || '') + ' ' + (e.innerText || e.value || e.placeholder || '')).trim();
  const vis = e => e.offsetParent !== null;
  const sel = act === 'type' ? 'input,textarea,[contenteditable=true],[role=textbox]'
                             : 'button,a,[role=button],[role=link],[role=tab],[role=menuitem],input[type=submit]';
  const els = [...document.querySelectorAll(sel)].filter(vis);
  const w = want.toLowerCase();
  const full = x => (lab(x) + ' ' + (x.name || '') + ' ' + (x.id || '') + ' ' + (x.type || '') + ' ' + (x.title || '')).toLowerCase();
  const words = w.split(/\W+/).filter(t => t.length > 2 && !['box', 'the', 'field', 'button', 'link'].includes(t));
  const score = x => words.filter(t => full(x).includes(t)).length;
  let e = els.find(x => lab(x).toLowerCase() === w) || els.find(x => lab(x).toLowerCase().includes(w));
  if (!e && words.length) { const best = [...els].sort((a, b) => score(b) - score(a))[0]; if (best && score(best) > 0) e = best; }
  if (!e && act === 'type') e = els.find(x => x.type === 'search' || x.getAttribute('role') === 'searchbox') || (els.length === 1 ? els[0] : null);
  if (!e) return 'nothing on the page is called ' + JSON.stringify(want);
  if (act === 'type') {
    const name = (e.getAttribute('aria-label') || e.placeholder || e.name || 'the box').slice(0, 60);   // before typing: never echo the text
    e.focus(); if ('value' in e) { e.value = text; e.dispatchEvent(new Event('input', {bubbles: true})); } else { e.innerText = text; }
    if (submit) {   // press Enter: submit the form if there is one, else send the key
      if (e.form) { e.form.requestSubmit ? e.form.requestSubmit() : e.form.submit(); }
      else { for (const t of ['keydown', 'keypress', 'keyup']) e.dispatchEvent(new KeyboardEvent(t, {key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true})); }
      return 'typed into ' + name + ' and pressed Enter';
    }
    return 'typed into ' + name;
  }
  e.click(); return 'clicked ' + lab(e).slice(0, 60);
})(%s, %s, %s, %s)
"""


def call(tool, args, timeout=60):
    """One tools/call to the bridge over stdio JSON-RPC. Returns (ok, text)."""
    if not os.path.exists(RUNTIME):
        return False, "the browser bridge is not installed on this Mac"
    msgs = [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize",
         "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "browser-agent", "version": "0.1"}}},
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": tool, "arguments": args}},
    ]
    try:
        p = subprocess.run(["/usr/bin/python3", "-I", RUNTIME], input="\n".join(json.dumps(m) for m in msgs) + "\n",
                           capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return False, f"the browser did not answer within {timeout} s"
    for line in p.stdout.splitlines():
        try:
            r = json.loads(line)
        except ValueError:
            continue
        if r.get("id") == 2:
            res = r.get("result") or {}
            text = "".join(c.get("text", "") for c in res.get("content", []))
            return not res.get("isError"), text.strip()
    return False, "the browser bridge gave no answer"


class BrowserAgent(BasicAgent):
    def __init__(self):
        self.name = "Browser"
        self.metadata = {
            "name": self.name,
            "description": ("Use this Mac's real, signed-in web browser. action: 'search' the web for a query (returns result titles and links; then open the best one), 'open' a url, 'read' the page text, 'back' to the previous page, 'outline' a long page (its section headings; then read with about=<heading>), "
                            "'click' something by its visible label, 'type' text into a box by its label (enter=true to search or submit), or 'tabs'. After click or Enter the new page text comes back. "
                            "Never use it to pay, buy, delete, sign in or approve anything."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["tabs", "search", "open", "read", "outline", "click", "type", "back"]},
                    "url": {"type": "string", "description": "for open: the web address"},
                    "new_tab": {"type": "boolean", "description": "for open: open in a new tab and keep the current one"},
                    "query": {"type": "string", "description": "for search: what to look up on the web (use this instead of guessing addresses)"},
                    "label": {"type": "string", "description": "for click/type: the words on the button, link or box"},
                    "text": {"type": "string", "description": "for type: what to type"},
                    "about": {"type": "string", "description": "for read/open: only return the parts of the page about this (e.g. 'tomorrow', 'repositories')"},
                    "enter": {"type": "boolean", "description": "for type: press Enter afterwards (search boxes, forms)"},
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _tab(self, url_hint=""):
        if not getattr(self, "_edge_checked", False) and \
                subprocess.run(["/usr/bin/pgrep", "-x", "Microsoft Edge"], capture_output=True).returncode != 0:
            subprocess.run(["/usr/bin/open", "-g", "-a", "Microsoft Edge"], capture_output=True)   # skip the 35 s wait
            import time
            time.sleep(6)
        self._edge_checked = True   # once per request: open can ask for a tab twice
        ok, t = call("tabs_context_mcp", {})
        if not ok and "dialled in" in t:   # browser closed: open Edge in the background, give the add-on a moment, retry once
            subprocess.run(["/usr/bin/open", "-g", "-a", "Microsoft Edge"], capture_output=True)
            import time
            time.sleep(6)
            ok, t = call("tabs_context_mcp", {})
        try:
            tabs = json.loads(t).get("availableTabs", []) if ok and t.startswith("{") else []
        except ValueError:   # a garbled bridge reply means no tab, never a crash
            tabs = []
        if url_hint:
            for x in tabs:
                if url_hint in x.get("url", ""):
                    return x["tabId"]
        # 2026-11-19 dogfood: with several tabs open, "the active tab" was not the one just used (outline read swift.org).
        # Keep working in the tab we last used, while it is still open.
        lt = last_tab()
        if lt is not None and any(x.get("tabId") == lt for x in tabs):
            return lt
        act = [x for x in tabs if x.get("active")]
        return (act or tabs or [{}])[0].get("tabId")

    def _read(self, tab, about=""):
        import time
        # Pages that fill themselves in (GitHub pins, Google Voice) change for a few seconds after load:
        # read until two reads in a row match, up to ~8 s. (2026-11-19: GitHub pins failed 2 of 3 runs on one read.)
        prev = None
        for _ in range(5):
            ok, t = call("javascript_tool", {"tabId": tab, "code": READ_JS % json.dumps(about or "")})
            if not ok and "cannot access" in (t or "").lower():   # page refuses scripts: plain text read instead
                ok, t = call("get_page_text", {"tabId": tab})
                return (t or "")[:6000]
            if ok and t and t == prev:
                break
            prev = t
            time.sleep(1.5)
        return t if ok and t else call("get_page_text", {"tabId": tab})[1][:6000]

    def perform(self, action="read", url="", label="", text="", enter=False, about="", query="", new_tab=False, **_):
        self._new_tab = bool(new_tab)
        if action == "search":
            from urllib.parse import quote_plus
            url = "https://html.duckduckgo.com/html/?q=" + quote_plus(query or text or label)
            self._perform("open", url, "", "", False, "")
            out = call("javascript_tool", {"tabId": self._tab(), "code": RESULTS_JS})[1]
            from urllib.parse import urlparse, parse_qs
            def real(m):   # duckduckgo.com/l/?uddg=<real address>  ->  the real address
                q = parse_qs(urlparse(m).query).get("uddg")
                return q[0] if q else m
            out = "\n".join(l.rsplit(" | ", 1)[0] + " | " + real(l.rsplit(" | ", 1)[1]) if " | " in l else l
                             for l in out.splitlines())[:3000]
            receipt("search", url, "", out)
            return out
        out = self._perform(action, url, label, text, enter, about)
        receipt(action, url, label, out)
        return out

    def _perform(self, action, url, label, text, enter, about):
        if action in ("click", "type") and refused(label):
            return f"I will not {action} '{label}': that is the owner's to do."
        if action == "tabs":
            return call("tabs_context_mcp", {})[1]
        if action == "open":
            if not url.startswith(("https://", "http://")):
                url = "https://" + url
            host = url.split("/")[2]
            if getattr(self, "_new_tab", False):   # keep what is open; the new tab becomes the one we work in
                ok, t = call("tabs_create_mcp", {"url": url, "active": True})
                try:
                    tab = json.loads(t).get("tabId") if ok and t.startswith("{") else None
                except ValueError:
                    tab = None
                if tab is None:
                    return "could not open a new tab: " + t[:200]
                call("navigate", {"tabId": tab, "url": url})
            else:
                tab = self._tab(host) or self._tab()
            remember_tab(tab)
            if tab is None:
                return "no browser window is open"
            call("navigate", {"tabId": tab, "url": url})
            import time
            for _ in range(10):   # wait for the page to finish loading before reading (up to ~10 s)
                time.sleep(1)
                ok, st = call("javascript_tool", {"tabId": tab, "code": "document.readyState + '|' + document.querySelectorAll('img:not([complete])').length"})
                if (ok and st.startswith("complete")) or (not ok and "cannot access" in st.lower()):
                    break   # 2026-11-19: Amazon sign-in refuses page scripts; waiting on it timed the whole job out
            time.sleep(1)   # then a beat for scripts that fill the page in after load
            return self._read(tab, about)
        tab = self._tab()
        if tab is None:
            return "no browser window is open"
        if action == "read":
            return self._read(tab, about)
        if action == "back":
            call("javascript_tool", {"tabId": tab, "code": "history.back(); 'ok'"})
            import time
            time.sleep(2)
            return "went back. Now on the page:\n" + self._read(tab)[:3000]
        if action == "outline":
            js = "[...document.querySelectorAll('h1,h2,h3')].filter(h=>h.offsetParent!==null).map(h=>(h.tagName==='H3'?'  - ':'- ')+h.innerText.trim()).filter(x=>x.length>3).slice(0,80).join('\\n')||'no headings on this page'"
            return call("javascript_tool", {"tabId": tab, "code": js})[1][:4000]
        code = FIND_JS % (json.dumps(label or ""), json.dumps(action), json.dumps(text or ""), json.dumps(bool(enter)))
        ok, said = call("javascript_tool", {"tabId": tab, "code": code})
        if ok and (action == "click" or enter) and not said.startswith("nothing"):
            import time
            time.sleep(2)   # let the next page load, then show it, so one step is enough
            said += "\n\nNow on the page:\n" + self._read(tab)[:3000]
        return said[:4000]
