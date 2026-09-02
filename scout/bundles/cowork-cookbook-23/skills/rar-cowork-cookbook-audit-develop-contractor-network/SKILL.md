---
name: "rar-cowork-cookbook-audit-develop-contractor-network"
description: "Audits develop contractor network records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_contractor_network", "rar_sha256": "049ddacf8d59d0f22e349662e7ef7e3aba9a5b11d7aec9c4867fcbfc84dec161", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_develop_contractor_network_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-develop-contractor-network:c25f571d930bd293999bb93ede9ff506ad52361bde3ef0666838bad14c3eaf67", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_develop_contractor_network`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_develop_contractor_network_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
