---
name: "rar-cowork-cookbook-ppt-exec-track-and-analyze-software-licenses"
description: "Generates an executive-ready PowerPoint deck on track and analyze software licenses status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_track_and_analyze_software_licenses", "rar_sha256": "3d242b53e402e02b5b8e911b8d6f9334e220afc1eb16d663897b1dbfdf9277c1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_track_and_analyze_software_licenses_agent.py` and embedded as the fenced Python below (sha256 3d242b53e402e02b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_track_and_analyze_software_licenses_agent.py` first:

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
    "version": '2.0.0',
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
