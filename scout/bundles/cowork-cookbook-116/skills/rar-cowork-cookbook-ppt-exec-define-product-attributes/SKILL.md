---
name: "rar-cowork-cookbook-ppt-exec-define-product-attributes"
description: "Generates an executive-ready PowerPoint deck on define product attributes status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_product_attributes", "rar_sha256": "54e46639febdae042ba1009d5bd9af2eaabfd3735df080ab39f17e2b9528fa0f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_define_product_attributes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-define-product-attributes:58a3e7eb328b2e1b950b46fb89bfa4e1f8c56b0d738cab0e824f25650bb79a89", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_define_product_attributes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_define_product_attributes_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Define product attributes Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define product attributes status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-product-attributes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_product_attributes_agent.py` and embedded as the fenced Python below (sha256 54e46639febdae04…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_product_attributes_agent.py` first:

```bash
python3 ppt_exec_define_product_attributes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_product_attributes_agent.py   # or on stdin
python3 ppt_exec_define_product_attributes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product attributes Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define product attributes status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-product-attributes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_product_attributes',
    "version": '2.0.0',
    "display_name": 'Define product attributes Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define product attributes status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-product-attributes',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-product-attributes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6265b2a16e5b4e48',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-attributes'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-define-product-attributes', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDefineProductAttributes(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineProductAttributes'
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
    print(PptExecDefineProductAttributes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZPixpruX9Gt+dD2UXVp3+qEI0YIiUWABAghcDuqtaQW0L4iPP7vNwVUdXtszzm+cSOGjq5CUuab7/q8T6bq1ye7qcOsfHp92gI7RSZ2HEchKBE79RAp67LyDH9lZwf+R9wsrcvIaeqsrJ6enzxQuWWU11GWwukTkILSrkEFpyLgAtymjlrwuQS21yN61oFSz6K0RjzgnpEshb/9KAVIXmZe49aIXd9Fw/lVbddN9QyXS/IY1ADpojpE3NAu6+qmV23H5ygNPuc3gWkGJ71AfcDFHiZUT68///L8FMHvT6+/PrmxXcFbT3pey1Cr8W1Z/b6q+LEonB7baQDH5T30Rwqvc1D6WZnAW1BV5HH1QwVi/xn5xz/OnV0G1Y+vX1Lk8fnyNPzbNClShwCpM7uqgYe4dm47URzV/Qsixp3dV0gJ6qZMoSnQ0hLa8XKf+U1SliM/Dc9+uC/yEoD6hy9PWT74Fzr7y9OPSFbC9cpm+P4ySMl/+PElHpz8w4/f5FSNcwLQt1AY1Prl7XH9EAsHfhsa+bdVf4JS72F1wJen74wbPne9BzvhzKeXE/T+D3fBMIgtSO3UBT/8+Fdi3RAGPo6q+t+S+/NdcAizB9r0UPzH55uTf0HQh0EfMv962RyG9e9YAoe/L/eMPBz1V7Jv/v9vomOYXdWHx/9U3J9NQH9Cfv5L2/6nCc+I/+VpDGJYa6XtxOAV+fVtq8vSz5+8bzc//fIbFP0vxWyzpnRvEt4SO418UNVvbz9/qm63P/3y86cmh7kG7OStKeM/k/lnfr2t8zsPPkb98Pu5cP1dek6zLkU+Mh35Ncv/T/nbC2LaceR9u1+9It/Xy/BBkcGI90XvLviuZiqo63d+/PHpN4gQKbQGosDwGFb5f/wHsozcMqsyv0a2btbUCAxwHSVgUN4IowoxHkX9davOFouXxPuKwLtDuUOIsJu4RialHcUDqA0RHyzIfOTrf7o3IP3sPoAUy/P6bYDItzsIvj1A8O0bCH59QYwQLpyVURCldoxsRF1H7ABAwINL3pKjapLP7bAq1Ci6o85Gmg2IUzUx+Cfy9V8v83aT+JL3gyFfUhgZGw6ECAuSPCvtMop7xB6Qyulr8BkCLESTMotjx4YgPvxo8pfBO/sQpA+fuR/wD5A4c6HqfgRB+RmGvcriFiLj4MnqHMUx4kUldFNW9jdYh95+HYR9/frVsavwS3qHYgq5t5kKgwM+FEY+f85L4MdRENZfUuCGGfLp198+If+F/E+zbsKHNXTYFG4eg+kcI/OttkJgbTYJHFYhQ2JA4LnF7tff7qEYtIMNDoEVFfkRuE2G0r4lwmDBPT7vwYE2DyqC8rHS7/2GdCH0CxLV0FuwyqvnL+kgIoNDyy6qwLsT75Pvrn+P9n2dISbVw4cwTn6ZJbextxwcgulmpfeCzHzkw1PQXBjXoY0iYVYNzTgHqQdSt4cz7fpbCGFTRSpYOZXfPyNNBU0dJH91oOjBOQmEJ7v+iiwlHXa6LIY/BgfdloezszQaAv9I1/ttKKT8BHNs9C7iBVkB6E0kt0s7D0u7Ardxvn3PCNjh3udD4TaSgg4ZejoYYnSr6Vvmjf+SRsjvHOR79jEe2MeXhsQJGvlfZiyD9uJkspEnoiGPEXllbA73VBt41mD5nZpB6oBA6nGvm2904h153jH5SxpHMDxl/8/7SP+WXfcxd5xrSpg6G3Fzkz/UeXmTG9UwR4agl+WQ1/aX9B38n6HbYYSqAcdgKZ8HYMg+Fhyevmsawnodrr8RAeSefoP1MLGRvHHiyEV8ALxbDdTh4Ob3SMCEAUO1wZJww99ZhUDpMBmg/CECEXQnbBA3161gpUCX3tP+Y3g00Kt7hKC2sJTAC7IfMhtmZ4U4AHKkYQz0wqebKCQB0MdQxQ8PV6Gd35UZuO9DQXuIRZbAZPk+Ao+HwSOPvG8lCKXanl1DX3YwCLDCLvfIfuj5iBVUNhnK4Tbp9+F+2Ip836X+OZQh1PFbH4B0fWjw3zkHYneZ3LMOtt5zBQs9AY8Egplw6+Uv93Z87/cfurz+gfD/8Pf2BLcGu/t95F6RsK7z6hXD7k3wvQe+wFrBYI5EOaiGfvh5KMDP9xL7/Cixz99K7HeS7456Rf6edr8T8UjrV4R4wV/w4dEicsGQt48PdIb0eXT4TA9Pv6Qb8C3Kj1QYIA7CrtN/dJr3IbDdBCUIhsH3zlMNDauDPfIGeLfO8ZEJjzqBYJEGQ5ussu/qd7BpiOs9bB/ADB+lA+R7A8ELwLD5iQf1K/D0mjZx/PyU2gn4dzY9A/jCZIXeGPZK0O+QMNURuF19kKfh4vebvVtJQSzwstehsmCjg0T3GfngrM/I+y7itjFLG7iN+nngy8OScCj89TH2YyfpgCe4b6v7fND8vjUaaNqDPv9RiaGgoMYuGFp59lGhw4p/EAK/BAEo/yhEu32x4wdMQCQfMBt25UdxV1BPD9KpZwTGDhYdrCMIjw2c8Mdl4DolKBrYkL3B3G/++2ZWdrflt5sb6vv+8tend7gYvt/ZwT1vhu3ov8/hBqe+9963QbQ9CLgxrZuPbwz1DdoXDT32u0fBQBje7on49ArRBjw/DZ4sI0i7r7cN9dNdH2jIN24LJUDc+FwNnAGDdQQlwU6eD0bAZud9t8BwO/Ju44cvr39GiP8FALwyvE0BDjgUyTskIByBwR2a9R1ecHybBoTPuwzr4B5H8a7t4IAnaZ9kWDjK4QSbF6AaQywT+6EGRgxRgAZ8uPr/gaY/3SXAngGXgiIYGtAsSwk+cDwb4DTp2ASOCx7jeILtk8C2Hd+jOIrxfJzHbQeOJDhAQmNI3rdxf5D3oIl3td7eKfl7XO5I8AbRM4kGpUnbdnmXI2hP4GzWBRTuUC4gSAI6AuCMQPk8D2g4/2PqIzZD6O6WD3kLGSLkZ+2wzq+PWA+5yNJw5JSuZuL9I2GCaXN7ztmEjlCy4HC0sJkT7YrecEbr+lyxp1xbnSVjcmbIqJ+ZpCQz58JOtOWls2WvnGjhWBBTbj5tG38u7uZGXSt0q4wSunZJp6EWZ59haM4cbZQM9SJ1147UgurnJ205YVcxGYabitP0WdIs29GishR84dvM2fbC69kke4vC0NDBd7knuUw72UbGiCgCS68xXNG2xHpucX69E+pmkhaS2+7yqJDl4eDoZC2IuHPknL52dL3Y22wSb8yDGvXqhtWMuOfba8yCdlxz14oD7aKl9cRpiWAubaNlF129pHTW+J477pI8IUolnagMpwY5Fy5ofW6YO0dddEfFWJjWBPWbLF7sD0E32miBU6yUa8Roi+JCnyCvUQnbThZ4L6s9MZe15arsd1ti4khAr7ZNaNONpPQReyGLkNQu2QoUDNPaNnY4uuXOn/Uy3i8MLXGNEyfx/aE+Lu39ulnnYW+tkuhS6aZYkMqyJn3TPjaNx19HMyJutsbRtpaqxi6SSb/qylQlvKrw9klC94bdTHnxRFnrrDn4jp+ETZKUyrmQUnPlUmO+2ljyKlDJ6w7UB1ARJdMl27IN6MkGq3cKLaiENusrf1XGRlBuJ9qcuXa4b1XT4hjRmHZmCZQ6xWs30A2N8ytYXL6sNl5Djkm0SWdsdbSOE6vE7EWgbq7O/rA+ZobbXMT8aNXHqjQc6dJVfHkpPMmMVpXjkwe2naVzvADCxsi3jIEtgUYF+bnb1dVsL2MqJdPh5tLMCC5Hw6DHuGlZXGNnQugmL5yrqquubc9MzKpby85sK9h9cZ1vtg4otjYoDNvL4h2BdpUwcTGD89BwzktL7Nhh4QgTobf4cLmbnVj/OpZZ3yg51vMP6QifGaUPGmGxbIt9btb7I5Hv85xV1HXsl87mgANDbopIK3o8mrj6IdY6zG6plu8m4k6lZVed71tjG9OMyKWOHzCbBd1NsmW8PjoML57bw8ya4WNPlWMpiA5zwB+bTbqdFUtuH6mX7BotVgWZF8QxDS+rqXw6evzsKrJYlTPHMHfXKDPrR+Tcxf2IOio4F4ac7LHrubbbJMaMv5Kmp1i9E0oUKo4iKsu218rDEr+76uttZQWsseboVqpWXGceKJPjXTEMnEslE4VpbPBen8gnT0vCek4YR0fn5w1EKC1ZtrbhdYIQpta5OPfLbbnudkHNjhJyg/WqtVR0GnR7B4Apo8TsZn+keNRNTxstLFpdZI/HCNul+SJHi9q2LBSfSlLDb2aHHa91JGnLZ0waSTi6Wkmhcd4wm4Pn1BJbjXSpvSqjJTtNcWVtnRfanrgq/X4z5Yoj2vPlxr2ggmyd+621HY2vs+tsnNizcgxhVmIoPbddEmdEyqqDSdWMwxSoaUMZk3G9zM/RlgsnQSP1Lkza7YYUxhs3gcQcr8ixPeH7HrdEkixo7MxRh3C+Qp1kfp1TYV3OS2yKtnMxDQSRWS70zWhH8iPC4CJ6LpzLPDNLo8HxkHP1JPUwqt5NmS64sGtd60bRkdjJ45N1PdGjOECX565n4hngz/Zy23HUuU0nB8M/82EVLArqtNhfxDBn/YpF+eOqnB5TNXUvFVWaqBBtGVNqnEPs26V6ONXTi6hoijzzl6pMbecrLDMjGU0wJdT103m0XUeruRmR29BZgJgaTTadZIh7Jd+EyqQQDdMgjofD6brkXFQU1U0Z7lFb2WzLfRpazQTz3ZpW1/PSbApaAWongEpYejXPbdfF7qo1bZUQID2SGEhzZbaUcnPLXAiUB+dzcB3rbL51/MN5Kgal1q6r60zAikAJ6ys15YKZvHEjmIE8yGmM7no/cv0iRvVZq8djPisiZc+1fcbJoWj10nSbbDIXX1j1Vjoosya+zkupGjv+SDAkmrEn3awJzONVCGxc2WrOJR8ZsqDyc5aRRNj0iGbRKnrAzf0LQcs0nZJRbIzJpGkk0d+XO0LUOcilVkXlj/bO0l2pq7V5rElNakIUWuhdYcNW3Pw0n69F9yDko5DqyKNDHiGcxROnvewom2robKdiozUf5LSjsOf6qEy3TULJkzmbrsjVYb3Kjptd2rplyRlZqenJNnKtw/xCCeiysa25GXr0bDlJNFBsqsN+ISwwX+Fcw8v42dbMUXVMx4dOzg8X1022ZBiBpe2VTrK9rCJ0rDvyTMwnx/HVsMiMuMruSuSrc0mum5NjjGfTlFwm000T1Jm7l4vZ2Yqvx4yURXeLq/K+unisq+srW57tZ5wjkuZiFx7FnUguqirQAlLrTfYaGMekbo3LYV/ItunMRNS6lEncFaugko+8A46VFNnajFt5wtEqBHNt1t1cqkh+Pq+SrdtQ071dgLFcKyd15WRbt6SxJbUrJv62zXkZn0uMgxKlS1bVtliBbV4U8cEZYQVbG2f7tOL2AR7UEmPtqw3h6/0Udn43XuaOd7IELZLTrJODouq58T6qN+NsQfAZrRVHIgn4UjLSaMKNWnEXj8b5Qg7iKJY203ob7d3RWEXZtcKDFcwW8qQa05U41VILa8YLP8NYqlRxN1BOhCLOyoi3cXdq2Yer7RE7czcR9GmaNRzqt/rKEsPjhj8fFtG4XUtYk8ju5IJ3tQ4aomkqa1v2jNnmBLiynSWzwBBKx2Np94gmU1nSTlaCck0wkm2IurPJFRKzkmxCS+zLsXAoT7Nq3U2WGz51eG5l2Gk5sWb6YnToVNja4qIw6fFprJ/ndheGsjk1/UTMGErocxldtJmzy+wSi7fKahtMGK+oiwgV53ux20ioTdFx5+ZZftaoVNnPbGaGVmvVcqJCmurLBQE2+06OMw0E+xFI1lusnvvyRmvqPqlzBlcSeoRaqzm7wezJPNfUmLuSp7m/1BqpqZemvNFP46W5wKdWouLH6rCZGTEzpzUlzdb+9SAEvOId57i2WNjS4Vwv1u683LJkleEbh+dnHSuIXe/hpHomcoNPi8v6cGEc7RpvbIki4rmpKPRsf5UmGBHvONI3MkNQ3MiTpmc9OaXdHFjlfrlIliS1ToLdjuDzBhwcE2+LeUvMjzNbOwrT/db2uOIinrzIw9S8JEuAkwBM2qiDnWakSrQQzy7qYRdctMkua8X1YUa3+2UxjSKTOIdzO2uyy3nj0PNuRUnKugW+kGZXfG5oLL5uacI3cG8524SHrFGX0YQgMnsbQBK3P43BWq2uQSau5CCE9h/X1mFhenFlW+fTNoO0cCLMCtNlTMeKiYjr4H7FoE1peWn6MyU2y1253wRbSImJ897RujiWLiEVJMdT4h0r8qw6p47wXbwdbVdrgU8Px0IVRqjcMPhMQ2tptKMJOVDG2Y5T1MK97sb74Bj0qSWktHLCJktdsw3mmtDS5cS7kVCu2VKjTNpQz3I3w3qGyfZz0qw5Qpg1wspc+fK63QsrYQSpCX5K9XFnQwIvVsQsb+j1xgtPmX1Q6g2aa668jaSox1lgl2a+DcYjJZnSh/EosM/B+OIHF16NKmI/OmTHylLD3vRWucBp85U1ItZrLUOb0AmBIE1lytmvR8ayUhVCmvOVZQW0t8zWBzeSKl4K6TPulV1am+I2jeWRV1t9O57jFFg2AU978ZzEdV3KVNZG1+fjRlG3dHYi8p7BS0Zc+9na9c3F9WBlnVcugYDWTdsCnSM2jc4V5Xx1rUyN6MvanqUNr40LbooSw27TnSquZmmGFwaHvVA1SybKdiJLnFpKQXE63vXs3DT2naec/e7onvbdhWvLJA/0uAINIAtqzl0OPSw5JomXS4M+Abrla1MWDuIkc5piXq1KXifPmuJ1hhgk9JS32oISWwZlVFYtxZQ9CPtwvXSoDdtVsKh6FFf2+zbMjBWnkigXTLoOAwFNZXGvUA3XWRnPJ1eeIAT0EkCKcZiYtY9dMVRNY0EHLMOcLII97dica3bUTtjMs5B0MlWfX3G7lqviUuEXlSGqHF3XYL1Zr4Bf7RdhKo6MU913yWqp04vZgZrDzSc1ZZYQ6qdhmpg9G/tLQelWxYQgWdybBvSaOZRrS6fNEbUoBMa4JotO3R4mvRLHteLvDsd2MfJQnR4Xlz0RYFjqZ80E7fugqspIaGQrIMk95R8s/ujGQ1WtR+FKCBNOOOuWNwrYCZsElylTLPITwV3izOfMRhNyL55hLIel02k0jZVaMKeVeJHPBlUJqzYDk4BbcUI6r9TGsnlvOTpexH1VJkxSlxxpKVg98XxNkrie3wGedhqnAV7XWKTkROKCJ1QSbLqWHFkNdhrBoj4k1Rk9efkIXCYr8oKNL3i0GXWHGWvOSeHknVd8XzWmzGPVbIQfHC6Vz2te6anDyAGXkONFOrIohdleLgQ1JQN/JXZmPmH4NdWqYapf1/r0dGGVJbig+IiYzfd7pj1wB6UC++kGckRytKbVjDrGAb+TphdjtCt1TgjF0nR24QzTrxS+iydCh5GtE5cW1aCA5/ec5Fy9imFVcISErVb0/uQofc4xspdKquBNm6nv9leyo/a4zWhOalknPZXDyzhhJ+drp2DdQbvQBxs9iRTOVKOgsfB9Shk1B0z+4pwokxIJsZlEHceGJfTDpDUFxmyM1cojUcrGd4s1RzhqUE9hsUktJJiydhgF6myB5pnU2lZjZN0sm/ZLn1Dh9qdQpiNU13M5Q9kj3MjwrT5XSE3ogmk4tql1lU+nl5YEnINZCVfqaMKuGIIGO2HCb6eAYzFPDZmNKgScWlmASQgU21mA8iQHNJAYnipwMakTZu1Wp4iDNALteiG6yCuG4ue1FxECe1hclGk8TWbzrFNWZoTSyXXKKzQ52nHb1WQr+K55ZLipT2BrYSUupXjmmxSP6ZoQZOFk4V2Y6aJc6lLSoA6kpEVcyyTeYkWESf18V7v8GIRXm1/L+GSEx5FYs7EnnUaZsgytzOkn+6zGqCoHJAgtulLWuiSHJ2/MWvquB13I69MRvydWQDH4gL6OeEkqNxJYlGuFaUfJRjHRTGD3hHjNrvLkeNRG46PRHARVOmtEuugc3e2oyR739QaqOcZaWpnzo9i1eVmgyAzdSI61KDQFq7qaO/lBfESvxBHtank9XbaLcy3FJzMkMzbD7I1U+BhkiDV1BSdOTKc0w4/6ILl0tZbWcK81OYOLKHltsZX1iwIjE5/TKCVtWLBTKjo1B3rcpi7X6suj51zYFaZPlwTqRWdRFH/66en56fYq9+mVwFmCfn4ajv4fB/h/7/g3uEb520MWxRH889P/v5PJ+ynh++u923E+sL3X2+qvf0fNX56fSjeCKt2PjKu4CR7Hkf/t/PXzvz4VHub39/fRw5vIS/3+/qO2g9uxdZR6TVWX/VuVxc3t0Bo6u6mGv0mp3h4vD55uhiX58Cbi3ZD7S4koSN/qbDiDjUrwNPzFyPByDXiRXb9fBo8jfji+hzGL3OqNYpk3UOaDoY/XTMM57fCe6em3/wvr0dp9cCcAAA== -->
