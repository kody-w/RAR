---
name: "rar-cowork-cookbook-report-manage-service-accounts-and-certificates"
description: "Builds a structured summary report of manage service accounts and certificates activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_service_accounts_and_certificates", "rar_sha256": "dd351038ba67c4643304794fe3d6ce2fd3114600e40c5c349a18e0d455402aa7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_service_accounts_and_certificates`. The original RAPP
agent is preserved byte-for-byte in `report_manage_service_accounts_and_certificates_agent.py` and in the RCI capsule.

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
