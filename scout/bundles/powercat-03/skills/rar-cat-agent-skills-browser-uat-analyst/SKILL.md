---
name: "rar-cat-agent-skills-browser-uat-analyst"
description: "Run evidence-driven UAT on any browser-based app \u2014 Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app \u2014 with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/browser_uat_analyst", "rar_sha256": "04643dc07fd9ae22b95b57a4dc006100bfe3cbe9f2336dad00061f7953b55223", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Al Macey", "tags": ["testing", "uat", "playwright", "quality", "copilot_studio", "power_platform", "automation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/browser_uat_analyst`. The original RAPP
agent is preserved byte-for-byte in `browser_uat_analyst_agent.py` and in the RCI capsule.

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

Browser UAT Analyst — Run evidence-driven UAT on any browser-based app — Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app — with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#browser-uat-analyst
  Upstream author: Al Macey
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `browser_uat_analyst_agent.py` and embedded as the fenced Python below (sha256 04643dc07fd9ae22…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `browser_uat_analyst_agent.py` first:

```bash
python3 browser_uat_analyst_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 browser_uat_analyst_agent.py   # or on stdin
python3 browser_uat_analyst_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Browser UAT Analyst — Run evidence-driven UAT on any browser-based app — Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app — with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#browser-uat-analyst
  Upstream author: Al Macey
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/browser_uat_analyst',
    "version": '3.0.2',
    "display_name": 'Browser UAT Analyst',
    "description": 'Run evidence-driven UAT on any browser-based app — Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app — with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config.',
    "author": 'Al Macey',
    "tags": ['testing', 'uat', 'playwright', 'quality', 'copilot_studio', 'power_platform', 'automation'],
    "category": 'general',
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
        "upstream_slug": 'browser-uat-analyst',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#browser-uat-analyst',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '09f0ebd3b94914ed',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.571, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:quality', 'tag:testing'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class BrowserUatAnalyst(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BrowserUatAnalyst'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(BrowserUatAnalyst().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
