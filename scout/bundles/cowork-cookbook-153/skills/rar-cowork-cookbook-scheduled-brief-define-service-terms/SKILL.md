---
name: "rar-cowork-cookbook-scheduled-brief-define-service-terms"
description: "Schedulable morning-brief email summarizing define service terms for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_service_terms", "rar_sha256": "a0409bcc96518293e36a8dec10f286fbcab75ba1b2fa70abe47cf4149488b7a9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_service_terms`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_service_terms_agent.py` and in the RCI capsule.

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

Define service terms Scheduled Email Brief — Schedulable morning-brief email summarizing define service terms for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-service-terms
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_service_terms_agent.py` and embedded as the fenced Python below (sha256 a0409bcc96518293…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_service_terms_agent.py` first:

```bash
python3 scheduled_brief_define_service_terms_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_service_terms_agent.py   # or on stdin
python3 scheduled_brief_define_service_terms_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service terms Scheduled Email Brief — Schedulable morning-brief email summarizing define service terms for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-service-terms
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_service_terms',
    "version": '2.0.0',
    "display_name": 'Define service terms Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define service terms for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-service-terms',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-service-terms',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '560e9db5793a4dda',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/define-service-terms'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-define-service-terms', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDefineServiceTerms(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineServiceTerms'
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
    print(ScheduledBriefDefineServiceTerms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjVpb2X2FyPlR5qEqxL9XRESPQBlqQ2ARyOcrsIBD77tf//b1Iyiy77Z5pT0zEqCojBZx79vOccy/5y4vV1GFWvnx5UTwrhdZWkkShV0JW6kJ81mVlDH5lsQ1+ICdL6zKymzorq5dPL65XOWWU11GWTsud0HObxLITD7plZRqlwWe7jDwf8m5WlEBVc7tZZTSC+5Dr+VHqQZVXtpHjQbVX3irIz0qoDj2o9Ko8S6toYpR1qVf+DdBXUZB6LlRnUNmkkAsYDhCg7zwvToZXoIzXW7c88aqXLz/+9OklAt9fvvzy4iRWVX1XznO5SaPFXbzykK5OwgGDxEoDQJkPwB0puM69Emh0A7eAttDz6mPlJf4n6D/+I+6sMqh++PI1hZ6fry/TPxloNxlRZ1ZVA4UdK7fsKInq4RWaJ501VMC+uinTCrKgCngzDV4fK79zynLo79Ozjw8hr4FXf/z6kgEVrMnXX19+mEz/+gI8Ab6/Tlzyjz+8JlnnlR9/+M6nauyr59QTM6D167fn9ZMtIPxOGvl3qX8HXB9Rtb2vL78xbvo89J7sBCtfXq9ZlH58MM7LrPVSK3W8jz/8M7YgAE6cRFX9L/H98cE49CwX2PRU/IdPdyf/BMFPg955/nOxOQjrX7EEkL+J+wQ9HfXPeN/9/w+sE5BY1bvH/5Tdny2A/w79+E9t+68WfIL8ry8LL4lakB2gYr5Av3xTjkv+xw/u95sffvoVsP5v2ShZUzp3Dt9uVhr5XlV/+/bjh+p++8NPP35ocpBrnnX71pTJn/H8M7/e5fzOg0+qj79fC+RraZyCgofeMx36Jcv/rfz1FdKtJHK/36++QL+tl+kDQ5MRb0IfLvhNzVRA19/48YeXXwFGpMCaxrk/BlX+7/8O7SOnzKrMryHFyZp6gpo6unmT8moYVRD4/wAo4NcHPj3oQP5PEZ40znzo5/907rj52Xni5qx6Q59vd0D89oC/b0/4+3aHv59fIRXwzsooiFIrgeT58fg1tQIvrSe5OUBFQA4QxR5q7zPAos/TFyhKoZ//Ffbf7pxe8+HnO7JHD5SSeWFCqAosfp2sPIde+rTJAc3A6z2nAUKSzAEa+RGA108TPGdJCxBu8kgVR0kCuVEJzM/K4c4beO3LxOznn3+2rSr8mj4gFYce3aKaAYJ3daDPn4FpfhIFYf019Zwwgz788usH6P9B/9WqO/NJxhHA+zMmQENRkQ4QqLHmBshAuECAAYDcY/LLr08HAzagpUAggpEfeY/FIEdjz33ztrKZf8ZICrI94GXg4VuelfXUtaL6FRJ86F1fIHR6NCF5mFU16FK5l7pe6gyAqwXMefdkmtVQBRKx8odPUFN5d6k/26V1V/EGit2qf4b2/BH0jSx563ITEVicpRFw/3suPO4DJuWHCuLeWLxChykrodwqrTwsracM33rEBfSLt+WAuQWlXvc1nZqkN7nqXiIP9wAi4BnnGdLPU8xB2wedO3WrN9l3Gmvqbuq9y5Vf0+qZ/lY5hcIB7QAIDZrInZrC354pVYVZk7h3/3mPVv+MgvuMyj0HF382G7z3b2h5HybubRz62mAISkD/l5PHpPF8vZaX67m6XEDLgyqbD09Ow9Lk8cd8BQaApxhQNd+HgjdIeUPWr2kSgbQoh789KO/+f9I80KopgTLyXL7zB8EHnpz43nNzyrWynLLa+pq+QfgnEO47XoHwgEKOH7a8CZyevmkagmqdrr+383ssS3cqa5B/UN7YCcgN3/Nc23JioFU51dczDCBRvanWujBywt9ZBQHuIB8AfwgoEYGKAd69u+6QATNBWPwyu30nj6YhCWjhNg7QFkyj3it0BiUyRaACdQkmnYkGeOHDnRV084CPgYrvHq5CK38oMw2wTwWtKRbZDWTubyPwfPg9qe+6TOoDrpZr1cCX3QS0rtc/Ivuu5zNWQNnbVIb3Rb8P99NW6Le95m9f07uO79gOqvuRvN+d80zMCU4ncKoAwNy89zx9dOTXR1N9dO13Xb78YWr/+NcG+3ub1H4fuS9QWNd59WU2e7S2t872CqBhBnIkyr3qe5d7FN/nR6l9fpba57tFv+P9cNUX6K/p9zsWz8T+AqGvyCsyPdoBWVPmPj/AHfxnzvxMTE+/prL3Pc7PZJjAFZS0Pbx3mjcS0G6C0gsm4kfnqaaG1YEeeYdaEImv6XsuPCsFIHkaTG2yyn5TwfeWCyL7CNx7RwCP0hrIdqdBLfCmbUwyqV95L1/SJkk+vaTWzfvXti8T8IOEBf6Y9j2geMDoU0fe/ep9DJoufr9ru5cVwAM3+zJV1ydoGlk/Qe/T5yfobT9w32SlDdgQ/ThNvpNIQAp+vdO+bwlt7wXsweohn3R/bHKmges5CP9RiamogMaONzXz7L1KJ4l/YAK+BIFX/pGJdP9iJU+oqGpras1R/Vbgb+n5CQLRA4UHaglAZAMW/FEMkFN6RQN6oDuZ+91/383KHrb8endD/dgp/vLyBhnPGDynQkAOavNzNXXBGchUIBBcP3IKPPsfzYtPHgDowKwCmFgIgbC247AUiTIYi3s4ZTGu56CIjzGUbzuWTZO2hdqYb9GIZXsE7fgESrAEw9i0xQJ+j+z8NrX7aNILsyyHcWiUcFnaohwPR2zc8VAMdWncQ0gW9xnGI4CL3pfGACWfxj6Mmzz5PrpOTnna/MuLTRGAckNUwvzx4WesbtnnmS2HO7hM4L7HqROu5Rqc5gZpbDNijMj5ErGwXVzyiRsksLzF8jLaJ91wvWUmJcyyHdy1zdm9JQMcrXg/JwwuixcmJqkVLQ2z43F3UJZz5SpjRe4M52qbzEpZSLaJXJW7fIsqTb3PPbEScO22yS/WzjHadkafW3HV55W6TnappLOSiQ/FuT7qNwFpWZ6kdqy4KHIlWdW6Fek7s2vcczysxrQou6Nn1YakWvWVv5bGVj413PnUonaxrZt1xm7EePDTC8JKRk6wy5t/NEh6thQKQxPPZrsSSfEsu6WG5QWF+/KqkYflbi0VhxQWcKw81Xai5Y2c3yQFTRp6bLncNF0jOPGuvtNFpSOPY5KysrDZ6re6jHd9LeyiZeFhp4zA9rW7u1iNGEtbdFsgWOOEe6cxJOTcb+y+olF221C+Fx22rL5rpWUrrs19qA0q4hJG5V3USlYKVTkPsl4FmaXhF8aWDqeq93VLhBuX6cJsV3rxmZnPDT0dtsmI4RLH8HtrOIi1tOadeuVfjlQnY2Vyzk/thj0nduwOdZRckjKuNn1P9YLNycyNIK2eLdCd2CV52UfIoJI41se5n3v56JSc54eeV+yFbROqhTXExaH0FugRlStjcE1403dmZI1bQw+xDq6P0UFrjA1PtyobYbCybfejPKLDzQ3p/nwKNyYxY4asQDErwLYWlg+IylmI6DACXAvGobfaKMuZi9P74XGzQrKbWaXYcrfwqb7fLgVuh2v7mlSx9aKc1XJTNnpo6OdNWqEpz/fSbBeP+0tm7RHhPOzZRsuiZiyUpigUuNjKcFqyOWkpBDzuCpjLZ0tntso9HmbC0fdNEBGtZTblNXKPbR/Cge5dK1JfgXL3EbTBiZzYYr1CFduhQsw4Lmq90M14s1mf7FVYxU5NXDUknxd7bI73K3HdXEpScYWFwp4K46otObflFulx4enVJtJ1NqBQncdPYbeYH7osyjPlquz602HYU9ycgw3tGtCxoCSxpo2XNAz3m+XMgZO+WdXwoTXWw001eCpYnpx4H6zEo8BFahCY1GzZkDvEX9qSLVIpFloXfGkfxIY5dgWyJi9jWfvMzLTjfjhr3nl24BqA+yWsbs3WSNYCdxK6BotV/aIqjqMyJ6KMsKq+mrwVGURC0mGPoDKiwYvswF/lVb7skBOhafBhbG7MttbBchtfGTu1RSicFxLJPqqkjrLrIhrXPMY68/amb20XaQ+UhbahUSsKEw1Fjc21jNAwl0Diq7bNjdo069jJfWSIDVuZ77jTYr/ET6oXksxpFhMRZeiR0iidUMPiikIWyl47zpJmWWgWq2/YcC/Os4u84r0ak0ikzf3asfjALrFuYVhRmXqk4dbn/ca6qN7iTAa3fIlLt71FYgm3dfPi4urUshGLfrFuWHEYXO4s5dRst65QyiVIWIvSMVnSpGp4CdZsLyK34Aa13EdHTkJ5tKWuvYopoxcbJR64xWIAgEQTftCYmxoOwsFyWHG9Dq/HxUUKGXTYjMHRS08KjmRClFp7TdwLcocjMacdTHvrjBYrKjMhrg8q4883gYYRNSepTkMw3iwbLjtaY9djQ6GSemErsgqoaogWbHdebBdamaxgTjx1onm1OkeQ+FMiqgLKm7rtNjSG0w22DBciwtnnxDDWN7ZgFgfVnqdVKkmrU5fvCs4wvEuWr9EtecDc1XzvsfMtFeQCQTrc5VS3onC4ti7vddUYd0xGH6U2RSmvtRki67UgMS8FvjnT8kxVrlkBO3Z8KaWU0LgIsVbp1RiJqjvvcd/km65SEn7l+6l+9C/42pjRKMXMkhUWF761I2RtvWvtcVAdLZ+bA7+hbqbpoNebnqy07c1QSFxbK1zTZnB50xTaloUmSPSRkUdndWYwV9O5q3Md0jLjZSsUy70RbFWOUMJrFYvk/DgUh8IbzFugcjB9GpCeYnZ4waPL0RMy70SeFuetLTZDHV6ZKBExN+WspO80/rbLClO8Hn3OrHtRdxuep/xSvSH6ihYthKoWcon4+3huLAS8ShxikOrZQVquiXFt7zfaeU9cKPPKYFrgyUdDOWz9XW2xK5T1VOk8iuOFNsNNuEBVdxttz/3NJWBawJf0cqNkyNnPCo/0JM5W9oaVEdtB2i22ca2Q7nBWtctM3hx5npNW7nXbh4TlD5kIctPaynSJJLbKrdNsOFLlOdftLiPE5TbMA2N50ImDSGano16h7p5RfYvZauoxWUexdSsUKxhW1AKZq8y6kNUjd76Ux0NM++eQn4+URi3H6rDeFTGFAlhaw0w/pwRu3zmno43ToCdT9nVnnbYrtCIWek8M7oDPMb+6bDuZyM0k4tpkvoDHpeou67DNCbRUVtjA1hjJyu5YYJ4l77Fh2XIziwKp51wl+hwgQS2QJaYzrKawMhIt8VC5lXt54aUyryJ2oVrbrXLtxmQvmJLM2JnUX85nQTE1pFkeMN471fKw2cuynGtbs5DKfXHmubk1K5QVKx2kpKVOyjJQsuMOGWf0rg4dhtrbe8QJEhU7z5UuJA/UUuLiWaollSFr9vWoGRmMw157VHAOIKWlI0WxqDrQxc5XTzXXJpO2p5jAb7v8gDo3XKPaSz+uhkOiefWsuTpRgMmhsu/5gWRRNIi4KgyS0yG/Xj1viynX2N3MYRnk7Q6Z0wvNUHuiGbS84PudsATuNdFsrNTLILKL63jURLuTC20rFSQo8l1bJvlJK/Gq1+W524lDoYJOrdSGVffRppM2xIKPabSA0YbLRSmd72RtxeQFoqLXEMniaFDW/k3NE07xMoBPnFkou9VFXhRtnLInE6XOhS2m2HC249VqzySJzXbX26rftyvr3Ng8ccgQ3Yl15KJuJa28CccFDxL8ZMpbXkHwfbrokd2ss1l10JFzKIYDgJjLwkq5RNzP6mhLCUFxON6umwXDVzJzyjy3ilpW0nTQaWHM3VxCMxApNFYXSTU4MiaXJW5RNL29EDv2NOo9T5gHdJH2CR6YWMDWBMgGbp9YjcCEip10s8owmArJCimkrqV7kCoUVgV6UI/9WfQdVy32I7OQd/OGGoSKTvbsGq2F6yIS8NVJ2NNNLGabc2TSIKfInDRPJG+nvjSXAg1UMj2W1GFV4PnMpuZqfObd2TUOjaPTuu5V6ZEQWXv+mUI5AGBefq5PMTw3snStzO1cXJ8DagjwHAywG9ICt2+ZLBXiYhdbWs7aZZpwLnG1z7Ez1PkplWS6uGztQ+J0/FkYL1WsL2CTCpl9Si6Hi3jU1kucTgqvGj1LW3Z21460icFWvmyivCpqIV0yomNZp/3qJKEleU1nMsgFh9ctmuIBlDNZf6WcNFvqgbRu2aEkqAtBYlTLq1rScEvZqJqKr7SVwXgIj2MzDWM6Gs21pZGaKyOyNlHH+VRj3mTdRZUbtTeMZbB3dTg/88hlvk4wFGHKANGHvD0J8SIMwPxldrqsBgsftfYo1vHkaSSlxZEcajFn4XqHzkNUjmbz+biwt1c4IaTOpHDn3IlnPubF27h17GVFnnQ0kMUw0j2DIHZg+DMRoQ+QdryuioEiZ/VV5nzOTnZZV2+WK0Y5jmOxLsb2Fi9Ph03uCCSM7Nw56hJb7ZIIvrsHsyLDSGwTeipM48RsTYOB4YjXVm7jNuVtjjQaFT69IzxcnKH2LGhclGnCqMbpClnzeNuGTWUKsr5FGtpxaLUtLhsF7KpCYe6p/um2XPe62pwb79ZRRY/RvFV6N2whnYSIVfaUw6ThIu991p6LsMCVBOnrumePxJ4RG5jGAu6ELzezTXvDD7HAXnW0Pa+OSD+rVycHa66gIvCZmIDN27lpQ1Pl6C0G0+G2C/305NCNQg407l4WiOeZNAxj8IyIWEEnLMBoRuWzq11gme86MFNSRH9kwY5clsL2tItM7UTxZVeJeTgnu/Nxny3t5hikIyeKezDwAxw/L0chsJau5J2uvUAFTN7O152xEhhlkK6pd6Ys3ZZcZrf3eGyXHnH3KhPN/GBYg65yB8Ud0NbbE6R8m/ejzUTmxefwWhLsSxUZczr08IU5nvziaO6u7f4WnPeG2dr5hmilAbNJfqZtbnY+WxfcgmWDRQrHR9/lAmpt73hzwaIrM2C8aHFZwyR1nRm6V8zY2j90/SlJT6Vvysf5QSfnzLntMCmkyZG5IvjSsMFWBptXRHCstjCxr2sTHoKWzfGCFLOTt8GueLp2SIkkcTBImGIzX7ajVl6IDT9bi82qW5/qMZC5LobDhVqg0R4vd4ys7ulTteTWrpXayKE/keOWYjV1hKlgI4PpRNoJeSeMRszb8E7GTXFYHrtkTNOr7fgWxyCLxTkw22hzIPQTC5fSzIXhYdzPR3fBnjZmhWr1yBgOXp260yqpA/7IrRLaItareV+dO1QO4Vm1Qg0FFxSjZ3KfU7Qtvmw7runrwqPX9Gpe9zEezEQaURxyB+al1XForUUy4pQ2XIQSRTxCZY5nb0gp7GqIo0NTzIUl4q3gzGRKkOYzbs/TBLEew2DF+JgwnnfBXi2rIz2LzyZLrstd1QebDWceEvkwgP0InqnslhbTc0NhdO/uRmHPelSzFojG7besb8TBKFdzvqJzuBsR07jg5u00R89HomI3pGa1Mby5Itd4d3FZXYUzdaFhN7zr8GFupa5v8KsAZmpshljdrnfRlmEoh0THs8+Y+dyn2xRGik0yN9B918+ODJip6daN4aW1kmvngPttfxlmjdtU8GK80c5pBg8YW4XLA4sPq6oVLThVVvF1l13V5RIjtre+KCufYWe6JIY6TFxl5Krjne4EbG4QCDtHlst+q9WMcZyRRDmsIn3dNscT6ToXMkZxsWz1qlqwIrPRAtUojvzqWDHZ3gs38mweHFZycJ2PKKNcvH60wLh3w0c7rpobPvOKhJYJhEGjisuUxDROM7IkpdQRvEXI+PrBx8KNn0tM58znrSOovWtx7Z5wMKEohxTX+oJL1Vu2JAdmu8Zw+4pkWwuvcmtxoW8LYhgWMoscLh3YsJ7rY7BvwRYXbyL0OAqqRToh0rK3VePYzuZszI46SgfWPJJgXZeog3grd0Hf6+x2uc1nAwLkGXt6g3FS26PEop6LHKhsY+SiXIpvocC7bdwsvcMydGVyBSYIhjWbq8vS6kZwD7Lt0EeDR111pBZdF8tHXt+e5vOXTy/TgfTzWPkvvTieTvn+1w4bH+eCb6+Z7kfKnuV+ucv68tfU+unTS+lEQKnHwWqVNMHzCPIfjlU//ysvKCYOw+Od7PRWrK/fTuJrK5j+tuglSkGu1+XwrcqS5n64++nFbqrprxyqb89D7Je7cbd8OhH/B2Om83KrAkZk3+4v0t9YROkk3nMjq/ael8HzzPnTizuAgEVO9Q2nyG9emU82P998TMe006uPl1//P4+3LJrKJQAA -->
