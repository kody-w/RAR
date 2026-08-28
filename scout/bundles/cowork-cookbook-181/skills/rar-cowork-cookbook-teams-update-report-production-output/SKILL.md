---
name: "rar-cowork-cookbook-teams-update-report-production-output"
description: "Drafts a Teams channel post on report production output status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_report_production_output", "rar_sha256": "545edc14b684915efb9fb33c8b413e0bc583375d2a24b28d44204d716ab12d66", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_report_production_output`. The original RAPP
agent is preserved byte-for-byte in `teams_update_report_production_output_agent.py` and in the RCI capsule.

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

Report production output Teams Channel Update — Drafts a Teams channel post on report production output status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-report-production-output
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_report_production_output_agent.py` and embedded as the fenced Python below (sha256 545edc14b684915e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_report_production_output_agent.py` first:

```bash
python3 teams_update_report_production_output_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_report_production_output_agent.py   # or on stdin
python3 teams_update_report_production_output_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report production output Teams Channel Update — Drafts a Teams channel post on report production output status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-report-production-output
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_report_production_output',
    "version": '2.0.0',
    "display_name": 'Report production output Teams Channel Update',
    "description": 'Drafts a Teams channel post on report production output status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-report-production-output',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-report-production-output',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f11de26cf197494a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/report-production-output'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-report-production-output', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateReportProductionOutput(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReportProductionOutput'
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
    print(TeamsUpdateReportProductionOutput().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+bfaSLLmv6K574eqethG++I+fc4IIRAgQGgDqdzHpSW1gDa0SzX1v08K8HXVq6433XPmDPa1kZQZGfFFxBeRqfvrm9PUUV6+fX7TgJMhaydJ4giUiJP5iJB3eXmD/+U3F/4gXp7VZew2dV5Wbx/efFB5ZVzUcZ7B6cvSCeoKcRAdOGmFeJGTZSBBiryqkTxDSlDkZY0UZe433jQFyZu6aGqkqp26qZAuriO4KBJnNSgdOKIFCO87xeOL4JQ+EuQlcm9i74ZAJZwQfIIqgN5JiwRUb59//seHtxh+f/v865uXOBW89fbQxCh8pwbqY3nlffXjY3EoIXGyEA4tBohCBq8LUMKFUnjLBwHyuvqxAknwAfnP/7x1ThlWP33+kiGvz5e36Y/aZEgdAaTOnaoGPuI5hePGSVwPnxA+6ZyhggDUTZlNAFVQ/yz89Jz5XVJeIH+fnv34XORTCOofv7zlUAVn0vjL208IRODLW9lM3z9NUooff/qU5B0of/zpu5yqca/AqydhUOtPX1/XL7Fw4PehcfBY9e9Q6tOZLvjy9jvjps9T78lOOPPt0zWPsx+fgqEvW5A5mQd+/OmvxHoR8G5JXNX/ktyfn4Ij4PjQppfiP314gPwPZPYy6F3mXy9bQLf+O5bA4d+W+4C8gPor2Q/8/4voJM5A9Y74PxX3zybM/o78/Je2/XcTPiDBl7clSGBylI6bgM/Ir181RRR+/sH/fvOHf/wGRf8fxWh5U3oPCV9TJ4sDUNVfv/78Q/W4/cM/fv6hKWCswVT62pTJP5P5z3B9rPMHBF+jfvzjXLi+kd2yvIN88C3SkV/z4n+Uv31CTCeJ/e/3q8/I7/Nl+syQyYhviz4h+F3OVFDX3+H409tvkCQyaM2TBCaO+I//QPaxV+ZVHtSI5kFSQqCD6zgFk/J6FFcI/DvldgkgrlUMgX2Ng/E/efjBZQHyy//0HnT50XvR5bye6Odr8+Cfr0/++/qd/74++e+XT4gOhedlHMaZkyAqryhfMkhvWT0tXJSgAmULKcUdavARktHH6QukSeSXf0n+14eoT8Xwy4PS4ydPqcJm4qiqScCnyc5zBLKXVR4kYdADr4GrJLkHVQpiyLAfoP1VnkAyridMqlucJIgflxCAvBwesiFunydhv/zyi+tU0ZfsSaoE8iwT1RwOeFcH+fgR2hYkcRjVXzLgRTnyw6+//YD8L+S/m/UQPq2hQIZ/eQVquNWOBwRmWZPCYdBh0MWQQh5e+fW3F8JQTAbrGvRhHMTgORlG6Q343+DWJP4jTtGICyDMEOJ0QhQyNRLXn5BNgLzr+ypmE5dHU3nzQQEyH2TeAKU60Jx3JLMcFjgYilUwfECaCjxW/cUtnYeKKUx3p/4F2QsKrBx5Av+Z1HwMgpPzLIbwvwfD8z4UUv5QIYtvIj4hhykukcIpnSIqndcagfP0C6wY36ZD4Q6Sge5LNtVJMEH1SJInPHAQRMZ7ufTj5HNY71PICH71be3HGGeqb/qjzpVfsuqVAE45ucKDBQEuGjaxP5WFv71CqoryJvEf+EFNJ0kvL/gvrzxiUP2rDuHZUAivhuJZz5EvDY5iJPL/v+uYVOXXa1Vc87q4RMSDrlpPCKf2aIL62VHB2v+Y/EiX7/3ANzb5RqpfsiSG8VAOf3uOfAD/GvMkqqaEOKm8+pAPvQ4hnOQ+gnIKsrKcwtn5kn1j7w8QjgdVQXNhBsMInwLr24LT02+aRjBNp+vvlfzhRGg2dDsMPKRo3AQGRQCA7zoTBlE5JdYLfBihYEqyLoq96A9WIVA6DAQof/JCDD0EGf4B3SGHZsKcCso8/T48nvqjp5egtrD/BJ+QM8yNKT4qmJCwyZnGQBR+eIhCUgAxhiq+I1xFTvFUZmpZXwo6ky/ydIqX33ng9fB7ND90mdSHUh0YXRDLbqJYH/RPz77r+fIVVDad8u8x6Y/uftmK/L7M/O1L9tDxndVhWidThf4dOAgMQBjAE49OrFRBZknBK4BgJDyK8adnPX0W7HddPv+pT//x32vlHxXS+KPnPiNRXRfV5/n8WdW+FbVPkBPmMEbiAlTPAvfxWYA+PlPt4/dU+/hMtT8If2L1Gfn3FPyDiFdkf0awT+gndHokxx6YQvf1gXgIHxfWR3J6OtHKd0e/omGi1WSAFfW9xnwbAgtNWIJwGvysOdVUqjpYHR8kC13xJXsPhleqTJwTTgWyyn+Xwo9iC1379Nx7LYCPshqu7U9N2nMPk0zqV+Dtc9YkyYe3zEnBv7h3mTgfhiwEZNr1QORh31PH4HH13gNNF3/cqT0SCzKCn3+e8usDMvWrH5D31vMD8m0z8NhiZQ3cDf08tb3TknAo/O997Ps20AVvcAdWD8Wk/HOHM3Vbry74z0pMaQU19sBUx/P3PJ1W/JMQ+CUMQflnIcfHFyd5kQUk9akqx/W3FK+gnj7scT4g0H0w9WA2QZJs4IQ/LwPXKQFkesi2k7nf8ftuVv605bcHDPVzm/jr2zfSePng1RLC4TA7P1ZTAZzDUIULwutnUMFn/3fN4ksI5DrYp0ApFEkB38NIl2ZJDqNA4HKBSxAe65IYAVDXo1iCYCgfd3DSxVmfJHGU9BmMdlwM92kaynvG59ep1MeTYrjjeKzHYKTPMQ7tAQJ1CQ9gOOYzUCLFEQHLAhJi9D71BonyZe3TugnK9751QuVl9K9vLk3CkRJZbfjnR5hzpuOe564aybMymfU9QZ8IozBusxYzjiZ7P1Zkc1oc1rFerCyjZLfuTavvDnndemjOHPcHPkDNuXUhZGUUqEDdJ0e02vuosKhdaYv7mQ2yLEkLjd+od86wvGK32plbmta1bQTSMr/TYjoziFXU14VNlVe5D2xpp+VZELSJqQhMUpVbAeSZqPX62gxleWAqA78V51q9XJokl9NT45v03bjJkUZeNXMRcN22qg1ZRAuituhGVc07MHeRo6i0f8xKlg6ykqSCYTxemJ7izvucuA+mxvcotT2ffNfAC4fGW1l1HCxMhD4rr1smqrtS8M/rUoSC9hF+qepu5uVbGSbAesFvukajzF1C+20qY0YD7rZ8poXqPAp5KRtx5QWMpjYmeT+jRBjHtXm+Fne72Mrljto3Pc65oPc0pkmJ2drdURdZWUmdmW47e5tmm3FoSbTLrHtirG8VPY9yx8hs2s02ybjaeiVxHohrqoRHe9CYcjvr7+re96iL4gqkNFJa3MvVLBU9cyPG6/3yyIG7uZNIS0NLw3eolSvtxuVlSyrR1YxPuFBSB5XGroyZn8doq1/KbXFr+/ZQnIDizPWUOgvsnGd9wzlhJp/djGTwebyl6ISmBtnGG7Dkhz3hyag84BQ5P6U9nhuyWwJFTTvXC01ANVGWWp2K78krX6drd3O+VoY/c7yL4251ZYXqAFubQqy5ojOn+8P51IxhF3DeYA39dR47ykVoMma1qvPZhsWWNyMnd+cjabuadFMyjmn6NK8xUzVxpaiSdrnsaVYWXbiSsELzI93kzd3CMI4wVv4Z3dH3Av7M3AakTRCS7Dx3goWr9JbSsfPF2CrJeUveB0yZLWSWTol5B+3atLza+0BCBUeRGbNSXcs+aCvq7B+0nXrZYbtak6N4d7h1+E6293bpinm0lo2CFBvBW58Thtd62jTukuXFdLhbn46A4l09NE0qovtTaETbeLERcEM9YQe1WJE33bseQ/iAOGs7KpTzrbaqzsZoZ1G/l8TWmydqI9WzdXXJ1jddUoE6iMbNi9bbJo9EOd5eS/bC3KITt12z+Igd6hjtmxx3LldWDsw8GZat5c4VVm10SaTU0WallY3RQ0vti5jzDOu84q/zut2k9y5ds56+t6hSmMdYUg4eueLoKGIJ1TDmnKcs3HFnq9Sl34CVFOx2B600LrnPXQYRtAqHxsL13qP2bD4Xm9uQ7lh2bSW31cz2bpVE01gxXihX63bU/bDbLckZTfgnKruehMLaMVpqXBNzrs5Uuyb5fIXtK71eLGgp6w9HPZYL/7zdkSMfE2R8KW1/E+lzNkZv2tW8521+iUNpZahWUh7q2mUoVspWfW5qbBViaG7bOPSObeoLPIUorNhbYoqNf7SxvnSPxj4Oa87d7IIg6ShvRZoo2Sz98t63e8J20JTQq0yaZcbxfM+Kvct4N8xfynIWrlXfjlVySen4arzM4nN/LvGrv5hJ5elEtMQ8vu6VMZSuBAkOAoxadydszzWL7ZZ9F4BbR3PYxo9v9428YUOjl8TrUu1Nq7NuVUkk8j7Wq1HpR4sVUmJhbwc3YaRsxojE5rBLCswfj8XgKnWm3CRvucr5BX/Z54e4uQT0YntgcA+rsm0YigftHG8vKa7BUlY3OBNeNydc5ld1YaorvLPw7l6HGk6swaojk3xnihCeokj7zcKfeStV9LhhR4bFhqaqyO4O113OXStXAEM1hiNrjcdj2+KwSFAxF2TFdhc718uxaTHuHGVbatnoKYuDCJKaagFwCORo7G3eryuZEai9sbEqaew3mLdvb7PzspwzdG/6gbZl8yCRTmRMt8HK77VQSEjRu9vYdVTX9lk0r3fK3GT+yTmlM/bqDK5qbxsxxpfmRe542zu7uomphnAc2h2A5S+5i2mtAj43smizO1KnrNtwO2vImSK0F/SSrkdZXXCoqcRludk4oq0dsWMLs5+fZ9WYbj1P7IrY2aUC2UnOUmrUXVF3xkX3nTMehrVdBpnZ7Syl59W8agWn9VVbzQGz1rxNckj3jd1s9mqns1SmXI7cNg3JpL82HD4WysGnZ80ikYk85K7UQqSFU4En+mpuDUeP4DoXbvWl6OzoEu22xlzik3ItJ41H2OvrJu4P9s7e0jeOPOa8vMOE01VH0dnqpEU8xxoQssLBU0GXVTQYiFq7E4sFq4erpb6Y7R20r3JbJE+Wf/F8Q2dbzbYGW2+LJkrTKhfipsNm4siXrIj3+lEd9ELBEjKgKyHUVIPmO4y7+OfikMpnYzuzwRYNswoGNI7NRrkHKTngt10E3COPeYGXmfVwyNy1ph/r+HzeirkxdvZgzZJqMTvimHea3bX6PFdLd2adr8Rlu76fE2s5P2ONH3sq6d7AVbT1I9CwZbkOcsW0Ym5jUdQyQOmtBq4HjVEXZxNsmP2oautR89YnqQZJFC3O272syn5I3LfGvbDi+KqTRnTyz7ZRi9oCnRupTFfAlxU0utn8rTtKRTbHL65ekfTJ3aNemOi4weuniDpQ1VG9MZmRVBfVcJYKpMSImHltKxE82fWOid7vy6pbK9VWrNJ+30cKKA9tu79o5cAdmgID4xjvbu6x4GTGX5PkKkqVm7C62vGMjE8qz3bdKV+jY6esa7ewu+M19ze6tU3ozTXaSSXHtsO+L2a9LEr9uoruUebczbM9W95kxbDdTr0bu+OdOq5Ocisnyckoiaq8HGh3Zmq2rtUmzRjNvprxLuA7Spg5RJqcfHsj3laSfvcEcT86W7rvaENTqe1S0bf4ECaK0e1sfu/vqjDbbg7B7EbA7LqcCf0qsviOATxZpje2YZXjWY9rV93H4prcU4Vusqqxa2CnbCkrgeOWp9zeCgKJoRdlEKXwUuu4iRr9NhqObWbLTiYm2/1cjXejv6jPQCQxP6T6Pc1sVZ/2ZtvbqTNssc5Wg4Pfyz7WTaf1iht1Za/nS4OhBO6NnLXGCwL2SSt0FJjzYgQ8LmU+6eQ9x1CnZBbxxCppJYVubnmz7/FrWfubzKT4a0uJ3Mqq5z0t3MaA8ERWIMs8RRuREQsKLERLtiXyvuCzAxodThyqZ7a2kiDLadJG91qqW6DC/DICuMXoi8OZVZhRFby411vS3CQEJkuBu9HYw8WkTybNyRdzpeZrykxnvJ5LQONdebHGb9SML+8XOxVoGiRJGoLjfbXb3I6g8PUsSWpALgktqZyohKY4Ln3ZlUnhdZfrZmlf82TsJftyJAN+ezT3qebixR7fKq3ij8C5iZ3btSNj4TOLEpu4qO71JhPZrec4p/3qdMRKKnSuNLEgeNVrgMOs0OSyWPTLC0orpzPFs4XP+H5nMNxYH5x1ulh6cZc2tumsyDHwOsaQA4Y7MUsZPwv8jWX4nNVPs3Moc8q4H3ZyczMI+0Ifu7tzBslFuNnLdTLgqJdd0WS4t7yYLGEBwflTZ0Z6tFyozt6kR8E+jdRR2VNCLRccbPUx8YotUo7n53y4a9l8sxstxg3OpwWUudulS3GOjznJWoZpWZGaOmDbcRvnOFjGngnRkQ6TZs5sD2PZsFXgr2Ss4gHJ2HkhXawAc/X9Jrw5Kj3T9DoENHOjLbQay3C0LLYk7E5zfYctuejaz0ryckVNnJvBvfJt9C4uTeADYMrOw+w5IbdWGyRWGQ0UU1SVvCTcMj7u4fZmdySOvhEwWZIXhLZ3ltm+w22f71bimLht3YCMB824LiW7jK/UcqdvroeLsqP4TL20wzwKhK3DC56IXRMOuNeNPC/mG9LaLyIClblsLPHaWnE61hP4QSGAm63CnKuWSmsTrpYFBWMAKXTGer7DNTZ0yFsgkQYdN9zo6r57vZ2Dop0TtDCnBT81LSfA24CM560r40YQeLM5rJyUXie6r+K3OpRy55azS9nKra2/Yrr94kjeYEJ1V01d8MdZEJ/H9M4vTno9DLfjRkKlZG8ZhLChlnHq9748jLow94c2ATG/Jn07ZWpaWXQ9zp7jxt7cl83lwAxZtoZAaRZAlbW8Oc5zNQv2Ipit+SVOlo4t1Lv5gj1wCboe48OK8axWpPAzEVgKW3qFn1VOKYYjthAUbgNmzFLt9viZ7yXmLvcidVQXzTXw5ur8em+xgMWVhrRybcy9ttpkuXhnQyATnSudOJaawS2dINd4Trj82Ttt8JXvpWe8CuzTZYZSmHdDN61MqcwYHb3WY90iUCoR44ULk5rVbBkF0f4idMvNmeo2IakF1rIwtX7tD/0cNwbFkBZ81F4KHFt64q4dQHsR2bHOF7AZy8frAGnbW3F8KrWn43WrdBG+PIqE59s9Sy5HrbIDQTtv/IsfbPV5kGXLfra2QDTLl+TJGRxm7qUWTu43yzgeF3Z4ow93f6FaR3cV7g3yUjO9b6Acvs72unzptEzwMZndBKV7H+seUIK8Vw9ki3ucWO61kyOrOlvgLBdwbaSkmsD5WSrOsehW2bMmx/CAOA7Veg62wiAdUd/kO4nVQimQeNw78PNr1K+dzluknq/OPXYk1u0Gs3zc40lSXlT3Q2OtyQu3dvOLvWcwQodBXQN7cb0TJtlLK6LaSiXD3gTn0PFGu5Pbfb3M8AMOa8fKuM4kRW18qbTlK8mtGCG9BKY3z62OUQofPR7YUCokl5ipxrEt/YobKp4lbHuOHRPAeZg0m8mnC01S81qOKEviVrdDgLrLBBsYgpKiY2/ADZmPsqwXdPKVKQ2PpWD+KkHYtjSqLluTi5hlf26LNCr4ns7JbuGnfME6dyZ39wE6v1ort96gtoxxnXkhJcucbZQTd+D3QrINzDnLHY5clEdwU5pRR0nfArvwB5rA3FJktfa42mww8noqdEY58lLu4wHPL9Wbt+2q3hPxoPHOkVQUxQynlnJRz/E7BfAjnqWVGR4EsV3SErMLbJSOdNRTrnReNuiW4Q5EurzxqzJaArk8HYrrMu1X5swQmNQ/7el9v8iAHp5wnPFAstAvYEjyQ9ZYwVXeKBKhYtliPnIxOuOH2RYsASUb8310KJNB0ua4dab6tvPtgOUul2aRCxuGsg0mR1OnapbSKkPz0z2b7/Rd4HtjFVgiPZcu4RHlb1LMUsF+vbvR2l0Mt/hMzVUS1VaYdDNmjtLV151CENzJi1BsW8OesjluaKlFoZXtLiCrguf5v799eJuOoF8Hyf/eW+LpWO//2eni8yDw26ulxyEycPzPj7U+/5t6/ePDW+nFUKvnWWqVNOHr0PG/nKR+/JfeSkwihucr2OldWF9/O36vnXD6baK3OPObqi6Hr1WeNI8D3Q9vblNNv9ZQfX0dXL89zEuLSdrvzXmdk3+t85dF053HK8YU+PFzwHQZvk6YP7z5A/RW7FVfCZr6CspiMvf1omM6k53edLz99r8BPgSqGawlAAA= -->
