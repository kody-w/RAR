---
name: "rar-cowork-cookbook-demo-data-identify-training-needs"
description: "Generates and creates realistic demo records for identify training needs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_identify_training_needs", "rar_sha256": "00c68ab53874bc0b52d3c3a81afe1ba4c1c840cf192d5aeee63f4cd69050baed", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_identify_training_needs`. The original RAPP
agent is preserved byte-for-byte in `demo_data_identify_training_needs_agent.py` and in the RCI capsule.

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

Identify training needs Demo Data Generator — Generates and creates realistic demo records for identify training needs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-identify-training-needs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_identify_training_needs_agent.py` and embedded as the fenced Python below (sha256 00c68ab53874bc0b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_identify_training_needs_agent.py` first:

```bash
python3 demo_data_identify_training_needs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_identify_training_needs_agent.py   # or on stdin
python3 demo_data_identify_training_needs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify training needs Demo Data Generator — Generates and creates realistic demo records for identify training needs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-identify-training-needs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_identify_training_needs',
    "version": '2.0.1',
    "display_name": 'Identify training needs Demo Data Generator',
    "description": 'Generates and creates realistic demo records for identify training needs in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-identify-training-needs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-identify-training-needs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9686183a09c31980',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/identify-training-needs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-identify-training-needs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataIdentifyTrainingNeeds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataIdentifyTrainingNeeds'
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
    print(DemoDataIdentifyTrainingNeeds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8Va+5OiyJb+V9zaH3pm7S6eCvSNG7EgiAKKIgIyPdHDI3m/5KHg7Pzvm6hV3bNzZ++diI1YO7oKJPPkOd95fCeT+vXF6dqorF8+vxyAU0xEJ8viCNQTp/Ani/Ja1in8VaYu/D/xyqKtY7dry7p5+fjig8ar46qNywJOF0EBaqcFzX2qV4P7NfyVxU0bexMf5CW89crabyZBWU9iHxRtHAyTtnbiIi7CSQEAfBYXE2fSQCFu2U9aUDhFex//PmyUX8VZ2U4aDz6u47J5heqA3smrDDQvn3/6+eNLDK9fPv/64mVOA7964eHyvNM66+eq+lPadlwTzs6cIoTDqgGiUcD7CtRw0Rx+5YNg8rz7oQFZ8HHyH/+RXp06bH78/KWYPD9fXsZ/WldM2ghM2tJpWgBhcCrHjbO4HV4nbHZ1hhGRtquLZrQRglmEr4+Z3ySV1eTv47MfHou8hqD94ctLWY3oQqi/vPw4gWh8eam78fp1lFL98ONrVl5B/cOP3+Q0nZsArx2FQa1fvz7vn2LhwG9D4+C+6t+h1IdTXfDl5Tvjxs9D79FOOPPlNSnj4oeH4KouL6ObPPDDj38m1ouAl46R8C/J/ekhOAKOD216Kv7jxzvIP0+mT4PeZf75shV061+xBA5/W+7j5AnUn8m+4/8/RGdxAYP+DfF/KO4fTZj+ffLTn9r2v034OAm+wNDO4guMDjcDnye/fj3shMVPH/xvX374+Tco+p+KOZRd7d0lfM2dIg5A0379+tOH5v71h59/+tBVMNaAk3/t6uwfyfxHuN7X+R2Cz1E//H4uXP9YpEV5LSbvkT75taz+rf7tdWLAGuJ/+775PPk+X8bPdDIa8bboA4LvcqaBun6H448vv8ECUUBrOu/+GGb5v//7ZBN7ddmUQTs5eGXXTqCD2zgHo/J6FMPC1NxzuwYQ1yaGwD7HwfgfPTxqXAaTX/7Tu5fNT96zbCJj5fvqw9rz9a3kfX2rZV/vJe+X14kOBZd1HMaFk000drf7UjghHDwuWtWgAfUFlhN3aMEnWIg+jRdjofzln8r+ehfzWg2/3Otm/KhP2mI91qamy8DraJ8ZgeJpjQdZAPTA6+AKWelBdYIYVtWP0O6mzC6wto1YNGmcZRM/hgUdssFwlw3x+jwK++WXX1ynib4Uj2JKTB400SBwwLs6k0+foF1BFodR+6UAXlROPvz624fJf03+t1l34eMaO1jVn96AGkoHdTuB2dXlcNjIILD4Ov7dG7/+9kQXioEENYG+i4MYPCbD6EyB/wb1YcV+wmfziQsgxBDevCrrdiScuH2drIPJu75w0fHRWMOjsmkhtVWggPB7kMsiB5rzjmQxkhQMwSYYPk66BtxX/cUdPQRVzGGaO+0vk81iBxmjzOCPUc37IDi5LGII/3sgPL6HQuoPzYR7E/E62Y7xOKmc2qmi2nmuETgPv0CmeJsOhTuQYq9fipEbwQjVPTke8IQjfY80fXfpp9HnkO9zWAkelNy+jXFGXtPv/FZ/KZpn4Ds1uJM7VGWYhF3sj3Twt2dINVHZZf4dP6jpKOnpBf/plXsMrv+kHxiZezJS9+TZYozs1+EoRk7+f3uOUWlWFDVBZHWBnwhbXTs9wBwbpRH0R28F2f8hbEycbx3BWz15K6tfiiyGkVEPf3uMvLvgOeZRqroaIqax2l0+VAyCeTdqDM8x3Op6DGznS/FWvz9Cq+7FCnoI5jKM9THE3hYcn75pGsGEHe+/cfkTt9FyGIKTqnMziGgA4XIdL4Va1WOKPR0BYxWM6XaNYi/6nVUTKB2GBJQ/gUrEMGlgjb9Dty2hmRDaoC7zb8Pj0X9QC7/zoLawEwWvExNmyRgpDUxN2OaMYyAKH+6iJjmAGEMV3xFuIqd6KDM2r08FndEXZQ7j43sPPB9+i+u7LqP6UKozltUvxXUstD7oH5591/PpK6hsPmbifdLv3f20dfI90fztS3HX8b22wwTPRo7+DhwYf3X+iOixPjWwxuTgGUAwEu50/Ppg1Adlv+vy+Q8d+w9/ram/c+Tx9577PInatmo+I8iD195o7RVWBwTGSFyB5k5xn0a8Pr1l2Ke31Pl0z7DfCX7g9Hny15T7nYhnVH+eYK/oKzo+UmKYmBCM5wdisfjEnT6R49MvhQa+OfkZCWNxzQbIqe9M8zYE0k1Yg3Ac/GCeZiSsK+TIe6mFbvhSvAfCM01gJS/CkSab8rv0vVMudOvDa++MAB8VLVzbH1u0EIy7l2xUvwEvn4suyz6+FE4O/oVdy1j1YahCMMa9Dkwb2PG0MbjfvXc/483v92r3hIKVwC8/j3n1cTJ2qh8n703nx8nbNuC+sSo6uA/6aWx4xyXhUPjrfez7RtAFL3Df1Q7VqPhjbzP2Wc/+949KjOkENfbAyOTle36OK/5BCLwIQ1D/UYh6v3CyZ5FoWmfk5bh9S+0G6unDLufjBLoOphzMIlgcOzjhj8vAdWpw7iAB+qO53/D7Zlb5sOW3OwztY4P468tbsXj64NkMwuEwKz81IwUiMEzhgvD+EVDw2V9vE58CYH2DXQqUgKLenHbcGUFTpOuh7gz3CY9waMwJAOY6pId5NIl6Acbg/swBAMyJgPT8OYPOUNeBRkLn3OPy60j08agUQANAMBju+cQcn81IBqNwh/EdknIcH6VpCqUCH3w/NYXF8Wnpw7IRxveOdUTkafCvL+6chCNXZLNmH58FwhgOdaLcbeQy1DwIzwlNo0iZOBZQsDZt1ArbNKHobIV4MPtDVTrHFM/t1TIztKHZU6LM7tBD0KTTYZbN9+kwm0kobcSoyTv0KUlnwGLUne8NmXBM7Fl+PieYEwfnQ1ctlniryZJh08eoTawwdYYcnAXJaBLHmO6swqKlYAgr217I7XKFiDV2c82zF5eEaRxSdLk+NA0K+4qSbaLoZO575aq3hyo9Bjvaj2pJIYzOyZc6vwwcfJuV/s5NB69TJBxclH4uxVNwsQgSEeY0cTgf8nAdOYPsglyoLXXwz+UcW9uHVC/8zQ1ZGomX7RwxrC4alalyVrSrOpbkGV5v2KOe11onV6aU4d7F1Af0WB2po47qOt6sYa5s/ShqbWdpDe1JL9S4PZ+veORFW1AWRmvmRMmI4RgTfID5RndqVzpmELmNziMRbNFUPc1n4fl4yDOGlYREwveiIEteL1sihnZtSiUknzopGDhN32+tmQ+ttj1yd7s6i3rIB2qwz3R0wW9SaQIRM6s8iLo1xH97Ohpw07VdegRHe15zEK+GK3Vbs9k5yWHwpbMzt7fQ5z7TCNqSOTO7NZ7621m1D+vDUrXL+IJqZmPl+rkItul5xhB8pXvXi64qwaVjDoHgdF6Xb9GpqCw7L8VMu0OK7ngL8Q0ZLxT7PKfXBEab2VLrboY+A+Sq0A05X2Anjew1xtU0NyZ2nHYj8Zm+WwTqKs/shQhObLOdUiuB1LQByNAHsjlUM36WEFigeIe8Tjsq3zC6VSVz390dXRWsF0v0rM7BMa/kqopFq4qXUlX1SuAWqsZe+pNTY1IQrq0yoRqiu4E+mWnxDjmxCcITJ7IgKAYJ9J3IDYwhYfUl2GC4dS3SiBjaVspc4EeH+GbN0XPrWMpmVcs3r/TZPmFxKVB35iWgfCEkmiysVXIZgCyT+2F5UfOAG44Gt1mLcEPjmvnJIbf29cQCTvS027AhqeWeEJgy3QrbFg0bWV7Gi8rOsq1pk6Su9RvCauL22iWkPAUnJ2A3YNjkLq1zIrG6as0NiKtGIkoynS23J7qYkUWeubNibUU9OmXXS1fwzjZWXhAEl4bjplquuuJ2cgULa/3BdVfzmxaV6IKV/VrAwHFbrAREUMW0YbeJI0oLg0w85kr7remrBRYXaEQPOLo9xTewc3rZTnFmwSpxghmOTQVzup8rwdovFpKeEzQOfCQ2DCOpILv0+g2buw7qZ3MHq7cBXqZrA/Mc2io0ROryq7S7lpqM+Hp5aLPT0kSqeHMxk/lxwXDHah6GTELN45N0LdCuPtrHJK0IMrXqQ3aK3ekMtOtCTFMNQS82C2NmUdaO4gckdXNXxMJcm4BuFli6dgp8nlFGpUt4Lsy1tZpmmtD56iyTSkTdhPyhZuQzmOq3eLnWB+XMeJKiVUkHLmfU3naJQKyoIuEV0zKnOx4clhIXLlFbtPWZrvd8cmuVa43HJgFqEXa46AqfqzXhImd3Hwwlws3FDVcT0vQoDIxtS1d+SC3xUBrBPF/QQyayZDa7Eny94Sqx3KQHxqZmznXNU+qNtizi2jZkxos2d8Vus/m0SJarRWE6DlIcl7usC62QT2/rdaAsTKeEJVwPZG2R0IrgmnzoXw9sterVeM65233NNA4VReuSW4TyGS9lEte46rbJ+MtCNn2M3LOLY1wK7mwF+3pObkWwZOgT5BQ0qoTi5PSndXs5wVBBAnpa0sMRHSpqp16IbB5cVjS2NyVOOg5GpzYdQxeZqR/pCq1uO5u9QuPKdLe7Ijc76U+s325vFE/Sx7VGT4PUKhgEIZPtjKIvaIO0QRAJi/4wlc0myTLAnPkwD4Vpv3b2fbtqLp4cStLFqKt2k3Ju2fLaBs3O+XXdcZGjwGSjl+YG1kCnUCsWT71Y4G52hWfmgprpoTo9XrdBpKJLxuIyHb+JRhRSTkWZNpdHAdPZh6WbMfOqv7ltdZptj0daDwzONpTz/DRssH43o0A2m8mMLgpGRJRXqtuJHddd/MGCjgEw3Ped7eJRCfMG2Tv7cHFVNkylFMBHUbXtF83UpuxEiaOEN9g8QKaSfy6kIs/5dMv4yaAf7OXBk0kqWuirLgJKHsOmVHGrE5GrvJcTaylZ4DSexcDyMmPlKNf11B1KPsXmm525ylvdCXOZC0/lqrvIWLs5Ql3IAZ1uz4VzpHo11OLodDhtgTyoC/a8dVprkS1ujBWx6ozOjzv76OsrQd1f9goRr8ITsmRpiEsTF3oyOyyvvHOWyJt8mceurjVXXrdzxRiKvSTVpNQ0RGR4bspsTKHLRd69pkq7E05Uk29OS83THG1gyy1nFXIxy0mDrRlKP5yi5pCJGKOYRNPz1jl3nMrG9gruEgYmR2us0/KtFi3mpGJuYnumM9OYR7eXg6FYZB7NfdRWtX02HFsrFvuYsRwWDcSBTzQDdrYmJ92ilR+mR0WeZU6sR+J2La1hoTPqKRtmqi8taLUgjNtcw7b5llWbnCB9vnZJxOVqDvWS5W3AWNtlZwZaqGa4L45Ze5ydZi1YpSVApsHFdXxYV7g+nYN1SKGNCzsyhGv8QNSLs+/UCo+e6U53HddqCDumVvo5kPGdGWWcUdk9m5QoonaUBoQKY7lr6DLbIhCNOC1CBI021TYWA4nZlhVcKiQr0s6URXtt9uy59MzcEk151vEdm6eSwxzOlbpZ7DqO9AdzkanV0sV2+0461pmxvVhueyQphRTFPculO9LtNJc37OVmukR7XjvtprJTCcyJhItqNpcE+dxJWNNb7wEu2bKmpIs9XxW5Pi19r1WybWGllbIdFnQcyGiFkPsbj6LFUobNZnda2zNGs+syc7DNbN+EvL+MqItN9tdcCeNeuEn7mJMJbpVirHUgvehsDwf8xJ00PNMazd1zQKvVxUa97J1N4W/DKmfk4Djbi4W4XNm9l++DJTnM5MaKvMHvHa12KWdwZ4pNS1VU3Lp1EzHoZs7VQ+/0mELMqtKdX04Ha+qnkuupUxHXETk55CW1ctQuRWeGHnMrMNhTuSoIRTpSOXI+rcglYfTK1pNESY8bUdrzQL0K4kJVsILsu841h1RVxcHAhTi7tgVLeGtsSy1LGcTaTDudmd5rgllqJAElBb3HIBqeD8KZN1A8FfCLnGH6IeZqQ7sAAeeIPFSv+2BbqiBcNhlup7Va2Kd1CSMn2y3WbRc5brix7BLFN6ebQAl4sNw77LEq0aMvEqdklbW3wJe6cjGTcE3OHXfbNrlEQTq7TQ+ZEOrDLincm7qneJANG/WQ8sOR7PzTWhTKpZyRUqYRbiiGUr5yeX+AbYIYpHub2SQoO71uMovDUu9YBBFTVfsD9DXpT7c3tbPBxiKkDltYU+KoIod8mWTCsnCrwjRWAs0HCDByXfPPcUdiqwMRYpUylURPGDouTo5zYKiwFu/FAy4K5GnFhWWT8KoWX061li8PUT5snJnsO6ZedCfLkbkzsXFYtmVX84q2SPFWXq3AvHL6opGliBMQ4pZeaTM1yqm/7xy/v9J7R+3nx41yEGzssIej03Pfzbt91jPMWe/UQCCP8znelYodacv9Ka5JW8WndT7X8/BgdhXH2rd+5Qca3V7rHsEOO2Wmd8iqbMOKuRgAuV4NWybyYXcbyBmogmtN2CvsqhrTme+GqAlpWZz3ob20FY1qMbFVt8e9mk9vFEeVdBHxfOh0hkwNs6Tmz8qqjtpzOziXDcnG60S+lWwMhG2xRLBLWJQhi/cDec5jfHV10dInKbVh9wS7moZ6RSxLjj8Y2FaVeBTgFyE9YV3SJieLNLJgSxhmkZS3LSXnAxmK6BVRbaLl3Fy5BFi407CZe6Fq5YYkHL6ve7SuEaTnkZ12wIuLv5lSioxo27YKHE3cX0LLKJMjGe964C+wep5m3WngDQdhU0bjyq25q9xc94QFwTuxtplekb0e89eMQV1tfrrRpj33qJjQZcofPMDFrIjpS3OGblcxGWFHV9I3JCYRisPM9OQiWsvVJqk21/M07mSaP97Im8eXSwpESzKcYg1KrDwjOpobvGlcjicv3TStZwsacesNGsX1FYJVtmvGJnAiPG0icaCtvcXrLXncadMu2Xv1AVGiGrsg5k6l7U1W6ETAKsqe0+1wHgSa7PM4Vcx2+kbzO4yiTnEfs/m11sObiTGUMtC7BNQ5p/kkcHbA828bJFBJS6e4bSQsp0rmXk6xSUa73o6OkndC9cbelZKzsRrt5jeXfjnn0ojchF529i92Jzu4dLDOAwAYKsw30tzu1+mOA8485O3+QvhhsdYCI8kUYuV4+ylLH2vORPdtLGLU8dpPHYB4U8Ta4zmV7gzWO9wOB4K4Mjeg8Zpgiji33gi622BX88SvbJc/iitmek2Nc9vtEySZuXP5lolkMmVN0sFt6lLAhq1bzxnLVsFQ5HbqKrZOlzjjJRwzFIdoCaa32+JCGadV6dbOls4x4lL3BRHvy+hGFyeYLsjpNO3RkzxELEFTjZY2lmAVhNdilxo7tRxVu+E5tCBH+a2MDQBfWB2gYZdd5B1pusxU5gWVUYdOLG8+FfqkugqLGyvw2gE5T1kXu1DpfLOQObrYYaW/Wh0WScqsXLQ47mdbxtaBVoSAshxSS65hq1yswy0hr67CYMhB8bMC6b2pP6elGvDimoftsKdme5qMwDlY1EuFcvALDRbMND1u1XkVNLDFRWK3PgJv1d0oJIA7tF7szWtJYR2Z+MGhHYCgSxwRLfI1l1wxo7CI02VOLQWQzCO2N+saJqEtTxXSDPrY4UpJ2oO6JhsvWPWawIhF1He7EwZsO4gNAqsuSy+8bDGSPxLhEW5obimroyoVhKxYDqrQ9IOHml7ngWhlp7CRdfYDxl2mTKbgN3SDGHHMlftso5TBopoWes7uInS6i/O2vl4u6cr01JA1O0Eiu5a18qloC4Y1T4i0P3Nw9Fm4DrQiDqtjPze2clurVmkCKlTlS3m0wA3fLxGEKnVSkekjqVCndhvHAtpZXqDsZ5FL5BiXtdNbZjPXTaivyHod+mKaGNng0iltLLZHxHbmN6rOfJ5fFNaVpLlpmGv0RbUyLq7U1InWC//SkXzACJGvrVZEXtDSKdc7nCn13IsKv21XdS2oEcFwUzQQXAGT9yz78vFlPHZ+Hh7/6++Gx+O8/7NTxccB4NtrpPvBMXD8z/e1Pv8FnX7++FJ7MdTocXbawC3j86Dxf5ycfvqnbx/G6cPjhev4vqtv347ZWycc/17oJS78rmnr4WtTZt398Pbji9s14x8vNF+fh9Qvd7Py6nHi/TQDXjt+DpcaX4d+bcuvj1Nj8DL+gcH4Igf48bfb8HmgDAUM0Emx13wl5rOvoK5Ga5/vNKCR+Cv6ir389t+3BbwZnSUAAA== -->
