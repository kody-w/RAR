---
name: "rar-cowork-cookbook-demo-data-analyze-sourcing-effectiveness"
description: "Generates and creates realistic demo records for analyze sourcing effectiveness in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_sourcing_effectiveness", "rar_sha256": "93e83209aa747caad617eaaf6f7c79606d4dc21ea1be4eab757056ced153413f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_sourcing_effectiveness_agent.py` and embedded as the fenced Python below (sha256 93e83209aa747caa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_sourcing_effectiveness_agent.py` first:

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
    "version": '2.0.0',
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/816adOjVpL1X9E888H2qKpAILFUR0cMCC0IBIhFCFwdZZbLIvZNgPz6v78XSVXlGnf3tCfmw8hhP0Lcm8vJzJN5wb++OV0bFfXbxzcNOPls56RpHIF65uT+bF30RZ3AP0Xiwn9nXpG3dex2bVE3b+/efNB4dVy2cZHD7TuQg9ppQfPY6tXg8R3+SeOmjb2ZD7ICXnpF7TezoJg0OOl4B7Om6GovzsMZCALgtfENCmqaWZzPnFkDZbnFMGtB7uTtY1tbO3E+LZ/UlHFatLPGg7fruGg+QKvA4GRlCpq3jz//7d1bDL+/ffz1zUudBv70xkErOKd1mKdy7aV783vVUEjq5CFcXY4Qmxxel6CGujP4kw+C2evqxwakwbvZf/xH0jt12Pz08VM+e30+vU3/qF0+ayMwawunaQEExSkdN07jdvwwY9LeGSd82q7Om8lVCG0efnju/CapKGd/ne79+FTyIQTtj5/einLCGgL/6e2nGQTl01vdTd8/TFLKH3/6kBY9qH/86ZucpnOv0MVJGLT6w+fX9UssXPhtaRw8tP4VSn2G2AWf3n7n3PR52j35CXe+fbgWcf7jU3BZF7cpWh748ad/JNaLgJdMefEvyf35KTgCjg99ehn+07sHyH+bzV8OfZX5j9WWMKx/xhO4/Iu6d7MXUP9I9gP//yI6jWE6fUX874r7exvmf539/A99+2cb3s2CTzDDU5jHteOm4OPs18+asln//IP/7ccf/vYbFP3finlUxkPC58zJ4wA07efPP//wKFYo4+cfuhLmGnCyz12d/j2Zfw/Xh57vEHyt+vH7vVC/kSd50eezr5k++7Uo/63+7cPsDBnF//Z783H2+3qZPvPZ5MQXpU8IflczDbT1dzj+9PYb5IkcetN5j9uwyv/932fH2KuLpgjameYVXTuDAW7jDEzG61EM+al51HYNIK5NDIF9rYP5P0V4srgIZr/8p/cg0ffei0SRiQc/+5CCPr8I8PMXAvz8HQH+8mGmQ/lFHYcxXDhTGUX5lDshgDwIdZc1aEB9g6ziji14D/no/fRlos1f/lUVnx/SPpTjLw8yjZ9spa75iamaLgUfJm/NCOQv3zzYIcAAvA4qSgsPWhXEkGrfQRSaIr1BppuQaZI4TWd+DMkedorxIRui93ES9ssvv7hOE33Kn9SKz54tpEHggq/mzN6/h+4FaRxG7acceFEx++HX336Y/b/ZP9v1ED7pUCDVv2IDLTxosjSDtdZlcNnUViAVO/4jNr/+9gIZioHNawYjGQcxeG6GuZoA/wvi2p55j62ImQsg0hDlrCzqdupCcfthxgezr/ZCpdOtidGjomlh2ytB7oPcG6FUB7rzFcl86lwwIZtgfDfrGvDQ+os7tTdoYgaL3ml/mR3XCuwfRQr/M5n5WAQ3F3kM4f+aD8/foZD6h2bGfhHxYSZN2Tkrndopo9p56QicZ1ymHvzaDoU7sxz0n/KpYYIJqkepPOEJp9Y+tfBHSN9PMYezQAZ5wW++6A5f7d+f6Y9uV3/Km1cZODV4NH5oyjgLu9ifmsNfXinVREWX+g/8oKWTpFcU/FdUHjnI/PNZYerqs6mtz15TyNQSOwxdLGf/J8aShwu7nbrZMfqGm20kXbWe0E4j1RSC5xQGJ4OnsKmMvk0LX7jmC+V+ytMY5kk9/uW58hGQ15onjXU1xE9l1Id8aBiEdpL7SNYp+ep6SnPnU/6F299Brx5EBuMFKxtm/pRwXxROd79YGsHyna6/9fkXfJPnMCFnZeemENgAAN91vARaVU8F94oHzFwwFV8fxV70nVczKB0mCJQ/g0bEsIQg/z+gkwroJoQ2qIvs2/J4CiO0wu88aC2cWcGHmQlrZsqbBhYqHIGmNRCFHx6iZhmAGEMTvyLcRE75NGYac18GOlMsigymye8j8Lr5LcsftkzmQ6nOxLWf8n5iXx8Mz8h+tfMVK2hsNtXlY9P34X75Ovt9E/rLp/xh41fCh+WeTv37d+DA/KuzZ2JPbNVAxsnAK4FeCfyk8Nns2c6/2vLxD7P9j39u/H/0T+P7yH2cRW1bNh8R5NnzvrS8D5ArEJgjcQmaR/t7P+H1/lVo778U2vvvCu07+U+4Ps7+nI3fiXgl98fZ4gP6AZ1uiTGsT4jJ6wMhWb9nrffL6e6nXAXfYv1KiIlx0xH226/t58sS2IPCGoTT4mc7aqYu1sPG+eBfGI1P+dd8eFULpPc8nHpnU/yuih99GEb3GbyvbQLeyluo25+muBBM55x0Mr8Bbx/zLk3fveVOBv71883UEWDiQkymwxEsIjgbtTF4XH2dk6aL7894j/KCvOAXH6cqezebZtp3s6/j6bvZlwPD4ySWd/DE9PM0Gk8q4VL45+varwdIF7zBg1o7lpP9z1PQNJG9JuU/GjEVF7TYm9h46luvap00/kEI/BKGoP6jEPnxxUlflNG0ztSz4/ZLoTfQTh9OQO9mMIKwAGFNQars4IY/qoF6alB1sDn6k7vf8PvmVvH05bcHDO3zKPnr2xfqeMXgNTbC5bBG3zdTe0RgtkKF8PqZV/De/3igfMmBpAcHGSiIxgGFYyjtOOSS9BzHJxYkcJyACEiPpAmU8Je+hy2As3DBEjguuSLRFQG5drHClws8gPKeWfp5mgXiyTbMcTzKIxdLnyYduBRHXdwDC2zhkzhAVzQeUBSU5X/bmkDGfDn8dHBC8+tsOwHz8vvXN5dYwpX7ZcMzz88aoc8OgZGuGrnzmgCWfUF4NzYqXQdiXR/AYm96Ls9kHLg328KoPT5ItEPlLGvGQ+tDtZMjjmZy8qB0fhcw2WBkhLlj3JLHN5me3lfpOKdWWBTGjJUDi8IQtMm29iLzImrw1FGwDwJeRJ5zxEBsLeI7ft1ip4YS9lmq3VxXJBHCRfl7XnmNYF1W1z01VlpnNwfdTLWDaju1vSluyx658fl+l/Faa7ZEr8keVTdEX3XeUMrZQh83w1lfe5ZYXbSlGaHzTtwOQSaiZJDf6euKIL0Lvgwa8lz1qmycDH0Lzlh7HrMyVx0stcPkBtb9HRT2bau5l8ghQhpzjNG9JitAlDkELQtY/Shs5aouDMFtljediwvbKK7nyI7AkLLeNhU8yOk9rqzOYuEUvI5bkaatzLu+vlzMLVba18ahL1XXnUmdJg6GhOuoyl111En3YEvud+ZIbNeCBC68lGtMJF1I/qwRllmLrQk7E54n1uHgkUmDhaFw7+93Zz+el3XOULuLbVcoSpgr7t7ktHWgt6NoFHrT3c2buc3zrDFiY9E54VxWrtoa27hsK2fFsaIB1RyqgmqrYmjyuVMoDLGtfDW1OrAVanaXSJ4+bDMew5p9BeL0Vo+GhayGvuisfVmfbwSZG/mwq2uxjHxlQG08iIV6N1I5ZlBRJrnxyFljgUnL5J4tVlW7MJwl2O9VIWMWQ0xKA+qost7qqyrKtRTfz3nKv5wq0AyBdWoOc7U79OtrRqXc/mh05XVUhhxf+Pe2IqpTQ+cNdWp0aSSO25270w7rbSIqgihntlCVGpGVOpGWImESywpLV939KsmD4PEbyl7N91fqsN8p6Y4PFxGHePvVNXaDG07TR8rabzF+0Rw7NtbsoAnivS/g6cZMbXwlDFtQG9VQeNnJKz0pjvDr7shZqbgcHWHP2okzrG7RgWBuPpqUpnxCiYVSyDdqdT8xibSKnIWOCWevtz3W2FGGqq+kYhn7jdioe008jWo9bL3BNhQhzthyYV+j4Sjur7JP8VeeQJobYYPQs0tUT9JjuDoEBzm+lPJOb9l72SfEfWMvOFopteV4K26UGs2Ve4Em1glv/VuG9LvulvWLvdHdrkwr3GokEizkct5tIpW/qzDWtoku9vvN3ZGdcXEY+qhPo9ht7pu5W1SCcjVBEVPYWTgI6ukSoCfZ3gwjfz7yFHJrBD+XY3RAPX44+kGwuxxWmyJG9mvHVkMkqc7yvdRtFLtSBrU4IJooxPmxs/en7F5DnfNoyyHnJjoRm1si7U1c7cTNKTweqZOJRStqe9kesnu262xsfzrgkqpghy4LeL3BCQJThXRTpjqiFkVoe1Uc7V266wCFtFqyZ0V+7bfM9io05/4mStV86HFNcDdZx9u1eD9WR2eVpaywKgXbPxMHUdixuYCN2n3jc4lyIBDRbAbHA56BqRXnn8VW2c+VA1WFFLM6isfuuKqXzNHGtnhOqlxVw3LvTss9Xhw4nESwYb5f9VlPdIFEslv9WPKUbi5SC1T9/Jj04yrlPSohDnxPX5Kx3gWc1Z+tZUwd5QJPGVf1cnd3u0FCV4+irBWLY6BXK/92atZRMBrYIicKCqNQNQCss84S5pJKXcLxSLE8LJ2M21DHKmZOq0NvZfxFv/CruCWMudGqyCZhMC3buOZ5J+QslmoDT2rjkHnmIV6n6vqaO5rFN4vofob5iO/38ToRK4yLFIbyTa6xM/uO5/fucBz0I0HMRzfFgrweEUXTdD5tec2mcVqpkqSYC7iQAlc5JfuwaGQlUO79QC2W8jhf0uHc3K43yj4/7nFkNecbNLBP8znoLjrGX4TdSkWZ9c28pG5mM8y52cmppJ9W11xp1xyfHrtUl4ujwQXBQINj0XNkyHfhwh5ptlK2o+B0o5CYVYomTAPUeHXIpDNDsaqqrK2iHSMlVImzlqorPXTXtkLgRsqwc9ROOclUkbG55/sNyi19hBGaK9ceIVaXTvOyLaVRG2NuFz2ZifuOxW5+cTnkooVJZupRu1I64bivRL3Nb2rOv5WOHWU+lRFev11Ux7tzjqxFlNOhh9x6bGNni5gMmoWPWTvEbui1LVh0shbSY2q4dKNcMEiWywu9isLAriwhispOFE07dw/pylBuBnUcTkFQeYwn3coTDcvYgMl0utleWlfOoQgvI8bOq8RcFaMWMOuSultl3e6Y0lMV68x3K5i8y464JPelVgdCSCUFfwlvJ7NdH/t+vhbJ9UUEBzR3Rk9BnfJkrEepc+7VeV1gVD+kQ7zUT5uw91zsQgwm7qwu6jbqocWYd9jKZewD7GYejwUMsihbqcnaq7HEbGd7WiPBxciW7uZgthc9asndyUW19mC0Tm+RElI4qZH4OY/sCjT0d6S5i1l0L944/nD1tkLVYFKAEgcNXBk9LqqrJSAalxncfr7tWa5BxE2CbRLz5KOwx0qLWItjU+RzltnIzVV0+XTPnwTFzHqajH0NpwstCe/9USxzBGfZGnJOvBokUWSNMWHW2zuQypi7tTvnLPnb5LzF9YgkyGieuwtMdykmVO0Vh/P7blGb7JpfAf9+KyWRG7ikQ7rULd268ncavTtXgYZdHJgBl8JjN1dru75hdMOoMSNsNbZBeceN0kS0TMMKSNY4nOPdjaH3KDBd6i5V1tGhWBa/ZzJPulR57mlYsiV6Fc2dpEUqemFSRrA1WjC2gu8IcCHMTeLCV7LZuUJlm7fQ4xhmd0Libm6hG6RljzKLDpwnKN3aLTej1MNJFrb1DWLg54o99DF7t7ZJue9Um5ErXQuG9WJEO5j3oEoakhHHAy1qOZ1xppwlS+hquFixei5XkuRt7HlRC9sl17jSXor3bLfpPS07aKW83RfnIMussCCIE5f4pjyaQ+ds5FuGb8/N6ZwIwfzKcdQ6GYhTAfxdKhMeeViH2rUh5OE4nCtDQh0tjbuwdQ3eRbTz+WZzciTJWwoOst1p7uwCNp0DySJSpMFRib50Q7PjZI0khl5A6vkGGOy1AqdzU+cmEQf8aOX+WDpShZdZnmRuwzB5fNnam3q3zK10d+j7du3z+PrEb92btx9uWtkMRqS5VerHRZxcFqGLbdYxRaFbV7WoorEdG4tqenQGjA4v1GV/QduyiYTo7CslK7WE2Qhr89Q6/IGE3UOmIFXLLNayo8e0SXfe7caS2CICi2lE5Q291xlCO4z2YC3BXTt4WpSdcHiW6c9CXZb8Cci7+2m0a69fJNQQkWFmJ7F/uDnJ3bpGGbkIKPPKrIENPN10HLlfdR7N5SXTpLKYaWs2ElitBEfb8C+W5B/tCHPBSqbYqzLyxy6zCRYs17yIgBETgg6Xl4sCst6REhBntTrzboPS41U6pUE7rHHHWMJZIby59IbUwz4P6/B0b50DKSX7S25bZiYT2q3k78rO7BvDyq9ouxAvvKJ5diQLLG6t7zykm6K+soV71sJsvXHtsQwcvW6D3Bl2FSk7DNMwAlZ4R3RzL5bdTfSYMtM2G3LLIrshh0mXni11d8I0eTihuoMNK2M3hoM+v4bZWB8W8JQmYVI3l1f+9t7dNrf02hYaMS+zDaOCNMbThLB47HaQC1lwCRRODEf8vKA2Fe7kAm4VFBIx6UBI+AJ05OV6wRdYILGlMqdkbqzwduvTRnBhhgsdEyQbNqRFSQs29rZGquB1DBxPq3Kf7YqrCDcESzicYrZB5y7MQbM5Aow3K6yMIN/y9VKTTG+Zp+sFGyAuxlL9deSzO2MCF1/J0hWO0HON6RVeDO63KpBC2Y8vi63DK0aGtBjvYfJ1HvK4j5+jiqwpZ93PfeycrvDeTq4g3Q/Y5rbI8Ia2lAWQNWuezRGkEJBiu7TPWY3TJ2RoV4p97zo5WNA31LiUemHptYvuqGqrymHtXZTTQMiFiNLMpu3QMadZ9XDcMQ2N9PXaRkNJlmuFOaFLKqTKq7fr9T0fZHeZqzvRlsQOF+YrTGTcFM/8/IQCKeZq8RIK6lDd5wZKjlGOHkKjGeXkzonLHVqPOdgfzr1iXdo7eY85Gtw5zx/ypXpyuS0CT8Gi0tyq7tQh9DIljOHMC2leca2SqXS33G15FW1WiXRHXU3f0O7SkeixFZGjg+wQ2qJotQnFrujnYWaEcTdEZUvtB1RxsSDxj8MWo2FD6LfXzXo5tvrOwm65DS5d7y488i7m3KiW+BU75DRFw/NUc8SY02WZnVGaG9zmiDsLjo3Jfpkdk3kklaw87MTFda7egpMhMqGe7vK6VzB1MQijD/vmXQxxNbzJm7M6Lg1OOW5bca/IfbDTvLEWd93BHxb5/h4qW2FIKd5ZRoO0oBKFJqT9FcbYwkLaYLFDKezmuHx30/Bk7CM5WQeskJA2etiGK9RkBm4A10DXogC3HHQ4Ysg6Wepd2fQulbYOfRtw9ew24m2D6XlZHmLY63o4ELANXgaN4TDj6XJdwKGWvLp7i6N9FR9t/Ha5XMV8Ew1cRuyMofcRy5KHpeXMrww3eli4vIhLYaAZDOmOnSMNdEkyY3jhDpbfGot7Q3C6ivhnN8F1vMth643Cai9zNuCKKgqKO1izR8Vjttv76TqIhXtRSSs5MStTWRYrcWVoSgJPiWie6LZEn0UQ7yNC1P3liRyW67lwUxE8vV2ClTd3bX9xOTHzjhqREtOYOakodGkoEoNXtdUSWcZ3HVLQ/l1EhdZl0QJbBKkfknUFMgzkpBKENwieynVnek0Cuw1O+pqyryt2Ea0rntVXhklqmD2n9tveuTrqctzVbVrfQmFe02EQVQ5rbYVTV9dLwvFJVt23WY0g8l5XgV22c2NJNthVNw6teAL1eGOiM6nIDFcALGAYSU2aQ58MbaxLuCyeUoMkAcjFksBQHGAZuaHnymAeGJMbr/NxiwOz2Po5t5wL62UZO5QOB9FVyFpH9rJGIWX37B1chavAzstWg2l8j0ZDO1nzs+jQ2okWQOzX8iU22ftVPuZXE89lrJfmNMJoS5ElDGuP0BJLxwmKXyiTD1aRpZg0x5P0VdD10AkzaZ6rMiGxe5FM9aEchA2RUlSC5eTlSO0z6diyyyXXHmRONZubwO00n23X/WaJsJCniAMzXkcxlxS5jp2j0lXUissXpkR2Pqb0xP6G7qNSCVOTKhmG+evbu7fpIfTrUfKffos8PdX7X3u4+HwO+OUV0+MxMnD8jw9dH/+8aX979wbvQ8OeD1SbtAtfjx3/y+PU9//qC4pJyvh8UTu9GRvaL0/iWyec/uejtzj3u6atR2hb2j0e7L57c7smfhj2eoD99nAyK59Pw19OfXs62hafS2fCNc6nVz3Aj50WvC7D10NmuHGEEYu95jNOrD6Dupycfb3umJ7JTu873n77/+uuNZbpJQAA -->
