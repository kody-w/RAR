---
name: "rar-cowork-cookbook-report-configure-and-manage-mobile-apps-and-devices"
description: "Builds a structured summary report of configure and manage mobile apps and devices activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_mobile_apps_and_devices", "rar_sha256": "fe30851f19d84584b5b56db8af7fcb7d08e75a31b180f8670b91ef079d050232", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_and_manage_mobile_apps_and_devices_agent.py` and embedded as the fenced Python below (sha256 fe30851f19d84584…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_and_manage_mobile_apps_and_devices_agent.py` first:

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
    "version": '2.0.1',
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
