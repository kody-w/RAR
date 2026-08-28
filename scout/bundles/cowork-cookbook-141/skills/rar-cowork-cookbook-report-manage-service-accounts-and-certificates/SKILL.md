---
name: "rar-cowork-cookbook-report-manage-service-accounts-and-certificates"
description: "Builds a structured summary report of manage service accounts and certificates activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_service_accounts_and_certificates", "rar_sha256": "8975cf3460043643d4fcbb71bbe5425cbe587ee520bfe95a856f8a7f5ae9bd69", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_service_accounts_and_certificates_agent.py` and embedded as the fenced Python below (sha256 8975cf3460043643…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_service_accounts_and_certificates_agent.py` first:

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
    "version": '2.0.1',
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
