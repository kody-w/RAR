---
name: "rar-cowork-cookbook-report-configure-and-manage-microsoft-teams-integrations"
description: "Builds a structured summary report of configure and manage Microsoft Teams integrations activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_microsoft_teams_integrations", "rar_sha256": "bac9c98b973f564185040a2e053dea81f73a886ba75de4cbfdbee78621e7c372", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_configure_and_manage_microsoft_teams_integrations_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-configure-and-manage-microsoft-teams-integrations:85638dd959de1049d9b363c1bdcb43aadc3ac1a2e8a83a1406f0b4804ad14526", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_configure_and_manage_microsoft_teams_integrations`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_configure_and_manage_microsoft_teams_integrations_agent.py` is
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

Configure and manage Microsoft Teams integrations Summary Report — Builds a structured summary report of configure and manage Microsoft Teams integrations activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-microsoft-teams-integrations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_and_manage_microsoft_teams_integrations_agent.py` and embedded as the fenced Python below (sha256 bac9c98b973f5641…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_and_manage_microsoft_teams_integrations_agent.py` first:

```bash
python3 report_configure_and_manage_microsoft_teams_integrations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_configure_and_manage_microsoft_teams_integrations_agent.py   # or on stdin
python3 report_configure_and_manage_microsoft_teams_integrations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage Microsoft Teams integrations Summary Report — Builds a structured summary report of configure and manage Microsoft Teams integrations activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-microsoft-teams-integrations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_configure_and_manage_microsoft_teams_integrations',
    "version": '2.0.0',
    "display_name": 'Configure and manage Microsoft Teams integrations Summary Report',
    "description": 'Builds a structured summary report of configure and manage Microsoft Teams integrations activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-configure-and-manage-microsoft-teams-integrations',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-configure-and-manage-microsoft-teams-integrations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '727298e0809e4fea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-microsoft-teams-integrations'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-configure-and-manage-microsoft-teams-integrations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportConfigureAndManageMicrosoftTeamsIntegrations(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConfigureAndManageMicrosoftTeamsIntegrations'
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
    print(ReportConfigureAndManageMicrosoftTeamsIntegrations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
