---
name: "rar-cowork-cookbook-d365-administer-to-operate-administer-system-features"
description: "A Dynamics 365 F&SCM expert scoped to the Administer system features area (a level-2 subdomain of Administer to operate) - covers 20 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_administer_to_operate_administer_system_features", "rar_sha256": "ead63756c45a93b06d1ac5a000f201b9a11b92edb0771e49429adb63ddc1ed80", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_administer_to_operate_administer_system_features`. The original RAPP
agent is preserved byte-for-byte in `d365_administer_to_operate_administer_system_features_agent.py` and in the RCI capsule.

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

D365 Administer system features Expert — A Dynamics 365 F&SCM expert scoped to the Administer system features area (a level-2 subdomain of Administer to operate) - covers 20 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_administer_to_operate_administer_system_features_agent.py` and embedded as the fenced Python below (sha256 ead63756c45a93b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_administer_to_operate_administer_system_features_agent.py` first:

```bash
python3 d365_administer_to_operate_administer_system_features_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_administer_to_operate_administer_system_features_agent.py   # or on stdin
python3 d365_administer_to_operate_administer_system_features_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Administer system features Expert — A Dynamics 365 F&SCM expert scoped to the Administer system features area (a level-2 subdomain of Administer to operate) - covers 20 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_administer_to_operate_administer_system_features',
    "version": '2.0.1',
    "display_name": 'D365 Administer system features Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Administer system features area (a level-2 subdomain of Administer to operate) - covers 20 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-administer-to-operate-administer-system-features',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '199f030de51c9810',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'administer-to-operate/d365-administer-to-operate-administer-system-features', 'uses_skills': {'custom': ['d365-administer-to-operate-administer-system-features'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365AdministerToOperateAdministerSystemFeatures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AdministerToOperateAdministerSystemFeatures'
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
    print(D365AdministerToOperateAdministerSystemFeatures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
