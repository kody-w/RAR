---
name: "rar-cowork-cookbook-ppt-exec-plan-software-releases"
description: "Generates an executive-ready PowerPoint deck on plan software releases status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_software_releases", "rar_sha256": "e877c487bc8aa89c47d1db3573f4f533205ecc055f929ef5cb910487850d431e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_software_releases`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_software_releases_agent.py` and in the RCI capsule.

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

Plan software releases Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan software releases status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_software_releases_agent.py` and embedded as the fenced Python below (sha256 e877c487bc8aa89c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_software_releases_agent.py` first:

```bash
python3 ppt_exec_plan_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_software_releases_agent.py   # or on stdin
python3 ppt_exec_plan_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan software releases Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan software releases status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_software_releases',
    "version": '2.0.1',
    "display_name": 'Plan software releases Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on plan software releases status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-plan-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ffa5523311f4c1b0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/plan-software-releases'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-plan-software-releases', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecPlanSoftwareReleases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanSoftwareReleases'
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
    print(PptExecPlanSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
