---
name: "rar-cowork-cookbook-d365-acquire-to-dispose-acquire-assets"
description: "A Dynamics 365 F&SCM expert scoped to the Acquire assets area (a level-2 subdomain of Acquire to dispose) - covers 12 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_acquire_to_dispose_acquire_assets", "rar_sha256": "1e307b2c63c2a9598b526ff5b50f9a9db782ddb6348bdda29e7331fec4b1cfcb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_acquire_to_dispose_acquire_assets`. The original RAPP
agent is preserved byte-for-byte in `d365_acquire_to_dispose_acquire_assets_agent.py` and in the RCI capsule.

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

D365 Acquire assets Expert — A Dynamics 365 F&SCM expert scoped to the Acquire assets area (a level-2 subdomain of Acquire to dispose) - covers 12 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_acquire_to_dispose_acquire_assets_agent.py` and embedded as the fenced Python below (sha256 1e307b2c63c2a959…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_acquire_to_dispose_acquire_assets_agent.py` first:

```bash
python3 d365_acquire_to_dispose_acquire_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_acquire_to_dispose_acquire_assets_agent.py   # or on stdin
python3 d365_acquire_to_dispose_acquire_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Acquire assets Expert — A Dynamics 365 F&SCM expert scoped to the Acquire assets area (a level-2 subdomain of Acquire to dispose) - covers 12 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_acquire_to_dispose_acquire_assets',
    "version": '2.0.1',
    "display_name": 'D365 Acquire assets Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Acquire assets area (a level-2 subdomain of Acquire to dispose) - covers 12 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-acquire-to-dispose-acquire-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '87f438f8ab12d9b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'acquire-to-dispose/d365-acquire-to-dispose-acquire-assets', 'uses_skills': {'custom': ['d365-acquire-to-dispose-acquire-assets'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365AcquireToDisposeAcquireAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AcquireToDisposeAcquireAssets'
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
    print(D365AcquireToDisposeAcquireAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
