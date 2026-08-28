---
name: "rar-cowork-cookbook-audit-develop-contractor-network"
description: "Audits develop contractor network records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_contractor_network", "rar_sha256": "049ddacf8d59d0f22e349662e7ef7e3aba9a5b11d7aec9c4867fcbfc84dec161", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_contractor_network`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_contractor_network_agent.py` and in the RCI capsule.

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

Develop contractor network Completeness Audit — Audits develop contractor network records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-contractor-network
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_contractor_network_agent.py` and embedded as the fenced Python below (sha256 049ddacf8d59d0f2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_contractor_network_agent.py` first:

```bash
python3 audit_develop_contractor_network_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_contractor_network_agent.py   # or on stdin
python3 audit_develop_contractor_network_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop contractor network Completeness Audit — Audits develop contractor network records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-contractor-network
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_contractor_network',
    "version": '2.0.0',
    "display_name": 'Develop contractor network Completeness Audit',
    "description": 'Audits develop contractor network records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-develop-contractor-network',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-contractor-network',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ca251399bfa49239',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-contractor-network'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-develop-contractor-network', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDevelopContractorNetwork(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopContractorNetwork'
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
    print(AuditDevelopContractorNetwork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
