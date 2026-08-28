---
name: "rar-cowork-cookbook-configure-plan-workforce-capacity"
description: "Applies a bulk configuration change to plan workforce capacity from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_workforce_capacity", "rar_sha256": "13e224d96474cd4dbefc456b797c68181c70e2bd13e3088f8249a9b35890441f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_workforce_capacity`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_workforce_capacity_agent.py` and in the RCI capsule.

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

Plan workforce capacity Configuration Bulk Setup — Applies a bulk configuration change to plan workforce capacity from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-workforce-capacity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_workforce_capacity_agent.py` and embedded as the fenced Python below (sha256 13e224d96474cd4d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_workforce_capacity_agent.py` first:

```bash
python3 configure_plan_workforce_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_workforce_capacity_agent.py   # or on stdin
python3 configure_plan_workforce_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce capacity Configuration Bulk Setup — Applies a bulk configuration change to plan workforce capacity from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-workforce-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_workforce_capacity',
    "version": '2.0.0',
    "display_name": 'Plan workforce capacity Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan workforce capacity from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-plan-workforce-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-workforce-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aba204977e09b4b4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-workforce-capacity'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-workforce-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePlanWorkforceCapacity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanWorkforceCapacity'
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
    print(ConfigurePlanWorkforceCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaeZPiVpL/KmztH7ZX3a0bQU9MxOoABEIIdCHkdrR1H+i+Ja+/+z5RVLW9Hu+MIzZi6a4oJOXLO3+Z76l+ebHaJsyrl88vimdli52VJFHoVQsrcxds3ufVHfzK7zb4WTh51lSR3TZ5Vb98eHG92qmioonyDCyniyKJvHphLew2edD6UdBW1vx44YRWFniLJl8UCZAys/XzyvEWjlVYTtSMC7/KUyB0EWVF2yw2g+MlCz9KvA+LPmrCRWclkfvKa9asypPEtpz7om6LIq+aT0Adb7DSIvHql88//vThJQLfXz7/8uIkVg1uvbBPfbwzUOD6Jp99igfLwe0A0BUjcEcGrguvAiQpuOV6/uJ59X3tJf6HxX/8x723qqD+4fOXbPH8fHmZ/8lttmjC2VKrbjz3YZ8dJUDEpwWd9NZYLyqvaatsdlQNvJkFn15XfuOUF4u/z8++fxXyKfCa77+85ECFhwO+vPywyCsgr2rn759mLsX3P3xK8t6rvv/hG5+6tWPPaWZmQOtPX5/XT7aA8Btp5D+k/h1wfY2q7X15+Y1x8+dV79lOsPLlU5xH2fevjIsq77zMyhzv+x/+jK0Tes49iermX+L74yvj0LNcYNNT8R8+PJz80wJ6GvTO88/Fzun2VywB5G/iPiyejvoz3g///w/WSZSBGnjz+D9k948WQH9f/Pintv1vCz4s/C8vnJdEHcgOO/E+L375qpw37I/fud9ufvfTr4D1P2Wj5C0oiZnD19TKIt+rm69ff/yuftz+7qcfv2sLkGuelX5tq+Qf8fxHfn3I+Z0Hn1Tf/34tkK9l9yzvs8V7pi9+yYt/q379tNDn6v92v/68+G29zB9oMRvxJvTVBb+pmRro+hs//vDyK0CIDFjTOo/HoMr//d8XYuRUeZ37zUJxcoBCIMBNlHqz8moY1Qvwf67tygN+rSPg2CcdyP85wrPGub/4+T+dB25+dJ64Cb9hofdIiK/v6Pf1Df1+/rRQAeO8ioIos5KFTJ/PXzIr8LJmFlpUXu1VHYATe2y8j2Dtx/kLwMrFz/+U99cHm0/F+PMDOaNXfJLZ/YxNdZt4n2b7rqGXPa1xAAp7g+e0QEKSO9YrDtcfgN11nnQA22Zf1PcoSRZuVAHD82p8ReU2+zwz+/nnn22rDr9kr2CKL177RA0Dgnd1Fh8/Arv8JArC5kvmOWG++O6XX79b/Nfif1v1YD7LOANYf0YDaHhQpNMCVFebAjIQKBBaAB2PaPzy69O7gE0GGhuIXeTPjWpeDLLz7rlvrlZ4+iNGLhe2B1wI3JvOrQUg9CJqPi32/uJdXyB0fjRjeJjXzcL1Ci9zvcwZAVcLmPPuySxvFjVIwdofPyza2ntI/dmurIeKKShzq/l5IbJn0DHyZG6Q1bODgMV5FgH3vyfC633ApPquXjBvLD4tTnM+Lgqrsoqwsp4yfOs1LqBTvC0HzK1F5vVfsrk5erOrHsXx6h5ABDzjPEP6cY45aOIpQAK3fpP9oLHmvqY++lv1JaufiW9Vcygc0AiA0KAFzRq0g789U6oO8zZxH/4Dms6cnlFwn1F55OD5T0YD9nejBDNPFwrAkGLxpcUQlFj8/04es+b0bidvdrS64RabkyrfXj06j0uz518nrIeovHqtnm9jwRuovGHrlyyJQHpU499eKR9xeNK84hWodRcghPzgD5IAeHTm+8jROeeq6uGML9kbiH8AnnkgFjABFDRI+NkdbwLnp2+ahqBq5+tvDf0R08qdTQd5uChaOwE54nue+3BCE1ZznT0DARLWm2uuDyMn/J1VC8Ad5AXgvwBKRKByANA/XHfKgZmgxB5ReCeP5jEJaOG2DtAWzKPep8UVlMqcLjWoTzDrzDTAC989WC1SD/gYqPju4Tq0ildl5hH2qaA1xyJPQQb/NgLPh9+S+6HLrD7gaoHYA1/2M9q63vAa2Xc9n7ECyqZzOT4W/T7cT1sXv+02f/uSPXR8B3hQ5cncqH/jnAWorrR+pNwMUjUAmtR7JhDIhEdP/vTaVl/79rsun/8wt3//10b7R6PUfh+5z4uwaYr6Mwy/Nre33vYJQAQMciQqvPpbn/s419rH91r7+FZrv2P86qfPi7+m3O9YPLP68wL9hHxC5kfHyPHmtH1+gC/Yj8ztIzE//ZLJ3rcgPzNhRthkBI31vd28kYCeE1ReMBO/tp967lo9aJQPvAVh+JK9J8KzTF7RBvTKOv9N+T76Lgjra9Te2wJ4lDVAtjvPaYE372GSWf3ae/mctUny4SWzUu9f2bvM2A9yFXhj3vKAugFzTxN5j6v3GWi++P2W7VFRAArc/PNcWB8eEPlh8T56fli8bQYe+6usBbuhH+exdxYJSMGvd9r3/aDtvYDtVzMWs+avO5x52npOwX9UYq4noLHjzf08fy/QWeIfmIAvQeBVf2QiPb5YyRMl6saau3PUvNV2DfR02xnTQexAzYEyAujYggV/FAPkVF7ZgjbozuZ+8983s/JXW359uKF53Sb+8vKGFs8YPEdCQA7K8mM9N0IY5CkQCK5fMwo8++vD4pMBADgwqwAOKO5hGOGulwRFOC7hgunFIcilTa0pZ7lCV6hDIR5mu4AOR1Yrf4URa2tt4+RqjRAE6gN+r4n5dW730awUZlnOyqFQwJWylg5YZ+OOh2KoS+EeQq5xf7XyCOCf96V3gI5PS18tm934PrfOHnka/MuLvSQAJU/Ue/r1w8Jr3bKNsz2EPDQl60FWyYtyj/eOi6W51UjmRsfOskjxddIcylOP0Kf+wK5Y5xJId3EoTwfRv+vQzVgfsnVPdAx7J93SVyPN8TQ7Wnc2uvYNm9nT4c6eBDMaGtWIUDFVInnc7NO2KfcaKXbr4741Lf10LCgdM6+EttXdaLuG4fvV2W6uaSLrynBULvZpkwrkvUusSBQkKuyU+HRNmQOJAHr7hINtxOaSuuU+JZFGPhpiIxXEaEz64ZKOmGAadGJvCa0ocRqRsmwguqkenMyul/AW81qcXEM80aLCXY70MarDJVYkSkztE+EAAtPww1TGJhxVdLZ1MaHQnBgX3O0kON1Z25j7G3e575elUirkVViRp8mM1mh1L9Jy2Vw6YaJbdjA3SwmdzjqLXXO20scKKY5EqqVtzbSltV/GqGZLiX2poKrOJ9sQzAuhJ0o+mFpl8O2W5K/OcnNpE60i4eYi8AmNXVK0P9QDjQskVjctEffHzNnsVgxtKFtjckj9bFsET5FIm0IHxzwphDEhU8lkbKOXCbNqSEEXpM6JkjAhczN3zsggDoeKmfMAtQY30o6HPhMn4XBAqrU5IhXaaESl9EZCGFkZsmzRaxSL8geEXuJZaVTZ8ZQJJIFwe9e9dOr52GTZmrN5O700ZYOs+eOhce6FbULJPb0NEYYQUa4fU4zaQuZUQvX1kKKrjmBHsra4oG1Yg2d4tGHMIBC7tixE3RngvOXYXjf8fBOfzirP7527eWaUAWWO1gVmVgNsN0V50HVNdzMTSc7cbpBWxw0lQgGo7kuTxofa1kB8S+xu680+Lc8JlOVFRognfskfe35aqRlhnfuNbkHI7R5xsAHne19d2ueuQKBe4goju6brlWoUPnuOYps5lLdO4GPtftf7VqG0O5EHjSmeIhrxd2JAJOvb2lrBTe8w2VZNWcMoVMV1ImtKgt4plraSBDUpXyU1Nm7HK7+ht0m73egnf2PJEmPhe6rY3A6izrPtLbJYTVa3iXMjewLjIjSTSD0JXB/SRBFDagQFBZ02m0q9RkNYxNOKr+5msDrcEWxCT01tiOpJcVcWU7SQEmUGDu/gyRlOyJ5cjyfyXPdMCmO6sa3qLuzjgyv3oYbeVd1WW0867EQPlWULO92PntKxdtbycVvGuYbVJhScDY1IN5PScWF5yKTSv+jLdMdMJnwksd1SXCM0ec6HjQnDZ8nfJ9qVoO6GEPBrpLiAXYXZqWOHqNT1rjKufu14fWNPldRC5KVMoDK7FragjhZVuR2nh7nJLVeBssshn9EhRZSpHajzjbzJYkVdKXaTKBsigaD4rhRyxmgwISS303IUWN51c3xyfEXL+34gyLTpLw3T6AY+RkvNcQ5IFDCHqmasZT0N8a51C1PeI+i+0/aNy/Ob/SULDH1FHLCY41eUm1SK7aaldHalXGtk3SZQbHm4B7uukvg6IqZ91gcZfMNPfnmwt7cuU+JOsQ+US8EwcoKc4eyPFHS9THhNhvv7qNTd1bLcw8h31+jmeksew5Ttjr3p/YhXUShHB/1G0SuTSuyePsISh+gTRRjSXuEkdVN4K6xKsDU33MNT5pnWOdbJpsgYnGDvm31wLQXd2SMxFKtHecuT6X5sDTpjDs7dJyxJ2jQlbtgXFGcFhdns6fKodIJ2MUlh4rdhyUoIVfTtZesocdhlqS2EoZpPOhp2Bn/27nVfXiUsvRvjtasc11CWpnuNJe48bFwcXR5ao8C87rha7g8gn2u5wHGjd3ToII+Gk56g2uWydhVF5Bo9sfwZze/1sfVutq/SeLqPJSOWEQiCpf1x7cVHaJOtBq4V8EFBMNPEu7K7HUzWFfZOFLP8ySETU9YS5TjclqUqEtSux3PM0hy55aOR09VjvzNqQ2hLal8y28O5s7xIUk7L02mDKrYvmMcuOQidAmEaaZ2VVCylUsmRq4FauxsRF1IkxbuKN6JcONecY6V5YuxooSNb69Ld71N4ITPJzruadWocP+SWkG7yIQvwY4wum1Pv8urW0rCEbszqGhYZznVjPwS35YbyltcpBsgqIWRwrETPGRH5BgUZWTQTbpiCpcqUp7bXeI+a45qBwp0g5+FBN46HPbF3To7qyNI4lftIWw3IcGmnpUhjSzxOWfq8LatuTyKFe/N7hy2jCtE19sJK5R1WgryqUH2TrZe4S1DuDfJvrN+cTIk/N1ej1KJleegIiFCIXVKO+8rFjXyrKQSj3vRpMg5+H1xclnBbBVStZo/ZRSXFNtVFB23vE42b45jq2qRT6uAgoiluJYgQzoGVF4F43OP0tmeOvWhGpBPd8atXcT0cCgPDKyjC1OFKc6/FqRXy/mryRHRg+ABJuwpHKJ87jamMhEdFhKc+Y6JoQxw7TNpa4y0ISoWSFVKgoKmRPZAjfk+g+gUalQRkQ2UTN4jCFXmXX5MbB13R1I1oVaDuVrwxY8kTVlxVLu0lvcly19moojZ5mcyqyE3o9a1GhLqF38dQMMhWY87SGB6bTXYawzbAplO5SctyG7H7k8K4WwY1E3YI9v1OVbYlx8WFDW20ZL+VAnx58ttb0pJx1ew8Th6nRDQL2rt1UhsyS2zQxoSxEXtlCnwHZ9SI1qtBYrB0ZN2gWXrMGnT+bCdVgQkjXicTwRL1DTNBRAohb1GzU0tbWeJWFsluTrSbmN4vu5bY8fkmZzcOU4u7LEhvjD5228AjYu1winZnZpTyvMbNpa+VOZqwsmodTnraiswtW7HFCJsZu2nyHN1vDd3L2NzE+5Hd6OKaWpLTFcw+eSzchORSo0ygnumbBOIMMDAhK2KTRuGJD5FlQhdXrt1gFuEIcu80TFbcl2Z/SaLbFgl2x8y8VIYMb9L1BRmXYMQzGTGtcdoaSeLIGlO8Fbn04LFic8NthGEyFN3UrG7qaiJOskWHPnU/SCu0X5V7MeBURICRvX5NDQ1eHxNlV2cDZ2bw6YIsuUhIp8rEQUEZS4FJT0xSLAfBR9byTmATzkXd9BSVqyInrzYumt4N2ScN2VxXF55kzSjRba9JVneRSAwAUrW5H8s9QokpOdwgrUyjKcESDb6uHLgslWiJ7zDXHYvuiq7CDTw2ozDaVHJOitR3lC2ZDFqoSt5BOsgrhz1qJ/Uu0bV64PWjfNmh2UHThgRGlHA7lBlNOYcLvTbzU3sPyeHowCLnNGcrMzSSYibUPNv8xepOnJzuTdxLhEhg6WRTXSvXI45OdpX3GM0SDYPTbLNrVZGXEewQJPTS1ZhR3rJrtWx2R+4K91AacDcSPoft/o7jOw0/Kl6QEXo47aIKj5Qik3IPEcpkkygV1Io3ZunDWuEJ2vaAB262I++rydy0YBy5rQVis0cdi7tL4UXUqqI6xBbCiLR7bb1NuRlAMLadyqw5g95SpTxohHYCGOlg7qlkZSa2uU5JTV1gSeLWyO36pEvdRcTqWxAiFX2kJtXd9Qy0LFLzcEOUrYYivDL1+XA+DGkQBLCItlnipFGrAxA5cLfb8RRY4la/E8CbRiagJnPem0i2TVflNcEgcpcsw3AJUCigj5dA6XzN49u2mTx6qwljKA4mPNQEKRy4Zb3HTVs473uXaewbYbE3DemmmC7HkqROyKaSdamlmLr0vEimEEY3jGnH7XcR0bJ7COxHfJHkyyJIOTaMR2+37nyP0gmcaPh4VeNZiBgEBuFWFUwG25sqbhohKULnnBvFrhn8pCfXpmhT7NBMtjNQibyXpwaNlNSwHEWpTlLf3yQw9Ggid40KQ+DKU90qt7V7WAeeatjZli59RcREn4/Zy+p6sLZnXOYUMLkjxp6H1zcrhUo/kDY8rVDJEYrj4JzkjKsmqI5JPFLrejQhW7A/VuuBoIsYLizuAp0wtyHRKblzvsD1OHccSbyz1a4iQPteoWsYku9wsK1NMGXBJARHxeCreJt7Dgq7OS+NnRukAtgs2Xs/XbJc30ihS4dkhPS+YXWbzAU9XRS5AuecqNvtEHrlrJjznbkyS8W7nQORlSmAdPx13SF9izmUGdxK+9Y6YGO/iydHSW7VQRdv6Alk95pQ41jsWc+8Kodwu9p6GqF3u6HwOJ3DYIsqmfUO7EVOwxbZTVEH7gXQeWqqFrrwVO+QUFrrFzaVl8cRvkOUXXMGU4690WM648m8DB3Ru0WBncnk6ssKXqJrnNPZq8s58IW1aKVTGPLsMzeXw9VsmRV57mKobd+gkaXbvoqD8Yo2lLBa44lX5bvwRPjl2XNlsOPPcEcw4TDd0w58Upss0KeVmRIGLbM4GO1tVl72XmFOGx+3eVh192hQ770d5KWUduqVrDus1s4llnCGj1OndjzGDdxNqxUd0fFuiO9lH+WSE857Lu4oZIHRTRB7m9M0VsQAlzKx8s49xSE8FkghU4VVto6L+Bj0MSYexa3IKjRWIcw2IO8pvXZDz+gYVFbxm0UPp5PPRM5hUs4Eaa8BMLdYO8iTYzbEWfHWG17SemPy3FWFoS4tQexdbU8OFndMZ0sWRcWVhdZZg1bkwFPhZYhTgg85Ihn0mzT0uYXFNN6TNRPWRn/N8OEieMZqsCL8OtFBYHDHmwv8MbZL3pAw6IgLaZpCp8YieVXbrcvBy3Kn7mRspa3thrjnEut0acNQ65LarUROYCiOJ3CJQ/M0JLx43atCVRYeUtQ3bqm6rO33DBViayw/bdew2XSIHuopVfmwslxt15PuXAaRhvHz2a2084HGS3cQINk7RigsI15W6heMAm1FhuA9fpgqy3eI3WSf/aDrEEThumTNUufB6Ko0OtADkZMjW/WMCuYf/KqKPrG+V6jfmADLqiqTjYC3wTyO02uRFsXk4Ov4an2S3CAPd5WZgDbStFl6wZ1UWl+jHkfUfl+cl+3tCvqlPF36NS1xS45ZsgyTHu52X/drTsJpfXvqdjhngq0otD4dhgFB4G1ZM7fd/YJfIDJGz3x98HgO9kYL61gIjhu5J/cs2ofn7ZCzqwnq+6iENxa5cy8iIQLPl2rgX6+U5iWe2nlRUqG4d+Hi417o2nWSJnBM0cjqnsApx59Go01tDpdU1lUnXzXOUzgZe5hvwV7ywveQcjOgq2bo5Xlreym0EQ+Xs36GUvO0Xk8SE6eZ0RMrpo32AZ5mxz4YkPjC52DMNvArC8QrUr6K7EmFgjpmPOyGhNhGnSCEHMblyN19mLaNTZ2ucCGg6ZcPL/PZ9fME+l9/yzwfCf6fnUy+HiK+vYt6HD57lvv5IevzX9Dppw8vlRPNGj3OX+ukDZ6Hlf/j9PXjP32FMS8fX1/dzi/NhubtrL6xgvlPj16izG3rphq/1nnSPg6AP7zYbT3/GUT99XnQ/fIwKy3mU/N3ibPH88pzrLr52uRfnwfsUTa/CPLcyGq852XwPI/+8OKOID6RU3/Fl+RXrypmQ5/vROZT3PmlyMuv/w1TiYhW4yUAAA== -->
