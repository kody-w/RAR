---
name: "rar-cowork-cookbook-report-configure-and-manage-microsoft-teams-integrations"
description: "Builds a structured summary report of configure and manage Microsoft Teams integrations activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_microsoft_teams_integrations", "rar_sha256": "ad6bf1e4cfe1a75ff89af435cd2886d171aef4e7c62d28421f0aac5156d03587", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_configure_and_manage_microsoft_teams_integrations`. The original RAPP
agent is preserved byte-for-byte in `report_configure_and_manage_microsoft_teams_integrations_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_and_manage_microsoft_teams_integrations_agent.py` and embedded as the fenced Python below (sha256 ad6bf1e4cfe1a75f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_and_manage_microsoft_teams_integrations_agent.py` first:

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
    "version": '2.0.1',
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
