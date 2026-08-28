---
name: "rar-cowork-cookbook-demo-data-analyze-sourcing-effectiveness"
description: "Generates and creates realistic demo records for analyze sourcing effectiveness in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_sourcing_effectiveness", "rar_sha256": "e1629a38c1347d4303aec8d08c12dd862f27baef8c655aab400b1dd3ca973479", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_sourcing_effectiveness`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_sourcing_effectiveness_agent.py` and in the RCI capsule.

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

Analyze sourcing effectiveness Demo Data Generator — Generates and creates realistic demo records for analyze sourcing effectiveness in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-sourcing-effectiveness
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_sourcing_effectiveness_agent.py` and embedded as the fenced Python below (sha256 e1629a38c1347d43…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_sourcing_effectiveness_agent.py` first:

```bash
python3 demo_data_analyze_sourcing_effectiveness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_sourcing_effectiveness_agent.py   # or on stdin
python3 demo_data_analyze_sourcing_effectiveness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sourcing effectiveness Demo Data Generator — Generates and creates realistic demo records for analyze sourcing effectiveness in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-sourcing-effectiveness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_sourcing_effectiveness',
    "version": '2.0.1',
    "display_name": 'Analyze sourcing effectiveness Demo Data Generator',
    "description": 'Generates and creates realistic demo records for analyze sourcing effectiveness in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-analyze-sourcing-effectiveness',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-sourcing-effectiveness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '52a2823dd0d5985b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-sourcing-effectiveness'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-analyze-sourcing-effectiveness', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAnalyzeSourcingEffectiveness(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeSourcingEffectiveness'
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
    print(DemoDataAnalyzeSourcingEffectiveness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816adObWLLmX9F974equrJfiR3c0RGDFkAgQBIgBOUOF8thEatYBTX13+cgyXbVre6+3RPzYeSwJcQ5uTyZ+WQe5F/fnLaJiurt05sGnHzGO2kaR6CaObk/Wxd9USXwrUhc+HfmFXlTxW7bFFX99uHNB7VXxWUTFznczoMcVE4D6sdWrwKPz/Atjesm9mY+yAp46RWVX8+CYtLgpMMIZnXRVl6chzMQBMBr4g4KqutZnM+cWQ1lucV91oDcyZvHtqZy4nxaPqkp47RoZrUHb1dxUb9Dq8DdycoU1G+ffv7bh7cYfn779Oublzo1/OptA63YOI3DPpVrL93b36uGQlInD+HqcoDY5PC6BBXUncGvfBDMXlc/1iANPsz+67+S3qnC+qdPn/PZ6/X5bfpzavNZE4FZUzh1AyAoTum4cRo3w/uMTXtnmPBp2iqvJ1chtHn4/tz5XVJRzv463fvxqeQ9BM2Pn9+KcsIaAv/57acZBOXzW9VOn98nKeWPP72nRQ+qH3/6Lqdu3St0cRIGrX7/8rp+iYULvy+Ng4fWv0KpzxC74PPb75ybXk+7Jz/hzrf3axHnPz4Fl1XRTdHywI8//SOxXgS8ZMqLf0nuz0/BEXB86NPL8J8+PED+22z+cuibzH+stoRh/Xc8gcu/qvswewH1j2Q/8P9votMYptM3xP+uuL+3Yf7X2c//0Ld/tuHDLPgMMzyFeVw5bgo+zX79oh22659/8L9/+cPffoOi/0cxj8p4SPiSOXkcgLr58uXnHx7FCmX8/ENbwlwDTvalrdK/J/Pv4frQ8wcEX6t+/ONeqN/Ik7zo89m3TJ/9WpT/Uf32PjtDRvG/f19/mv2+XqbXfDY58VXpE4Lf1UwNbf0djj+9/QZ5IofetN7jNqzy//zPmRx7VVEXQTPTvKJtZjDATZyByXg9iiE/1Y/argDEtY4hsK91MP+nCE8WF8Hsl//lPUj0o/ci0cXEg198SEFfXgT45SsBfvkDAf7yPtOh/KKKwxgunJ3Yw+Fz7oQA8iDUXVagBlUHWcUdGvAR8tHH6cNEm7/8qyq+PKS9l8MvDzKNn2x1Wu8mpqrbFLxP3poRyF++ebBDgDvwWqgoLTxoVRBDqv0AUaiLtINMNyFTJ3GazvwYkj3sFMNDNkTv0yTsl19+cZ06+pw/qRWbPVtIvYALvpkz+/gRuhekcRg1n3PgRcXsh19/+2H2v2f/bNdD+KTjAKn+FRtooaipygzWWpvBZVNbgVTs+I/Y/PrbC2QoBjavGYxkHMTguRnmagL8r4hrAvsRJciZCyDSEOWsLKpm6kJx8z7bBbNv9kKl062J0aOibmDbK0Hug9wboFQHuvMNyXzqXDAh62D4MGtr8ND6izu1N2hiBoveaX6ZyesD7B9FCv+ZzHwsgpuLPIbwf8uH5/dQSPVDPVt9FfE+U6bsnJVO5ZRR5bx0BM4zLlMPfm2Hwp1ZDvrP+dQwwQTVo1Se8IRTa59a+COkH6eYw1kgg7zg1191h6/278/0R7erPuf1qwycCjwaPzRlmIVt7E/N4S+vlKqjok39B37Q0knSKwr+KyqPHGT/+awwdfXZ1NZnrylkaoktukTw2f8XY8nDBZ4/bXlW325mW0U/WU9op5FqCsFzCoOTwVPYVEbfp4WvXPOVcj/naQzzpBr+8lz5CMhrzZPG2grid2JPD/nQMAjtJPeRrFPyVdWU5s7n/Cu3f4BePYgMxgtWNsz8KeG+KpzufrU0guU7XX/v8y/4Js9hQs7K1k0hsAEAvut4CbSqmgruFQ+YuWAqvj6KvegPXs2gdJggUP4MGhHDEoL8/4BOKaCbENqgKrLvy+MpjNAKv/WgtXBmBe8zE9bMlDc1LFQ4Ak1rIAo/PETNMgAxhiZ+Q7iOnPJpzDTmvgx0plgUGUyT30fgdfN7lj9smcyHUp2Jaz/n/cS+Prg/I/vNzlesoLHZVJePTX8M98vX2e+b0F8+5w8bvxE+LPd06t+/AwfmX5U9E3tiqxoyTgZeCfRK4CeFz2bPdv7Nlk9/mu1//PfG/0f/NP4YuU+zqGnK+tNi8ex5X1veO+SKBcyRuAT1o/19nPD6+Cq0j18L7eMfCu0P8p9wfZr9ezb+QcQruT/NkPfl+3K6tY9hfUJMXi8IyfrjyvqIT3c/5yfwPdavhJgYNx1gv/3Wfr4ugT0orEA4LX62o3rqYj1snA/+hdH4nH/Lh1e1QHrPw6l31sXvqvjRh2F0n8H71ibgrbyBuv1pigvBdM5JJ/Nr8PYpb9P0w1vuZOBfP99MHQEmLsRkOhzBIoKzURODx9W3OWm6+OMZ71FekBf84tNUZR9m00z7YfZtPP0w+3pgeJzE8haemH6eRuNJJVwK376t/XaAdMEbPKg1QznZ/zwFTRPZa1L+sxFTcUGLvYmNp771qtZJ45+EwA9hCKo/C1EfH5z0RRl140w9O26+FnoN7fThBPRhBiMICxDWFKTKFm74sxqopwK3FjZHf3L3O37f3Sqevvz2gKF5HiV/fftKHa8YvMZGuBzW6Md6ao8LmK1QIbx+5hW89389UL7kQNKDgwwUBBASZRyM9hAMp3wcW2IO8Gh/Cb9AfZ8m0QClXAcEtEcShOO4+HLpIr6PeQ5DwR0MlPfM0i/TLBBPtoFlADAGQT0fI1GCwBmEQh3Gd3DKcaBgmlpSgQ/7wvetCWTMl8NPByc0v822EzAvv399c0kcrhTwesc+X+sFc3ZIaOQpcucVCSz7sti5sXHTdbCvKhEggum5OzbbgLHmCqPydkGiiTcHr1hvWYk3Xo02DJtT4qH124DN7kZGmjzrljtsm+npSKTDnCbQKIxZKwcWjS6WdcbZSOZF9N07DZItSlgReY6MgthC4hG7cuixpiUhS7XOdffUgnSXuzG/ebVkXYirQA83rbVrUTdTTTzZTmVviw7vF90uF/hspzVmQ/aa6tFVTfa31ruXaobow/Z+1teetb9dNNyMlvN2z92DbA/RzEfmSpCUd8HwoKbOt/6kGkdD58AZbc5DVuYnB03tMOnAuh9BYXec5l4ihwwZ1DEG95oQgCxzCFoWrHRZ4tRbVRiSW+OdvokL2yiu58iOwD1deVwqeZDTe+xAnPeFU+x0zIo0jTBHfX25mBxa2tfaYS63tj1TOkOKhoLpy9Pmqi+dVAAcJfDmQHJrSQGXnZJrbKRcqN1ZIy2z2jcm7ExYnlii6FFJjYahNPbj6AjDGa9yluYvtn1bLkmT2Ix1zlgiww17o9DrdjQ7k8vzrDZiA2mdcK4ertoa3bqrRs0K+cYAuhZvBd3cinudz53iwJLczT+lVgs4qVrxieLpdy7boWgt3ECcdtVgWAvi3hetJZTVuSOp3MjvfFXty8g/3Jc2FsRSxQ90jhp0lCluPGysoUAVPBkzhLg1iOHgQBBOUsYi95hS7kvnpOqNTtyiXEsxYb6j/cvxBup7YB1rcX5qxX59zeh0I8hGW16Hwz3HEH9sbuTtWDN5TR9rXRlImeNdXhPXXLI/SHs1s6VbqZFZqZNpuSdNEr+hKdGOV0W9S95uS9vEXLjSosAfUn4XItFm4QnENXaDDmMYmbYEDt0htdyuYs0O6iAWfAlLt2ZqY4R050Bl3O6Flx290lPiCLvy8sZK9/jgSMLKTpw70UUiyXb+MilN9bgkkUOhdjQxHtlEISIH0VHp7PW2tzJ42jjphFLgsV/v65Og7Y/Dqbpz3t02DlKcrUrEvkZ3eS9cVZ/eXXfkou5IG4SeXS71JJVDQgxENb6UKq83q7HsE3LcyvMqXeRJ6dtCf5lby7lQLl3N2zloiw0BLlwuV8+93nTz3pvJBVncU8+93Ub+WCR2QfGbppKc6xWaJCi+kxT4CV/3dyXzr4HSG9wFuR2258CVom1qFVJ3kwU59vCtlG1BMGIcGLOT5FHq1srUror3Szo2Tu418uWiD4azlPvLsiadU6sGTkIVHHLWMkG+FrqPQJ3zY5zOb5lR+mt94MfKKXLuujuuBWDtnWM931RDONijcJErodzCvpVTLKYHyQ51Gd+1Ui02hnJRLI2jdzNOx7yZ55cDCNBS05MkWaloqN0TU6LNNEOAhQclp2TaZSsvUyI78743aH3qLZFde2PYNNW3Q7r3RTtWw+GS0AHSmVYjqaoT7JDV7Zai1+vikszPR2floavsYlpL+sjLlEYNTJEuzzemwCxvTS23EcUsKGshMPjG8i8bjsVs1NiaYuUM7QE5Brxm2d6QqEA78wlulgPhXw+r2pFk4wT4g+FqhVLAWrlesMWh3mWcIJoOL1QInSGFKWodIbmOjpiAAs7ukLNNpB/ZakgwTcwCw9jSir6KAX85sTuQ4Ft9W0VlQt9N5hZIZoHFGqvv9VgppatyCl2nsrbn0sZHeb8lVtqu1EdlpW5NpyckoscpmJMrjUNccchDU65WqDrWBDHaGJ/hUeb7gasM1GFEiCAXV2KioZlYz4l5jmiaEXBu6nRKXhw3vWEKeZcTuEU7nuAGntkH+3W0zq9jdqUYegE1HpJbsDhc9iK13XN7r3B2m0u1Hxp9G7I3dCVoWVnQxD03o1UytGdNzA3+JnYdjna8Ya2Yfns5OjUBQoaLbU65ENxxj2i4FoLD7mRkIx/HgC1u+Uo2TOKY9wUilVoxL4/KVc4R+6aF6wUpDxFf7RY2sMfrzVnRPBNy4BShrR5SG0Rs9fW8NNdSsF1aPsVdsR1xaWkx0dPWza7HFuzNrHCJVsBxeSudIxVbNjV+V4Huq/iaRHi7k/ra6XW0VwOMdGN5dO7nDiUzSt5cahREalqb/Sp1Mu3GzdG8otzNAuzBcugPCSJzVr+8cGklU10y0DcBg5HGi0N35lmVx9ACkAkurWprd6lbDUGULa3tbZ1dIM7eM2zxwK7MuV0biFmtjZZN61t98c7xgsbO+8GmxfMhPQLN2+6Pl2KPRrxlBSuOKcW0k0m9sVXB4YxCEl3+AmcAKTJdYFmDRXjibq1ZrULtGatyG68s1jju9b2tJrfcuPOdC6mTNy5bk+tkbb+racIjZGV9Wy3y6qYbhzipjKrEUWbDKqRoZjcztWQmY5aNVmgqlQRXwzqqV7/anFjy2iDRdntv1+nZpPiG9Lfl4RSKd+Os11xQrXRpdQ0knI3mfhpr7lrbS6qzCmR+uIt3W+S2ehjGB/PENYm2SSQuv+oWYEa11Oml6BxtSxWW44IIWabIXdvD+SYPb6cju1oTHU/fVxgaKbDDx4MUUmLPMAy+0BuSEhV0fYSuRVSywkimZFdb0LUEsuSbCI/Ic3BxmqXCYOp15V1vyKF0990F18VluwtPsnS9UOaS3d3X3DpiUUdWlJ4cuHojyQckvm3j+wYrwJU87JX5CSYCr4CwIAj9wPvK3LxZZmKSNHlKYTcXjwVZhVrIyRVI1+tUbTiXGLV2fhYTRBAvSnOW95deXYXrze4yXhZbax2gYZbvSGvVcsJFPCzjE483nHwixDi46QXCJuSJJer1YMCUT2LhLJYHPLII56K6fH7RTD/kCJlOS30+RldB1zyjQXCHDqN7jvBZG28ZA0lZejVXsk1734TY2mrF07b00vWV3nW6rh6Ns7+LBrXK7b2FcayAUXYszXfSwCmLUxTNV5rFFJ6iXrXcV89ZdFydUF9wMivGJH5QxOF+OaLpbassSkla1FF+zPL1fOuuL7ug2R/CYXHga19boC7JzyvEMjebXPQZC1d8ZLFWJPaOHQoJPetX/3RIXFlvCUNREXc56sPILVnWHfdxHZ+vxqnWrlvcAld1q0e7rdRg6h7HSm9pSVapIFoNJ6Tj3ukVar3SwdxZN0UCDFNuZNfC5jZnUfNenFfXkkTp5RH21lag4wxFRDNd7Xdmw2+ZXrdy88i6AkuZIaGGZn+5XTf2kmEXKUuIjK9aOH+WOJMk5L71Dna1VVfauNM7hel36XmJJoUgbOzClc+t42jA6hn8JA+wJLHmaMunYWSGZr4/xatu26ni9aAIR4CpIBqXhaHl3F1csUPKRmaXyTe1qvmW3w6Ukns52N1zYstfdHnBHozNNsUam+IUzO2AY2yzNQ+EQPHmt4RDHUCcssJpUDxym5thqYl1bsAtKPvjqT/jkm02WyYjN5We1Htd8MULndj5dW+Zkqrf4TzHVZkgqnIvKCwlr9wEP/bL8z1eKnF5HMW1IhNmp4gIeqAaa3P2c4VlzZCzjZa31vYSngnSmjXG/Tr2wzConNFS95qUSNedvhfwwhEV16KljXvES+Z0dN1zMhAdqVI8FnCeGhMYdjsPJxQV/YsxrtldNxDuoJ3lrXtJcuMgKIzDqlHr3kh0faZSPXUTAwR4rOEMT5Hd2a+IiiIpJQuX6QIIGwJx0bidF4d9YVWA8P0QN/0abMmQkNc3J6WQ+0FRxbPehohxb/KVLdA8tqPkGxgbmIN7lD+4283ZNfreUrdnuuRLldb7iCy6hTKyc+tEbfVTvO8UghbUkSKzhRgehYTrKAwRsl5Q73sn7rb5TQ/Mcau6wmnRy27rxj3CIHMlsgKVkgba7dXh3mlXnGIv5Oii85ojD4IoL1w/CGguMCRalqgLNS8CHKXTmsAuQkfOMVISlyKtikiKb+Y+WwjHc7vvCss/mJxjhmsUc2x9HhZJtmFRk8HPkUz2fCqc83hHGt4RGGO7sfbX5HC3hRUGw5elFz0PvJELm4EY1bFwDup9haRVz7EkQmCS4xPH0dkOEnriNDvK6Y12IcZuk9x6rt7PCcYmNvPD6dq2/UjvikMUY/W2S1MUQy477DKnB2ZnSTWn6cwKFShpjnmbdcLiJk3yhKNU4tps6IaHp+B0kTXBNZjXHtjNj9zFsIJe3x1PAWzK8/kGJ4WGOgxqdoypeYpT1nqMV55tilfZvYx1t184itP6BDdGxDTIUPI4B6Bvc5R3Q3ZPjxIJVn0HrxpnVYw+bui8FhyzZZFaV4W8L3ZYt1sLYb/qr/BwKVA7Ek9tuRJxKj3q8FTaraXd3ZOiLlmjzTXPj4erqNrntLpsW5wcN0QvrBtrANuD1+MJOXe4OaNe7/jIytQR3Fhqu0z3gSvY3dDvdps+P64OYa4xNb5d9x653zmR1emdWMKTfaI4eGsHK8cTMQO1mrmGNgDDqaJoUA6LKfG+NOpR3aycvZuyKLXsUIlb27v9SB5kibmn1zqat3BUUimsKu8pFR7xaPQ3awdXsVYWjnNZueiwfahu74mppzjzUPcxPjjw1hxlWMivq7pV0ZtDmP6mLBb1rSHtklro5Pl67JE9HPPy1RI5dku7W7GZULPrmCpOfb5UqoKRNYmlrwJteDl9W3FDsLmTOrmvs3mRdvaq95Wq9XY+Tq8CDisYalhUHd0GSt3iVcEGl7kdLN0VGzBdPl/ehIx1kbNsMvq4PV8WtNcSKcmZaUwuXafT2t5HkINOHXRG6IbLgap30UKaR34nm91NXAH5Thd4v/J5tlze9kzpyguwiS1Ob3ZLe4PMe+TSC8F53h+OjMLK63R3OWM0o6hMWETo6DMLYV8VBxlFAwn4pnsqbzKa7oQzcSmONyaHNL5U3EPB8gVpbC3HQe9iQgnKTZPOTHdw8yXjOm7n6n4MFoJ13YZwCD8t7DV12BtrdYzogFt5xv0AxDndez1bZ2wVkVtRt1iiO0HeYxcGWvI2a/eUJLJyIDUdKFkPYqkiwmbcs/d7zuv3ihpTF1cZEISix4WMVO+ZeRbO74PjVmAPExNvhb15TXx0TMWoV3qdX4xh6mdFlPpkhRt9uma0ORjcEwMjtBnVzGRpb4XW+aqojEu6isQ2XEaW5AUs5Cl/G9snWHFZl5/vylbAfM+LRrLKGARyH+5fF/hmUPk7ltEly7J/ffvwNj2Efj1K/rd/RZ6e6v0/e7j4fA749Semx2Nk4PifHro+/fum/e3DG7wPDXs+UK3TNnw9dvxvj1M//qs/UExShucPtdMvY/fm65P4xgmn/3z0Fud+WzfVAG1L28eD3Q9vblvHD8NeD7DfHk5m5fNp+Mup709Hm+JL6Uy4xvn0Uw/wY6cBr8vw9ZAZbhxgxGKv/oKRxBdQlZOzr587oI/o+/Idefvt/wCLwFlQ6SUAAA== -->
