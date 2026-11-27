---
name: "rar-kody-w-pdf-reader"
description: "Reads a PDF the person has handed to this Brainstem and returns its text. Call it whenever they name a PDF or ask what is in one. With no file it lists their PDFs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/pdf_reader_agent", "rar_sha256": "96c6f0c340e78db12732e86ef28038d0f30a5ba1db225888bad665e675579d05", "source_kind": "rar-agent", "source_commit": "0eaae8dad7392645d9dcaf60d13dba2fa4624d44", "version": "1.0.2", "author": "kody-w", "tags": ["pdf", "documents", "reader", "phone", "offline"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/pdf_reader_agent`. The original RAPP
agent is preserved byte-for-byte in `pdf_reader_agent.py` and in the RCI capsule.

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

PDF Reader — lists the PDFs you have handed to your Brainstem and reads the text of one, page by page.

Where it looks: the folder named by the BRAINSTEM_FILES setting (on a phone, the files you give your agents),
otherwise ~/Documents. It only reads; it never changes or sends a file.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "file": {
      "description": "The PDF's file name from the list, or \"\" to list the PDFs available.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pdf_reader_agent.py` and embedded as the fenced Python below (sha256 96c6f0c340e78db1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pdf_reader_agent.py` first:

```bash
python3 pdf_reader_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pdf_reader_agent.py   # or on stdin
python3 pdf_reader_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/pdf_reader_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/pdf_reader_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/pdf_reader_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
# /// script
# dependencies = ["pypdf>=5"]
# ///
"""
PDF Reader — lists the PDFs you have handed to your Brainstem and reads the text of one, page by page.

Where it looks: the folder named by the BRAINSTEM_FILES setting (on a phone, the files you give your agents),
otherwise ~/Documents. It only reads; it never changes or sends a file.
"""

import json
import os

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/pdf_reader_agent",
    "version": "1.0.2",
    "display_name": "PDF Reader",
    "description": "Lists the PDFs handed to this Brainstem and reads the text of one, a page range at a time; read-only, no network.",
    "author": "kody-w",
    "tags": ["pdf", "documents", "reader", "phone", "offline"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # other hosts
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        from openrappter.agents.basic_agent import BasicAgent  # type: ignore

MAX_CHARS = 6000


def _folder():
    return os.path.expanduser(os.environ.get("BRAINSTEM_FILES") or "~/Documents")


_PREVIEWS = {}


def _preview(path, limit=80):
    """The first words of page 1, cached by modification time; "" when unreadable."""
    try:
        key = (path, os.path.getmtime(path))
    except OSError:
        return ""
    if key not in _PREVIEWS:
        try:
            from pypdf import PdfReader
            text = (PdfReader(path).pages[0].extract_text() or "").split()
            _PREVIEWS[key] = " ".join(text)[:limit]
        except Exception:
            _PREVIEWS[key] = ""
    return _PREVIEWS[key]


def _pdfs():
    folder = _folder()
    try:
        names = sorted(n for n in os.listdir(folder) if n.lower().endswith(".pdf"))
    except OSError:
        names = []
    return folder, names


class PdfReaderAgent(BasicAgent):
    def __init__(self):
        self.name = "PdfReader"
        self.metadata = {
            "name": self.name,
            "description": "Reads a PDF the person has handed to this Brainstem and returns its text. Call it whenever they name a PDF or ask what is in one. With no file it lists their PDFs.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file": {"type": "string", "description": "The PDF's file name from the list, or \"\" to list the PDFs available."},
                },
                "required": [],
            },
        }
        super().__init__(self.name, self.metadata)

    def system_context(self):
        """Tells the chat which PDFs it holds, each with its opening words, so "my lease", "that document"
        or "is a burst pipe covered?" reaches this agent."""
        folder, names = _pdfs()
        if not names:
            return None
        shown = []
        for n in names[:12]:
            hint = _preview(os.path.join(folder, n))
            shown.append(f"{n} (starts: \"{hint}\")" if hint else n)
        more = f", and {len(names) - 12} more" if len(names) > 12 else ""
        return (f"The person has given you these PDFs: {'; '.join(shown)}{more}. When they ask about anything "
                f"these could answer, even as \"my lease\" or \"that document\", call PdfReader with the file name first.")

    def perform(self, file="", first_page=1, last_page=None, **kwargs):
        folder, names = _pdfs()
        if not str(file or "").strip():
            if not names:
                return json.dumps({"pdfs": [], "note": "No PDFs here yet. Hand one to your agents first."})
            return json.dumps({"pdfs": names})
        want = os.path.basename(str(file)).strip().lower()
        match = next((n for n in names if n.lower() == want), None) or \
            next((n for n in names if want.replace(".pdf", "") in n.lower()), None)
        if not match:
            return json.dumps({"error": f"No PDF named {file!r}.", "pdfs": names})
        try:
            from pypdf import PdfReader
        except ImportError:
            return json.dumps({"error": "pypdf is not installed here (pip install pypdf, or install this agent's card)."})
        try:
            reader = PdfReader(os.path.join(folder, match))
            total = len(reader.pages)
            def num(v, default):
                try:
                    v = int(float(v))
                except (TypeError, ValueError):
                    return default
                return v if v > 0 else default
            first = min(num(first_page, 1), total)
            last = min(max(num(last_page, first + 2), first), total)
            parts = []
            for i in range(first - 1, last):
                parts.append(f"--- page {i + 1} ---\n{(reader.pages[i].extract_text() or '').strip()}")
            text = "\n".join(parts)
        except Exception as e:  # a damaged or locked PDF should say so, not crash the chat
            return json.dumps({"error": f"Could not read {match}: {type(e).__name__}: {e}"})
        cut = len(text) > MAX_CHARS
        return json.dumps({"file": match, "pages": total, "read": [first, last],
                           "text": text[:MAX_CHARS], "truncated": cut})
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/61aeXOjyJL/Kqznj7YfbkscQsgT/XaR0IFOQAdC4wk3R3Ff4hLI6/3sW4Vkt9vT82JfxCqiAyiq8s5fZuJ+udGK3InTm8cbPzbrr6eb+xsTZEbqJrkbR3BZBpqZYRom8iMsdwCWgDSLI8zRMvgvMoGJ5TF84WZYP9XcKMtBiMF1LAV5kUYZ5uYZloMqf8AGWhDAR+zkgAiUIEXkaizSQnAlH6eYlvnwvZZjkJ4bYXEEHjDFzR0sijHLDQA6H7gZoukAN0XHsgcoM6i0MAlAdvP4x5/3Ny68v3l8uTECLYNLN6JpITVAytkgyuH2QItsuJ7UUPcIPkOlrDgN4ZIJLOz6dJuBwLpv2H57unm6Qbdplj8nmg2+EfcYJH59WEI577F//MM/aamd3T0+Rdj1Z8UBZHvfaJlh37DnxLSy27sfG1wLqpZjWZ7eNvpBGyBedw9wxU1uP9L6sL0h9+kV+l2MjnnQQw9mESbZ7cvTDWL5dPOIQctA2vA4QE9PN8u4MR/mgBRgNYAemiDHQV2QS+u4gO5A9souej883bze/czyX7JrZPx44qRFOTRBnD0kWu486FoG0J7bN93v3pV+COITSD+aKdRyw4GHIxhJt7cRtGuKRShCLoZFZnk7hH371rC6u8eQX+4akz79LPjfk0EnH1KQBJoBbp9uHqA2yPONT5qNb2zeyP/FlY2oj/8HQ4E0jVNkKevNF40YJvaCrPEf6evDhfPfGjRP6098rDQOsaSGJzCYA3GaY++h/2MjqAyQ5JjQbBgiIf4taaFAFwZZoy5KeZjYUOwmjm4TN3lbu0hyjxzwttIARRNVXzLM0FLz7lNY/VWntBEf+v5dldu3EPJiN7p9S7HG7nefIjSPIVt4NgDR7YXQA8rY7NM2lPVREd6W9+hWK4L87hfZ9VfZ3n4lZOFG+a0VxFp+W36W4oPVbzd1Ahqj32M7LSgu93d/Q/fqiatMf5vvJYq9Evsn1sZAkIFf72+SGMoZQpshXX+A2T1GwGhuTPVJcARx1yOhVjXH3lHvCocYjpF31/u/oZJoaY7A748/P0mEAgMlVQrhGFwEwr5iV2j9lU0aSg9akoDIvIVp8/XrVwzJgr24UA7iFYMLMNVffvL1H+6fDzDfU83In1Elum0g4cuXd7h5hbn9KWzgNigwzPqnCIJAE2cN77u/pNGwucBaCWsXBh4x7DdYzUwthJxNxCeIDR/eoezOnLgITCzTaiyL75vsMVItc5q6asCq92+CxqAhh8ggdbGXJgNeH7GXHMbYLbh7eH5GmPH8jNbA68+JZhT5NS+QsncweBbc/nkw4eT1j02/FAGhE5KgYdcAFLIyWmmcj1aQPE3JaXx68eef97+O8evv6QbJ0VCB1z8e36VpqlaeFpGh5aChCkV/vYNVO6tRt/FsxBE6ci3ePy82NfxjJCEgf7rZgCDI3s0OOw4XVpemGML+woGAkt1jQINrJ9R7oBYmhiHnRjZ2ilP0MoshpbCG9oNV7ALTOaJkxkYRQnSDTN5ZNiUdwR6mFyjCIUJCvjHsgID5n083yHmGA7IP2PhwkfLfbyN+1RdcfYiK1Y8XMBRP0aeU/LkY/vFIkH9+IuW4TQV/TlJQuuD0axyOPqNfw+tD0r5Erxgs+iidHlFlvnlBdF/R3R00B1Sl4dMgWfSxB4hhffmGNfUYNSovKHgbWe8QapCvzY4LhQ+v/glfXYj9bNOrXZBEm5/7WtstQYQaIBQh8BwKDJhBX37HvlxUbTS6e31B/F5hgwob2kszi9pXTY9hamkR7C1RwHxk+W5pFC2IstFksBZlJ2Q5gNhC/sgS77EF768dzKcIe0J2MFBRfS+Ml3BFYd30kk1r/da73d28wsYYluG0MBBcob74t9+whWukcRZbObY2kNwwz3I3hJHyFG1QPLqXNElRw565OqR62ZeksQcaQlhsYd//6zI9tGBcPl+w97mJ5O8PGDJunLq2G8FKLHOi+BQ1rxBpGEgZSEuIj3qdg68wAr+iGxSE3z+Tekjq743f3cbYmDwQoPpJVgTgAYnbeOEinKFFEJ4BxAmA8BfyRfaAaQvZxUEJLqmW+S40nummUI84rS9TSxE9ImLfv3+H/anzFF1GBAq7jERZC254FwdWG6iAFbi2A6EbGE6MfXl5/YL9N/avTjXEEQ8RDidX40IJp+vVEoPjQ+PcrGmYEKgj4768Xs0IyUTQy9AVruWCy+HAjWB9ebPpesJ9JTsMpgMLZculCURh6ML2XrCwd3khU/QKoZITQ1AyAUpPEBk1ljeV6N2SzXii5W5m1fdYkYGG63f9bdh7Rgj6HVsMRAj/cYBGByjmBVu1KI5caP53j1/WIZH0y4d58QFbNvMgrLBa4sCKeOFhaRe/xNc5BHVYMZQ3AqenCI14AJlKQzF4MQ/cBC1jXF36tckBIw5D6NjsjXezBxUSbBPDooT64uwax1qKXNEAc43ZhWtqkQF+v4bUtXYj+10m1zcvmFevNDGIqvw1FZ8Ksk3QP4bVS3lBoOJoMAJ/zM7NoPV5dkYzNzrUNCIwBpoBs+l09Lq5voV8ehmJ49iHENVYrYHh6ySh181aX+aE5XozXDyPhPlwjWUgb4LiFmmNJU5D/Q02LkIiDPw4A97B6h3DLenJhe75nxZ/haEMhhWUMArqi9S/I3Eu4z0MDNjWZch/cNJrPiIg+mhcD1wDQLvfPEZFENzfIGE/juloIoexEALonwwN8hBtID7nLmieEBV0/flDxeZi4y/ZR/BD89AlS1Abch2ukdXRwg+3aKXmBpp+EQ51T5Aeag4j++YVwmYKjgWMKfPydeH6PtYRACJUhcNifvl88HIDZdZMLdeuUl8xEm5PtfRrhkKpRTy0IRf4fIEE+O7v0PO6LXM0mNNwX48xGKttUHQbdFlTJ8guRQKWARbJtinWbFtUW+voGmHqJNlhWVbXTIbpAKbb6XR7ZruDeiboUgM8o7RwEes20DTAmprZpXokQ3fMnmloFtM2CcrUNdLSaIakTZr+cdR3I/Oqz0VIZKF3IEd6X9V6udEZGu6c0JnAXX6DFr5T9W3Ll505Lqa4e25l/dXZpNVhj1oZ5Gw6kBxF2yzntlCAamZvFZFSByzIe6J5iPTh5iBZ/g5X99RU3Fl5wC9WdaHhE3+hFwGTHo9HAI6lOmcNqyzxkRX1GRBx7n7atWb5dlHUDKl26O0an+5wR6/k5JDN9utjdebXIR/jo9Ig51IhBV6Hyfazw5xyVMpOur1Jty1V1Kpqp1s52AgKySi93TpcDmbmKFa2R8MzlCyo5TIYUEw9k+vJdHEMiDDoz5WjkawEhW6NclYLD4aqCM7JS/2qGqzrsVCMNkvG3Jhd/2BRVbB3rYAJAHkMaKulhm4Wzs7z4LhKohPtV/qyRdRdtuyttYNPb2ayFu5GR7mdZds8WPfF1lTfJtWqa0Qp5bRkdaBHCkMG1HjZjeZMkdFEtfCO5HE/n05HsVH7QE3yaUl76XG/FFZ5MB910rxdRpPtarngkpRfVnnnQGn80JimXWfRUywj29C1MhvMe8OeZkYJvSrH3WmvRdfbcHcOzfF662rstjJSY12M0t6KLnKlY6w1h2MJhja02S4nAVWu1P0qEb2jfFjOpo4uKGwl89tdZtTsTu2lptoScsueT2ewG+cXjs6dFmE3oxaVuptQnLRWlV1HyaUiFGLPW43cluqwh528TSWvLw2zgResmXzge9C0c8Mw5ttk67VVdzInhERyjwrTK1Rz4puWW/XOYEJvQrmfjBl+RNubcNPpVd3pAo+MwfDcrqUW22vhY6MOJVcP51UNhv6OnQ6OiyyUHclyhaOjsKtg36dYMS3P663MDeOOWFrVIOqO9aoi8ZZbz6iaiwecq2bbdjImD5JDHTl12p9OctKYe1w283stfzAjmE0ukSNHcXr7dFS2RnGP72ycmJsd8jFF9/tat7cUg4nQp3feTNknDBDPZFc8x0nPFyGv1TmWd+diH/B7eyEPwNEb788Hd00tW+PQ7hDiUbHZduA4gRdxPbz0QYfaDqp4cjDG7NDuRz6By0tNYeyTwhkTn9cMe3M8eVo7WtQ46W7ndZJHos3Jc0sk4844q6K1MMV5M1TPQHRweejr5EDeDNpBUsnn8KRnVve088Q2PknMMLKXTGETPknU27wCXfqwKUAnVY+dcarUhe+RM0Ka2Jtl17P4UNScg5Cy6ag/m7QrfuNMBTOOtJwYlED0i9VBmhYjuTgaRE4tY0erJEqqdTru6t4m76geN5OZzUk99WhSLGU3PK4Ee7hc8lSMzymB3Xv77hCPtt5GTf3gdIhMbVrjvTon06BFzOfckT0HdalsomoXVNncE4/B2R8VC2IP/PVoHwGRCcZDvmSG0ibol+xRmvKJVsj1MtoFIlh4JtNWuYIK7HCcyOy6vZos+el6Ui13q/1kMWxbY41f7Oh4Z0dc4sK2cLBiQ7M3xGdTeVTs1JHCdvL1mN3pOWNr7lGeSWvzXGdrS22dvLm2sviS7eF4l6CBfzBEXCx1stdW3O0xDVVclVYC05JmI0Nf8jGZHjdztVQqLtPiniCpdtE7x2xJy6l/AlO+LW3Xh/G49nWn36/A2e+tvIhmRCoRdzgFjpk3T+fERvAnwNFZf19AxTtEx+VaPBGlHq8MNG7DcFo8NtqxSwdDeOA8n6y1M7WwZww4VoBbcZ6cz2YBsT64W4LheDVeTrZ6spv1vM1x3BLdYJGvuZMo90bhHuKjqDpTmjmMTa8TuaZExdKBknFmz3dkaqHsSL29pPyM7k2ls2JsU74ddpVxBTZL/DyinO2gI1QLSjgpjkcPJXnN69GM5X2ZOAQUR7iZwJv9kbXsd8bmHDDj+UzVvWPPkyciLljFxGO8uWwPzy2eWXczxqxJaVwe6+FQPC1MR0gZXwo9R5gqY22eVGUi6Iacb6htfh620nwoQbZc0ZuOhtVIlQIykU6uEFZRHIRH3HK1crHYl7x6xgVhvR7nXSAONVknxyYw3BM+E11i4khhPisOckqbQK2mk1YRD/uG2HH2My5NliZQ0hbpzbdr2ReTqrX1R6sCKn0cjMAkSal5Zy4SzpAR9UQ4DqecHNOkT9Itj1jN1wNqmJp+5k2CSd+S9PORX+F8e3twJxPqJLQHsqFRvVm33E3mvKmR+SpvT2ehb4/68mTH02w56w0EXmLCtIvH/TmlzsFeHQ62VRm47MgepPXorM3VzaFD9HN2GujAGxgEzpmdRB8ccHXRsdi1Zjnzsl0X3JkexaBfhvp81fH3UTxRvBNlwmhQisnaK8fEoSy68jYAi5400UR+MF5zgpizbntGp+f5chgMWZW3+vPz8Tg/UZJsDQ+HQxRucImz7W62SiZSNho42navnuSjf952+dFG6i6UkyIEA3ebm6fZqppDBLZ7hOAecXPU2svicrf3x14/dbZ4tOM2UqJSsPbhTq7U+KJn0nW3HJMC7Ceimc3t2dZaypN0a9k524u6i958nmU9NtUm7ljeVYse0QM82PnFbFzTR03KN8oQ16XzvIrrxaCYbY1Nf1MM2WLQ2gvFpjsn0rTGB+Awo0u7tm2cCPuznFsEXVLqS3EnHwkTOQmYPWPXBy7zsnVJ7plOh1NaVij6swXRXTu2oYvsYMbWQ2I76gG8YNcWh/vtwXJvBsx0smdp0V+3S9fcabhEB7sy5EiBAxqR4pF2kgqOcwEn1yvQH3XKuPBd3TuduNEqHLJZtloZdnw+nvrApflZ2bLjGKKGlOphW9nES4mqFsMxMxmy/cmmr/Vb5zpe2GOxGC2Yo9/H7VRadZc1URZRt0XTkZqcVcpcCy3R6VPxdCyfyVBYgGME4cW1k3rMDGWGKQ05KTUnA0PczFv7rT082pONuFd6hDFcuQB2NDaTG0NeTBaE2e2SRzak3DLVxPUB5G7tgd28Vp3SVrvhtjdeZzyRE32yPTeEnj7b8qp8Pjmd0Smjk65M0ooejU6n6dFdwDlxeV7vuc7KGvnzrlrGquCIO0JsV32V2+dSAg2G85V3WEWUsooztU8lPpWGreJkWb6t46pp1Pt41V61pj3mNGyZgw5zXiiOTzJq1ZNb4dbGlaFw1r3I94qpRghnqopLO2gfNzLHF+K5mJW24FQU4xTJVibZ01Iz+/ExO2zpmi2rLiBOo/WuVtatQXEe9uo0ObXBigWKvMcpY4Ir/NYYdWLGmHX71SEDfMzKhMh5DjOPyJ2M42Zc9DZjnG73NuS+miiTjPdqtkMGNElNW+TGlwYtd7bJg3Ob8DKuK2YxM5Hlkbf04j1bzzOGD0thY1W7Uqi1Dk4MZscYP/XSPYwog43V1oRy0uNCpsP87PIHfRN0dZPaES1VL0UVFjIl5O0sPVmOaLgUdeiSsOEEY8mUl2UB0zggzUpXxlG7IyijWZy64262Pe4q7tCOtUFCSQllzqAz6pm/VNJ8QHp8sBy6y5woty2LFsQyXMpTQVjNAH1glGK7KeJaau/ysTcZ6MODp6XkYbON8nHpnTdSJTCge4zbbKJXyYHw16xEdEcrGnTwdcX31ZXXqZfU0mRmNMO0nChe21N8rikGP5KriElmOH3ocyFXeq0TrLdku6X0fTgWffsGxys0tV4H4V98+kLz1//bGHiZ2OIS8osMyPCP5oP9Y8Pr8VfM4dSbGi5kfZlds6CwryPgZXL9Cg99Td9m98/f5S9Dfq7Z6M/zSDn0nwzevh+gGfd96EdfIuA1tqzAhXeQbfPZsRmgIesH8ub1fwHHRodUsiAAAA== -->
