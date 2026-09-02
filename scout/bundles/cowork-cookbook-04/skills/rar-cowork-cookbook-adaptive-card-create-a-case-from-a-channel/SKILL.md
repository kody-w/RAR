---
name: "rar-cowork-cookbook-adaptive-card-create-a-case-from-a-channel"
description: "Produces a reusable Adaptive Card JSON snapshot of create a case from a channel status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_a_case_from_a_channel", "rar_sha256": "f7dd38a3fffa82057652d5a2bcda3faf99b29e3acab9bbe4c135a02cb582301c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_create_a_case_from_a_channel_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-create-a-case-from-a-channel:047f2aa5a8f204f4b8415ae2554f5c89742e2bc6e5e944a66990bd21266ccc85", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_create_a_case_from_a_channel`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_create_a_case_from_a_channel_agent.py` is
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

Create a case from a channel Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of create a case from a channel status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-a-case-from-a-channel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_create_a_case_from_a_channel_agent.py` and embedded as the fenced Python below (sha256 f7dd38a3fffa8205…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_create_a_case_from_a_channel_agent.py` first:

```bash
python3 adaptive_card_create_a_case_from_a_channel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_create_a_case_from_a_channel_agent.py   # or on stdin
python3 adaptive_card_create_a_case_from_a_channel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create a case from a channel Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of create a case from a channel status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-a-case-from-a-channel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_create_a_case_from_a_channel',
    "version": '2.0.0',
    "display_name": 'Create a case from a channel Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of create a case from a channel status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-create-a-case-from-a-channel',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-create-a-case-from-a-channel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1e126d0d736b4e7b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/create-a-case-from-a-channel'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-create-a-case-from-a-channel', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardCreateACaseFromAChannel(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCreateACaseFromAChannel'
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
    print(AdaptiveCardCreateACaseFromAChannel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166XfiSLbnv6Lx+5BVT06jHeE+dc4IEAKBBGhBgso6Tu37LqGlXv3vEwLszHzV1a+7Zz4MPjZaIu5+f/dGhH9/Mpraz8qn1yfZMVKIM+I48J0SMlIbWmRtVkbgK4tM8AtZWVqXgdnUWVk9PT/ZTmWVQV4HWQqmH8rMbiynggyodJrKMGMHYmwDvL460MIobYiX9yJUpUZe+VkNZS5klY5RO2CCZVQO5JZZMl77Rpo6MVTVRt1UkJuVkJOYjm0HqQcFKWQblW9mgF71DF4YQQy+wRjFMZLqBUjldEaSx0719Prrb89PAbh+ev39yYqNCjx6epdoFGhxY88sAPMV4M0s7pwBjdhIPTA474FpUnCfOyWQIwGPbMeFHnc/VU7sPkP/+Z9Ra5Re9fPrlxR6fL48jT9Sk0K170B1ZlS1YwMtc8MM4qDuXyAmbo2+ApaqmzIdbVYBy6bey33mN0pZDv0yvvvpzuTFc+qfvjxlQARjtPuXp59H5b88lc14/TJSyX/6+SXOWqf86edvdKrGDB2rHokBqV/eHvcPsmDgt6GBe+P6C6B697DpfHn6Trnxc5d71BPMfHoJsyD96U44L7Orkxqp5fz081+RtXzHiuKgqv8pur/eCfuOYQOdHoL//Hwz8m8Q/FDog+Zfs82BW/8VTcDwd3bP0MNQf0X7Zv//RjoOUpAO7xb/u+T+3gT4F+jXv9TtH014htwvT0snBuFdjun3Cv3+Jh/Yxa+f7G8PP/32ByD9P5KRs6a0bhTeEiMNXKeq395+/VTdHn/67ddPTQ5iDeTcW1PGf4/m37Prjc8PFnyM+unHuYC/mkZp1qbQR6RDv2f5/yr/eIFORhzY355Xr9D3+TJ+YGhU4p3p3QTf5UwFZP3Ojj8//QFgIgXaNNbtNcjy//gPSAisMqsyt4ZkK2tqCDi4DhJnFF7xgwpSHkn9Vd5udruXxP4KgadjugOIMJq4hrgSgBME8mH0+KgBQLyv/9u6Yepn64GpE+MBSG8WQKS3OyK+GW8jIr6NiDhe33Hp6wuk+ECArAy8IDViSGIOB8jwnLQeWd+CpGqSz9eRO5AsuKOPtNiMyFM1sfM36Os/z+7tRvkl70fFvqTAUwZwnw3VTpJnpVEGcQ8ZI3KZfe18BqgL0KXM4tg0rAga/zT5y2gtzXfShw0tUGCczrEaAPpxZgEV3AAg9TMIgyqLQZmoR8tWURDHkB2UwGxZ2d8qEbD+60js69evJsD/L+kdmnHoXoGqCRjwITD0+XNeOm4ceH79JXUsP4M+/f7HJ+i/oH8060Z85HEAleJmOWCc+F60QK42CRhWQWOgACC6+fL3P+4uGaVLQckEGRa4gXObDKh9C4xRg7uf3p0EdB5FdMoHpx/tBrU+sAsU1MBaIOur5y/pSCIDQ8s2AKXyYcT75Lvp371+5zP6pHrYEPjpVlrHsbeYHJ1pZaX9Am1c6MNSQF3g13r0qJ9VNQjj3EltJ7V6MNOov7kwBcW7AplUuf0z1FRA1ZHyVxOQHo2TjAFUf4WExQFUviwGf0YD3diD2VkajI5/hO39MSBSfgIxNn8n8QKJDrAmlBulkfvl2B2M41zjHhGg4r3PB8QNKHVaaCz0zuijW47fIm/xj9oL+d5e/NihfGkwBCWg/y9amVEDhuMklmMUdgmxoiKd7+E2tmGj9vfODbQTN8q33PnWYryj0TtOf0njALio7P92H+neIuw+5o59TQnCR2KkG/0x18sb3aAGcTI6vizH2Da+pO8F4RmoCLxUjdgG0jkawSH7YDi+fZfUB4qO99+aA+gegmNqgOCG8saMAwtyHce+5UHtl2OWPfwBgsYZjQzSwvJ/0AoC1EFAAPoQECIA0QuKxs10IsiW0cw3V3wMD8aWK7+714ZAOjkvkDZGN4jQCjId0DeNY4AVPt1IQYkDbAxE/LBw5Rv5XZixNX4IaIy+yJIxAr7zwOMliNSx8gB+H2kIqAIgroEtW+AEkGXd3bMfcj58BYRNxpS4TfrR3Q9doe8r19/GVAQyfqsJoJu/Re834wD8LpPqBkmgHEcVSPbEeQQQiIRbfX+5l+h7D/Ahy+uf1gM//WtLhlvRVX/03Cvk13VevU4m98L4XhdfrCyZgBgJcqf6qJGfx6L1+Z5qn43PY6p9Hm06Xt9T7QcOd4O9Qv+alD+QeIT3K4S+IC/I+GoXWM4Yv48PMMri8/z8mRjffkkl55u3HyExwh2AYLP/qDrvQ0Dp8UrHGwffq1A1Fq8W1Msb+N2qyEdEPPJl1NMbS2aVfZfHo06jf+/u+wBp8Cod4d8emz/PGVdH8Sh+5Ty9pk0cPz+lRuL806uiEY1B5AKTjCsqkEWgo6oD53b30V2NNz8uDG/5BYDBzl7HNAOVD3TCz9BHU/sMvS8zbsu3tAHrrF/HhnpkCYaCr4+xH6tO03kCq7u6z0fx72unsY979Nd/FmLMLiAxAPVqlOU9XUeOfyICLjzPKf9MZH+7MOIHZgBYH+slKNOPTK+AnDboswCaX8cMBEkFsLIBE/7MBvApnaIBFdoe1f1mv29qZXdd/riZob4vQH9/eseO8freLtyDB0z4N5q70bjvRfltZGGMhG4t2M3Wt1b2DegZjMX3u1fe2Em83aPy6RVAkPP8NFq0DEB/PtyW3093uYBC35pgQAGAyedqbCYmIKkAJVDi81GZCADhdwzGx4F9Gz9evP5l5/w/o8IrQkxdzDBIg3YxhHAJkyZQ0nAwkiRc0qJnUwJzMNOiHNKZEYRBUbMZYtoYilGUZVk0CcQZfZsYD3Em6OgVoMiH6f8v+vqnOyVQWDCSAqTcqW3jtIG7rmvQGEJOKRKzSQPIZ4OHhjubmdjMwQ3LMGem6RAWipMGglkmSWM4glojvUc/eRfv7b13f/fTHSbeAMQmwSg8MI1FW1OUsGdTg7IcHDFxy0Ex1J7iDkLOcJemHQLM/5j68NXoyrsFxngGrSRo5K4jn98fvh9jlCLAyDVRbZj7ZzGZnYwJNjUlfwfrCNx1E8JvSC3j9xjqrTckutZsnSFFrg7IbZvrxALnY/OIdppG5HPMPhvMAZHdKpq1eIU023x+TCmHYwx4qQmpjdvpBXYPB1GN2GPIkjteruKcDaKTxl8SD53pVUWfyIQoOOmk4ZzcFzsZRQqrDzen6wTvC9w/JaW0jwXdUuuT1uWRMRzKaedaV99C47PtJGxyzqNrhVUJFeZyssKqY6HoGsyGmV6YSomxCyfV5gzl9RPBcdDIr8wwOqcDSdnpgEwdHcdKxZ/Cbkl36ILWg0ZKdp3syKdIN1CxAKvLnsI1LNldj9WZyjCXKOhd1JTMSRQbQfAxvapb2Pb3Ohe4vTosfKUoqNM2Ig5DnNKnXVokctd45Ypui0WPbpWDejYTp4mrWmW7aa3ltpqsyJgvywUlNCgmimXWWGefcuBAFK0ixpPgLCpsu/F6BbEJvXIuSiXJhSJrvXRCPE9J/dkQBVk3rWYm34C6yFhpHCfH3XbLlJNdyZ/NrT5vnKVlR/OpJlv1Sl5ZWFagRa5mru/v5FpCy+gEYFZYWvictqxK5loVUNtr1cGo5d7iC4M+12qE2bOq31t2MTts5GpFODxB8apfBvw+L/dKNo/NgzrRNcfcnYahWsvBZmM1jnZNr7OFuTaaY53UxGxd8rUVXfQLjKZcZhZDsPXVxlxFxr6XdDTpRP8aE63miLh22a58MWCuMLbI+hUIshDPi2GlCRNakfzLlnQ251rcD2s2s5V+z8VhwmmITy7JcEJd82Jnn9STHVImb7Yt7VwXHdclAePb22WjHMBCMNj5CJXzxbZw1NNK6HkcxWRbt1sxLnYhue8ogl3T+UArc5pdTpl+bVEqcMHEpwUrLGdk5earzrNSo7FDHFGN5Q4+VZJ5vojyitRs8SQEzak4GZGmbHDjtDxX9cYvlxiv0AJXhu3eWqX6IvYYHQzensJIbOwTtawngoVwQhev3PM+00+9r9HccYlJ8VrluUwNZDewI3m94Ppeyo4rq+PUKgiSUiAEviUSM+x1jtAl2nb3x9mBkwzU3KT8jhRbuT+HFpuvTGonDv0s2NHeOTbOk00u4MNJrIJo1mSYU4SMmZ1yvo8nsjlZkUub2ptBZCtUs/ErNLb7i7mmLK9vizlrYnRglFsjDAM7WIuWBnNdPWeVZSAjs5a2RdXm0rS4ZozS5ELM5U3EI0q98FQPUcQ1fGW3M3gv4oujUnSIY7uTMJYvyspxRFUeVvAF1Nk1RXX5SZ8pMrJbFOJ2uzwvI7w+kml4VOSrlqA1E6vXCE31tQSX4tETzvTxgvkkvdZX2/2grQq7EY78RJQOxXI6Vf3t1p1EFEupxv50mC3oZEEukh1bl6hBzQ8l7Vgu68U7rF1q+jwoe0pr2mG9jEUvjIpmw5f0oOxCLbFyRgNTEvUEX5Vg2Cj9rkat7U65hLBz7dFctBOxcQtJuVC+02c4Tk7VHCFgjwHAJhR7fgbPaxtdhSntJ7NzqbmKt1l3yjCpkcm6QQ5mrcyTjWWH+xXPORxuu5ciOlyZvZAeZRzf7PtkK9adOPUBJhMcYXi9ROI9Ezcb7xyRh06xJotkWMgX6hzvD1nnHvSNuS/ykh9mF9g4iNc9e14x3FlUGYHORSQwXWrviCt53lnh9ngU9vKR2xYcvkDK8+la4FRYCkjOHKLcP6HZsJI9Wruco6olq/a65i5nr4CJoRYF9rzgZ0XXEtMw7HyNRZfcdGh36smfKpfCms3oaTAIx2HfXKsGdtJLT1+HyIt63um4xLUnIcjQ7V42EbQR00peZkd9rZfawMwmdbZAGoIMYWI5RwzBOVyz3r3M4Zmb6LTkFsXMWwcxrdaLUNjOZtp6vmO2s0Bi/atx4LXL6SibTpmq8gWZTxtzyvE1H++FhFjwmShZ11ZnuqqISivJ2SR12ZXqbxRbBHOJRUg5bNdOh4VLhUgebsMitqw9r17qYg5Hp3STayeb7s3jySZzJUSn+8FRVn177JNFVpzP4cbxBHsqFuZ5ldN9cyx1UqP9QlGFNXqIzpfNnN3OcYByINt2U9M68nhiYeeCqM7t0Hbr6XU9p9pB0Q5+P2u6y6oU0exsbmpZWrFaQSQ5509Dd6NbinWmN8qxgHubSM8tm587y1/Y7qk/sMc0xrcXW2XpwLWOmzl/0piMw5tMpLKIWizPeRoUMlqLLCj6VKs46La02EQSmGUnrs5dKa69XJBaoi8KsgDdXSOzWX+Rr7nhx0m8mXtNK3IszrTwIiDKdHPhkdTo6QOtScfMK2xP6+zTWivCi4eSnJXs/A2jhssuveBXiZtofCHU/HKjcbjP64eGF2CaQrrQP7LtNQ40ijtsp4fhINVHhcKwOOT8rV6usbnZ4CtyX6zyIk60Y3q+zvRTofo0iREIF62zVAQdZxMSoLVSFjskV1YJb8KhtFCQS2E6/DYoOyZtERX212lXMBQaX7Jo5csWITWtPqzyGFRPScoFTsuacFMkLT+n1omCZtFhNhVznUZ443g5H0LEwOF2d1wdQJHIjL28yIcts5n6NDol9k3Mp2pc6ZJqzA54moGuxL4eLvqCaQvjhBTB8nrcT6qEpdcSRSJp6p4JPNnlKGoluEpeL82w6vex6tTXZmbRi4kiBnN+qEiHao4SEx1bdcMNColvSDO/tMIsszfKmY+Lzc7f7nLC1i/bwV6d42BOLE8M6irocIH52TI8HCLeaKVC3e4Lcr+Shus04Y5qjmelLhg1vs2FpMy2pF3oq8T1oglzZkK3Ngct4zKERci1snWC46pXZky003dFvljvhAHp7QpUAlJYJMflTi6PV3lj67RsoiulLK08qRgkTsi5oxx4Q5tYG9OnDCUITUnwEQ4X4Dw40dJ+m4AO+nxYLlAaOWYXXll1xaaxo43O1NtULTKCUpaRre17rttLeykPdO5UHelo64qctiZWZkj6DDG9nA6URZQLb32pKGdYdCvjhPYDT8VqI2CWBGphmTrD1F6Y6g5VlCRfTjMeWepkgocV6okJiTW8JsRGtamiY9lhOote14dtkWbOpseUsLStQe3a8EqqMw6ZTiM3viQT3eOJuDtJouTwGC8F7AYPxaO6ZyslX5923XGHRhtE7eKZILPTZLCGS+sjzDzFLVO0t/qw97kBXutFsU9ZgsjEtSwdFYPe6qfV9sxUJw0hFOBR+XQZPOS6a9XgiFuZmi6Q2lHlHGHSeCmn6GGrFXU99Ew6gUWf3XealynX7awVfJHr4mxiMhcV5rY7CkWWV3Hfr4+97ORiKrETokRdb2ttmFRzQw5J6BTj7WWqk1vmsFYCFDSpx0WKFKeQO3GnZpm0ydmqcFxYB8IFPnbpMLhetWC6YIJX5YVHzdQ0kE1c7Oelt9OFIp5bNI8KzWyuixNVWxpEDHvsrsGlPUII82lPn4XpPtCGehVTrmiflT3MznopEiSdG6TeOcj6NqE9eY5xzPS8X841cs8K/Crq9qWwXS3FiKCHaIs0wKx0olqHE3fEPKrYX04mcWrtVOomltby8sJarBJfgLFl2NFcdMpUVEkKh2kjy9jP6KPAW8iwrRaNFppCeA7MZmCp/VE9uZtsYYHgd/ZLqSx2lOCDhZF82J4cktcmoiXKlmCY5XC0ox0smfV5tW5W+1XDSOTE20xDxGwKGsOudmjploHTsj4jrE2qXZ1+OmXoxg/qaY0ZS/+CdYSSc9JZZ+sdXoa6YQWBa2+7HLOV5SVtuXSD0YU9rYeGOKSV1iRYAUq479GshOXJSUAUIsyIK10b7IxlZpHVLYqr2NFrOsJAfyIzhG6tZymo/qAnh0kem2nzA9LA9bK1sCasvTMO4/F1N9O0q58pwnQLzzDmFIdwveowpkZX+HV2XiKOc5rCGAVPCMZmt7S4pSYT+jjpELaup7h5qIvuiig7QyFYKSiJ+dTYNHsmpHVdbTya2JkxzaCa2/ITVZCX85CqLQDQnkVMLY9fDuvZYrE99CY6t+a9fCAAyM+I/qofSxKvmnkTaheH5CRivz5YkrEl00XmkJZ+3e8t0MjkvGduNE1rT7NjxMGX1YneH9d1h06Oc+oELwlzustWKbvYUcQRXg5V2TTH67QhV5jWxQyvXDN251Y+Na3ENTNczkvWTbImOehRoPmTWiOmGIon9aR0YcuyNheV0zHVaZesLB30kNJ1hq55zMQHVjmfXNdoHUEyesa0tAvmloaDJ52JHvES5+bx4BZrwRWn/GQ9dTeX2ouylp3YVJq0LA/zPaZ63QLdkyJ1jDaNFQh6trZqV3SRYD7vz+1kh+iy3wSnmGz0MthLVMTAIPalgVS5pbPAPAVouO6ilMgvwdDtmn3Vwta8LcFa318Nwn7nXHll4iznGWL73C47nBg7GM4yjrX14EjLOaNxGMNX7EWvUy9Tl2vJXKrceta06em0s/ztZD3siL3ic0QAb7CpgR2n17JSFzhnOssqTSVpEIjDKvMbdeo22uF4UXkvuB6ySVsirAbDLEXV16gu7QZfqI2/9NcoWAZNSsI909by3CI2vF+zl3LecpehwRtzGCyNntlhE3vL7fwsxtIUZMMJP1KXcrptZkI1vc4ptJHOhj/oNIABMdrN1mZ75D2cmcsW0lkWtcOxaSVvGKFc05wT0pSo9Yd1R4HVXZXABTk59i1oA2paqAmP86967frnw3Xn1JMdtnR2TQMfdzmuu3tKb4egHXBXH0r1sGVw4domfgGjcAxbxKlSjYTBbdFdl2hqhfYlNFOdcr0J3FOz1mdFEqfF+sobcBmsonDXhgrLIsQ2zvVYxK9l1wnbEmONfWzApFwSy+t2wq0zLfKSuRxdAxKGm9g5qjKO1h283pXaQYgbUrxQFeo3+STaRnxBg3VmPktjxkeE6SEDSwXE4ttqsFjObSzOX+d5TmHkcpfXJAaaD8yZ7ZDzlDVY3uAQF1PhoUOZsCLcdXfUV5WCB+5VWAvMbr1Y0WvZ3ymLtdjvCzpbUQIVXRA+WQpVyvh0jp1n22VUT3nNoxxSokAM9jBuo8U0W0ycmcqDVbS1pVezCMvgbmHoZXNYHaq2npZghQpPzn1EE1zGh26uKk15lLYYKdKGJfv7whXqQz4tE3s5LFKtJej5zBeX/nnqIBwfGeaOZXgMjjNpwmprdB2pjuF2dU/tD42MkaFfRWVpTzfxroQPktsuBrsv140cMQzzyy9Pz0+3s+CnVxShaPT5aTwveOz6/3vbxd4Q5G8PmvgUp56f/t/tXN53Ed/PCG/HAI5hv964v/474v72/FRaARDtvtVcxY332Lb8b/u1n//53eSRTn8/6B6PN7v6/TClNrzbtneQ2k1Vl/1blcXNbdMbOKGpxn9+qd4ehxBPN0WTfDzR+EGx24Y80KjO3m7/FfFOIEjHgzvHDoBcj1vvcWLw/GT3wKWBVb3hFPnmlPmo9+PoatzeHc+unv74P2L/JP/rJwAA -->
