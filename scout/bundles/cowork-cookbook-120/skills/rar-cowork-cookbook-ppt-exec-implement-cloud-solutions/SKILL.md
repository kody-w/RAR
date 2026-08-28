---
name: "rar-cowork-cookbook-ppt-exec-implement-cloud-solutions"
description: "Generates an executive-ready PowerPoint deck on implement cloud solutions status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_cloud_solutions", "rar_sha256": "4e5ec5fe565f3f04bf769f8d99f5da19d320fb13f888573527982b4c00eca15e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_cloud_solutions_agent.py` and embedded as the fenced Python below (sha256 4e5ec5fe565f3f04…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_cloud_solutions_agent.py` first:

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
    "version": '2.0.0',
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
