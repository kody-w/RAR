---
name: "rar-cowork-cookbook-report-configure-and-manage-mobile-apps-and-devices"
description: "Builds a structured summary report of configure and manage mobile apps and devices activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_mobile_apps_and_devices", "rar_sha256": "e4cdb7a2e91aa33dbf40b6393785bb6e5e9c8b13f099c5bf55e3b1bd4a690e89", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_configure_and_manage_mobile_apps_and_devices`. The original RAPP
agent is preserved byte-for-byte in `report_configure_and_manage_mobile_apps_and_devices_agent.py` and in the RCI capsule.

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

Configure and manage mobile apps and devices Summary Report — Builds a structured summary report of configure and manage mobile apps and devices activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-mobile-apps-and-devices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_and_manage_mobile_apps_and_devices_agent.py` and embedded as the fenced Python below (sha256 e4cdb7a2e91aa33d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_and_manage_mobile_apps_and_devices_agent.py` first:

```bash
python3 report_configure_and_manage_mobile_apps_and_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_configure_and_manage_mobile_apps_and_devices_agent.py   # or on stdin
python3 report_configure_and_manage_mobile_apps_and_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage mobile apps and devices Summary Report — Builds a structured summary report of configure and manage mobile apps and devices activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-mobile-apps-and-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_configure_and_manage_mobile_apps_and_devices',
    "version": '2.0.0',
    "display_name": 'Configure and manage mobile apps and devices Summary Report',
    "description": 'Builds a structured summary report of configure and manage mobile apps and devices activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-configure-and-manage-mobile-apps-and-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-configure-and-manage-mobile-apps-and-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd5f917aad3b3fbda',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-mobile-apps-and-devices'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-configure-and-manage-mobile-apps-and-devices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportConfigureAndManageMobileAppsAndDevices(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConfigureAndManageMobileAppsAndDevices'
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
    print(ReportConfigureAndManageMobileAppsAndDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
