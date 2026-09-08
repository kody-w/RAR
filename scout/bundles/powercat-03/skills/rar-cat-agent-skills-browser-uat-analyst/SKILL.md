---
name: "rar-cat-agent-skills-browser-uat-analyst"
description: "Run evidence-driven UAT on any browser-based app \u2014 Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app \u2014 with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/browser_uat_analyst", "rar_sha256": "04643dc07fd9ae22b95b57a4dc006100bfe3cbe9f2336dad00061f7953b55223", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Al Macey", "tags": ["testing", "uat", "playwright", "quality", "copilot_studio", "power_platform", "automation"]}
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
