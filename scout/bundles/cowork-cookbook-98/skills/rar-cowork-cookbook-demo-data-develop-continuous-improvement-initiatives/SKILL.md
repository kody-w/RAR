---
name: "rar-cowork-cookbook-demo-data-develop-continuous-improvement-initiatives"
description: "Generates and creates realistic demo records for develop continuous improvement initiatives in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_continuous_improvement_initiatives", "rar_sha256": "36663a068a15b32bedaa780ebd9dd9a9d441bac4c03277b9c1e8efe214cee389", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_continuous_improvement_initiatives`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_continuous_improvement_initiatives_agent.py` and in the RCI capsule.

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

Develop continuous improvement initiatives Demo Data Generator — Generates and creates realistic demo records for develop continuous improvement initiatives in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-continuous-improvement-initiatives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_continuous_improvement_initiatives_agent.py` and embedded as the fenced Python below (sha256 36663a068a15b32b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_continuous_improvement_initiatives_agent.py` first:

```bash
python3 demo_data_develop_continuous_improvement_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_continuous_improvement_initiatives_agent.py   # or on stdin
python3 demo_data_develop_continuous_improvement_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop continuous improvement initiatives Demo Data Generator — Generates and creates realistic demo records for develop continuous improvement initiatives in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-continuous-improvement-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_continuous_improvement_initiatives',
    "version": '2.0.1',
    "display_name": 'Develop continuous improvement initiatives Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop continuous improvement initiatives in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-continuous-improvement-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-continuous-improvement-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1963f90b52570d0b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/develop-continuous-improvement-initiatives'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-develop-continuous-improvement-initiatives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopContinuousImprovementInitiatives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopContinuousImprovementInitiatives'
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
    print(DemoDataDevelopContinuousImprovementInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZOjWJLuX9GNeaiqVmawb9nWZldCCBACJLFKlWVR7CBWsQhBTf33OUiKyKyp7rnTPfNwlRYZAs7x3f1zP8RvL07XxmX98uVFC5xixjtZlsRBPXMKf8aWfVmn4FeZuuBn5pVFWydu15Z18/LpxQ8ar06qNikLsJ0PiqB22qC5b/Xq4P4d/MqSpk28mR/kJbj0ytpvZmFZgxvXICurO9Wk6MqumSV5VZfXIA+KdpYUSZs4bXIFVJJi5swaQNctb7M2KBzwfCLR1g5YVkR3llWSle2s8cDjOimbVyBhcHPyKgualy8///LpBVDPXr789uJlTgNuvayARCundVYPQdgPOcRvYojfpAD0MqeIwMZqACYrwHUV1ECMHNzyg3D2vPqxCbLw0+wvf0l7p46an758LWbPz9eX6d+hK2ZtHMza0mnaANjKqRw3yZJ2eJ0tst4ZJrO1XV00k9bA4kX0+tj5jRKw29+mZz8+mLxGQfvj15eymlwA/PH15acZsM/Xl7qbvr9OVKoff3rNyj6of/zpG52mc8+B107EgNSvb8/rJ1mw8NvSJLxz/Rug+vC8G3x9+U656fOQe9IT7Hx5PZdJ8eOD8N2iwHFe8ONP/4isFwdeOoXLf4vuzw/CceD4QKen4D99uhv5l9n8qdAHzX/MtgJu/Wc0Acvf2X2aPQ31j2jf7f+fSGdJAWL63eJ/l9zf2zD/2+znf6jbf7Xh0yz8CoI9A0FcO24WfJn99qbtOPbnH/xvN3/45XdA+v9JRiu72rtTeMudIgmDpn17+/mH5n77h19+/qGrQKwFTv7W1dnfo/n37Hrn8wcLPlf9+Me9gL9RpEXZF7OPSJ/9Vlb/p/79dWaCQuN/u998mX2fL9NnPpuUeGf6MMF3OdMAWb+z408vv4OSUQBtOu/+GGT5v/3bTE68umzKsJ1pXtm1M+DgNsmDSXg9TkCpau65XYOaUjcJMOxzHYj/ycOTxGU4+/X/evfa+tl71lZoKo9vPqhGb8+6+PatLr59VxffvquLv77OdMCrrJMoKZxsdljsdl8LJ7qXzwawDJqgvoIK4w5t8BnUps/Tl6ma/vqvsHu7U36thl/v9TZ5VLEDK04VrOmy4HWyghUHxVNnDwBKcAu8DjDNSg9IGCagGn8C1mnK7Aoq4GSxJk2ybOYnABsAsAx32sCqXyZiv/76q+s08dfiUXKx2QNxGggs+BBn9vkzUDXMkihuvxaBF5ezH377/YfZv8/+q1134hOPHUCDp8+AhBtNVWYgB7tJ+wl5QIl2/LvPfvv9aXBABmDdDHg4CZPgsRnEcBr479bXhMVnlCBnbgCsHky4VtbtBFRJ+zoTw9mHvIDp9Giq9HHZtAAUq6Dwg8IbAFUHqPNhyWICN+CIJhw+zbomuHP91Z0QEIiYg2LgtL/OZHYHcKXMwH+TmPdFYHNZJMD8H7HxuA+I1D80s+U7ideZMkXtrHJqp4pr58kjdB5+AXjyvh0Qd2ZF0H8tJky9B8o9hR7miaZOYEL8u0s/Tz4HIJ+DeuE377yjZ7fgz/Q7CtZfi+aZHk4d3PsEIMowi7rEn0Djr8+QauKyy/y7/YCkE6WnF/ynV+4xuPrvtxZTEzCbuoDZs4GZYLNDYQSf/X/X0UyqLXj+wPELnVvNOEU/HB8mnzhOLB7NHOgkHsSm9PrWXbzXpvcS/bXIEhA/9fDXx8q7o55rHmWvq4FdD4vDnT4QDJh8onsP4iko63oKf+dr8Y4Fn4BW98IH/AgyHmTEFIjvDKen75LGIK2n6299wdOUk+YgUGdV52bAyGEQ+K7jpUCqekrEp29ARAdTUvZx4sV/0GoGqIPAAfRnQIgEpBbAi7vplBKoCUwb1mX+bXkyuRRI4XcekBa0vsHrzAK5NMVTAxIYtEzTGmCFH+6kZnkAbAxE/LBwEzvVQ5ipW34K6Ey+KHMQMt974PnwW/TfZZnEB1SdqR5/LfqpQvvB7eHZDzmfvgLC5lO+3jf90d1PXWffg9ZfvxZ3GT9AAZSBbML774wD4q/OH0E+VbEGVKI8eAYQiIQ7tL8+0PkB/x+yfPnTiPDjPzdF3PHW+KPnvszitq2aLxD0wMh3iHwFNQQCMZJUQXOHy8+TvT4/k+7zt6T7/F3Sff4u6f7A62G6L7N/Tt4/kHgG+pcZ8gq/wtOjbQJyFdjn+QHmYT8vj5/x6enX4hB88/szOKaqnA0Anz8g6n0JwKmoDqJp8QOymgnpegCu9xoNPPO1+IiNZ+YACCiiCV+b8ruMvmM18PTDkR9QAh4VLeDtTx1gFEzjUjaJ3wQvX4ouyz69FE4e/Etj0gQgIJ6BeaZxCywCLVabBPerj3ZruvjjBHnPOlAu/PLLlHyfZlNr/Gn20eV+mr3PHffZrujA4PXz1GFPLMFS8Otj7cd46gYvYPRrh2pS5TFMTY3ds+H+sxBTzgGJvWBqCsqPJJ44/okI+BJFQf1nIur9i5M9K0nTOhPEJ+17/jdATh80TJ9mwKYgL0GqgQragQ1/ZgP41MGlA1jqT+p+s983tcqHLr/fzdA+JtLfXt4rytMHz+4TLAep+7mZ0BQCgQsYgutHiIFn/yt96ZMmqIugBwJEMZIkMQcmaQchXAx1A99xKBoOXJ/xfcZhfBxHQI3HPRhDKcplPCSgAb6jCO4FAUYzgN4jeN+mNiKZ5AzgMMAYBPV8jEQJAmcQCgWEHJxyHB+maQqmQh9Ax7etKSiqT+Ufyk6W/WiRJyM9bfDbi0viYKWAN+Li8WEhxnQoi3IPscvUZHA82ZDoJsZFd33fXKdX8lypSMrqy5RAE1o0O04ZNhyieGakOoaHrHb7eF4emPSMYeN1ucpUEd0e3OMyx1sPdTtsm4ZAC8pcLriSDC+H3Mo5sdhIBGZX9Yl18VrDpEQZki72EKSygtQ9eabe6kJycYY0kIjB9GopUyW7wIgOakQ5d7xEOpjQ7cLIKFwW4sVEKqOSc/Nyu0lbuJ3PK2/g17E/Hq9LyxwSm9eMg6ml49akblmpKzp7aqNO0fn4sjuQ4a7I5uFOZ+be7mYXW4bxwriTFPS6njMc31woq2p1EykzxxkazfLi4wnayyFiHe1lgPZxipbwKFTagOnMyFUeYci9oZMX7aIRljQwynYdzVtTBoPcwZKS/sIOiKQ7xtHNgy5rWoPbUNWh8o18TWSbuuZJuUNQRanL7nRCdXs+OvYKPgjpCF8yIVhTAh8MlMlelJMtKoW2iE8nKN1kIbuV7dZKwroIZVFjSWyzbhcLE4sRFFZTCobVJS13yahUVdcMJ+G4I2Gd3GZWta/XCtqeEner1sdzfMs6J5qrO+u0OkpKhAquxbdWe1I5RA489KK5EoRqS3EOylN6MnaVsq/2ZrUquP7gXRTXWiE7xLwWg3mEqFtfdkehKswWxYJ2lyi2aussFeqbBAs0qcdRukCNIc5lKhlWx6FEtyQ3FgjiNKPhEoEoFLoJ52x21PGzCblL65SMu9VhhEfiXPPhfFu2Jwmsw1tFHQWu9PVB5bNzzltwTKyImkFD3bBJsrxQQo9qWBzjbbBO/ELmljxpCCfe0o+ZASNMkKIUs6lROL86GgnNzYa4eNB6jl6P2VxigwSHVoc5dz4LQ5aepP4c0gJM3JQrdEPnmSefE8IkUDgETL1mad/Wl8wjL9LQoCdpsw5q44KUXnNQG5S/Hazbmd902gE+tYddJGv+cbCHlALYSCbGVRD3HgXRwjUwKDFyeLpvj9V5LXW44i2GVSKVySkr4cRLts1BAGYcDpfburmtDfmS5FuRlIkez7fnm83jxqHxQ3XNKDwa3KJhMxjq3l8LhpoU5f2HL7oYq/cpM/LyHBPGnWKhg7pHnbPLHNFzoGW2urApARpb2oUOsGg0l2sG7ZWuqTt3cwT25Zt2LxYokuqmqzeep8tHomZHFlPKbc7alC5jo7demoxTI5sQXp4z48xplpHMRdUmiX5/kAz8YtVzu+Flu7iQscfAx4uy210b2MgNkJlJxjW3MLc329v80jone16ejly+5rP1gfb5LVsd/XUrk2tjx2ikuTpp8z3qu+2abEEBgle3pepsCxChRr9VjlaF4vWippEFxF0oN4lVEbrGwGXGiTVDZrlJ+HG4SJxfdxkchUuOJmRik9ptyTUbdaPOtYFiZE+Fh1yT6px3pHTcjGrnn46acAkyO3PicURUazhfvZZb7/eNEuzIvFaslMd2o0jA5H6OpTgWQ3alrCMmIuSt3MlEjS/YEVuPNppYN6tGzz5FC5eo30D2kYaMGFfdNl+JjUtAF01eKDTJj6d9iLLeSU2yXafd1jsjEI1FJ5yDceGvL6sNb4cbzRI0XhobissYWnJVaT84e88a6A4rD/KwrLRePsTOddOosG9E9TG2Nbg06mwpXVFx0Wr9ank8S71nqOx+vdU2BLLfRPuecPpuVeqNYvdi6xiu54ijIZZsji55XeU8MWYlzWB3HD0e9GVunXdsGahBT/h7I/KbQW5Fnso4i0Dbbldap+EUcKeisBHEs905fTWIZH+4yoh7rpVruCHM1NxJ7eAhuU5Ly72krEaiJvDQs2QhDL153yXCCg531GlDX3cCbYW7KwW7OKQdKG633tKls+JPJkW2KqstjkcN1oRTScO33Ix5g+xMbYMZPLsZrzhK8J3Sc/ZCa4lOzIbVmlcKc60XRkkl8oETaQ/RtToOokoUKolTYWmhWOxlpeVNrl6EPYbqQzOeglvISKdDrKe4M5zG3EIgU1HzIe23poZXYskToPkX4b1J5akIhuVa6EQalEaSRmPHOyDwwSFUMlUsJ766BiSg/cJLrbi2bbW5lpAQnpdbHM5H3hZHnqctER2gwj3wtnossVM9p/g0S0kB35VpLnsS75ltsUoEbKVBgRhwxLjiBtJPj1bo0N2oUUD8+kxH62YjbOWkZ9qVbYrZfh8ulcYYbU+8sMftpnEWoZOZHbvn8n7D57BsICBgDXWBNcfW9jJ9pLGlOJzki60R+1o/cco+PFo+a0cAPA+exg1WEG7Qpl1Jy9YQDR+yMx+5lOhR8W75JsOLfuNHeNHQGLEL6hQBRT1KxZXbp3VCc2jYBe3+eGjM04G9bZnVLpVsJi8zesNsQ/123qfbrKD4dnQSotBZGNFHV9QaYV5fEPUgyRjjrDQWXuXX00mHoS0iqHjk5bWo2Yx0NrByMMpkW8biFRb8nK2wSu7VZscyW4WNmkHPE2tcXiPtZGo37hYfyUQku2FzGLjmTFRRmOM5fIUcrhJletWTfjg/itdyg8CYGl8IXErlNDI66laf9jZ00fm6LptzuS4XNCPDkM5A+NBrfOLuu7W390lpw3R4EaFqnmwohFd9IiEPob1pEdVFw+bmnStTqF2qsLVFBcPHSINJ1MTIYSEeHY6NF5gTWpRcmxt1eW1XFesu5VhDvKXGhIU5PzTYwdq4kbfAOGUJzwmt0lU8YAk43lqSoi0PiL1AegnkRZquJYaUkJGv/eGiby6U1tlO1pcFzgU9vxAxyqJha3lWlop6gIezYSy9FNpvWGQgL/t4GGVGLlxpYcz1RZUuBvgKb+FEMCEuZw4G6Kyl43bhb07d3k7HwcquGMvjQZ7iFxR0W+flZbW7HDOfU5KqkDb5qoracJlueJW7eU63DU/ser9B8UTuSpy0lylowLR8VK/OukpczuQWReEUS5638fVcnye9MTrZjvTK1frMZQ3e6fzNDDxVq9dkjKyS7bA+hZS1h6rVLvYl3qHKnbecwx5oP9QYR7ids6pjMi7OG2PlIYV03itziw7DC6kl+Cg4KoARnLE5VoVSHbb1a+fyBurOy6iIbNPlrus+PYJGtz9mC9XYRiLHe1gn4EXS+PyQS90+sXL5nPVtsRD2YhboVHkLosMG9A0yFTQ7ojBHl+QKsguwHB8PkhUnPTqQFlpJcLk5ScilxxqW4vBhsXJEYYAF3GBRCVF6ptY9TjJXG+IgVLK51mKz6wJjjcVEe4wHCTVZjyi6ZVo1qNGu2qOu5F1shqd56hEVuZcsS0M2DSlC9Sqg5nsELvfD7pq6K1Wn4Hk60Fy+weCy9/JyvsyLRWxdc/mi1gbPLLmBIormtJOPI31Z7qpLEInAnQMFN262wair4xhczvKBELbecDG2Y64SFVo6DEomCGmVjSdGHcVwlB71RVTf8LEht9SOs+1LiVse10ohAapiU0fHElGFKsytzlA2W2HlySs+crlkhYZRL9aHPLOinOVcAEGhpddtWDgb/kKpzmLRLHZoTVcwP5aUFVreUmdTcYNueIgf617WCvO47w68FSALWHfmN9yQxz18Hs5RN1xAvi/gEN1dR5l0sMI/GGG9PVeWzxxMC2HYaFiWt+3lssuLunSucMwyijfiZaIJYbOEG3QLs5gGqTgUGv54I82bBaFkcRuPpt8xfupjcX/zHWi9HR3B7GVzToCBF7aYxuHJW8SsD1uLam9wqyrGSS3msL0Ql5sdw7sLgb5kw3pEMOE47Ow9ZLopeug1dnvhCgUkFr0v90cIhZahJjqOGkZmkTOByySwsGAPt/RY1V3SSKEawWZiIxtbgY5gvMZJL2fP815GmdZvJHOetYdjoNYqRtf4dljW+hmnVoW7xBrXc2vZO48MA83DtIBEdn8y4wo6MVBSgZa86K4BcpqHx2swgLa88M6dEi72lK8ccDVIuj6D7YJ1OSrOz6t5PMIJuziBJDMzZb/gC0EvYtE5hvtgf+t0Tzynu+GEreHrVpG3DCbNT+R24Z2Q3L0e4GAVr4pLmxljbAheV2PZTvVOpdEMSrrabnGVLhEhlIsLzR+3JO5ClzWzhJaewmQwe0tOa8gToSWB2kgo2kxGJ8T2SEacPyJLGaPEeY6vlrCMWvIgEJdNtRmChPH5ORH2fhTW4bzxfJHYrzGrCXtd3B9CNyLDcEn7S9QtqJ0uHvwOwakj4MWifT02Iwgfaptg6LkrcoWlBtoIaNzt3C7w+05AeTdabOlRQoNlf72lbuws062HGzoA9nJHpkZz6JgjdKkraRCifjlY1ZxZeUYgD/TV5GiIEZfwcUTH8yB6LI2uFzmU4D7oNeP1PFCNjibHM9ULeXRk0ZVJH8SrlOjUvBLONzAsNbt96CxIMEXn/RUNcq9bsQtcbHrzuLmcPfUmN4Ka9Lx4lEiG2V0kh1wdcqnAaLNgT/ARzD/kGluh0M7PzETsaN1VgzzLN81pu3SZkr+FICpupb5ZBio2sCCkT1surC+KnzNjWy+vWLJv4rEVlKMoQUQTHmlvedz34dzPxdHaRvJY1xiEjSvZohmkhfP9NosadSgd0naXLtYFWZiNZ93X/Xm3PuR8cPWdFefbKi6AaMFBl+YsovRKapEGAphQz4skChcDpIwl5JSGJ+DMfGMKYI43l9S4oBvsSGEsF3BK7V+Gxgt56ESdvQ3RgZYt7tIl4yF23+wjKO5HKLBXZ2NHcoZ8xVcxSUJ+zdS9u2+QttF9zG9MH9oh8bqLbJcWQmi5FebrPdb6PU/Osy0Wiby2u7Jreb+y40ut1t14He3dnuARnUhaQVfsEDfBFJtB5z08unOBFuxb30MYCzqZdn6yCGWFEGiGSlRo5bQ55DRix77eK9pGbjx6FcSjQ+85mF/CGbtSRo0YiBvJ+blVX1xD7nKsdkeEcqiLXt1QERHZXimhpmOwAlT7Uz/fJVG3PebQ5kL3dL9s5IXZt+q6bRYeaL/KIYeMHC6USMa9jEv5XaahPCEH2e6gIsW23y6YvuDtvt1eGUpkoXAwJG+d0pK8Zhi0nN9Yx6673XrX9K1QH6NhDp2GlMb5cnMOK1jvajB6zgmZPnlarNah3CoVw4zqkjjr2z4IFpimg9pWbIfoBhf7275ZqvY4Z6/zZK+WdEKN+nzRuIc5QyWC6CtR7YFUjQ31RjHr4aDdsn4vRYvFy6eX6dz6efr8P3pRPZ3+/a8dQj7OC9/fVt2PngPH/3Ln9eV/JuYvn15qLwFCPg5km6yLnkeV/+k49vO/8t5jojg83hFPL99u7fsBf+tE059GvSSF3zVtPbw1ZdbdD4k/vbhdM/1VRvP2PAx/uSufV4+T9aeyk6vKOvCcpn1ry7fnIXxSTC+UAh+wD56X0fPMGuwdgGMTr3nDSOItqKtJ9+eLFKAy+gq/Ii+//wd9wHTqliYAAA== -->
