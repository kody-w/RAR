---
name: "rar-cowork-cookbook-demo-data-configure-and-maintain-cloud-based-printing"
description: "Generates and creates realistic demo records for configure and maintain cloud-based printing in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_maintain_cloud_based_printing", "rar_sha256": "884b0fb02d1041d5e1182452defbdaa328fb94b6023dfaeac71873752f985647", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_configure_and_maintain_cloud_based_printing`. The original RAPP
agent is preserved byte-for-byte in `demo_data_configure_and_maintain_cloud_based_printing_agent.py` and in the RCI capsule.

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

Configure and maintain cloud-based printing Demo Data Generator — Generates and creates realistic demo records for configure and maintain cloud-based printing in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-maintain-cloud-based-printing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_maintain_cloud_based_printing_agent.py` and embedded as the fenced Python below (sha256 884b0fb02d1041d5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_maintain_cloud_based_printing_agent.py` first:

```bash
python3 demo_data_configure_and_maintain_cloud_based_printing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_configure_and_maintain_cloud_based_printing_agent.py   # or on stdin
python3 demo_data_configure_and_maintain_cloud_based_printing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and maintain cloud-based printing Demo Data Generator — Generates and creates realistic demo records for configure and maintain cloud-based printing in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-maintain-cloud-based-printing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_configure_and_maintain_cloud_based_printing',
    "version": '2.0.1',
    "display_name": 'Configure and maintain cloud-based printing Demo Data Generator',
    "description": 'Generates and creates realistic demo records for configure and maintain cloud-based printing in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-configure-and-maintain-cloud-based-printing',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-configure-and-maintain-cloud-based-printing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1e846f414e9978dd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-maintain-cloud-based-printing'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-configure-and-maintain-cloud-based-printing', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataConfigureAndMaintainCloudBasedPrinting(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConfigureAndMaintainCloudBasedPrinting'
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
    print(DemoDataConfigureAndMaintainCloudBasedPrinting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
