---
name: "rar-cowork-cookbook-configure-process-inventory-movements"
description: "Applies a bulk configuration change to process inventory movements from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_inventory_movements", "rar_sha256": "3b08465c39cd80384fc8be56e7cd75896c135f8726348a3dcae734d4a47ba757", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_process_inventory_movements`. The original RAPP
agent is preserved byte-for-byte in `configure_process_inventory_movements_agent.py` and in the RCI capsule.

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

Process inventory movements Configuration Bulk Setup — Applies a bulk configuration change to process inventory movements from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-inventory-movements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_process_inventory_movements_agent.py` and embedded as the fenced Python below (sha256 3b08465c39cd8038…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_process_inventory_movements_agent.py` first:

```bash
python3 configure_process_inventory_movements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_process_inventory_movements_agent.py   # or on stdin
python3 configure_process_inventory_movements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process inventory movements Configuration Bulk Setup — Applies a bulk configuration change to process inventory movements from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-inventory-movements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_process_inventory_movements',
    "version": '2.0.1',
    "display_name": 'Process inventory movements Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to process inventory movements from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-process-inventory-movements',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-process-inventory-movements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '32335170b0634c57',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/process-inventory-movements'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-process-inventory-movements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureProcessInventoryMovements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureProcessInventoryMovements'
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
    print(ConfigureProcessInventoryMovements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abOjRpb2X2HufHB5qLrsIFWHI0a7QAgQq4TLUcUOYl8F+PV/fxNJ95Y97u5pT0zEUFFxgcw8+3nOyUS/vlhtE+bVy+cXxbMyaGclSRR6FWRlLrTKb3kVgz95bIP/kJNnTRXZbZNX9cvHF9ernSoqmijPwPJFUSSRV0MWZLfJfa4fBW1lTcOQE1pZ4EFNDhVV7nh1DUVZ52WA0ACleeel4L6G/CpPAWMwVrQNtOkdL4H8KPE+QreoCaHOSiL3QW+SrsqTxLacGKrbosir5hWI5PVWWiRe/fL5518+vkTg/uXzry9OYtXg1cvqKZMnPYRg32Q4vokASCRAUjC3GIBZMvBceJWfVyl45Xo+9Hz6UHuJ/xH6j/+Ib1YV1D9+/pJBz+vLy/RPbjOoCSeNrbrxXMixCsuOkqgZXqFFcrOGGqq8pq2yyWA1sGoWvD5WfqeUF9BP09iHB5PXwGs+fHnJgQh3I3x5+RHKK8Cvaqf714lK8eHH1yS/edWHH7/TqVv76jnNRAxI/fr1+fwkCyZ+nxr5d64/AaoP79rel5ffKTddD7knPcHKl9drHmUfHoSBb4FBrczxPvz4j8g6oefESVQ3/xLdnx+EQ89ygU5PwX/8eDfyLxD8VOid5j9mWwC3/hVNwPQ3dh+hp6H+Ee27/f8L6STKQC68Wfzvkvt7C+CfoJ//oW7/bMFHyP/ysvaSqAPRYSfeZ+jXr4q0Wf38g/v95Q+//AZI/7dklLytnDuFr6mVRb5XN1+//vxDfX/9wy8//9AWINY8K/3aVsnfo/n37Hrn8wcLPmd9+ONawF/L4iy/ZdB7pEO/5sW/Vb+9QvqEAN/f15+h3+fLdMHQpMQb04cJfpczNZD1d3b88eU3gBIZ0KZ17sMgy//936Fj5FR5nfsNpDg5QCLg4CZKvUl4NYwAdtX33K48YNc6AoZ9zgPxP3l4kjj3oW//6dzx85PzxE/kDRO9r08U/PqOgl/fUfDbK6QC4nkVBVFmJZC8kKQvmRWAsYlxUXm1V3UAUuyh8T4BMPo03QDMhL79S/S/3km9FsO3O4pGD5ySV+yEUXWbeK+TnkboZU+tHIDIXu85LeCS5I71wOT6I9C/zpMOYNxkkzqOkgRyowoYYEL1O0K32eeJ2Ldv32yrDr9kD1AloEfdqBEw4V0c6NMnoJufREHYfMk8J8yhH3797Qfo/0H/bNWd+MRDAhD/9AqQkFNEAQJZ1j4Ky+RiACF3r/z629PCgEwGCh3wYeRPhWtaDKI09tw3cyv7xSecoiHbA2YGJk6nMgOQGoqaV4j1oXd5AdNpaMLyMK8byPUKL3O9zBkAVQuo827JLG+gGoRi7Q8fobb27ly/2ZV1FzEF6W4136DjSgKVI0+mglk9KwlYnGcRMP97MDzeAyLVDzW0fCPxCglTXEKFVVlFWFlPHr718AuoGG/LAXELyrzbl2wqlPfouCfJwzxgErCM83Tpp8nnoKinABHc+o33fY411Tf1XueqL1n9TACrmlzhgKgDTIMWFG5QFv72DKk6zNvEvdsPSDpRenrBfXrlHoPSP2kVVn9oL5ZTx6EAPCmgLy2OYiT0f9+NTBosdjt5s1uomzW0EVT58rDs1EZNHnh0XqAlgEB4PbLoe5vwBjJvWPslSyIQJtXwt8fMuz+ecx74BfLeBWgh3+mDYACWnejeY3WKvaq6G+RL9gbqH4F17ggGVACJDQJ/Mskbw2n0TdIQZO/0/L3A331buZPqIB6horUTECu+57l3IzRhNeXb0xkgcL0p925h5IR/0AoC1IHRAX0ICBEBqwPgv5tOyIGaINXuXnifHk1tE5DCbR0gLehTvVfIACkzhU0N8hT0PtMcYIUf7qSg1AM2BiK+W7gOreIhzNTaPgW0Jl/kKYjk33vgOfg9yO+yTOIDqhbwPbDlbUJe1+sfnn2X8+krIGw6peV90R/d/dQV+n31+duX7C7jO9iDbE+mwv0740Agy9L6HnITWNUAcFLvGUAgEu41+vVRZh91/F2Wz3/q5z/8tZb/Xji1P3ruMxQ2TVF/RpBHsXurda8AKhAQI1Hh1d/r3qdnvn16z7dP7/n2B+IPW32G/pqAfyDxjOzPEPaKvqLTEB853hS6zwvYY/VpeflETqNfMtn77uhnNExomwyg0L6XnrcpoP4ElRdMkx+lqJ4q2A0UzTv2Ald8yd6D4ZkqD9QBdbPOf5fC9xoMXPvw3HuJAENZA3i7U+8WeNPeJpnEr72Xz1mbJB9fMiv1/tU9zVQLQMwCi0zbIeAE0A81kXd/eu+Npoc/bunumQUgwc0/Twn2EZr62I/Qe0v6EXrbJNz3XlkLdkk/T+3wxBJMBX/e577vF23vBWzNmqGYpH/sfKYu7Nkd/1mIKa/eYHqqWM9EnTj+iQi4CQKv+jMR8X5jJU+0qBtrqtZR85bjNZDTbSds9ybzTVUSoGQLFvyZDeBTeWULyqI7qfvdft/Vyh+6/HY3Q/PYPv768oYaTx88W0UwHaTnp3oqjAiIVcAQPD+iCoz9z5rIJxEAdqB/AVQIG52RNOUQc8edocSM9J2Z7VG0xzguQ83mtIMRlD9jcJogZxbhOpbHEKRLWiRjWwzFAHqPAP06tQDRJJiH+h4xx3DHJWicosg5xuDW3AUrLMtFZzMGZXwX1IPvS2OAlE9tH9pNpnzvZyerPJX+9cWmSTBzT9bs4nGtkLlu2QZiyyEPVwnc9wR9IrRiQLvTVlvB+7Zk1NV8FQemyOTZYuvGaVsc0IKv64TxguMCQWXkcp5zvn9kVhSnXarRuQYOH4dqpNaMOLbdeLvpsrvPZUNXTIs49bZWWonQ9I7plDcUNohtGpW6J5hG3SjZRkAxmNNpEAvZNmMQhNUY/tj4h1UUK0YcEpYgYvzWPGAbS5sjS19PL1eT3WF1mW1hr9Eo41A4oyYLTOFFeGvSs7GPUS09FFIWaUMX7ogDmqiYvT7RiEczESJ1agK7/tCJGQPT8C5OzyWqR/ph3VFLoVMtvarcyFIKuWI0vVT6JM8EOkxnWMR1ClYYSort2hgtDJyeOewllpXN+lTsdbXUeifbkjePjnld3dpnB9mgfXksyRI7uhV7imC9UvzTyBslz6Z+ipwOLb0TneXQLK/ZGS2ZQsRO270TR7rFKaUVD213YUeqjjE6uRyKc494NSbu5Do8sppSREm7zSqXx8b9bS9qa5Nc3aIgN7BRQ5fJeCNanR4cJmkigpcVcT2vtDqi9MKwIhk516Gpa1gkl8LobBZ4K+Hm7lKKAY6P2qGxWtOL46Or6dFgcgh+uVrz81ks8XrLKXuKitWgPO3EW6IO843QbKmYrozRXLW+cKM3xGaNjdHAUJ1G9Dsq48ur61/1CPeUQ3McjZEQzRu/cuVYacocS5BZgTnGeYungzbv3QtxlfWyXGCszgw9Zp3Ey2FdEUU6bo0VMlNl5aafkYDaW2IkiSeKG8QVcMDKGEJ6TY1z3Fa1M83kLeOPMScaQunOCGVGpMslHSq4Lp2KoSgvcG3JjYmO1gBXg5u2doQ4auUgS09aOpJ5m6drZj10GqmDIoosQKaqNkJZfm5uY+dcXsXOvS0Fr4EP5qqpjTYdQElYcpxV6ZZuyMthTLyhJo4Hs7706+GkXLFAnyn89XiJvJuqzBVaLWLNcG47Ps/VFVoneW7JuGMx28vNZJWjQFbXzUHo+SXN4/3WZSu+2NWkPmq6NtgHp74GWbvfoI7XbolVVF+rOd4X8Y4mTkZkY1uyuUSO0cq150eulh6lXMP3pJ2ltpnwlduLor5GM55XxngOExI8J2N6JZpObMi0hDtHGG+pugnnomYdLHFh4PPI6g7bse+PvRqWfLUYMZjqTkdidJK1PrdKbHMe8zWm2KK+YVrSpFQxWZlh7O2Yoc0OfgkwaAO2dhWJyp7f03nZ3+rOWFT01r3K2LlgjHqLWIOcdMzViEpYCgQSXZrkJoirOdaGB1wPdIxQ17LRHbRo426j+Kgc4Ws1iym15wrXy0GqHuI9GZ9tP71E+nxmX+LxaqwKn9xhF9Eqq7ViOrQrtvyVjsqjePQUM/ZQ2Vy3WC0Wq93gHotbdJkvyrpwSHekVdnTbE6wOnTTnc1eNvYcKxOOd3HyE8ZI+7kuGJVSqRlt7FxRU9teaOhsdduMM262Tja4voE3c9G2kIMXZE2Wjk55mJ1gdj6I+2bJzM/OdU7KEdw5nN1uYEOrSkLV4qu2nFtciDHlabQ5jaNCc81H4nZxvVl5b2zpG7PCL4EJO9kl6fyQJcPFkRHkhBkZMatw65ihrECNOSJoBpw5Uhfw7HERrNiiyQNDorezcLtY2KLcaPW+XSkUd75h4kFoLCKxiR6lV/5iBUI4kf3swLJeUjQ3Zb0/WNuBkoINgIOBHs5CbC7PA3kYbiSTJLelYgq3whqV3anKZq44Zpfao/iYu6ZhS1EzBFFrRMp4B2e5dGfUVDOOJ33g5AHz0xlXz0Fdma0Ger5JgwzByti5tl5uu6osxexlBvu+ms9I15fiwPOlfV4j6sgz+BXeYHJKJBQFt9b5xJmrDCxlL6iKy+1W0flOH8vmmMqUaDOpapxLnlmSBscKsi8FhtHXaVIe0+IY5/CcGw4ye8sxzdY5j81j6aDFjMDOtnPmsDsq+7JfhHaaj2s5gVFFTIyO2ynVxQr83kNEY8Hx8bxVZrct3vtOGZA6q/b+dkkj+3LOqwndBrweZmxBM7qKn/ZL4rpdBxy+Xbe4PmYiTbUoGbrZ0awHTL4MYUHK3cicnYNi5rDE4fwyRmrGDEP5umVRISmrdBN7a2IHyy3bmRdhp+88FjZzzprvb/5ipmG1tkiu5wPMuRaK72frRVmU8223iJcpVwBbHg70XFc5xGsyb0kYUkau0nXgXldV3/EYpztYtBElmBOX8KrjKhvXlsJZIZfny07q5a2HZ+WF3TfegAhWbsW1aZOH2U4rCLRcqEv51h4OjSmc3e1+P+8OSykdQFux3S2F+NTv5sEl4EUuYXd+r4vKcHAPGEW67PEQVSAHl6WOGKoFOoJFQjKaMlO5rZSTSXc6E7zPH3FRRkPeEFYjGS9Xw35W5bqYHG5mWucHRraokpmNjbEoKB4EzxIUT5qcl+kV68/XW6qYSk3ftnMBOdDxKY73F2KXEwv3SDF7M8QI7SIpi3TO2ouyK7f7ApHjYrlwTAX3coUQt3KVcTcLI+2hRDdkz+Eea9fiTLUG08jzi39Z7iJiG+s2vQlOS41L0VBsqZw+wfLIBivkdJ3bBNxXxkpqcZMS9ryo9U2sUdGMZo57xhbUg7PtmUBlT1cERnxFzwj9xtXpSZut2xMndS0OGKO0KsEZNgMIbjAwfGwS3MuklZ4Prsqdz4xOX/n5Or+hzoLj5qBB2y63Jy0KhCTY1dtxQbcaOdvjGy7h6hO29dfW4cyQpEQLhh3dqlw4nM5HAB/dBgl04zxzZnLSLHeVVtJVTWprcbaTg6jIOgdfWpjd6idKlalyi+fHNUcu1vE2dAQY6wR7kaAnLp+J2RHbryoyY8Jl3O6V1NlLCmWpXOqw+QXnTqycMivg6wIpZY8dTNcWxFmQyoYdSKaDZiFP9VHK9RuQfsZR7emQ62kmNJblPC+U0MylDZcJ8BEdb8ZGDCplc1hEulGcDTgcCtCpXZL6dg1yQWKZSI5h3CXVSMeDnMtU82B1CoGJ2rIMC4Vwzly1K9vUFPVydkjVVhi2pseY3c7DlfSSGMD3sAwrK1dh6MFa4PYJJ5z8vK/SITyjxikRaIbGFZvSLQ07X+Cx8uZY7EarK7LkkMTczAOJGEeecMZFzNB5WojxbHPxlDVKb/KW42thz0mg6QnkSlJAy8B3M33FZ5q4xEnltoTHhe9yKh7dtlVK5XbCMRpNB92l9RiOOdFrvc+tG7UU7aHQ5MtpkycWxlyxJRNTI7e7Lc5uLgasnuu0HdO7tD9uyr0apaLCltnOPeeUeSG8PY4G5z1r4n7UCOGYHA9olvPw9uL0dTmn8PLCl/tmVRZyAfo5KxMXHsDw4zlKlopL7s2+NSURl/nAXKv74hwU22p98ULtsI4SfW3WJzwo8mWJjf32lh5n7K2jL1JusIveHc5sF8VSPjaYuRkKTltJdUuZlCQfO8/iNbtTdbVCd0K1Y1n3cFvBs1rsg4V/PVhpbwi7Xhd8Ga1n4lEbnAsbH/fUrkFnpTPoh5g7XHIpDOrdIlJYnpqtZ1F1xCJ0AZ/GSlRt0BUI3ZxesoLKEeoiWSzEjE/EoXPOusfs6CVIjjgiL4NvY+gwMzZ6DjdKe/HG22xhif2gObucG+kgaOHcDJPsoDKDt7xeGf6wNnOaWcBlbsr6PqAWFVWs8OVFBwEqBzv9vN6xs9VasItzjHSYJ/X4xvGuwvxc4hR22OcWy/sdx3RcsGoCX98yLR+BzQXhpn4uCp19DqWallfptnCHC8qopa4VJbe7mqggpFlwjGXB1mxNwPDhXNViLeEWzyIFxpNyaqfUsVaDiiAblAg3/UYR+fp2k5gU0Tm4lG7ibr8YmIRHsuuVSHJuriYYhosSmrvn6LbZEktCrXvyaF5vS7AVgwXcbShsTOIFcriS81Qsxs7HibNBUts9fUbgmdrBi8xO8F02xxCY7xicnIN2BJe6chniGuNoxMnNK3ONoormyQWqSRtkt0hHmkxAN5CbDZvfth6FkDJ5wq97NUuP1MIPPK1PVe9wTd14RPjc23n2uQK7gxFVWVjDdW9ryKS4B/uaqjJOu4ApGM9JmFu2Sbl676yCdLxK9MHJRn4nJUPMs2eX3lSDRBprZ+7K6UalYGS7lwe/mRPY0j+s87Vb7OJa34jF1bFjsthjRLBp1kJSHUM4j+rak2SjvfoOIcN2kWN75Cy1pHXEMkWSSDYNNhUaeCqBnvenOUrBBW0d9n5jtPiiDgK1PpDkMWlssNXo5sW5pFmWk/i5zIyl6HQOzBSy5ACnrTMmdWv4Gvrh5rwir6xB9ex4UbrLiPFL6yrgPbKxi/1xHS5uyIgSGtgXlszgS+cNO/Y3maQydb+Pz5etzGMH2xMi5rhjVjyiOFxDoZlPbDxrGfDW8Ryu61k5cxDhNgP9WVXYa3Pc04HIcVVoV7OR6tggD6SjvYjrlbPG+2Blrw35st7iW8qb7fVD2J6wdUQr8BWl1HTT9euF6xvztCcOsh0JnU6rWR1SUXTtLb5LRLTKR3ShH/RbhaGgY0diXrJd11Yq0IW5vneEHdC1OcRpzkqLDrR9uLRdGyi77tbpbbejfNnwneuSo67jtuVd9bheLR2hCTFsfRaZ3HXXDFk5pWXZFAz6UVc42US1pb1w6Od7uz8J7T7kTu5mhwz0kpg1uECeNtqVEfyrQotgM7bvaZFYHku4LBgl7WOpaFCuQRb7dm8TQ4CeiXmLw4QIIrJtkIGviYwIi1sRkUukhX3GyL2T3OlMhKH5jBKqeXdCJGCnuWvBKG3icorP5/2FEKsGvyLI6swxx7Dr54HQUHw3svIx3juaRi8FeFXUVmnHUuZnyxEtO/yIOiwmwGx18RsLEZCFsFgenYTztyMCe4dZkCcxX5Pz9WnGqMjGbCvd4ynDspYkr5E3zSiacb9Q0SPjLxa7/CZu6n5wUPECsC/cm8FhrlqLAVt28HzL9yMqInoULfNFwvKlv+rh7Ao8vO5nvin4Rsj7vUjenHhpkacsAps/63IjHQCLyb6VM9BjrI8nk47JjZCI9BVlDw6RF9baZcCWbxiuNlObJuWTMClIHFChk0dnPQNeno/xLTNm+GY+RkiNDVLPtB27kWdSbGxverLFrGtvEEUHttvaGlORSld93xkDhyqwmSgt7Dw6CNtimLFHl0VX9H6jXmEO4GIeVyV7wWco0u5ZVO2OVk5lrGXbNWhF6HXuIWAH7iaRYQ/5YrH46aeXjy/T2fXzBPqvfXWejgP/104lHweIb9+k7ofPnuV+vvP6/Bfl+uXjS+VEQKrHGWydtMHzsPK/nMB++pc+Z0wkhscn3ekjWt+8nds3VjD9POklyty2boAsdZ6094Pgjy92W08/k6jfJH65q5cW0+n5O9eX6ScLb4o0+dfnDzzur6ePQ54bWY33fAyeZ9MfX9wB+Cty6q8ETX31qmJS+PmNBOiJv6Kv2Mtv/x8aHbocDyYAAA== -->
