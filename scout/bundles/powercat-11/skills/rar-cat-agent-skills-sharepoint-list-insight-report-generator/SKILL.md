---
name: "rar-cat-agent-skills-sharepoint-list-insight-report-generator"
description: "Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/sharepoint_list_insight_report_generator", "rar_sha256": "29a7c49ea3bc92bfb00f7b609f89aff2c1d0b85e5e6323b8e64c38353388513e", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Marco Rocca", "tags": ["sharepoint", "microsoft_365", "lists", "report", "html"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/sharepoint_list_insight_report_generator`. The original RAPP
agent is preserved byte-for-byte in `sharepoint_list_insight_report_generator_agent.py` and in the RCI capsule.

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

SharePoint List Insight Report Generator — Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#sharepoint-list-insight-report-generator
  Upstream author: Marco Rocca
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What to produce, and about what.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sharepoint_list_insight_report_generator_agent.py` and embedded as the fenced Python below (sha256 29a7c49ea3bc92bf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sharepoint_list_insight_report_generator_agent.py` first:

```bash
python3 sharepoint_list_insight_report_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sharepoint_list_insight_report_generator_agent.py   # or on stdin
python3 sharepoint_list_insight_report_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/sharepoint_list_insight_report_generator_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/sharepoint_list_insight_report_generator_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/sharepoint_list_insight_report_generator/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
SharePoint List Insight Report Generator — Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#sharepoint-list-insight-report-generator
  Upstream author: Marco Rocca
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/sharepoint_list_insight_report_generator',
    "version": '3.0.2',
    "display_name": 'SharePoint List Insight Report Generator',
    "description": 'Automatically discovers and validates a SharePoint list within a connected knowledge source, analyzes its structure and data, identifies key business insights, and generates a downloadable interactive HTML report. The report includes dynamic filters, interactive charts, sortable and searchable tables with pagination, detailed record drill-down through modal popups, and direct links to open items…',
    "author": 'Marco Rocca',
    "tags": ['sharepoint', 'microsoft_365', 'lists', 'report', 'html'],
    "category": 'integrations',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'sharepoint-list-insight-report-generator',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#sharepoint-list-insight-report-generator',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '271bccfbe07e039e',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class SharepointListInsightReportGenerator(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SharepointListInsightReportGenerator'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(SharepointListInsightReportGenerator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+16WbOj1pbmX6HPfbBdykwxiClvVESjCZAADcw4HWnmeQYJcPm/90ZSnrSrfKvv7eiHfmg5HAli7bXX+H1ri/Pbm913Udm8fX4T7cYtoWvpuvbbhzfPb90mrrq4LMAzpu/K3O5i186yEfLi1i1vftNCduFBNzuLPbvzwR0kR3bjn8u46KAsbjvoHndRXIAHblkUvtv5HpQW5T3zvdCH2rJvXP8DUGJn4wTWx10LtV3Tu13f+A/dQK/9AYo9v+jiIAYiqT9CTt/Ghd8C+aKNw6hrPzxkQ7/wm5cdXnkvstL2bCfzgVgHHrhdfPMhThEFqPGrsuk+QUrkv66BjJv1wGfIGws7j10oiDOwCqj+42oXuDdv14IlD9Xzvq0PAhc9bh9ftg+vocoO48Ke4/cB8vzOjoHTYDe3bIBbTZxlH2cjoS5qyj6MoLz07AyqyqqvXv54MZCe41ikLdSVUFn5BQiRn7dfehRGCZAkf7DzCuz49vnnXz68xeD67fNvb25mt+Crt0cyqjkZAsgF/wzW9eEv+4wVyPuHt8wuQiBdjaAOCnBf+U1QNjn4yvMD6HX3Y+tnwQfo3/4tvdtN2P70+UsBvT5f3ub/rv3sCwhBabdzml27sp04i7vxE8Rkd3tsgfMgr8WcHpDkuAg/PVd+11RW0L/Pz358bvIp9Lsfv7wBv5tHHL+8/QSVDdiv6efrT7OW6sefPmXl3W9+/Om7nrZ3kjl0QBmw+tPX1/1LLRD8LhoH0Ff5vNu89gIRjysfKP+Df/PnafpL3SskX5/CP5bVB+ivNc/+/Duw99lLDtD712pBDMDKt08JyNWPrz0a0GCFXbj+jz/9I7Vu5Lvp3Gb/lN6fn4oj3/ZAtF4h+enDI32/QIuXb+86//G2FSiYf8UTIP5tu/dA/SPdj8z+J9XZ3OzvufxLdX+1YPHv0M//0Lf/bsEHKPjytvUz0PDN3M+fod8eJfLzD973L3/45Xeg+n+rRn5A3Kzha24XceC33devP//wRL4ffvn5B9DtXePb+de+yf5K51/F9bHPnyL4kvrxz2vB/moxw20BvfcQ9FtZ/Y/m90+QNqP29+/bz9AfO3H+LKDZiW+bPkPwh25sga1/iONPb78DBCqe8D0/Bvjxt79BYuw2ZVsGHSS7Zd9BIMFdnPuz8UoUAwhvH6jR+DOdxDOGPuVA/c8Zni0uA+jX/+na3UcbIHz3sU0BdrbL9h3cvs4p/frigq9PPP8afgO4X58wXzbxDMcZdGXO5y/FQ9W8edX4rd/cAGA5Y+d/BH39cb4AqA/9+s9u8fWh7VM1/vrA7fgJhNcNP4Ng22f+p9ldPQLw/XTOtQvIH3y3BxtlJeDUmW18APvAmDIDPNPNoXk4+mKBshkfukH4Ps/Kfv31V8duoy/FE7Ux6EnW7RIIvJsDffwI3Auy2egvgH2jEvrht99/gP4D+u9WPZTPe5wBi7ySAyw8yCcJAs3W50DsQb0dQJJHcn77/RVkoAaEBAKpfJL1vHimL9/7FnGZYz6iOAE5Pog0iHI+RxJQAeC1TxAfQO/2vnh5JouoBIOE5wP2A2OAOwKtNnDnPZJF2UEtqMg2GD9Afes/dv3VaeyHiTnoerv7FRI3Z0BNZTYTafOiKrC4LOaR5r0ent8DJc0PLbT+puITJM3lCRi9sauosV97BPYzL4CSvi0Hym2o8O9fipmL/TlUj155hudRMGC0eKb045xzMBflABi89tve34YYD1IeRNp8KdpXH4BifMwPwJQRCnswcwF2+PurpNqo7DPvET9g6azplQXvlZVHDf5hPJtHAug1E0DPoQB6nwqgecJAVtD/H/v+3xv75jwyLHvdsYyy20I7SbmaT59AsLu5Dp8TPZi8INBkTyz5Po19Q9xvxPOlyGLQLM3496fkoypfMu9J8QBsXh/6QUuA+pr1Pjp27sCmmTNkfym+MRzwA3rAOShaAG+g/Wc/vm344VkWD0sjgGHz/fdp51uoQCRAV0JV72RzVnzfc2w3ncM2o86rPEH7+jMC3aPYjf7kFQS0gy4B+qGyeBQYCPqjBaRyLs0QCpoy/y4ez9MpsMLrXWBt5Df+J0gHwDE3TwvQCoyYswyIwg8PVVDugxgDE98jDMiiehpTNuk3A+1XLv4Y/9ej743+sGQ2Hui058r/Utzn6vX84ZnXdytfmQKm5jM0PRb9OdkvT6E/EvHfvxQPC985b+7mR91+Dw0Eij1/9vWz8KIy91/l861jPz0njudI827LZ2jDKBDzRPcHNUM/5t9I/zEfqH/OyWco6rqq/bxcvot9CkHn9M6nuFz+F57/23cW/jhjy8dX9398dvDHdxb+01bPqHyG/nCm/dPzV3l+hpBP8Cd4fiTErj/X3+vzGeqLdwT98Q/Xr/Q90uN7HwDaz9QAjJkrtY187zGYXf3v+bX/BKLO+M6630QA9YaNH87CTxZuZ/K+g3nhoRtk4EvxXgOv/gDIU4T+A5P+0LeP8WNG02eOvrEjeFR0DwAH+kL/03zom91t/bfPRZ9lH94A+Pn//IlxJkJQrCCG83ETtA2YCbvYf9zZvRfPgZyv//wbwulxYWdzZ5XzUDGzXvctoA8nAEDe/LkVw3jmvg8QMDwEoDr7dZ/bcZ6cHOBn24I5xJsd6cZqtvx5opxn0PcB9b9a8OhoAEVe+Xlu7A/QfJj4AL2fC2bEfp7UZs1+0YND8M/zmWT2GYiCf95l338icfy3X/7CjNcR5R8b8UKbJ+jbzkzis4t/4RPQ1vh1D3jBm+357uD3fcvnZr8/7Oyex/ff3r4ByitLr4EaiIPO/djOc8MS1D/YENw/Kw88+z8ftV+KgDgY8YAmlLZJd0X7Nua4NOoEDgwHpEPAdEDRdhCgLuLBDoX7uE9gKOZQPrFyMQrDMYyicATzgb5nIX+dp6R4Ns5x4QAhaIQCjEA7KIoRMOXDAUYTZGATPob6HgXDsPN9aQo69eXx08M5nO9T/6Nin47/9uYQKyDJrVqeeX42ywViLzHBGRpjwcGLYb8kttauXyeJ1OHdAXEGhXMVLBnWzcHx7dOYs8Z9f9itGYEX4s1BQ3zvvJODlYKbRX9d4IspPsD7AwCDiXAufqKq6x4NzkW0DBbuqi9WcbBc7pSgVSrKzQ/Hk3BXI0MrUV5hSfa0G427TpdXKj1mgzak9VUw8vt4SzqKd4e0iM1ICYp6PE6WNXbi5rBI1txicfAFUe+JSeWzwDaFEs7GOj4QAn89CAdZVPaaGMHXRS+1aONe+ctYeII8qGZzUMfITU5cL1IbytJ11yw5fdr7KxpWzfRoKaKmR/3yZOXLpBMGXGiIMzzGpFSch6VXOLK6th0eVA5F52cuVnJdWAyeeDtXXZftxmNihqOlyvbe2+6MTScdl+yyleTDaV87LelSGLxlrKvTJTWxjcnEzI5tOOWWjd/Sqy3LyvWUW4tBNpMgClrrkDNIcWZubNFs43ipEkMiMUdzUkTHlzW7aZNI04+J3qCnraCLQ3w5eDvOLiwi2NZTi3pB1PCrVUtz5F6dxKGvNAuPRl2Vc/R4oP2joDhsGpGVadaJ3LYJnObufqGuXMsXbi261mrFnE69Igl4xzmNes5yBKOvK1KhNYl3j5IgXnXWPGN7Jo+l7fq007cmvuJW4nKx1kVEO/WTXqtMWjh30h/pXDg1enRnJCk4jtQp2GxXAnPDbqestI6jSY6MwIH003gWNRkMlzdLKetogys73QHb3xOesmTj2Guav1xNvrwcTq25zG+cBF/sPUGsTzxHUPfApe65n6vc4To68W1hn/FlvwC9qZ83+wbAzr0qoqSRsxNqNbGnaxIVSOflsOUsa98dPEZmnbui6tOGZOrTWh52q7TMXfkiXC3QLmnZ7zrvfgwPPJ8pssare/G0Gid7pexlltn6fKLx11HsCnq7cDiZ9RRiy7dyjZhSfz3e9+juyCeGaFpuXSFmJlun9KJs1ubGorKkCGhzyx5cuW5j7XpZUBumP47Kgl4u7a5ldoq7J61pCJVDru96bwdOSe3qIE1rYXvupp3N2EhzMplaqApdSqPyRuzohc0lBl+5hnupFcvdNvJalU9rK+qUrYIeLPayXlzTUkl0Ix92XtumZcG35CRiBhGzx/Mh6XNwDGkY+wpvFXc6n5dogA/oMigwgrgZwwLxghgJgpuypB2y9VAhZ1rz0qqWBhunkUnoMrblaOrNUvFLe3kU/UE7shrGVYftMZH7ReBt0mgLqAPExi+ENWFWiSysgyMvwUxWKwZ+LSomxEJpK7rsWlQ5KaW1eFc6UsZ0EmkMd67qVSYpSeSelPujFdX1uFOncGXkuNyGjpyqDavhI6pKQ3WIxDqochtXspM0wHQshrpP81JcwtdBbTkj8b0h269Wmkmgk7MVrdPuciFiqrz4OaFeI2wJzBF3bLCTY8OSTGxNp267YRgRhS3f0ZJQzVfIGFyyerS9pdei1cID9lr62uOte3zd94Ynhde6Yhc3Tk9uBVvHq0oXNi7ZnLygTxx2DebmJAecaovG/UgXqOzyF5SOGJ4gMMlcd3GOjo0hXNX+kjsbg2M5tNvjvZBRRjdMB+HMHpI9y+SJiJ+6+F6wS7JoootTEsiuayRqu5BdaYyoa7Qe8cN2McZGpZbYQB70/tIHoZ5bAN7Hu2gFPbKhVFyXBGW1AWMcj2yvNpcvW2Sf67zIq/d0qLEzvpXQOD4sytvGvZTaBs4HVTqzlErrK40z726jKofuOiR1FWzVvXajt3UYOg6TL/izNtyygyq2WI+gCCwz+0DeUDoPU5VERVlSBaoYM+urxEuG7XL3Lbcz3DW5vgmeq2U5bvClsershAvaHNtswvoEkFKXECvZnM+kcWNM/ujAbmAAS5SKn85hQXIna6klCLdzU6XXOv04oSjXGVPm6Ld0id02N7WpkY1WoEOflp2NajktnOT93b5N6lXSSiI1ETUelucJuxEih2+qLUfcB0I65ejGTiLrtD3uVSP3yKuYy6cNhZFipxJn3JYvXGQNfKVSF3Z5NGiUJA2ida/5tD9mGqGcy3A1zoHZ+nvL7/Gl7KfjZdmCLrK5QAngWIkrGQnDZe/U6HQ8pg65xxZMiwvcyVPvnUx4um6KS2sYGcoa74KurMcKIZp1f79fKu4KJxG1PsYrJWxcxGBl9XLZLqi1paG5ex+2vnXDkdhFdicO9xG0toPzKcmWLM026rQkr8uWqYNlp5k6U+qJaC9UDik3aN52BSA8dS8bVdtcQ5VKOPt8ztO91l3Gg16e5ThKc8VMU3jNRvG9kfAI37qjqGOGZ55O1y1GrhpJY4+4QfQp+L8olgQwSWhrK8yCUOT3443UQf7L7iQam1I7BmupcbaeWAmsuchPFc2TTLRusGNeGZVtjxvlvi8moaSUaEEZgH421VW4mVefZLxK6pS1z032oiqwVbTL8nzlBscViS0s3GA3i8LSsz3rxtfUFyXWjh3xfqEpwrtMF1GzSLkUO0rYH4lY0Saj2Zp777gvld0RS1TOL8zzVeTKLLxfca2S9+PKvWQauurXNdF6jHf0cCy9iIvgOp0lt9UXUVTG2PZUBbB8PrHp0os25W0QgrA00426hPMjfS4zzwkleTrkDWGJxyXN1TmiH/nTQCR3kzjJkjZuqsOkY5wgJ0dtKW3kEFDDlmZvS0tRrwxAI6JIUUAKIlvX8tbRvQ6cTGxxYXQ1G7RqbnhFhJQxe4rMW7I58UygsGZLagSiGvDd2rP8yTKYs9yx3DlKUz1aIdphs6XXyW4rU/2UIm43YXcS21PLCEmboRzve96Pe9gPxuRmgmmyEC7EOqFWu5VKNaN3NoWxMHnEiQ/3g1zTPhNup0kPk0SPT3V3LGycjXcH56KneavzjmqqEj22B0UAOCSqzva+QEKRq5Dr1vNM2ZKnwOUPw+AR5YEBDR+35vo8yKKXGjqeTQsZrlNlynvsSJrhMT0O5PZ8Vb2Uzca1CUcHW8YPa0NVLuR5YPRzKo9mm3TMdXe+CXtYGS5ZdYYXW2yxv1agj3JFZukiEvcmbolmfTb2Hb266JiI2ILMS8xQ8rcj63WVvTA1LV2Eni+xvS1rF7mo2RLPLzDNKsh+W9vI5ZLzV+Iui+5RMyvjEOx7m0HdUMSxvsQ8kWW1jXAlPImq+Sz34wnFd7gsS8KOr84XrayuPrwjIqOk5WPDOsfGEXzxZNRrMt4M3DnYgJHX6w6dvQKzz2IIPdF114212ZJbG77KUsse6hDmN4N/R+/mLU/65mLdEjfZ09SOplabg3oV+WkH49SVqejjZlTNSyTXIEzmcFYPTQ5nMZcDPEMbTUpZw0NCmBwzETs6zuVyJeDUq28Oj45xLS5CSgsrixGjvQCXFe+dPMAIGhHxgdC66oZZ61q8dfB6bU5sdfF0XhPrPtJIGQxXS6oJ67OWJOfIb3Y9fChNf5FPYsaQW7oOaS7LModspnTTBhkSgzpfj2k4XqjazHW80uvyvB5ZeWdK0lHzRzAQ0mCyZpyJGcljKW2vvKNsiTIhby2/9+DjSjlFU0ba9oZHtAtrsN1ZyqupYCn4mIEjw9Y2DxtKLnnbjk6HC7HMPGKww77asxYlKEQLp4jsGIF5rESUReGKiDik69AkcBSCjPdw7taqvGn53Oob83CBeW+RIix23UUuopfOyV5rbIMnJYISiRZ49eqo6f2yZjzPIqKIPhFpF9obWWu0rkr4yw5ry1PWZIaN5lpHr0PpShNRWQTO0cw0EbnfxBO6IAt9JE2HvJ27EbaWFqHvyR1yuy1uIphsrkgwIL5BLooxBWDZWj1dByS/WKcM20UoXp6uEnHS49tSrdZWplqOPKSaTTABXHMbRI4dmOTcTOB3Szq4K3e0XRuU3tCHcYFyGYC1aN2Z57oQL3jopliIrO4gTzvH17sLR5A5Kd3YbtO1yp2SldLiT9KUr1bKNHChB2cHONxhbkGJNHrpOCE4ucYVE7um2/h5dNnvxj5k1qVWk0I/2Os15VMiUl1EjsgDgDwRSZz9krI0UW55ALhIG11c81w6/MZTTQyndrhIU+dTJsa0h+LFdB60OrodFbTxPBJlWGR7OZEoHii3o+ryk1pZ3eIi5rflFk1zJ8YQUuWIVUkK5urQkzy9CGgUMWAkDvZLl3cPOJohDq+vcueO22xNwWMLC66zMttmleAHe78wOxxD7jApqoIadCWGHeGgGnWiCpCERlieEwl8KLZitN7T/TbylkTqTC15y9U8rOweudvi1QJHGle39OBm+2DGd5AL2RTHdbrwkS6XOO/mJdoy7bLbrrrvlzZqSEveWDVT5y92QmDulP6gRKMX8xoGMnWYOmYM1936LjJmFgXB2j/q4zFXWHiJx5WfMasjfhhGUmWZ0wYNlYJU0eSA3cERDBmOXEcy5+Kyy5zF6O0Uayz3GNUVE07T8Z1nbv0a5kpQmx07unVz8/bJMbivTdnkFI3kVu5ut8FKQjjX0f1WYzuirM8FFq9aO1hQbsRduPvBSrr9vl+cBldwry1xWvndXhCTpavHnKUgqn/xZY+P7vVNkKT7YaXzS0NAe0VfkRRsdXZ64kWSrLfGRmVPVH7WzwgXRCuiOzn92QokcOjChOlsryhEUWKVwm7KkCJnHabLzsm87HpTJN7LDLkdwdH8FEXxaUr6tdFQ7uYsHsPzoPTFKa2JKh9WITO2Qbgmt5YrI6l42/ny4UqrJDpoSCb2J/jYrUIu4qwJHD0lEsYao08kAi26lL6SOGIYLsEb3AIPLZauDewUNBXZna3J6qlbPpLrLukI8XbHd4J1oRGBC8xFQWDBcufTeigsKM8wioshlDv+Uq0GK97Y4lqxu2UdIzhWTqWpBT2veicEiVJrPFcUwUWtXi3OlIKe4Kwl4jhnDNPDswOGi6q+MOO1ltqliaqbK1sqSNDq3TpmS/LozcXflssEoS6HwtxsBwkcDg1w2IcTlMAYLwp8HGCTMqzxaDPhaHBdRzWexlxv3Pk7sgxr9HaFLyK1Sre4O4LRN18t68TxLPLQ0Ef3puebSpAbpzuuhtygEQ3bYxkoOWIdMCqCD0K0KiPpYt8xG4MZX8LXW5as3ORElV6SnfGNdzeEBYCAHC2ouJNwd2+hlOZlBR2SbM67+QJAC3o9yGzb+UJnKD3aViN+42+yUw7azcUDdeGrSrshaG57VI0J51jbu/joJVdHdh+aHL3yNjkGaP+6P287l8MOdrbK7CAhSlleIddxNDlCXwgLzD40E874YSCt0uuyYPa1XRT85oYbdBIrt3wtYvQoxhOBNJuQSjGf5US92I1mn7FpkiA3C7dsYgwyYUf1rXBM9kUPSOpCZ7fGCirNqThuqY3UuT9rO3VFLtLJbpLiLuYtdbCvXH1zY6ZoGKQUqTbWcYs9O9OyCyiauwQKsuDK8HbR1RbnhEtBoujqVumrVLXgrDft3j/RntPDQQ53nBVsV21G9IeFsTgERTlsp02rg45UaDAws67p7/X0uK+Hk5tkaDUta4muBbtsy2S7hSudGEANn0pSStt+NKlpya/aVtXKcstaLr1GKkAseOnEGz0DoCiCBDClELjXmJkabuLXhaL2K/Rw2E8Fxt6ZA3bNKXQdOEnVKlGuDlOfM1hHbuilbE9HJF86F2d9vm6ro0QP+02gGnez3hL3e+0hyNkVDBAFCfNDxQusG2DeO0ftLyoI7knX0nCZU9miFkZNv4oM6+4CluJ5zg3EITylebLsaUNtgjTt9oEedk5zps7TlaKHgGgzbOK4QseVpnM607qti1bAa21xDww6BMSLKbszsLzzpSQpExpPPFISJ6z2vaJosOVkVgy3CQw39939fQhqSUKYbsFrMs+H59pTFi16NyxmvaOR3XBJUcXwuGQkav2WGKariwXrbvf8QoNZMhKu+6uDcfuFuj0IB6+4BHvOP+z95ZHdoja5kXwXoPpNateb7aKQLMqm4cVhnZu+MCaovL1ZqxC7DWTcWwnMrgYHlonYzvX7vjtNV5s8u0hC9EuATRQVh17PN4pH3CKBrtJiQxhTXlCBuxxKlBQO8G6/D7RaQCdZaablmga1NLDwiWGYtw9v8/ui11uff/nvXOZf1/+v/cj//D3+2/vfxwsX3/Y+P/b6/K+b9suHt8aNgWHPNxtt1oevn///83uNj//sm8VZzfj8W5L5vfXQfXtr1tnh/KeXfwggEH1/q/kVI/DHm7a2a+dXIw+t4CLq8mw28/UOEliHfYI/oW+//y9PcdVzjCsAAA== -->
