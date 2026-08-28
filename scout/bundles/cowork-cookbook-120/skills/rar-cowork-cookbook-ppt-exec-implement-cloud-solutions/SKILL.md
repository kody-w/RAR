---
name: "rar-cowork-cookbook-ppt-exec-implement-cloud-solutions"
description: "Generates an executive-ready PowerPoint deck on implement cloud solutions status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_cloud_solutions", "rar_sha256": "7071cf0dc6f28a168255a9be740ff3883ee6ccb0a7a2714369967e7a61ad65ae", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_implement_cloud_solutions`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_implement_cloud_solutions_agent.py` and in the RCI capsule.

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

Implement cloud solutions Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on implement cloud solutions status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-cloud-solutions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_cloud_solutions_agent.py` and embedded as the fenced Python below (sha256 7071cf0dc6f28a16…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_cloud_solutions_agent.py` first:

```bash
python3 ppt_exec_implement_cloud_solutions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_implement_cloud_solutions_agent.py   # or on stdin
python3 ppt_exec_implement_cloud_solutions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement cloud solutions Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on implement cloud solutions status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-cloud-solutions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_implement_cloud_solutions',
    "version": '2.0.1',
    "display_name": 'Implement cloud solutions Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on implement cloud solutions status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-implement-cloud-solutions',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-implement-cloud-solutions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8aab46af56fbd3b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-cloud-solutions'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-implement-cloud-solutions', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecImplementCloudSolutions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecImplementCloudSolutions'
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
    print(PptExecImplementCloudSolutions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
