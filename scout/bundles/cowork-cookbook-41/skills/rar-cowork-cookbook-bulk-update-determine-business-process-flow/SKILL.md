---
name: "rar-cowork-cookbook-bulk-update-determine-business-process-flow"
description: "Applies a bulk field update across determine business process flow records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_determine_business_process_flow", "rar_sha256": "5eee37ddd22445e4614ccf34b4c462b702ed51f3fe43a22d7efc157167d17074", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_determine_business_process_flow`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_determine_business_process_flow_agent.py` and in the RCI capsule.

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

Determine business process flow Bulk Field Update — Applies a bulk field update across determine business process flow records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_determine_business_process_flow_agent.py` and embedded as the fenced Python below (sha256 5eee37ddd22445e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_determine_business_process_flow_agent.py` first:

```bash
python3 bulk_update_determine_business_process_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_determine_business_process_flow_agent.py   # or on stdin
python3 bulk_update_determine_business_process_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine business process flow Bulk Field Update — Applies a bulk field update across determine business process flow records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_determine_business_process_flow',
    "version": '2.0.0',
    "display_name": 'Determine business process flow Bulk Field Update',
    "description": 'Applies a bulk field update across determine business process flow records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-determine-business-process-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd43c76b21ba53c6b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/determine-business-process-flow'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-determine-business-process-flow', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDetermineBusinessProcessFlow(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDetermineBusinessProcessFlow'
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
    print(BulkUpdateDetermineBusinessProcessFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abOjxprmX9Gc/mC7qSp2EHWjIwaEEAhJSCCEhOtGmX3fQSwe//dJJJ1j+y7dc3smYuQqS0Dmm+/6PG8m9eub1bVhUb99fdM8K19srDSNQq9eWLm7WBV9USfgq0hs8HfhFHlbR3bXFnXz9unN9Rqnjso2KnIwnS3LNPKahbWwuzRZ+JGXuouudK3WW1hOXTTNwvVar86i3ANDGvAFbpV14czfflr0i9pzitoFF3WRAQUWUV527SKNmvbToo/acOHW4+e6y8Es7x55/cL2/KL2gF5ZFrVfgEreYGVl6jVvX3/+66e3CPx++/rrm5NaDbj1xgHF9IdG/Lsm3EuR41MPAagBxKRWHoDx5Qhck4Pr0qvBQhm45Xr+4nX1Y+Ol/qfFv/970lt10Pz09Vu+eH2+vc3/qUDTNvQWbWE1recuHKu07CiN2vHLgk17a2yAxW1X57PTGuDZPPjynPm7pKJc/Mf87MfnIl8Cr/3x21sBVLBmv397+2lR1GA94BXw+8sspfzxpy/ADK/+8aff5TSdHXtOOwsDWn/5/rp+iQUDfx8a+Y9V/wNIfUbY9r69/cG4+fPUe7YTzHz7EhdR/uNTMAjo3cut3PF+/OmfiXVCz0nmsP4fyf35KTj0LBfY9FL8p08PJ/91Ab0M+pD5z5ctQVj/FUvA8PflPi1ejvpnsh/+/xvR6ZxZHx7/h+L+0QToPxY//1Pb/rMJnxb+tzfeS6M7yA479b4ufv2uHdern39wf7/5w19/A6L/SzFa0dXOQ8L3zMoj32va799//qF53P7hrz//0JUg1zwr+97V6T+S+Y/8+ljnTx58jfrxz3PB+nqe5EWfLz4yffFrUf6P+rcvi4uVRu7v95uviz/Wy/yBFrMR74s+XfCHmmmArn/w409vvwGkyIE1nfN4DKr83/5tsY9mzCr8dqE5BUAhEOA2yrxZ+XMYNQvwZ65tAERe3UTAsa9xIP/nCM8aF/7il//pPDD0s/PCUHgGx+9PWPz+gYff3/Hw+wsPv894+MuXxRksUdRREOVWulDZ4/FbbgVe3s7LAxBsvPoOgMUeW+8zgKTP8w+Amotf/oVVvj8EfinHXx6YHz0xS11JM141Xep9mW02Qi9/WegAZPYGz+nAWmnhAMX8CEDuJ+CLpkjvAO9m/zRJlKYLNwKYDuhifMgGPvw6C/vll19sqwm/5U+AxRdPHmlgMOBDncXnz8BCP42CsP2We05YLH749bcfFv9r8Z/Negif1zgCyH9FCGi41ZTDAlRcl4FhIHgg3ABOHhH69beXn4GYHBAfiGfkz0Q2TwYZm3juu9M1kf2MkdQ77QB6KeoWoPYCkM9C8hcf+oJF50czrodF0wLiK73c9XJnBFItYM6HJ/OiXTQgLRt//LToGu+x6i92bT1UzEDpW+0vi/3qCFikSMH/ZjUfg8DkIo+A+z9S4nkfCKl/aBbcu4gvi8Oco4vSqq0yrK3XGr71jAtgj/fpQLi1yL3+Wz4Tpze76lEwT/eAQcAzziukn+eYP4gXBLZ5X/sxxpq57vzgvPpb3ryKwaq9B78DVcZF0EXuTBF/eaVUExYd6BZm/wFNZ0mvKLivqDxykP8v2oeZ3hfCo+94svziW4chKLH4/9+azOqzm4263rDnNb9YH87q7enWuaea3f9sw0BvsADzniX0e7/wjjbvoPstTyOQI/X4l+fIRzBeY55A1tXAdyqrPuSDTABuneU+EnVOvLp+OORb/o7un4B3HlAGYgWqGmT9nGzvC85P3zUNQenO178z/cs7c42DZFyUnZ2CRPE9z7UtJwFa1XOxvYIBstabC68PIyf8k1ULIB0kB5C/AEpEoHwAAzxcdyiAmaDOHt7/GB7N/RPQwu0coC1oWr0vCwPUy5wzDQjAHDcwBnjhh4eoReYBHwMVPzzchFb5VGbuc18KWnMsimxOjj9E4PXw9wx/6DKrD6RaIJWAL/sZfF1veEb2Q89XrICy2VyTj0l/DvfL1sUfaegv3/KHjh94D0o9nRn8D85ZzEnbPLB1RqoGoE3mvRIIZMKDrL88+fZJ6B+6fP275v7Hf63/fzCo/ufIfV2EbVs2X2H4yXrvpPcFVAEMciQqveZBgJ+fxff5o+o+v1fd51fVfZ6r7k9LPD32dfGvqfknEa/8/rpAvyBfkPnRLnK8OYFfH+CV1Wfu9pmYn37LVe/3cL9yYgbcdASM+8E+70MABQW1F8yDn2zUzCTWA958wC8IyLf8IyVeBQPQPQ9m6myKPxTyg4ZBgJ/x+2AJ8Chvwdru3MoF3rzdSWf1G+/ta96l6ae33Mq8f2WbM1NCNg9p5l0S8DxokdrIe1x9tEvzxZ93eo8aA+DgFl/nUvu0mFvbT4uPLvXT4n3f8NiS5R3YOP08d8jzkmAo+PoY+7GNtL03sGNrx3K24LkZmhuzV8P890rMFfaO0DNxvUp2XvHvhIAfQeDVfy9Eefyw0hduNK01k3bUvld7A/R0QQv0aQFiCKoQFBbAyw5M+PtlwDq1V3WAHd3Z3N/997tZxdOW3x5uaJ87yl/f3vHjFYNX9wiGg0L93Mz8CIN8BQuC62dmgWf/N33lSxQAP9DMAFmk53k47bouhhEE6REUSjiOjxM24RAUZtMI5rkk6uO+R+AWhrm05zsoSaMU7aI0QhNA3jNVvz/ZDojELMtZOjRKuAxtUY6HIzbueCiGujTuISSD+8ulRwBPfUxNAHK+bH7aODv0o8WdffMy/dc3myLASJFoJPb5WcHMxaIw2lZDG6op72ZeYcnOLyXSNKsxL9UB34ysWSDOQWpXqRuEkCplZR013KTF7a1HJL9Yw+aWids8TJ3y3O6EW73hDLRz9pivwNchr1aspCaMXt2qdio1SS5aHy2q5Z4XmWt1zdR47JDoPlzkBlm7cB5p4wVSFBxfXsq8ci1D2wwrqKmvFex0Rb8LGHzrDcFVjk0hCCABO1XmysTTi5ZqttNtu4OYqtFZsNNS31wBEVFop8qqUaZsdGi7dpd5MeJlkzn4+YTQfs4vVXKE/euxJ9bYEmu340WOOqHeVwf5qpFrJkjHAsOk0iJjUZUneFVy4uaC0duTE7eyezlLt7svrS0SqbJCWwvqYKh6tVa9XFgO3qnsVpguKUu7XxPUNrCIEdu3+1rVSsmxELlCkEwPD/7t6pZZBxjbNCcJwjbHZo+hY3U2rHFpGquzKZ3zi3muDHnUtUgyr8g6c9bxbWVmnOOgMr4ZkLuSl9JyRWKccGdPAhJdlvhGnzAkWcG2gjZ4yPEIsgthWZMlz90IRpH5bSzpDU8J2S23ifWGKiAzcYMK42/m4WahGzKhNX0YBmu7bWrY1OMQqddEbfXXmLjmUbhalb1ORE53LrjUPq7vV8OzZXWaGvGUkaHXecY975iwjVucNYAyTpwmWDc6dQOftctanWwjUU+hUIyHPS3V1XTLZHxcnnbHjKokweqzYXOHmkFIJIfYV3iZTYKxhpdn1SL0k1/c4oMyiaLkJOSRW6kTt7vdYG4Jd1A9mJFOWuTVmfK9Ae1hmzCJHFOiw4ps8oPcVumuwbLzldlTd+oG3SlLvzLIOd+tDaJT1rS46xu7P/GY5U8TLY61Q11CrYbDZePEJgMrR0QbR2WXnmuTW26yaoTXjKBgu/jkGXl+0JMChdpVfUsIU4BNwyZ5bbM3Q1KK1QQJoL0mHaatLU8dF041qXXV6UriNqEQzZ4yemNfyuIWLRrhzuenjYxHwZ5C+sMJX0d24iXqho95XWoMKQoSMYHMq5ghfHTrjpe9HV6MgVkSAoLWIi34p867NkdhZxyblBGJ7agx8bRs7fQQMNvt3ZiGQ7tEz11/r5qYoo+8dkzPCnKEXOZKC0UvEEiCLH3hRmNwuul2uOnGqFTIib3e1XpSI/l+ufaUEPESE26nrLy0rbjW/RuWXoxt1esCYijRngaFQcv3aqlWE0UaJxGH4luYMkv4YhRRPi4ZaScUAmTfEq9y/RsS3BlL0yr+ZiWXCmGw6iwtq1MiM0aXSnpXNNldcw4ZsU+9IkKTPcfsJoLr5AlPkvpGukigeQx3HKouiffwZrKnbViU6zvpwL0SyvnIthKKQSxee0fluDmpJW0K9XgyaSwzdmczVpVMh9S9z14NvfIUE1XLkLMqW9gVglqh2ogrWhDf9QYRTuWR9I5UVh205Ho9IoVOOcW1Lg8tlVf0IV3zS1GWm2jrbOkoQ3Edw3xEti/Z3WRUVodGxWcGGNoaOdyXa4rzXLbcr0ddvxvYlG1R/Ez157hH5EbnYISNnDggXWE4FwxV7S+h17C3Q5+I+3yLbYdpKYv77VYsu7UEASianIlLL+gN8rPjdDG7tAm4YMPoPNLc1tSgervlisESNaj3aml1hzW3XaXi2laxW5vl/dk94Il83Yh7FuNBol5ZE93xNhnXK7WhGZCUB2cVqEhaneUpikkLxcMBF8UYa/pK22E5clENuLMOMVxDV8crNctKKHqyScjPbWbp60QT2NgedTmUgTxiXTDaPTZMzCMHheP88qgtyxJmbqmo03Gl0Kazj0o+GUc4uuOEe7z2p9GCoGgHKb7ME2ddOIfXPMfILc+G+s6tznoYq0fTKC6CToH0yQgtFXvh3l4O5aUY8isbmlwlXYgVsdmmBnlN0C2biHArqYIgqlkVWUE9CuyF1IKrmV6HrrvpQ6mi55birOOIH1rhWKcDuqKi+l5sm9xKDFJADkd2r0ZRF9lVhnlZiWo61clWfxZQ5Syj8J2EmC06Xqh8z97rPBY7lDQHDRU7p6GqtkhQ2aR3TnLYccgZqhQAs6GNtReHOjuJ1GJKTpUhnXAxH4aiTd6Htha2edvWVEq78Xhb2cfT+hja3CUISMMB5U14DI626Jreib0uVWaheEy83GvH/a1zN1vsZATq3rykVCJ3IwjwERI59h5VHM+bWLKf9DHj1oGwCqxENhAyDmXDXotUe9ltYiPecqpV2Kaghkv22G33Q1wLFXEBVAPIZaj8bStkqKITFJvYCIeyKbFRucuRA3vS3ZYg4CSUTyN1ocjz7eBfTfNSSNANlctqh07r6nLmhzXIGX2zxLaVHm8FyeTwUOHZRtJq52xRajKeuBNbakND48rhuO657WSUkYAtHRunG9OLd6VnrSS0QncsXGDNOdFWpxz0BadwL9DT9aTrIjW1veqFrV2U2lE2xRJWk5LjLE9LvRtbHgTP1svevDB0X+x3Tr+FPMltlEi+5NI53Gw2CVvxEtRoqduvgXblKh+GEWlhTdE2lzULHZQ77BjZgRyRBkoLUpIBI4VnR0xoNKCyi+FqBp4BlqMpQoVyG54ubOR6eqjLNEvvUZEmVJFHzK7cmtiouG1MTeZl67aKrVybweWlC16btENf2auE3NjLQGMuya3kGqwu7rlmD8dQasiOx8PaWltjexvrDo2wIyH3Sm72zOEmNBz4nVUkjm3Q02l7PeuMitarTXWVtQvmFpvecieIT5VyvaNumy6JTjJ51QB+UxdFMaBBZdne5KENnbQnS5aQ8pqEClc0d2e7HHpSD1RS5o5nU+8DVLFOopRIDL6ROESbrlDZLsNtyrTIUWdHmfY4eJdFDOcr+/WgSC0pjUhgavyYElfz0MgXJCwlkxARZr/HCE3a9uUpwxNCZ/sqEKvytNEvslKLpmzzh418NJJYPhDZVj7EMb/c1BxzakoFM1XvTK5tYrt2KY3cqxImKZeMmbJztVtJtmdfY9+E9xelsneN3QW41kH7qnG0/uDzvbi8sabsOkdztcHr3L/J91IYNKMcmKsRk2xhiwYgytSTxx2AMVfP/LLeDud7EZ325CipISrtz4VGlQ3HBXFEmsyJQlZXU9uI6519YiXb2Zm9knNCTRe10QXIvR6MVVUgnm4lGL9NFBpW/d4/5OrAYUeFvyAssjXuUYpoerY6CuahXzOnydvrW3UMAEny04qHU9A+5UPtRIYV3ZZFk3Rb8hSj99bbA+DfHqpwlIkyISbfXG2nw4HecN2w2eyL5B7eWNbZr8R4jKOuTS8yItVHP9rcU3k10owCsM2ArO26k6GmYZy10JKOJenn7clDmiIxE3nJUqx76CBWEmN4s/eVGjBdxvKaxaIX0kOX2dLZuIdqnXPxkSfUyk7PuykbySErIAamIiy7EV0jBR0driEtGPOwHs1zQ9n0ETBxHRDFUuR24jIBPW3YI7pnqYRB6mnqlocQsAOH3eSz1I9533o7atK2p2m7Ouik0u6MjM4xKAqq9mwEbNevtAbmTjx+var4yJdOYFwkSPIShXQ8f7MVst1KtzIx2h/0zdQmgrgZKkDvEWwzAs+rV7VBGWQ8HnVzSZoBo54JpzXwK8NIwWpTdnWNHrPGvOE9hSIwFhyWNGhnyICESITKqKuYQ7dMOaodXRO2BYso7BKTujnD912wqkj6gsfmFe0VF2xtcfZmK9id9y89o52PdjcKJVrlW6Q2ktsNIA2OyB1Hmzpd7Iq2w2IJdg+Hm3O+iqyq3oakDITB19YsL0L4cMYjK9wphDeOVd0Ok8Fvwj0x7rm0yxDZg3YONp4xxb4wNwI+5xAScz1FKRgX+xN2XXIX5waBGVND00zF1muALfxUq3a3u1+pXiyWS/8OxwwD9yyyMm6Vj4rw8u7HwCgb73Q/v/DGrcaW6cDW7bUSiVtOEKszcS+33Wpn+jXPG8elAFl7hQM7Q6MDDHbyid0pHvB+s4yU/riyca4Rh/g4muKA422XgX1cfnMmQbbRS2LnOuIdgtoIm3Q9xTrl6Sndx6JgJmtnbJJpVRMbph531jEfEbG8tvRliexGBuMIOqqKA752rwwRLsXcvl6cwIfzcZe0cXUCheisl/4SdNYBdw2zsb+y00E1TvmW2g2ITaeUOLoXr4KpAcqHZMpcjoG4fccKbsaPHrQiKLEVRVw8CxoNpQR9W00rLuvrqZk2KEPvRhyLlbq2OJP2K1lRCmiqCYQm+T0oOIXL7TsobVCXgwL2popkbOrNmZKxwqTXzt040hVedZy05w/74Ygv8fXOW9cT6h6PB4l3GZUYQlM8hqcbbMlIdHLc0Fpv7+hhSvPoqtw7YYkA9wfGfSUyxCVy4AvYHsF3PrR5c/JR1o/4M4939H5SUI5jvRumjrd1w7f5KcFAcHpRuskjwxyqXUXzt822pJf7c6ZQjcfiTEYHtB93ejQJtjcBP7jaJKw3I6bj8ra9HvImqKRAveaIQ7hQsjv6vOtq+Gigd5wOdlc5jkQBOa6O/Y6lepcnetRVViJL3rkhvfRoTtjBBuyVClzE2ma94px9G2JogWtTcT64DHLpzu7RY45GO26MwqFggfSiUYDiA1Gs+7pvT8DLfiLzV6LCNxHLywOT3NXMFXnzGBOMQK+zq3/Zw6V9C0RUodbG8sSf6pYhT1eBoW30jnq9tTPRKyK6HQVDbcHeBsml7zWDymLK1viZuJxI34cN2Nsr+O583thdqiQH+NxtuzvYcPfMEfFgyfVZMzlAQFALCx5UV2LCiWOcFXIRCMf4cm1xM4eXjc9Vh+q+YVHHIV1YuQ5+dF/aGWuxmi5WECTnOUSgKjs0jIpLhXc/IrC6oasejyAjzKqlbDlUbZgg3XsX2e/OPDsEvZEEfY+oYrbL+ALsHap72/IaXfvt/XCNa9Ct0KIU6+yONyJozCfPK25uV/dLXcBAe0GINMyPrJAG524d9u0hmNLlZr258KRmnxyEncIp0U43CN2ZdTLQCbOmdSddXb2JV+Q81vCcwkKbobe3Omrq8RrATYZm21uGjlRc+rRpkOS9N0x/6Rp5xxUGN04VMVbaoAxEayf+CBq3I1HqJIZMEBrpokLRDhcH2xth7GwsCNn47Dvh5RCXBpL3wpiVzcQj525/t8OBIbb4YWlNCgVZyzXphgN1gNllAzXpjpRPLPv26W0+rX6dOf93XjjPh3//z84gn8eF72+kHgfOnuV+faz19b+l3V8/vYEuAuj2PH1t0i54HVD+zdnr53/hlcYsaHy+2Z1fpw3t+9l9awXzv1p6i3K3a9p6/N4Uafc4CP709reKvj1Mzcr28ezDtPlc3Wq8723x/fEq/n16lM8qeW70HDNfBq+z6U9v7ggiGDnNd5wiv3t1OZv9ek8yn+POL0refvvfcycWOSYmAAA= -->
