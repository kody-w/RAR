---
name: "rar-cowork-cookbook-ppt-exec-track-and-analyze-software-licenses"
description: "Generates an executive-ready PowerPoint deck on track and analyze software licenses status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_track_and_analyze_software_licenses", "rar_sha256": "3d242b53e402e02b5b8e911b8d6f9334e220afc1eb16d663897b1dbfdf9277c1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_track_and_analyze_software_licenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-track-and-analyze-software-licenses:a04593820b9d2e0d9162a2da9d4b704373f0bcb23a2a1752680fed9cbb5318fb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_track_and_analyze_software_licenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_track_and_analyze_software_licenses_agent.py` is
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
