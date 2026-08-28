---
name: "rar-cowork-cookbook-demo-data-configure-and-maintain-cloud-based-printing"
description: "Generates and creates realistic demo records for configure and maintain cloud-based printing in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_maintain_cloud_based_printing", "rar_sha256": "e4456c6e51b07f0c8c73ad505286edc5a26d6cc7cd57fec3f96c9fe74c564255", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_maintain_cloud_based_printing_agent.py` and embedded as the fenced Python below (sha256 e4456c6e51b07f0c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_maintain_cloud_based_printing_agent.py` first:

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
    "version": '2.0.0',
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
