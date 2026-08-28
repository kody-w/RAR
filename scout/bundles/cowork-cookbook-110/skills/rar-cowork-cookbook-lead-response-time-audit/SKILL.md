---
name: "rar-cowork-cookbook-lead-response-time-audit"
description: "Measures how long leads wait before someone first works them, and highlights the leads that are still sitting untouched."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/lead_response_time_audit", "rar_sha256": "8122afe519f09d14fe79b5b1b4e32690c7c59cb5c1b95e608dfd0ddb4c3fe614", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/lead_response_time_audit`. The original RAPP
agent is preserved byte-for-byte in `lead_response_time_audit_agent.py` and in the RCI capsule.

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

Lead Response Time Audit — Measures how long leads wait before someone first works them, and highlights the leads that are still sitting untouched.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/lead-response-time-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lead_response_time_audit_agent.py` and embedded as the fenced Python below (sha256 8122afe519f09d14…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lead_response_time_audit_agent.py` first:

```bash
python3 lead_response_time_audit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 lead_response_time_audit_agent.py   # or on stdin
python3 lead_response_time_audit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Lead Response Time Audit — Measures how long leads wait before someone first works them, and highlights the leads that are still sitting untouched.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/lead-response-time-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/lead_response_time_audit',
    "version": '2.0.0',
    "display_name": 'Lead Response Time Audit',
    "description": 'Measures how long leads wait before someone first works them, and highlights the leads that are still sitting untouched.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'lead-response-time-audit',
        "upstream_url": 'https://coworkcookbook.com/recipes/lead-response-time-audit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9cbb47434cf8126e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/manage-lead-identification-process'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/lead-response-time-audit', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.429, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class LeadResponseTimeAudit(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LeadResponseTimeAudit'
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
    print(LeadResponseTimeAudit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
