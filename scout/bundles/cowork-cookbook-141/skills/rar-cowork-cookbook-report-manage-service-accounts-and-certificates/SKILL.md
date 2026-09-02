---
name: "rar-cowork-cookbook-report-manage-service-accounts-and-certificates"
description: "Builds a structured summary report of manage service accounts and certificates activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_service_accounts_and_certificates", "rar_sha256": "dd351038ba67c4643304794fe3d6ce2fd3114600e40c5c349a18e0d455402aa7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_manage_service_accounts_and_certificates_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-manage-service-accounts-and-certificates:e69ac05b48dd62148eb3ca0602599bfe4bcceaa78fdf5530bcdc7138dacfb4b8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_manage_service_accounts_and_certificates`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_manage_service_accounts_and_certificates_agent.py` is
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

Manage service accounts and certificates Summary Report — Builds a structured summary report of manage service accounts and certificates activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-service-accounts-and-certificates
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_service_accounts_and_certificates_agent.py` and embedded as the fenced Python below (sha256 dd351038ba67c464…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_service_accounts_and_certificates_agent.py` first:

```bash
python3 report_manage_service_accounts_and_certificates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_service_accounts_and_certificates_agent.py   # or on stdin
python3 report_manage_service_accounts_and_certificates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service accounts and certificates Summary Report — Builds a structured summary report of manage service accounts and certificates activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-service-accounts-and-certificates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_service_accounts_and_certificates',
    "version": '2.0.0',
    "display_name": 'Manage service accounts and certificates Summary Report',
    "description": 'Builds a structured summary report of manage service accounts and certificates activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-service-accounts-and-certificates',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-service-accounts-and-certificates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '05e69ae41a3f0d9f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-service-accounts-and-certificates'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-manage-service-accounts-and-certificates', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportManageServiceAccountsAndCertificates(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageServiceAccountsAndCertificates'
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
    print(ReportManageServiceAccountsAndCertificates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
