---
name: "rar-cowork-cookbook-demo-data-inspect-inventory"
description: "Generates and creates realistic demo records for inspect inventory in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_inspect_inventory", "rar_sha256": "80beea2c5bfbd041a4b42f77b54f650fc7264264d569da7de821557ff382267c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_inspect_inventory`. The original RAPP
agent is preserved byte-for-byte in `demo_data_inspect_inventory_agent.py` and in the RCI capsule.

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

Inspect inventory Demo Data Generator — Generates and creates realistic demo records for inspect inventory in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-inspect-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_inspect_inventory_agent.py` and embedded as the fenced Python below (sha256 80beea2c5bfbd041…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_inspect_inventory_agent.py` first:

```bash
python3 demo_data_inspect_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_inspect_inventory_agent.py   # or on stdin
python3 demo_data_inspect_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Inspect inventory Demo Data Generator — Generates and creates realistic demo records for inspect inventory in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-inspect-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_inspect_inventory',
    "version": '2.0.1',
    "display_name": 'Inspect inventory Demo Data Generator',
    "description": 'Generates and creates realistic demo records for inspect inventory in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-inspect-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-inspect-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1aebb71234df1c27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/inspect-inventory'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-inspect-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataInspectInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataInspectInventory'
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
    print(DemoDataInspectInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaaZOjRpr+K9raD91edZcACRA94YhFCCEJBOIUwu1oc4O478Pr/76JpKq21zPemYiNWHVVC8jM93jeM5P69cVs6iArX768yK6ZzhgzjsPALWdm6syorMvKCHxlkQV+Z3aW1mVoNXVWVi+fXhy3ssswr8MsBcsZN3VLs3ar+1K7dO/X4CsOqzq0Z46bZODWzkqnmnlZOQvTKnftGny3bgpIDuBqZs4qsNzK+lntpmZa32fWpRmmYerfKedhnNWzygbDZZhVr0AQtzeTPHarly8//fzpJQTXL19+fbFjswKPXraA8daszcOD3+GNHVgYm6kPZuQDgCAF97lbAn4JeOS43ux597FyY+/T7D/+I+rM0q9++PI1nT0/X1+mf1KTzurAndWZWdUu0N3MTSuMw3p4nZFxZw4TDHVTptWkHkAw9V8fK79TyvLZj9PYxweTV9+tP359yfIJUoDv15cfZgCIry9lM12/TlTyjz+8xlnnlh9/+E6naqzbBCogBqR+/fa8f5IFE79PDb071x8B1YclLffry++Umz4PuSc9wcqX11sWph8fhPMyaycL2e7HH/4RWTtw7Wgy/z9F96cH4cA1HaDTU/AfPt1B/nk2fyr0TvMfs82BWf8VTcD0N3afZk+g/hHtO/7/g3QcpsDT3xD/u+T+3oL5j7Of/qFuf7Xg08z7Crw6DlvgHVbsfpn9+k0+09RPH5zvDz/8/Bsg/b+SkbOmtO8UviVmGnpuVX/79tOH6v74w88/fWhy4GuumXxryvjv0fx7uN75/AHB56yPf1wL+KtplGZdOnv39NmvWf5v5W+vMw0kDuf78+rL7PfxMn3ms0mJN6YPCH4XMxWQ9Xc4/vDyG8gNKdCmse/DIMr//d9np9Ausyrz6plsZ009Awauw8SdhFeCsJqBnym2SxfgWoUA2Oc84P+ThSeJM2/2y3/a91z52X7mysWU7r45IO18e+a5b+957pfXmQJIZmXoh6kZzyTyfP6amj4YndjlpVu5ZQsSiTXU7meQgj5PF1N2/OUvqH67E3jNh1/uaTJ85CSJOkz5qGpi93XS6RK46VMDG6R7t3ftBtCOMxsI4oUgiX4CulZZ3IJ8NulfRWEcz5wQZO57jp5oA4y+TMR++eUXy6yCr+kjgS5nj3pQLcCEd3Fmnz8Djbw49IP6a+raQTb78OtvH2b/NfurVXfiE48zSOJPCwAJj7LAz0BENQmYVk0lpAbp4m6BX3974grIgEo0A/YKvdB9LAYeGbnOG8jynvyMoNjMcgG4ANgkz8p6qi9h/To7eLN3eQHTaWjK20FW1aCG5W7quKk9AKomUOcdyXSqScDtKm/4NGsq9871F2sqXEDEBIS2Wf8yO1FnUCWyGPw3iXmfBBZnaQjgf3eBx3NApPxQzTZvJF5n/OSDs9wszTwozScPz3zYBVSHt+WAuDlL3e5rOpVCd4LqHhAPePypTk/1+G7Sz5PNQWFPQPQ71Rtv/1nLnZlyr2nl17R6OrtZuvcqDkQZZn4TOlMJ+NvTpaoga2Lnjh+QdKL0tILztMrdBw9/KvxTiZ5NNXr27CKmWtcgELya/X+1FZOgJMNINEMq9HZG84p0fQA4dUET0I/GCVT5B7EpWL5X/re88ZY+v6ZxCLyhHP72mHmH/TnnkZKaEqAkkdKdPhAMAHhXZ3LJycXKcnJm82v6lqc/Aa3uSQlYBcQv8O/Jrd4YTqNvkgYgSKf77zX7idikOXC7Wd5YMcDSc13HMu0ISFVOYfU0AfBPdwqxLgjt4A9azQB1ADCgPwNChCBQQC6/Q8dnQE0ArVdmyffp4WQ5IIXT2EBa0Ga6r7MLiIzJOyoQjqCdmeYAFD7cSc0SF2AMRHxHuArM/CHM1Jk+BTQnW2QJ8IzfW+A5+N2X77JM4gOq5pREv6bdlFYdt39Y9l3Op62AsMkUffdFfzT3U9fZ7wvK376mdxnfMzkI6niqxb8DB/hfmTx8ecpJFcgrift0IOAJ97L7+qicj9L8LsuXP7XjH/+1jv1eC9U/Wu7LLKjrvPqyWDzq11v5egUZYQF8JMzd6l7KPk94fX7G1uf32PoDyQdCX2b/mlh/IPH05y8z+BV6haYhLgQhCWB4fgAK1OfN9fNqGv2aSu538z59YEql8QBq53tdeZsCiotfuv40+VFnqqk8daAi3hMrMMDX9N0FngEC8nbqT0Wxyn4XuPcCCwz6sNd7/gdDaQ14O1MT5rvT1iSexK/cly9pE8efXlIzcf96SzKld+CfAIdpDwNiBbQzdeje795bm+nmj7uvexSB8HeyL1MwfZpNbein2XtH+Wn21uPfN0xpAzY5P03d7MQSTAVf73Pft3aW+wL2U/WQTzI/Ni5TE/Vsbv8sxBRDQGLbnUp29h6UE8c/EQEXvu+WfyYi3C/M+JkZqtqcCnBYv8VzBeR0QDvzaeZOqE2FD2TEBiz4MxvAp3SLBlQ6Z1L3O37f1coeuvx2h6F+7P5+fXnLEE8bPDs9MB2E4udqqnUL4KGAIbh/+BIY+1d6wOdSkM5AIwLWriHLdU3ERi3PcqAVbK6sFeLhuIWuPAyFPBtHsBX4cVCMcEzccdcIjKK45y3XCILhNqD3cMZvUy0PJ3FcyHOXBIzYzhJDUHRFwDhigsUr3DQdaL3GIdxzQMb/vjQCufCp40OnCcD3dnTC4qnqry8WtgIz96vqQD4+1ILQTPyCW1JgESXmXg19cbBCtZCt1gqsowHvL3Z5oJOtMVa7TC0rmh+ONMzbmi+YqlMyQrAlyBQ/7tsmdZk9y8d8A/sVU4bweExQe+7MUzCm0rR4O6HjBQsj+lYstBSEewGvypvBnI+utqMIrYyKYzBn9XSJNov4eBm2nSab6eq0RGMkvmK0nNQsrIVDLbNHycrPDo3t4OOVOyx4F2ZyXbhqI9azhS44JRwMmcIrlFH7Da8wQXGWBrvRd4jdKgTmnCUnLQnC8TYN6yBVTOf8VqK0SDdhvgAhQOP6RQvlIeL2ArZJ58WNQrmk22mKe1NObsxxznlpy/EYi+NGOhc5m3PxteCirrpsMVjFbFQOXHbtN9QAM/IGUq3ELeKKt5ljGWt5bcc7Iz+UJYuemh7h+bRocm2pLCEtB/GdhR53yWLhvOYG4YQGfaGJ5jAXWSHaUUNhnRUToy/XwqpV/CLMbSkix61YmiRZllSJVvYxrWt7u7o6u8RUFMeI8HnnwVkK7YVaDi6sRZgDnVycS8+UIz+K+02/GA8cLVUMgpk+XO6WXJfE4RDWF8XgiFE0e4izsZvZr1tWEijnYK4SmR02pdMJOVrUK1zBLQx4JjmI8AknhgGD0YWYZbUTeCcrnwuXrYsewmYkcP7Up5vK6Gn6gse9b7T54lSwtRNl+2HRtWzKSaddIZZjfMOg0F7uijkbpn087ub02m41ddgN8z64WsRFOHbULVnD2/1JrfPbcB7Tslgk1xjWAmN5NvyoVc4DdtoyFiMfqd26FNhjkhhskY/YMU8gjQjt1cpe7K1YyLk1R+O71WIrzenbbT/EkR51vrfeU2gvtIsemQcRI/VuYWP5shmM0oIua8k2L01xq8pjJA/OpdCoxtxzu9baBRVtH659YUTz3b50j+vDoJUJi6jpmvbb8zxaobSXHkt/OXaRfzpKOrItNZpzqXnHkYgcskk1nA7t7rQ84Bl92PGwH+ZXCqPUwNrF/MVY2cqmPyxTuzh1QotTzUUx5weFoI+0d2jm++KsbxF2Ae8KJVaQ7bZfL0eNr8KIaLLIgzcyXzVahdl6u11Qy8pytMGOZHPBOaxJGJp9AV63p86luQjWDJwosC5ja1U+rYiMMlmEJ2no6NWn0eM7dafDha5uFrXgHtlbrzJe6p5N+6RhCXM1QMzj1HU57J3Or7DKYVJvEY/5KQ/bM8UejXDh33zskhB8sQjPtSyR4VDU8/PtAKmIs4KiMdPEBVzmKh9zKG/AHaQUnUpTqzPNoJngbXa9hFYwKP1WAFHnUb2tZasOWXqV1h5XHNVDLxQ4SlPyIRlYdu9YYTouUpxlryrwqgMSHdQTEsatYbhLhKExSblGWk/WjmtEfakLasVxNa9wbCsdu0XEoBokN+oms/vyvEQvcJJKNyvFIhVxs1QVTXxNlOvkIJ47J4ETjaH7OTl6WNjfMGl0M63UK1Lu5s18oddnn4q3UNmIor61dEKWyqBMVdXst1Cn3DhIDeaDtyoLKnPlbm3xFkXFTHSONpfWtoM93QtJPj8fLV+F7PwYqoe5rs2tRsRUQvHL+KRAiAtq1eFkkJGPkPuDHC3lQ7/IuhXEG8vdcCris48eD9dwpXP6ATaUsL51uF0zHYlTolbLfB/5fJNcWE5llAp3uoQk86N4QJSR35GUblbrY7sC1U0LNnI/71qK2JiuPZipi6/s3kiPOS5dLo6XGnO31VFcCrlNlI3abSss5KE8FoKER2jLp5m4BT62T2/62PXrShSaBiUCRxa2WSQXwnm5WKP8+Qw1+g09pek53q6zYrO7aDjaNqxIUtzmlssYJJi7ke3CK7BZruLF9kAiS8iTFJY98T6ti2aDuiRUhPmO142dspdxXCal7DA/QeMl2zhdSaYS5wuRnzoHgr0OGe7UOmmsG0gMUJTfLaA85pxmbyft8bqVrcZOlgWUNnC6WrGOHNMqb5ALPDpvm03T1v4lVXbuBmm72uA0xLkV/njlfZKiL2h51IWqzSTOu202qyEZGX27ZRj5cphjfIpLjC5sMqjnkMU+yqPGhHq739BkfOzZbKRQN00WmLu+OOjNXx6Dzr1WVbtzrDResoaj0QjknPr1zmRv1PamLFVTE2WdrFWlHMXcRBJK5ejIOHgmrDWsuU7Fg5swJxVGiovakG5lOrody/p6uaPmxrrQ+aOoKh7Nit6VqSnOv0okYcur4eJ6R6Sqt/4mV6nIUZaxARcZcuXFPjrWq0Q8wP6qraIl4TklDTMXKIx2itVFpU/Tw76el91VqjRDonqOIJWI1Ykki6IjwXlKfxMjLk5xoU7NsE8FFoKV0TrI1X5eFrAgmSfPMbcyBW2T1nDHEeWC/faquDvWrPqjB2EH2b1tlDArbjS7kJpEPS6JNWiF7AVLN4N3VOK9Q7YJpw+RGUYhtLvyUtpHmmXSPrzBjsPS3qfOiEkET10iBtueCSQgKtvLDZhgeClEV6x/PvmnBjfSrbgaEwUps+zUFNGgnr2FcI7Sy+IgeDuFF2jRwUiFkCHLT4SURpdQUsGrENM8/RhDAo4YlWTfcvicW1ar38Qcyla+pLJnXXfthtq6AZmJ/CUxGquAZcW3cBETk05h1SIl1VaHRycqnB4OL6tdxCc3yTk1agGBdG4izkGGw5vqq47W8Vuq4Rve2MitG9Z2XyxtIK6ZrcsYye1FjPkYiBaKn8Mtb/jKVlSUyDn5BHkroxQLSLVZaiItuEaaR6jRkfFw3Z18xo0Ecp6IZotFy/CU6hdUUSEIY3GXXHBJRGw84bQdHI0bpDiO8gtDMJzLsiytxFtKG33u3HUgDrpkH6oBvz/6FUG1C9Y4LjYxie61WxVUSjIGpuX1O4PeolQ6SnEw36jZOhMFAdGUOXCRLiMtS0irrpIusWNXg5tr3I1PaSctCnRZBUsxSSlUhQZGnGOUQ8Jzo15hcVyNMOcoVG8Xm0YeQZPCgJ31yVM3y8w9DIhyKx3mpvbdrUVVgoFKEOTxEey+yd0q7vWeldwjcpRCmzqomlSFEoS39n7cS1eE3500G4fyE7rnAksgBV8+4PuFxBEHXzbRxGAI0xuFPNHX27OmEm3dJyFUUzXppFBei1ouyqCN0IOzuEOOfUQyS1mIM5458I3GKgF+qcw9VNDKEJ7l1W2IqdKz1/6xvY3XfltpFUvjQ6tuj4pU5dgp7BjvrIfFnHZIdFTWoXqK0kIxIKlwGUJfR+VRvEWeziKJneg0Adrco6Ccc8VH6ex2pXyt2N922t6otuohvvIZrC9L/2Rg0mYJDWfRK8mz4+KJ1kd4PtaES8sBd6LO88bQzN0qhD2fEznP0hSc2C0voAJenDB20MxVyM3CM1xj5yBH1ipMh5NJBLKwCB0llbzq5lIZmq2ks8naDyWEIcercNtoKIB01K7jpSS53ZaPVqdFykJJuqygVrX3GkMi5AbbMhreE51TKrrQ1b4c0StaOYcGXO2PN6w+tOKFbc9rywiu17W7vWbmBQ0izdjZBKZgTJmc14oNoyIxF5qSK0xEFTcnGNPwVWq5u/FoIGQuJOoGV1t03xQ+ekG1VYprerBOEe4G6TA8183UvHnLC7YUBxfvVmxReCsHaZRmxbC43Zi2yQkDv3Xsfh8WUcYjqI7c9sVllB0DDvLOVBZS3HEjG9m1XdY91N1gpIUQlG8T6ypthsiIQOM6MGy4mC/tLSRttWBs2GK9bDvEZeZFS502W65zRmGer4dthUNtwVaMm/OExYho5ew9sm/RgZ2rXAm6DhHxEK1GYVKLb/N61zebs8e1BuIvtBW6SVFuXCyCDSGWZFeW3mLcLvbKgFitY8/HEsFFzoldLeCJVjuuGb1S51yaaQTV7YhhtWExYhUtsv3x6HcnpDW0q3KoNrkEoatQiPf0Pj7hPkKt0O36InUOPoyKjDtD2zjAiWsHTVCI34crEubLo3ZawcclZxKocosZfbc/3fJTN8w3NYsPy3FlV5sztWgSf+Uv9Kpb7m2DP1TXoneW1L53ndrRhx1RLxkn3x41P1svRB30YG3dkp1B8rtWCJrLzawQNyQcZo5egkXqeIU3rzxn1Yu7VLY8UuHEjWL4mOdtbGeL4Cl6Vk6S08AYfqX64oyNpeKPF5jAuWGB3Nwy4WW8W0cmscJDo5k7fbMcKEs8sOudsHSDVdVTXmgH0cG+VkplnDPcJPVKujnVouchEOrdgUY5euGBvSfYGsl6MbjuqNLY6YijHUqfNxdz5W+tvtk7fnpQPF6JueXetT2XXKscdemkNmR2uFrNF4W0mrtnMt1Ce8QXgk2ZlxbB5TfO73yBok6hKCjV0he5zZhVQbGn5q2tFEXciEMZovCaOXapI3qUZRIeRaT9kpWskG93iJJmOZpcmRBSFyxf6fu0gXKoE/WyWnflfH8Rhj2G3PRjaePY2gA+wR7spUgkAtWuxh1y3m4v0IH2lKRjKNTbmJ5zSYV1hRbLfdNWG3Zjn+IAhkedwTPebnGstBPTxBuigQ8VL+KYya7cYDgSW6sT+WDpb0Sb3nk7dqv3INfQIqPe5vRZapx9aWxvK4Jpj6diXth4rl+FFGKw/WUtgv12jV+v8hb4k+VZ67mFerA+99cNi6LhsGLWLuPiw9oxA1yken6u2gf9UtaeKOxxGsk1fqlwPUJsliDtqQhaOC3kLo6OF4jhfl1iDLL0a8+FN8MmQCU0pMzTRrnC2pKZm4vNnu6K9iplmFbit6L1hXW5vrqBKVPXHSuDsMLXaw3dSIf2styf7KYm18MFj+C0GC8MZs899iyUNRNQKeKq1Fkcq7lPmreskwIjwQ6nhb2qKV5RLLgeGE2xFq0hExVhLor+QkIHeX3O2qom0luxOUvd/ByGTSkmi2Oz7uyOrICqncPS9QlY7oCVg69nYyGlYnI9DYNN7YfUuEGZIOOJWm/Wi4E8OcammuPzdSfMz42egg1Ffz3Jy60roxFf2U2E6c24XQrHgMK5dVos1wF7CgTB0EGbzzH4PoQDacFGTLYI1THVrTOuD6TgwcNqG5P8GF+ds0nRIc/zA0njZ6neeyG3LdKRPR+FFbYm9jyMc8uTzeepjbfbE+ooPbYFe7ZmCy9lnyTJH398+fQynSU/T4T/mRe700Hd/9l54eNo7+190P0w2DWdL3deX/4paX7+9FLaIZDlcRJaxY3/PDz8H+egn//iBcK0cHi8IZ1eVvX120l5bfrT3/O8hKnTVDXgW2Vxcz+E/fRiNdX0FwbVt+dh88tdlSR/nFw/RX+Z3va/CV2DZ4+/jbg/nl7CuE5o1u7z1n+eC4P1A7BIaFfflhj6zS3zSc3nWwmgHfIKvcIvv/03QG99FjYlAAA= -->
