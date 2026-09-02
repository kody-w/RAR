---
name: "rar-cowork-cookbook-d365-source-to-pay"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Source to pay end-to-end process - covers 6 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_source_to_pay", "rar_sha256": "3fd89b6e077f77ccffc0bd7908a04c6a6d31944807a03f8a7588656ccff3f6a8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_source_to_pay_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-source-to-pay:0a0274a2bc7f77b847c0d1ca4bc3eb4427ec2c795330c8ff849b7c456873fc96", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_source_to_pay`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_source_to_pay_agent.py` is
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

D365 Source to pay Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Source to pay end-to-end process - covers 6 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-source-to-pay
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_source_to_pay_agent.py` and embedded as the fenced Python below (sha256 3fd89b6e077f77cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_source_to_pay_agent.py` first:

```bash
python3 d365_source_to_pay_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_source_to_pay_agent.py   # or on stdin
python3 d365_source_to_pay_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Source to pay Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Source to pay end-to-end process - covers 6 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-source-to-pay
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_source_to_pay',
    "version": '2.0.0',
    "display_name": 'D365 Source to pay Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Source to pay end-to-end process - covers 6 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-source-to-pay',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-source-to-pay',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'efb867aacdb1ca39',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'source-to-pay/d365-source-to-pay', 'uses_skills': {'custom': ['d365-source-to-pay'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365SourceToPay(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365SourceToPay'
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
    print(D365SourceToPay().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V5eZOi6Jb3V2FyIqa6x6yUHckbN2IQAQFFxIWlqyOLfV9kEbHf/u7vg5pZVbe778yNmH/GikoFnufs53fOefjtye7aqKyfXp92vl1Agp1lceTXkF14EFv2ZZ2CrzJ1wH/ILYu2jp2uLevm6fnJ8xu3jqs2LguwnYEWQ2HnsdtAGElAfFzYhetD/wHtuqrKBoiN7LiA1nZhh37uFy3kXyq/bqHGLSvfg9oSaiMf2pVdDXaBq8oeIL/wPrflZ/AFVXXp+k0DfQZSnP26gUhohUJ27dvNTVYchVbY+yq/gYK6zG8U17Fbl00ZtNC8a+JipKE+aLF2a2dl+AJ08S92XmV+8/T6y6/PTzH4/fT625Ob2Q249bQAGt0l25eqPYD1mV2E4EE1AOMV4BqoEpR1Dm55fgA9rn5q/Cx4hv7zP9PersPm59cvBfT4fHka/2ldcZOxLe2mBUZw7cp24ixuhxeIyXp7aKDab7u6ADpCDbB9Eb7cd36jVFbQ38dnP92ZvIR++9OXJ2DT2h498+XpZ6isAb+6G3+/jFSqn35+ycrer3/6+RudpnMS321HYkDql7fH9YMsWPhtaRzcuP4dUL3HgON/efpOufFzl3vUE+x8eknKuPjpThj46OzfguOnn/+KrBv5bprFTfs/ovvLnXDk2x7Q6SH4z883I/8KTR4KfdD8a7YVcOu/oglY/s7uGXoY6q9o3+z/D6SzMR4/LP6n5P5sw+Tv0C9/qds/2/AMBV+eFn4Wgwyyncx/hX5726kc+8sn79vNT7/+Dkj/t2Tu+TBSeMvtIg78pn17++VTc7v96ddfPnUViDXfzt+6Ovszmn9m1xufHyz4WPXTj3sB/0ORFmVfQB+RDv1WVv9W//4CHe0s9r7db16h7/Nl/EygUYl3pncTfJczDZD1Ozv+/PQ7gIQCaNO5t8cgy//9378Dlp1bdi0EHNzGuT8Kv4/iBto/kvrrThZXq5fc+wqBu2O6A4iwu6yFhNqOsxGzRo+PGpQB9PW/3BvqfnYfqDv1APi83c361pZvABe/vkD7CDAq6zgEMJtBGqOqEMBVgKqAxS0Ymi7/fB65AAniO8porDgiTNNl/t+gr38k+3aj8FINo6BfCmB5gNgjNPt5VdZ2HQMUH9EWcobW/wwQE6BFXWaZY7spNP7pqpdRez3yi4dNXFBS/Ivvdq0PZaULRA1igLLPwK1NmZ0B8o2WatI4yyAvroEZynq44Tmw5utI7OvXr47dRF+KO9Ri0L3mNFOw4ENg6PPnqvaDLA6j9kvhu1EJffrt90/Q/4P+2a4b8ZGHClD+ZiEQrhkk7TYKKCxhN1apBhodD4Dl5pvffr+bfpSuAEUSZEwcxP5tM6D2zdGjBnd/vDsD6DyKOFauG6cf7Qb1EbALFI9VEWRx8/ylGEmUYGndx43/bsT75rvp37175zP6pHnYEPjpo/zdYmx0plvW3gskBtCHpYC6wK/t6NGobFoQlhWotH7hDmCn3X5zYVGCMg0yowmGZ6hrgKoj5a8OID0aJwfwY7dfoTWrgkpWZmP1rh+VDewui3h0/CM877cBkfoTiLH5O4kXSPGBNUHVr+0qqu3Gv60L7HtEgAr2vh8Qt6HC76GxSN86iVvO3iJvrNP/0EJw9y7jS4fCCA79H25SRv0YQdA4gdlzC4hT9pp5D8axLRtlvXdyoHmAQPNxz6xvDcU79ryj8pcii4ED6+Fv95XBLf7ua+5I19VAY43RbvRHJKhvdOMWRNEYFnU9Rr79pXiH/2fgmFHrEclAsqd3g70zHJ++SxqBjB6vv7UC0D1ARyuB0IeqzsliFwp837tlSRvVYw4+vAhCyh/zESSNG/2gFXBGC8IF0IeAEDGIbVAibqZTQC6B9ulu8o/l8dhgASm8zgXSgmTzXyB9jH0Qvw3k+KBLGtcAK3y6kYJyH9gYiPhh4Sayq7swY6v8ENAefVHmdut/74HHQxDHY50B/D7cD6jaHvDzl6IHTgA5eLl79kPOh6+AsPmYMLdNP7r7oSv0fZ3625ioQMZvlQF092OJ/844AN3r/B6doPimDYCC3H8EEIiEW6S/3AvyI+zfZXn9w3zw0782QtxK7OFHz71CUdtWzet0ei+D71XwxS3zKYiRuPKbW0X8fBdtzDyQhD9QuhvmFfrXpPmBxCOMXyHkBX6Bx0er2PXHOH18gPLs57n5GR+ffik0/5tXH64fQQ8gijN81J73JaAAhbUfjovvtagZS1gPquYNAm+15MPzj7wACFuEY+Fsyu/yddRp9OPdFh9QDR4VYxHwxpYu9Mf5JhvFb/yn16LLsucngIH+n841I/6CaATqj/MPyIwR/mL/dvXRH40XPw5/t5wBye6Vr2PqgFoHetln6KMtfYbeB4XbsFV0YFL6ZWyJR5ZgKfj6WPsxWTr+E5jF2qEaRb1PP2Mn9uiQ/yjEmDHvCDxWiUcKjhz/QAT8CEO//iORze2HnT1woGntsULGHxWkAXJ6oIN6hoCzQFaBRAH414ENf2QD+NT+qQM12RvV/Wa/b2qVd11+v5mhvY+Qvz2948H4+94g3ANlHC//um0bjfhebt9GUva44dZc3Wx6azrfgD7xWFa/exSOPcLbPdKeXgF8+M9Po+XqGHTS19tQ/HTnDwT/1q4CCgAIPjdjmzAFiQIogeJdjUKnAMS+YzDejr3b+vHH65/2uD9m9CtswyiF26jjUgFFOTOccmEPcW3ccTHfwXGU8l3UpWgCw2B3FgQznHYoFyfIGYUFLk0CtqOvcvvBdoqMVgYCf5jyf9BpP913AJBHCRJswQJvRjukD1OjUK4bBC7seBQNz2wYd0mb9DCExvEZTNkwFsxsipjNSIIcF2IBac9Geo/O7y7G23uX/W73B3sAd3k8ConatjtzKQT3aMomXR+DHcz1ERTxKMyHCRpwmfk42P+x9WH70TV3Tcc4BE0faLnOI5/fHr4cY4vEwcol3ojM/cNO6aNNYivnEhmTKxmYZbLOMosNqZ3W7RDfG1Yr0LhYqCqtnD3nRCXThjsd58yca0ypONqsqaa7YJ1Ot5Q/E5RMGlL4Mr3IkiBie4Sis2EyI2A+HBhTDc7x7Bg02/aYiVmc6WseozaXRHRP8jS4JvvJwKneOQvYZn/VQdARxXU5V6cXljqVTYRSy/3Ccgl/Rgzny9FJeU1B6wNxEI/iThcwbru6ijCSZ9Y54WPAYZs3qIkXpMjVyrJWjOQSnueevzan15U2uR55jNRh4XI8nVBtwpd55UmnoyMUrWUSg5HUloQNce6dliYhSAPtF9KE3iwzjC4H72xk2DTDRCznq/Isy8rmiLRHIauXVlMdSjGzwLizYS/XTWipLTfxbK62V2vP2oud72SUGfudxToznhvKlCw717teU2ydLBNTqzSuPhEsXbMsvmINmCDX7XVylEmhljfyer8j9OuePRpIFk02lxrxcxLH2nmhb4RFszHPmr2SM7aH+/OavOZgZSqn68OkK+frtFpbVOeW/GFo0bO1lCpQ4zYyd/KGnbPd8hbuecii2tCHfRSca1twYiepZIOZ5rm3XU8UmTPEc4v1cXVE6ixt1sVRcbHFrNGWXBvK6P7gK2agCzxi7o9H3EL2iWWgCCE5lV4RAhKqy14VUHphcLPo2C4Rak4W5UlFqo0SNDhxWIorGOkwWsHqfZkckQzuOwwf1nUZuTmf4VO4wa+ciyIn7mivXDRbrK0lmaEHq43MxvAVklPsqxCIGqVpTnOU8qSIK4T311OlTreq4J4bUeem5pXDNW3w2SzJZeOgEQviSpFnPr/sj+bRv258Sbdi3NOFuC0ULmIHrjgFIlwVxxgT16RnHi0BHcwVvclInOMpcUUn8xm3oJiBBa5lKonuZ0uVgOmpTqHS1loS5Aqpgg0qsepZX/WLbbUbTure3eMF7meorBzQTcK1sL7pt52WCFW+PwNznvnpVIo6ry5tr9dYtyX3SarmDe8vDJXfMtIWBGF9XEuu3uKr7QJP7JUoodtDoyvompQW80VtiZLMzretbETbaznDXakncy8aRHnBkNO2Is3O8ky3D1ATTXbpoZ/SYeuadnI0p6KnEoRc6NrsiKWah0uXGcyaO6yIVHTDeKdg4Mxs6TvGxT4GxlRALl29WttspJX7BheFRgo3SoX2bjeBk2rY0j0xBfBbw5nbD5PwuuUGg14bjBfCEctIvHyRjemZs/FNJ1QNhnBB5GXrI04W2mptkO2gkcGpFjI4yOgrU4P8aWR3ubKP8pDtVISUaerQRCbBTcvlps2HmTFj2mERHTis9AMO1jblhMjKTMlnc2W6Uy30oq9TFXOO1rrM3NgkW1rkbW2jW9q2zqaVsRTptZ0vteWKbSuW32/a45laKc6k7/OBr9O4E4lEvq47xbbiYm6b9f5o86tVriSyMNlfTYtJpy0+PZHNxdl67pXUlMXWl5QLHhCEWnHLdClFVnbJlDPjHTu8mwU72UN0MOr2E2ROelMwqlNN0IU9Q+7UTR/GVn7gNIDyGKn2fSCIF7qb0NbmoNeRWqxUdD0TgrK8aBLuaFoLmp8QV/WjekZV88JqoCiJe56kg3PYKPx0haDKvsnd0xXbitrctVNOqUJpctD1gAl6iTnPOHNdo4OME8zBFSN2idrkyW2V2rHW/WQNICRNyKyKK8bBQOBtZIDEa2pDLIY06xNFXZP8Ysi16bGOamy5NIR0dUJXkcQQV31RnfPqCmPXTllfjDVJTq/Hgd5clYtXSHP5sNNzqZkQkxzZ7Q6BoMpZ4KjbdNmX4UYNgmsPApLbnFCcDicMz3Ixb8yymTclkouEg1CfTuTzKlu45Wk+P1DqYKJHljmHiw0ix9vqXKjKhj3wbHdM5KpBS8zoLgursTRjiTGax8q7jl1oOF0sKNJWg9POyq+gf+wdeJuSZtikebLfq+4V2GAtWjEqcMRlWR3l4zJSZzSiFKiVLXgfQPfePInl1Gj5dr/wLma7awGinsWJM1RCigh8fbVhcefTololnF6mtdOnnInh/RY9Zl2CiRxfscsNj9MK68cmoUr5lUFXim/PsZ3I+GV1Olj5aRvVgTNbOrLTLiN2m2GoH6S1wPG8T3KZGoghoiLFbmhPK29SVFw2R9yql2isqxbYIeG37pWZzObxLsMULt1tLK0428iykxW0YBgkSH3RXml6aaR4VbsGi8TOzJiv19Z6dVS87XGnc+ttUNo1K/Y9yvIUa6x8CS6EwVVdu92uwpMV7gj/uDyceKulmEQq+L5gJCkmjaZGgtZ1Mo/Tl0ouLKw+PeC+dHZs2mR7nN5wzRxA8OWMdVdFW3G8ulujM5urvMZY8Q0lHMR92p3iTUsYNiprC6TTyLUWsdRaDzdSkmbYhBH2KCzPmQWZaUMAW+x2Ip3kEhXOsEdkzHwauYyWqEMkt2HFp0uP6/TFrkzL8hgPsrWjF0WsOaBLItipBaPy8nq4no5ThdVTwV/YtNBOG3F5ximnFnCkmfFb+cDIRttjSclMYKk1uEAuHCmk6Qk+2XskUSlovC0zYdkxqnfKzzU3H2inMGz7kCRLy5oEtrHD/Avp1L2pW4hs0R2dVHpkwvo6nE9o22kprWBkfjdvYN525lm4MvWDGVDzg3SMBTayN2XZYRYZHKryQrDOKgvdDIOrXReVitUs2gXbiHa2S8puIR7d1UBPDnPZs2XsmmfujDDEk6h3jnyyTufQNRhG2E6jbsK4ki3LlruoYqGG53h1Svc4xmQWejrtszC3q704YbiNw7SpeIGvOA/vZIPYYRdu39Zu1diON7dQJsiuml+otbBce/zqkuftYn/g6fWkLJDZtpHzpixKZTMZ8FSRYynetZImpc1cIjjrUKWIetZw185dfGViEiNixCWWUVEZeGWqRdFkYeGzylU3CVt4m2MebecZ6i3t3IwxeQHbu6zrXIs247PCG3pbYOThwhh9EkjWgioljDcIHEsaJFRaBctZs+drR55ZICz3huYFw2LHlmSR8g6CcXN0OaxzCXNPemIrpL0npJyCGX6SXQxtNe8kVNJid11vw0HpU3auU8TiNJ+ckvVRPOSUZJmnVVWfeoVi+a2vBR4Y8WBpr9qwoeJgSCtt85CwkYE0wn5BIpKeMSvx0Arc7KKZhb5l7BVD6idqi834+SlZWHDETDPmZB0UcnuI6b2cD3VxLMJrO0v7E2cuvEw6R67Z6WUcUnVynKe2TmS1WOx9ftfz8JRLT46HaNVVoFTUNvpMKDfkrnEzzsXUOZjYiOVyFzGkp3Mhz5aHKS+fzKFEz70cWnunGRR2TiWCUYAmZXbl5tZ2phx95FwdDC+mq2zHmpyDu7PNVc63BlHYqe7HJwGBj8S8JLYXGyWtIZ/3qm/4eXQiPWqdLo3MMqWcJzW1Eq8q1/XN4VAkcItIhqhuXSvayHPMZK9if0nFOlmUDr8Lc5ZzrKEK7GvdBol9EU7UxmbmxyWOZq4Ac9eS9MFUxVT5jmMpfj4RLkXvbrKDudW36G4zCeG9rQ/VHh3Cy2KSMMCWkoclKN8dvUnZYjBmk10mmxHDBVXewu0mP7eFvDcSkCzSPN6eFcwz5kzbV52CxJsLVa4vlHc0jmc/MSwDOyDNyaFxd4kcA5ekHHHazYeOUpBkoYFWpXTqhVJKknTtjB0H48j2QPrWRtCA9FPYclnLC73UyaRG9xof7fUclZqZDVDROFB6KEvwDmTvVLiy/jqc8lIS8UZOT5dGQgk5sTqLyyPf7DFklRqI6mbtPp5KkxzDz+Q80XEVVRLPII08OZ0uM4W1CkvHnMNCzxc4wRZt5Oib85K8LMWZjwVTqtKmA7MVDrxxXNoJNVkVML7bgJGdLxAkORKiR8jWsEmPM+baXmOtd2lBKbnmvOebHbpxpKmoT0QmFa5qs7iiJcskUWuW+jJfkPOBVQbnwoChf6+axeqgD5bhdcf4OjswMFWvKT8qZyt2uY/O88M1ORRNW2HZcgPqSGWlnpgfjV657G1hpqCr3gvPqysyXVC0f1243sXAta1tZZQrBiu1aU/dtptN8IEWTbnhkITmL0tKnmDugk1BusWkQNhKfVnr7awVZgSaTXMQYNNJ4/riZMsbWqSa81wUi84knWAOe3PUK8BEKwL4sGfeem4dfXRdp0Su1ARqZNNWaIPNjCWG2cF3cS93purSNq4Ur2wBltiZew5jgyp4tGMaq3PZVSItyynJbRsNc5tgcqa2TIiv14GYUm7UDUuB2Ozlk690QN61gl4iPF3NZ3zGCNjZ3OznGzPDKf1wdj3rQuOLy7bhnbmOiod9u7+AIWYxx2d+pPOACUNyXLuwVg1dx6m6WoThfu6FsT2PvcEyN8o82mz7Y4nNsNK4IMJV3CrT2bDhijJqhFnuiIrdeFiGXiUnkgqC3O3NwgITzQUNKYmoqOXSa0oO94yC84ljj4lTg/PonL7CSIlSF/GwtcBItF4vvV5XG1tgmxJw2DicteJ7vpoglGusk0YPZ0jhTA8sbq6kDq71ybVU1gqNHLu9p/pXFTTYAlu6PZ3hm3jgJ4mCi1xP98yhUBRj7ieKa7Sxxiwycxov0nOecoYEK6BjL7vBIWOdNpeLNeoTfYglPU1hfoKdV5N8avIzdKCazvHpgOAnVcPNp+gkoHalb87Pu8PFgYM1SPqpPCS5V27tA1aBHoumUak7SaTNk0FDT+aT6WLObQgDXrREjtDrw/KSq+lS5+Qy5NVMc1rDCiih2c9PSrVMRLtD3Y5kavKMbiZCVfLhoWLJ7pxYFtbwnIVaZ/qAezxCgDboWhhWDtuWomQehShzgrNrk+g5b5FjBDM/rbNI5nKnzEFmRrBkrSdGXQ+2fm5prKl8dBPsZ3rc89HMvILZ45qdNMPsfSEJJ7Kdn5nKN32LQRfzIxMteaJkXSy8lvFpehDohR1aMHECTeOZjZoOUfxssSvsa4bzRYfv4xrnM0qnUzaYujI3YYcz77NO4BpbdBjI/TgMqe6swFfCOfV0KpXSgcOJzCXKQ7Nv/IsARgBg1WRy2W+stpkiZskQmLEKNxxDbY4xSpfiToRTY9nvG2BXbyI2GzlYl26KXzEw1i8EOkpSOehFLDSJVtZIdcqUe6UkOUXeMszT89PtDezTKwKDEf/5aTyff5yy//Mj2/AaV2+PvRhJg63/e6eN95O/93dstyN33/Zeb9xf/5lYvz4/1W4MRLgf6zZZFz6OFP/hzPTzH09ux/XD/bXw+Lrv0r6/dGjt8HaUHBde17T1AJhn3e0gGRjv8drz7XGA/3QTPK/at/cz5Nu78G+nnB/ns3ExvsHyvdhu/cdl+Dhmf37yHm9730Zd/boaFXu82xnPVseXO0+//38KLe6FBCcAAA== -->
