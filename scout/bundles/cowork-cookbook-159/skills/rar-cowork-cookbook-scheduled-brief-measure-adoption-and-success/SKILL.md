---
name: "rar-cowork-cookbook-scheduled-brief-measure-adoption-and-success"
description: "Schedulable morning-brief email summarizing measure adoption and success for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_adoption_and_success", "rar_sha256": "b95d64ece15641e9f5ab51bef9b829c4ace71bb46e4038dae12828556de57cab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_measure_adoption_and_success`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_measure_adoption_and_success_agent.py` and in the RCI capsule.

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

Measure adoption and success Scheduled Email Brief — Schedulable morning-brief email summarizing measure adoption and success for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-adoption-and-success
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_measure_adoption_and_success_agent.py` and embedded as the fenced Python below (sha256 b95d64ece15641e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_measure_adoption_and_success_agent.py` first:

```bash
python3 scheduled_brief_measure_adoption_and_success_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_measure_adoption_and_success_agent.py   # or on stdin
python3 scheduled_brief_measure_adoption_and_success_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure adoption and success Scheduled Email Brief — Schedulable morning-brief email summarizing measure adoption and success for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-adoption-and-success
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_measure_adoption_and_success',
    "version": '2.0.0',
    "display_name": 'Measure adoption and success Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing measure adoption and success for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-measure-adoption-and-success',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-measure-adoption-and-success',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'acfb59770760788f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/measure-adoption-and-success'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-measure-adoption-and-success', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefMeasureAdoptionAndSuccess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMeasureAdoptionAndSuccess'
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
    print(ScheduledBriefMeasureAdoptionAndSuccess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZOj1pbuX9HNfrDdVCUziDrhiAYJgZAEiEEDLkeaGcQoBjG4/d/vRlJm2cfnnHvd3Q+tqowUsPaa17fW3uSvL3bbREX18uVF9+18JthpGkd+NbNzb7YouqJKwK8iccDPzC3ypoqdtimq+uXTi+fXbhWXTVzk03I38r02tZ3Un2VFlcd5+NmpYj+Y+Zkdp7O6zTK7ikdwf5b5dt1W/sz2ivvyu7S6dV2/rmdBUc2ayJ9Vfl0WeR1PDIsu96u/zYDEOMx9b9YUs6rNZx5gPMwAfef7STq8AqX83s7K1K9fvvz086eXGHx/+fLri5vadf1NSd/jJs12DzXYpxZs7ukPHQCf1M5DsKAcgHdycF36FVAsA7c8YNLz6vvaT4NPs3//96Szq7D+4cvXfPb8fH2Z/mlAycmWprDrBujt2qXtxGncDK8zNu3soQZmNm2V1zN7VgPn5uHrY+U3TkU5+3F69v1DyGvoN99/fSmACvak9deXHyYPfH0BDgHfXycu5fc/vKZF51ff//CNT906F99tJmZA69e35/WTLSD8RhoHd6k/Aq6PIDv+15ffGTd9HnpPdoKVL6+XIs6/fzAuq+Lm53bu+t//8M/Ygji4SRrXzf8X358ejCPf9oBNT8V/+HR38s8z6GnQB89/LrYEYf0rlgDyd3GfZk9H/TPed///Hes0zv36w+P/kN0/WgD9OPvpn9r2rxZ8mgVfX5Z+Gt9AdoDC+TL79U1X+cVP33nfbn7382+A9f+TjV60lXvn8JbZeRz4dfP29tN39f32dz//9F1bglzz7eytrdJ/xPMf+fUu5w8efFJ9/8e1QL6ZJzmo+9lHps9+Lcr/U/32OjvYaex9u19/mf2+XqYPNJuMeBf6cMHvaqYGuv7Ojz+8/AagIgfWtO79Majyf/u32S52q6Iugmamu0XbTIjTxJk/KW9EcT0D/x84Bfz6gKkHHcj/KcKTxkUw++U/3DuMfnafMArX7yD0dsfHtycavr2j4RtAw7cnGv7yOjOAjKKKwzi305nGqurX3A79vJnklwAk/eoGkMUZGv8zwKTP05dZnM9++Sti3u4cX8vhlzsUxw/U0hbrCbFqwOR1svoY+fnTRhf0Cr/33RYISwsXaBbEAHU/TahdpDeAeJOH6iRO05kXV8AdRTXceQMvfpmY/fLLL45dR1/zB8Tis0czqWFA8KHO7PNnYGKQxmHUfM19Nypm3/3623ez/5z9q1V35pMMFaD+M0ZAQ0lX5BmouTYDZCB8IOAAUO4x+vW3p6MBG9BpZiCicRD7j8UgZxPfe/e6LrKfMZKaOT7wNvB0VhZVMzW1uHmdrYPZh75A6PRoQvaoqBvQvEo/9/zcHQBXG5jz4cm8aGY1SMw6GD7N2tq/S/3Fqey7ihkofrv5ZbZbqKCPFOl785uIwOIij4H7P3LicR8wqb6rZ9w7i9eZPGXprLQru4wq+ykjsB9xAf3jfTlgbs9yv/uaT73Tn1x1L5mHewAR8Iz7DOnnKeZgKgCNPffqd9l3Gnvqdsa961Vf8/pZDnY1hcIF7QEIDdvYm5rE354pVUdFm3p3//mPCeAZBe8ZlXsO7v7V6PDR3mf8fea4d/nZ1xZDUGL2v2FAmSxgBUHjBdbglzNeNrTzw7PTbDVF4DGOgQHhKQZU0beh4R1y3pH3a57GIE2q4W8Pyns8njQPNANGeAA0tDt/kAzAsxPfe65OuVdVU5bbX/N3iP8Ewn/HM2A0KOzkYcu7wOnpu6YRqN7p+lu7v8e28iZngXycla2TglwJfN9zbDcBWlVTvT3DARLXn2qvi2I3+oNVM8Ad5AfgPwNKxKCCgHfvrpMLYCYIT1AV2TfyeBqigBZe6wJtwfDqv86OoGSmCNSgTsEkNNEAL3x3ZwWiC3wMVPzwcB3Z5UOZad59KmhPsSgykMm/j8Dz4bckv+syqQ+42p7dAF92EwB7fv+I7Ieez1gBZbOpLO+L/hjup62z3/eiv33N7zp+YD6o9kcSf3PODFRZVt+TdAKrGgBO5n/k6aNjvz6a7qOrf+jy5U9D/vd/bR9wb6PmHyP3ZRY1TVl/geFH63vvfK8AKmCQI3Hp19+64KMIPz9L7vN7yX0Gkj8/S+4PMh4u+zL7a3r+gcUzwb/M0FfkFZkebWPXnzL4+QFuWXzmzp+J6enXXPO/xfuZFBPogtJ2ho8O9E4C2lBY+eFE/OhI9dTIOtA77xAMIvI1/8iJZ8UAhM/DqX3Wxe8q+d6KQYQfAfzoFOBR3gDZ3jTQhf6060kn9Wv/5Uvepumnl9zO/L+025n6Ashf4JZptwRqCUxKTezfrz6mpunij3u+e5UBePCKL1OxfZpNE+6n2cew+mn2vn24b83yFuyffpoG5UkkIAW/Pmg/NpSO/wJ2bs1QTiY89kTTfPacm/+sxFRjQOM7NE/d61m0k8Q/MQFfwtCv/sxEuX+x0ydy1I09de64ea/392z9NANBBHUISgsgZgsW/FkMkFP51xa0SG8y95v/vplVPGz57e6G5rGx/PXlHUGeMXgOkYAclOrnemqSMEhYIBBcP1ILPPtvjZdPXgD/wEgDmDkM6VGE7/ooSRGozwSk7ZAoGHUYZ44xLmG7Po06DkH5BILPPdtHsTk2J0nK80natR3A75Gsb9NUEE/6Ybbtzl0aJTyGtinXxxEHB/wx1KNxHyEZPJjPfQK46mNpAsDzafTDyMmjH5Pu5Jyn7b++OBQBKEWiXrOPzwJmDjZ92jpy5DAVFbD1hUmafnPwKk8+MHmNioLnCLYtC3LeMHIvH4Z9tDDM1Y7flxx+IMgE0iSoM+htfirYoIj2OOXSirOUlXWksr17YhTVc02e319WRGH7jb6wMrto1tlqlFTgSUNbJdW23KB62+xKX6rXuJnlpWZv3eNNhWH9sgsJE5MuQzrmVyzfFUSZY/l1TOwTtHDhFVkRTXo9m+jhKplNviBXtrEXFeMKbzRdOh2u/eAcENv0dFJfyMRm3DIaFVdOdFW1wZFzEgtUI6WCQMeVU0VA8EiY1cBfd6csnSfVuk2vjpl6zo3IsHUprC7iQRhh1qEP9amJrwd83Q2i5Q/4khx40rX9W1hmKzZfmdQ+vimG259vYHJJaqfY9MFuEyati4cFidWRuyWPjZRsNjZ6sJWcy5K4wS/ZmRYyHDnxLV020BZJh+qknKWjvust8yoI7YoUjy7Fm22KpGF2YFiJTyVsj5FDJtSl05ypow+5GsINrX6y2LAqhlI6nJ3NiWv9pUnaKXbSDdeT9HMAIcZ1mR9L87qSocYyD1gzSMfMySLFuEAZe+JKmmuUrJBtxh9c6XqeF+UhwTS4JoUDlbaelp43fa2O6CLljoniGoKZaqPf+SV1beaUUZ1oXzmwOmKZdAMNFErO91cSo8+iQ9s7nRq0g5U5WNCeL812sb4ejkStYXo2H+oKzewLdl0gZUwYnF1LrssHR+SUEY3RmSYkt+eqP/S9t5GyrcVEiw4nateIV+KKBo46l7SxSuBcPR1wpa+u1WLM/DHi3CxIsXO2Q3a8zW+to4/pZnZyUiU4ybustZ2zr1yNKw2tasZyAyk+BvsEypQgRmCOg1j2gkMRbzpLSh2XEhUYEsMo8FnkkOpS3KDxsrdUqom3wUK6mu3m0lRlog2NXh3i2BLpRees0hsvr+1+c0pjlLcXI9En20A51JFCXCW/87h+qNSdA0t4Xkbr4x7PVtVhJ7v6jdh1y+5ibwrdMwu+gFf0OVR4i2PkcXOOqYWpGavUO54J1+B6gs7dzXpQbvgayi6WQkWdUR93MU3GhWt2PKlvb9mWP5EJuplfiEsxOqqJYVtDoC5WtVM5KD0m+VZgqttcnXNYQV63uuxcQ2wzHA+wlLqn6zDybIFYiLOQKzDiI6IJ88qGaHZyZS82l8xY0AK0DcvNrUBc7swkbSqQTLFYUtuNtnHCYbPnck0WrisDD1ImQgTIdFo+zT2gDsrMxWs2CAtoHoR5ViEDWWoqhlYGdaOSdH+UTNs9HPeSdaOiXs3CLPVTuRKWkQ4ZpufJItWsluyw7LnOFvPu4JrXSj4fS4yA2XyOrmH+Stsg2bfBreX4q+lcDyojjPFCHK4b3qtuK0QIrPWc5Cxpf2oKvi7lXgn1gdZ2roIMyS5De06Wxtba2eiYSgt8a5jDUCFH9ywt2oOHVilh8zw7otCpsUrkjJFQuZLzq4TvBAhWbVjKeP4sWo2VapF6Yz0aKuozlLj4dWXjNL/cQxslxhl4znQi0117+hzIxVIgKZO3NMeid0LPQrukGxh07c7TzWbRQacEyflRgBZVH3HkmHgFtKdi8qaZqpr6Z05VmFpPRL6+5dVcyY5r1LKospONBDvZyobdazskFBOJHELGIBfa0piz5+N6aEXeCBNOB0jVpTJGOnQargm22XX8cuEdGl3uk1DWM3+z9YXQJbiOEHhpUNaUMcrpHqlg8tp35PaSD9yRR5c8jbBb7xDRrnV16WVJr7IzCL3sWPKcAaBC+rm0Wu+Wq4vsUhR8QnXdPKc4WbmOek5ENuyUm15nGgzZ7KryRlyki7WgnaNdehPzAMeJ+U5cbntiDqvbbdk4hGby254eB8c1I9YdFqKekYWLGtkhXSGb7KSTuCno3O1WQGNmaqkTrtswtca5JiGrQXHaeJNrV4000IErZWCRe0o2Bkfq5aXuJEZfD1f56g9nKrFFSFbBoxt/go3MLFKSYTTr4EojwhRxbVxoTyJCBBtOCS3TCQ4or04Yl6W982gxFXn8yhTHnGc88dgaLbk8ZMVZ2cBlhLFCv2pA1xirLaXGONHtFdmqe3Rg+yhcXZqwGpdWCVNJeSLCGxiGoN2A1vyS87Zu2M1XV7EuN1G50lxYabbMrWqdWGx4W94iRmA5u8je73KHI7f6bitsiuYy0OmuvcZBprYqz0JUybqGg5k8c9Atbu2ujP4g+VgWn9cH2eNum/TQ6gck2y8u2XVtoSNL2kKqLITtAZcOKix3eyozNilKmWqCWiwiYlzcFSBXuqO6cq3tVkno4yka9/1ViFdjwjVbqqBQ09kJ9Rph+5r3QtPAe5Fa3kD7MLb2Pr1m7oHQze4QYymYXIZaCmx9LZ3DgCNYeAcLDKdWjn3c2TzYUwUGeqPdI0+vj9n1aFkLL4ZR71jqqgEGzr2992MXHdcLn3GCYuQWTlcah3YtqcY1kgYVldPVSjoQ50V2QmpzLrtqXG9l8VgvjDwWaO7GHvsVu8fjkj0XaikessNWYUPz7G0WcM7jKUzvU4nLigUUwqB7YFjVt0rjacPupEom59ZievJqmhJsTz+i3orLPcFaiLfbTRyODcy4yzAZ1szaJ9kRwkqZkC4l5PuMXF19MLWcUMzyli2TOfxpTXkGdcRoFPeXGehao7mMTrmFr9bbvTCULKZwQyg3xJXUjS4g9lcz65asOYq8earmpHK1TXvot2tkzh3dnmFbt0CQo1gJ3lpHr5G5d4PD9by94AEim9fidDuGKbWRuG16EFadcNBHs+0SiNsz+rUXiqYaj2fRxXhkPALI4tj0QkahWeMrU1AgKyvN3urCaDyv+EigcmW/vOaZARWN22xTOUWCZEdvtjoHb+OciYzdzhjcg0NpKRP2mBFj1okTtKs1RBYL6PC+X2hJtjsJZey2RqRR/AmVDgcuR6+nPVE3hRS7mFWPuixvz3FSrOeOS6w7imFJ3UOwReYgJWOs2PPOAgPmarCE0ikz3dOjwe0tbetQdhzQaolIcJUVO3lhQNTCY1HIaghaPi+d9uJc6IuIaql9cluxjCk4EtODhqi85UgkYvexJfgLD96UFbb13BIMKNXmzOFHTahcUiwGpuGvQr0RF/oaGduEKMTrYNpTw79JujUkpx3mrj22sBgczU3evpxuHl4i7GVTZ/hcMVCXGT2wjVAcPdpHFmM75ko3V/PURlmD4ECqW2uuRZLSXo7xMkj1hAjQKov9TcTPi8RsNVLPD23rmys8lho7GjZYugCqtVFS1tihYenzRc0Q7RAEoHNxJbTfHY86KtXUGt+ufBraH5BiP6o3xAGzOY1iyTBfZxsc6ToXO2h1tN+lSzK+ZXrB2j0/LtOsZcY5d1GHtQvlDiF0Jq/W8rglBoskMeq20Mw043j/VLf1ogZ6QRiywDHGxGBtfWgS/pCfpVNsi0nHBejRyrSTBw8ZFeUnPuQaFyqPLmKxwgpDkXkVIoehvO3XiReFO2xZdAffCJcdau9Qqlv0+9FSlio5NFLJwPIWFTlUC9WQ9WMh9ZmLK1oeHVPsZm9GmjucDca9ihu+rfUtoiyq8SAK52OmipGwFlLobKVH7aQC1JW2pDi/eKpEEkXeGmVkK5KGYh7jmuNiLQn55pYn9Flvo1Id5A0CreVYUDcyvlvpuH6TYWc9D5I501Myjvq4k9uVf1IG1Ed6LOq8k3vDt9385nXuoSNd4oALXORgA3G5rfS1KTbjBZUUhExTnyiXTj3PlFENVUVTySMtVVUTirdaqSTMJgo+Sg+8fqyylWwaRb0kGuI0xscLm69liwxOWQct4PNeUKQl23nYITRIlB7mG6jckDrN59TNOl063sI5bKy3UKrfiqjaGj1iZXB60vy9bJ8D8ezShE/GzuidL4gPQBqmhjlMsPvTtpa31Ame71UaT5iUxlV1vHINZtK6SSJeXRHc3C6vKjsiYACF4jmxO2dgQjsFiJQn+/2SzommJguWTQjaraWlsYQWgyAPTs+6EWSoRBsRFpn6bXkaVc1dBko9eJRy6dydh66KKnM3EZ32PtjAD5ddlmRcHVmWw+Ho4uyQye3U0ayPiyePvZQ4oUa3ug2Prra+VdGSUJWhpckFHG6zk+UIJpthUBR5sC5WbYe4SzkNdxpkx9SZCeIeDA6oc7k5J9/GoQYm+76L0r0TxBrN7jSJZ3y19NzlgOTWLdj1coRS9GkZxVuMFZ34ooyMc8Ln2Ta4CqRPdOubw+zpS9mSfk/hwxCcpSvLqvixIuerRbAAzYLg980YagqR+wleaDHD02nFXJUkWSvLhUj6GW3Knd7B0sC42qiaodhfFFpRN1GndidkcYZoDTlLkHBydoROj5Wi5qy/WV22BGf2/AK+zvcwGnZ+EGi2UAQN6+nLoyGO9MkA+9Ked3nhvK35ct/gbnZcXvZng9+tPBvOUU72tHrgRxjeXSKJWlMLHBLoVRXkLdL2/NaXGlzV9ZHHd2hYQ4lo3aqLdUZWaXhb2qQmQoFbxirai+1ok/ghwelod9qXw4Wa8zzMrNnz3F2eO8SDVJq3Kq4TrB7DOzhUCJSkaLGFw+WGO8uphuIjvqALxlPoTe5nlE9j3hVf72SdHo5rom3ABCg63V4KcZbTXQR1M2qJkh4m8axyuEAbVYMOfEWqEcFwrVRn0JWENaFfymCvvGuIUIhwB4xztYinLQoh2NLfti0c0SV+ClSA1cJ6CXvzAEr3cwDbFLysxC3dYTfkumygm7lQ6AKAcZAGF7oqfNdtRwoOwhvc6/oyNpkBd/vsVi4GbtHXId1FGs+ShH2lK2d3Y9BkLWvNeX7eHtARxZFVsIIktetldi4ka/WAzn1FZboiVionW7XGPvI9yYsVHC1vKze9ySmhmtTSjI2tqLJ44WI3npO50JP24egiitu6fiRa6ZXK0CUYxilszvhYS/YIAa/shDsLiYPvIXpE2bwmgmW/P60aIwgb/+xbLLbgNoSeLzCMU5zOMq0TjkqNNJ6XiihpEnchzSZqDbE0EKOxhvlixF2pT+fiAceZhAvgub5SFkO78hcQRh+DdSRvU1yMcex8ZPrb3nKCmjwG7nLP93AHtmdauUYdN2slVdpfDjdMzxCIIvP9vCvRuaKyQSGF/nZMyf35apT7Qmdzh8o4EfSfk+lrHlnC6lEuYJ9pjETJ5lor42Nttj2IPVRAR2tcDgCP2B9/fPn0Mp1hP0+i/0vvoqcTwf+xg8nHGeL7m6r7MbRve1/usr7819T7+dNL5cZAucehbJ224fPY8u+OZD//lXcdE6fh8dp3etHWN++H+o0dTn/V9BLnXls31fBWF2l7PyD+9OK09fSHFfXb8yD85W5sVk6n6n9nHLhje1mcx9Or2bemeHucT/sv059ATO+RfC/+dhk+j64/vXgDiGXs1m84Rb75VTmZ/3yPMp3yTi9SXn77vwJe465PJgAA -->
