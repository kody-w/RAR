---
name: "rar-cowork-cookbook-configure-plan-loads"
description: "Applies a bulk configuration change to plan loads from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_loads", "rar_sha256": "be27faa5fb2636cdb950c56fd18a0ac4d8f7974962c492279cbf575ce6482cb0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_loads`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_loads_agent.py` and in the RCI capsule.

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

Plan loads Configuration Bulk Setup — Applies a bulk configuration change to plan loads from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-loads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_loads_agent.py` and embedded as the fenced Python below (sha256 be27faa5fb2636cd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_loads_agent.py` first:

```bash
python3 configure_plan_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_loads_agent.py   # or on stdin
python3 configure_plan_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan loads Configuration Bulk Setup — Applies a bulk configuration change to plan loads from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_loads',
    "version": '2.0.1',
    "display_name": 'Plan loads Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan loads from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-plan-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '51bb804c681b8b23',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/plan-loads'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-plan-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePlanLoads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanLoads'
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
    print(ConfigurePlanLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZOjxrbnV9HU+6Pbj+5C7NA3bsQgtAASiwAJIbejzQ5i34X8/N0nkVTV7mf7zrsRE6OqigIy8+znd04m+u3F7tqoqF++vOi+nc82dprGkV/P7NybccVQ1An4VyQO+Ju5Rd7WsdO1Rd28fHrx/Mat47KNixwsZ8syjf1mZs+cLr3PDeKwq+1peOZGdh76s7aYlSngkha218yCusgAn1mcl107W11dP50Fcep/mg1xG816O429x/JJmLpIU8d2k1nTlWVRt69AAv9qZ2XqNy9ffv7l00sMrl++/PbipnYDHr1wTxF8FfDcTSzBEnAZgrFyBFrn4L7066CoM/DI84PZ8+5j46fBp9l//mcy2HXY/PTlaz57fr6+TD9al8/aaFLIblrfm7l2aTtxGrfj64xNB3tsZrXfdnU+2aMBRsvD18fK75SKcvbPaezjg8lr6Lcfv74UQIS70l9ffpoVNeBXd9P160Sl/PjTa1oMfv3xp+90ms65+G47EQNSv3573j/Jgonfp8bBnes/AdWH8xz/68sflJs+D7knPcHKl9dLEecfH4TLuuj93M5d/+NPf0fWjXw3SeOm/R/R/flBOPJtD+j0FPynT3cj/zKDngq90/x7tlNU/TuagOlv7D7Nnob6O9p3+/830mmcg1B/s/hfkvurBdA/Zz//rW7/asGnWfD1ZemncQ+iw0n9L7Pfvunqivv5g/f94Ydffgek/69k9KKr3TuFb5mdx4HftN++/fyhuT/+8MvPH7oSxJpvZ9+6Ov0rmn9l1zufHyz4nPXxx7WA/yFP8mLIZ++RPvutKP9X/fvr7Dhl/PfnzZfZH/Nl+kCzSYk3pg8T/CFnGiDrH+z408vvABVyoE3n3odBlv/Hf8yk2K2Lpgjame4WAHmAg9s48yfhjShuZuB3yu3aB3ZtYmDY5zwQ/5OHJ4mLYPbr/3bv8PjZfcIj/AZ5/j0gvt1B7tfXmQFoFXUcxrmdzjRWVb/mdujn7cSnrP3Gr3uAIM7Y+p8B9nyeLgAkzn79K3Lf7itfy/HXOybGDxTSOGFCoKZL/ddJCzPy86fMLsBX/+q7HSCaFq79QNjmE9CuKdIeINikcZPEaTrz4hqoV9TjA2+7/MtE7Ndff3XsJvqaPyATmz1Av4HBhHdxZp8/A1WCNA6j9mvuu1Ex+/Db7x9m/zX7V6vuxCceKgDsp82BhKKuyDOQQ10GpgF3AAcCgLjb/LffnwYFZHJQpYCH4mCqOtNiEIOJ771ZV+fZzyhBzhwfWBVYNJuKBsDhWdy+zoRg9i4vYDoNTUgdFU078/zSzz0/d0dA1QbqvFsyL9pZAwKtCcZPs67x71x/dWr7LmIGktluf51JnArqQpFO1a5+1gmwuMhjYP533z+eAyL1h2a2eCPxOpOnqJuVdm2XUW0/eQT2wy+gHrwtB8TtWe4PX/Op7PmTqe4p8DAPmAQs4z5d+nnyOajIGch3r3njfZ9jT9XLuFex+mvePMPbridXuADuAdOwA2UYgP4/niHVREWXenf7AUknSk8veE+v3GNQ/V7nuR9agcXUHegAHMrZ1w6dI/js/3vnMMnHbjbaasMaq+VsJRua9bDb1OFM9n00RaCcz0DwPHLke4l/A4g3nPyapzEIgnr8x2Pm3drPOQ/sAUnsgdTX7vSBq4HdJrr3SJwiq67v+n/N3wD5EzDGHX2KSWUXhPVkgTeG0+ibpBHIzen+e3G+e672JtVBtM3KzklBJAS+792N0Eb1lE1P24Ow9KfMGqLYjX7QagaoA+8D+jMgRAzyA4D23XRyAdQEiXT3wvv0eGp5gBRe5wJpQQvpv85MkBBTUDQgC0HfMs0BVvhwJzXLfGBjIOK7hZvILh/CTF3nU0B78kWRgTj9oweeg99D+C7LJD6gagPfA1sOE4x6/vXh2Xc5n74CwmZT0t0X/ejup66zP1aOf3zN7zK+IzfI5XQqun8wzgzkUNbcQ26CogbASeY/AwhEwr2+vj5K5KMGv8vy5U+t9sd/rxu/F73Dj577Movatmy+wPCjUL3VqVcABDCIkbj0m+816/OUXp/v6fUDrYdpvsz+PXl+IPEM5C8z5HX+Op+GdrHrT5H6/AD1uc8L6zM+jX7NNf+7X5/On6AzHUGRfK8jb1NAMQlrP5wmP+pKM5WjAVTAO5ACy3/N333/zIwHpoAi2BR/yNh7QQWefDjqHe/BUN4C3t7UZoX+tO1IJ/Eb/+VL3qXpp5fczvy/225MQA5CElhg2pmA9ACtShv797v3tmW6+XEzdU8ckPFe8WXKn0938Ps0e+8WP83e+vf7NijvwAbm56lTnViCqeDf+9z3nZrjv4BdUjuWk7SPTcnUID0b1z8LMaUNkNj1p+JcvOfhxPFPRMBFGPr1n4ko9ws7fYJB09pTqY3btxRugJxeN0E38BdILZAtAAQ7sODPbACf2q86UNO8Sd3v9vuuVvHQ5fe7GdrHzu63lzdQePrg2cWB6SD7PjdTVYNBbAKG4P4RRWDsf9TfPdcA6AK9Bljk+CgV2DYROCiJka7nMMTcJcjAQ2h7bru4RwcUQ+EMibo4g6IU4zoBQRGuT+I06jqTDI/4+zaV63iSw58HPsYgqOthJEoQOINQqM14Nk7ZtjenaWpOBR5A9+9LE4B7T+UeykyWe281JyM8dfztxSFxMJPHG4F9fDiYOdokTjly5EAUGYTVhabnTGWXS3dFZY5Gngx96XHJ/rzzijK0t/FJky/dWAnlQWypBcujgpptgvOOuenreaMw6s6KAktYrZvEGGhVDPpA8Mb1yjTW+KHRzHXiNOZ6e/RIzDN0+6hsd0Qdm/VVr6t8Vd9gWGjIumqXWy5O9U1zQYnMckybPLqr86F3oqPjWByGaWf5QLh9gxwEoMJhKV8LBtn04mZ965HR9O1YTkxt7K42urUrQ8Hi0TfoimT8U04gcF+POsYTsHraUeju6ldycSa9rYgaF7lyTCf2zDI6dwWJCWfuaJw89hbwioWtDRM5lJ2IHxUbyXu1lwzdQlAutuaZ2Vap1Z2IkTn3sp5WadZ49RonYw6v+3xIyHnDHMqzjEsRVl3spK/Wo01eN5XXt6SqHRtIbhc9eWpP2UUv00xPtYq+HRQNocLOk80ukmrR2ELBtWOHhECpYV5qYiaaOKq0fZMfPNat5xd0L2xtIYCdpLKoXb6A3AppsTm2AX3YOnDUbLiSTqq3Vs+32qXUZPJwrPRaWrrYgrbdRt8MR0dsVaVR7Ys90mJlQ+f2kKAe05RHeVkxqmA2a9wXCUo8RHUsykN7vrmDUqZ1S5AG5pAL32NHHZEoBh0phhj21Q2lit2ZMl0DSdBudOsGtrf7rXZzzPkeP5p0e0X8aESbWs7sel/fWJq0S2kway7YbFXM3u5EdhfI+51FEga8kPL6qnGQ3jaFuYLTS+zvQ7L3ACNEtQ5SD10pslujy+iEuqez6Vq7hmK7W3NDl4tNtEVPKlprujuvEkUP9IOoY2OyoyUT3ayS3X7XGEtoxdMsJwfk/KodBAtW1HoNC31PRMzFVUWd8XAJbs8JUSKCR4tZa5Ouana5yG+ZujVtMQ6a9aI9KfS+i+pVaZ5uum9ck1ByZQWX6kWRitdxxfs9zNboscx3rLWNUPR2Oa1qf4NxKovoZwEVz/JKXdjY6lauzjtJtuLUjrexeTSOuecSA55dsuu8I45a7AUdwUgm5M2NJhT2bkIJi9JcaJIGNVCkrvy2YW6OsSZSSuOCwU+8pDu2qLCHbjSPHi2VR/xkiKBdzdsMcNMOOXpGybtLHqJ1G682TIkp16XW7hbLIxrurVRZw35hqyhdayVNJczKPLGrVMDikyLukmqUA0ixzXG8nLgKRiGmsKMaTpRr658NgyIZUV4h3nG+0YydxNOye9Lnw7lU6DNt624M0AHDodVl4xzVWDe66HihkS610IN/cJRuM9LImLKbY7rIYY2Goltc67fjuvKggFOH1sCuQqNAmXrdk+EOKKBBPs77LKjQdmOjHXaqRTbJsdVW0DdcwyGJYKoomV48YkzRTKI12EsQbdV6vpiWBd654XLTM/sKQXRXJK7+gZnnF5bkd5ZxhU+GVyEFTEBWrvQ2j64yj1S2jBwhPM2L+Rlhj3LPukGEtzY06qgtn/30oO7VXR22sE8scV+No2vIhmrlrsXFuKmY5bGUVENUpF7b8pSMXxpBXBPbXdkhjbXd2PtO2x1r87KxYi4e+uv15HIZtrTPsZOj/AVl+JN029ptnY4LgrQaL2xX6yBW96d4aTOaU0pbOFS1tjOt67xPExCPJbngRMe+nOumRFMvuEW1M4ToYl6EsbxcsJXEmAonFFirsgXLJci+NiQOPV70LkBrfml5CjfI1n6+NfotC7CUtU/Krrdc/2yZ4gW9NATBwIER031W61dBZDO9OWcGcUBEMSrl3jAzdHHdKouF4EHV6PEwUwDTYSwddOGwWI+cq85hQwtx6GZcacZYQCmP4Qc2PjTxpXSJ87HnLXclsRFabvS1nDCJpR0XxZFsPdk6hLvlWjBxc1WY49IJV2aMrVxqIV02g6PNCVlX5TJeGazMi9KcHBSr81l0mS5q1rsOvZLIjXOu3AAOZeZ2hqw2iGn+QKZ6z0tZv7Y4BfJrAAPItZlrIS+fRkbUG3MXqlGf4MTO0/PNoV2y8Mm6VboWYR1eGWVFk6f9+TTPULq0qMK9Dnwj19yhP9vr4eARuW0PRpop0IkE6D5oTZkTfN1cGNim/RLdlhncJEhEDvu1sPIQ9zhudAmmbiccWw1unIEOiG3O3EGAoYw19riJxAcJ1Wu9crRlh8CaxNW84GYka3HHiKdJf96oW1nvLoZDIp7Vnw4Rxm/c89q6rryLf7LaI0nJbe/jc3x544UMuRJFIdKrbH901isEcWQa2gs1kULbVGMsYnD257kjtT1ascZiSbec0zVmH3GXHY1FvL/mkoOrHTWjT7b7fr/RQBdoHdcWvbaOzZgNBsGtF0uzvJT7dsDWfjc6B+08YrkSKb1ULTKZbVprE52dm50VHJqcj/hJXPKlINVeS3FlUlDncnvTqJTDo4tscIS2CG5tbxzUGNguXJQok8kSM78Zx1ocWdhovd4qV62CZ8mQrXZ53Iqk7sMhLCTywhkz/row5mQ5uqB51oucjzdtre3t9Rhs1jo7UuUmoBW951RyYTWKmivIKsnivafohKRXVnjgQ/MmgYpxQxsoVW/7tIzSYqXE8EBvOuOCdRlzEq+sr0r0Qup2t96dB211c8uDWWQUpEcOzEDwpXZlYzkQFruPlz0oGV63ljZXBDXURY7Mu0bVbyQj92Uf5LvVaUUyBm9eqfkm3MlyJazOywUBo2m05UhWO4QOv3cGHqWObr2zeEjANpoVpYJnEOJpN+J9tfPtMaqlpjnpTLhlFWPQjAKu03m0MyWljAuydocTDw2NU8r70C87/VohbmUJZAB5xsXt4RXB+hv2FnXEupeXYXyzDGPlKUS1WJ5EHtuwqQdtC8Glhx74/Rbyy2yoz5yELf2z1Aa07iBro6/dsm+4eZoTC99Q17YJ04ITkbYRXxxDGmj+xqEVh8z1KF/6h528ouP10rKKM1FHwWF95tZ8o6vVgqIOyZYXyM5LmFhHjzvnYEq1A2q7N7esoEAza2XzuSOVwy1dn11O9nINtY7bmry4zeiXyHbf9isvL6u5evFwWDluhwoJzitiSRQEvT6lJXLhiFjuxlt3TNV0S1QN4Z1PKtMlKllL82BlOQ4yJ1PD2Sgbb6jSAr0ELt0UAJ2kRb9p+UAWeeFipxtxEDXdPI9b/qSQdhyed4qWlHrdW4iYb0vacIZoWIqmMJAaX65i51DdWKw2UAdpEJi7oWTYMrR0MPPiVGiNnyqXbSykyc6sOIg+N8umZuU4bKi9K7P1uU5ua9STrqdyr+THlZ9oZ9Ula60CFYNTnWLVydZNcuJ+OQipLM4TS/DXYnMNMI9GyeMu49tNWWpnJBudMAk9CkakU9wuhAWkN3Qr9TmpqWHg5OwYLTiXulhcdNwu4/S4Ozf7uVBai1LGxjakPVyLcGkM9qmy8MgLc1ysaxBd8IK62WEyWLeBmlvmLrJ7SKhy8xpX+anYOdlW26NalDMEEVz2i6FBEss7zzE7KJD2ZIQ5mwptct6Zp6E5WLmBtrfaLcykjSJls6yHNUDpoRl8+ljc9HJ/EzmZQ5Rud8ZQadeuWMQ9ySxrhlvCjgJcPDMBAodb6xAtlFK44VeXXOqHuF7s0OM2FCleD0xEVcJ0u0mDg7VGj4HK9IQ4P2MHhNZ8A664TVUm69Wp1VMIPyOYaKPQCUq7xcEzd9Ce6uzV3EeURQSf53510b1+25gYRBzJ3jHrSMLQK+1jriQ7g90zoX/CiSOFYNwlspQrbdSbvWDOG6zDtvIcTw8VGS2NZtxEqMJKnXa08ABP5yiuXhHVwzDPSU74eQstcQzsZI4bj17ekj0/N1SNvej8VrrQTMEs/LQ/B/46bxQ0gg+c55M8dFhvVTj0dTgbEGW30zBt5URjR+dbuFTCTs2N1PI9lz8LaimSwfWUGRQqNyrSyqKlbGC4F25wIZrrY1QOTADHFLRUWcJfMjcSCi0vibBEQniwPWTtrOKMrXRdX667q2hoDM3Nj8F8iyWrw0VtKEbwBMe49NcBgLyK88IBE/u1iG0ICa4IXuuzI0WkVrNcD7KeUfW8IFRtuKEsGsfnAehyWvG38LSV2q1u8eM6PYLd1MEk+mwvBxd9QfieP8L9tZ+fLsHR23dWfvWxmB98L/cO2/WQB1Kno0qxAI3DbkuaV/LWyzA7nLdqamVDl/UO3vgR7W1CAk0hQKXuocYNBMI6YucsGJbCXguckDwFGulFaNBTrCFoHoTglBWPFWQONdjfKAjN78a5coHyrOXwLT36LB50DuQHQ8ejnBOzO3qoGF9b9dfQiWztsHPxxGhEvj5vDvtGhBgLrnbtMubDcTGaJcTE7qGjt+7l2NDLUFjMrRtxi0RhzzVIyWZYiCvLhTJk8L7nTr53vi7x5VVv1g7YoAnHPYB8imj45Y2iJYG4wDhf7bfV+Rbi1GnEVeFSxLe1E8bxIqHm4+BvjaUbDVWt0kPh1ZUcW5EVEEdPpLR+r8Cx6rUkvcCOqFA6tQyMNe6tnMja9aCElEjVIBt9pZBw56QK9M5Ju2PUrSjUOW2pFsVJkSNXCuf1WqRy2yGWcouU5JMTUqOLFrhZk1sRHl0YWwu9YsGox4r6TmtaBSps3LwtiyTwjlSCGRgTtCaxjmyepa6nxbzVggLzOU3a0IstX4o91oUptGRibbVIBfh6mdsnkUD3c0YVndHYFnbmz/vuuBcpZln7wgLXUBgppMWNsdqeuYUHE3PUC0q2BEKZ9PLKhRCsqsvSVGUBK8UrB/HQQqxhGHQFG4+j/Mx0QAzdLAju4UraECnTzwMY12kKrze0A7HoKelgPGJHDUBpGbM2LWsW4kFs5DFzXkCrPW0UpFjBQ9WH/hhADhraHGetbTveURQDHxZLLd8dsQ3tdpIL7TZUdhv0EXTsJkRvFb+OjlGVSL6kLPd5CIWDH5b742htoJ3EDlQ7HjVQ5toR9RzHChzdK2AniK9H4Cddqut+JLj81LFsNIfUuGsrEFOiQuMuy7ausBc9kq0l2kWFqr8q/Tk/XJSLdDinCb6R0+52Kg+HvD9zCH/DBABe6foEn7FsiQ3LkUZZndr54wnnkbC9tpdkjpmkKuigKMzNs5osTfwgiqg87LbMbl+6ndWYbRUQeogsmQTDz/MbhMVXPltK7QJnlwyxuZzRoQXRaniBxg1zFNrjHE2WHGmIy1gOmOvV7fYdcdE6l4oN2IvyOZQn2OjEN3jjbfcs+/LpZTqOfh4q/8uXwNOJ3/+zg8fHGeHbS6T7cbJve1/uvL78azF++fRSuzEQ4nGI2qRd+Dx+/G9HqJ//6nXDtGJ8vD+d3mld27dz9dYOp2/2vMS51zVtPX5rirS7H9x+egEbhekbB8235wH1y134rJxOu9+ZvExv/6dT5QIsbotvz+9K3B9P72p8L7Zb/3kbPs+SP714IzB+7DbfMJL45tflpN/zHQZQC32dvyIvv/8frtd3rDklAAA= -->
