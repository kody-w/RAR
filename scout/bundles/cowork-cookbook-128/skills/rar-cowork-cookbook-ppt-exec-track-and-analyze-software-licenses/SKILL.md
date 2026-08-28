---
name: "rar-cowork-cookbook-ppt-exec-track-and-analyze-software-licenses"
description: "Generates an executive-ready PowerPoint deck on track and analyze software licenses status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_track_and_analyze_software_licenses", "rar_sha256": "f1eb2b11b2407167c815feab9dee9880d40d3021ea21b28c542e7c9bde83e3dd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_track_and_analyze_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_track_and_analyze_software_licenses_agent.py` and in the RCI capsule.

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

Track and analyze software licenses Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on track and analyze software licenses status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-track-and-analyze-software-licenses
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_track_and_analyze_software_licenses_agent.py` and embedded as the fenced Python below (sha256 f1eb2b11b2407167…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_track_and_analyze_software_licenses_agent.py` first:

```bash
python3 ppt_exec_track_and_analyze_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_track_and_analyze_software_licenses_agent.py   # or on stdin
python3 ppt_exec_track_and_analyze_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track and analyze software licenses Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on track and analyze software licenses status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-track-and-analyze-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_track_and_analyze_software_licenses',
    "version": '2.0.1',
    "display_name": 'Track and analyze software licenses Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on track and analyze software licenses status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-track-and-analyze-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-track-and-analyze-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '107ea81667e4aae5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/track-and-analyze-software-licenses'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-track-and-analyze-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecTrackAndAnalyzeSoftwareLicenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecTrackAndAnalyzeSoftwareLicenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(PptExecTrackAndAnalyzeSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
