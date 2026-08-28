---
name: "rar-cowork-cookbook-audit-develop-prototypes"
description: "Audits develop prototypes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_prototypes", "rar_sha256": "b99c89b3461557412123261961ed63139352d3d3260bd7e3d2ff98c08b232752", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_prototypes`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_prototypes_agent.py` and in the RCI capsule.

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

Develop prototypes Completeness Audit — Audits develop prototypes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-prototypes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_prototypes_agent.py` and embedded as the fenced Python below (sha256 b99c89b346155741…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_prototypes_agent.py` first:

```bash
python3 audit_develop_prototypes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_prototypes_agent.py   # or on stdin
python3 audit_develop_prototypes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop prototypes Completeness Audit — Audits develop prototypes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-prototypes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_prototypes',
    "version": '2.0.0',
    "display_name": 'Develop prototypes Completeness Audit',
    "description": 'Audits develop prototypes records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-develop-prototypes',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-prototypes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b73750aba529c39',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/develop-prototypes'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-develop-prototypes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditDevelopPrototypes(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopPrototypes'
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
    print(AuditDevelopPrototypes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
