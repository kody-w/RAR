---
name: "rar-cowork-cookbook-demo-data-record-asset-lease-right-of-use"
description: "Generates and creates realistic demo records for record asset lease right-of-use in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_asset_lease_right_of_use", "rar_sha256": "23c24e8f7152d45c5a7e79043aedd81a65b38f81e73890612d489643eccfa21c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_record_asset_lease_right_of_use_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-record-asset-lease-right-of-use:ad701ca2e255479e2e1765c0a848294ee106013a395c5d69047ae4a0ad6e275d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_record_asset_lease_right_of_use`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_record_asset_lease_right_of_use_agent.py` is
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

Record asset lease right-of-use Demo Data Generator — Generates and creates realistic demo records for record asset lease right-of-use in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-asset-lease-right-of-use
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_record_asset_lease_right_of_use_agent.py` and embedded as the fenced Python below (sha256 23c24e8f7152d45c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_record_asset_lease_right_of_use_agent.py` first:

```bash
python3 demo_data_record_asset_lease_right_of_use_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_record_asset_lease_right_of_use_agent.py   # or on stdin
python3 demo_data_record_asset_lease_right_of_use_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record asset lease right-of-use Demo Data Generator — Generates and creates realistic demo records for record asset lease right-of-use in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-asset-lease-right-of-use
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_record_asset_lease_right_of_use',
    "version": '2.0.0',
    "display_name": 'Record asset lease right-of-use Demo Data Generator',
    "description": 'Generates and creates realistic demo records for record asset lease right-of-use in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-record-asset-lease-right-of-use',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-record-asset-lease-right-of-use',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '10f595b76f4aad2f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/record-asset-lease-right-of-use'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-record-asset-lease-right-of-use', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataRecordAssetLeaseRightOfUse(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRecordAssetLeaseRightOfUse'
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
    print(DemoDataRecordAssetLeaseRightOfUse().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZOjSLbmX2HiPlTVJTMAsUdbmw1IQqCVTQiobItiB7GvEqqp/z6OpMjMulV9b3XbPIzCIsTifvbznePu8euL03dx2by8vWiBU0ArJ8uSOGggp/CheXkpmxR8lakLfiGvLLomcfuubNqXTy9+0HpNUnVJWYDpq6AIGqcL2vtUrwnu1+ArS9ou8SA/yEtw65WN30Jh2TyvIadtgw7KAqcNoCaJ4u5zGX7uwU1SQA7UAmJueYW6oHCK7j6va5ykSIrozqdKsrKDWg+8bpKyfQViBVcnr7KgfXn7+R+fXhJw/fL264uXAUZAzAUQY+F0jnrnzk3MtxNvdWJ9CI9tAEhkThGBsdUITFOA+ypoAOccPPKDEHre/dgGWfgJ+s//TC9OE7U/vX0poOfny8v0o/YF1MUB1JVO2wXAJk7luEmWdOMrxGUXZ5zM0/VN0U6KAssW0etj5jdKZQX9fXr344PJaxR0P355KavJ1MDuX15+goBJvrw0/XT9OlGpfvzpNSsvQfPjT9/otL17DrxuIgakfn1/3j/JgoHfhibhnevfAdWHh93gy8t3yk2fh9yTnmDmy+u5TIofH4SrphwmX3nBjz/9M7JeHHjpFBZ/ie7PD8Jx4PhAp6fgP326G/kfEPxU6CvNf862Am79VzQBwz/YfYKehvpntO/2/y+ks6QAGfBh8T8l92cT4L9DP/9T3f67CZ+g8AuI7ywZQHS4WfAG/fquycv5zz/43x7+8I/fAOn/kYxW9o13p/CeO0USBm33/v7zD+398Q//+PmHvgKxFjj5e99kf0bzz+x65/M7Cz5H/fj7uYD/sUiL8lJAXyMd+rWs/lfz2ytkAEDxvz1v36Dv82X6wNCkxAfThwm+y5kWyPqdHX96+Q2gRAG06b37a5Dl//Ef0C7xmrItww7SvLLvIODgLsmDSXg9TlpIfyb1L9pG2m5fc/8XCDyd0h1AhNNnHbQCOJVBIB8mj08alCH0y//27pj62XtiKjLB4rsPAOn9gYfvdzx8v+Ph+x0P38vwHeDhL6+QHgP+JXiYFE4GqZwsQ04UAFgEnO8x0vb552FiDgRLHuCjzqUJeNo+C/4G/fKXub3fCb9W46TWlwL4CYAuoNoFeVU2AGuzESA3wC137ILPAHIBtjRllrmOl0LTn756nWx1ioPiaUEPlJfgGnh9F0BZ6QENwgTA9CcQBG2ZDQAnJ7u2aZJlkJ8A+UCZGe8gD2z/NhH75ZdfXKeNvxQPYMahR/1pETDgq8DQ589VE4TZpMyXIvDiEvrh199+gP4P9N/NuhOfeMjAInfDTZULWmuHPQQytc/BsBaawgTA0N2Tv/728MgkHah8EMivJEyC+2RA7VtYTBo83PThI6DzJGLQPDn93m7QJQZ2gZIOWAvkfPvpSzGRKMHQ5pKAwvg04mPyw/QfTn/wmXzSPm0I/BQ2ZX4fe4/IyZmT618hKYS+WgqoC/zaTR6Ny7YDQVwFhR8U3ghmOt03FxZTuQV51IbjJwgEypdiovyLOxVlYJwcgJXT/QLt5jKoe2UG/kwGurMHs8simRz/jNrHY0Ck+QHEGP9B4hXaB8CaUOU0ThU3U2MwjQudR0SAevcxHxB3oCK4QFOVDyYf3TP8Hnnq/9BeTI0ANHUC0LNzmepoP0MxAvr/o5WZlOBWK3W54vTlAlruddV6RNzUh00GeLRuoJ94EJvS51uP8QFHH0D9pcgS4KVm/NtjZHgPsseYB/j1DYgglVPv9Kd0b+50kw6EyuT7ppnC2/lSfFSET0Ar4Kh2AjeQ0emED+VXhtPbD0ljkLbT/bfu4KvNCh/EN1T1bgYsGwaBf0+FLm6mRHs6BMRNMCUdyAwv/p1WEKAOYgLQh4AQCQhgUDXuptuDhJlMe4/+r8OTyY9ACr/3gLQgo4JX6DQFOAjSFnID0DhNY4AVfriTgvIA2BiI+NXCbexUD2Gm3vgpoDP5osxBnHzvgefL6BlO/rdMBFSdCYa/FJcpOvzg+vDsVzmfvgLC5lNW3Cf93t1PXaHvS9ffpmwEMn6rCqCdn6r+d8YB8dfkj8gG9ThtQb7nwTOAQCTcC/zro0Y/moCvsrz9YUHw47+2ZrhX3ePvPfcGxV1XtW8I8qiMH4Xx1StzBMRIUgXtvUh+nuz1+RE1n++Z9vmeaZ+/z7TfMXjY6w3614T8HYlndL9B2Cv6ik6vtglIUGCU5wfYZP6Ztz4T09sJdL45+xkRE+ABEHbHr3XnYwgoPlETRNPgRx1qp/J1ARXzDn/3OvI1IJ7pAtC1iKai2ZbfpfGk0+Teh/e+wjR4VUwFwJ+avyiYFkfZJD5Y47wVfZZ9eimcPPiri6IJjkHcAotM6ymQQ6Ch6pLgfve1uZpufr8uvGcXgAW/fJuSDJQ+0Ah/gr72tJ+gj1XGffFW9GCZ9fPUT08swVDw9XXs10WnG7yAtV03VpP0j6XT1MY92+s/CjHlFpDYC6biXn5N1onjH4iAiygKmj8SOdwvnOyJGG3nTAUT1OlnnrdATh/0WZ8g4D+QfyClAFL2YMIf2QA+TVD3oET7k7rf7PdNrfKhy293M3SP9eevLx/IMV0/+oVH7NzXpv9qczfZ9qMov08cnInOvQW7m/reyL4DNZOp+H73Kpo6iSeblzeAP8Gnl8mgTQJq5O2+9n55iAX0+dYCAwoAST63UzOBgJQClECJryZdUoCC3zGYHif+ffx08fanffNfgoQ3x6dRzHNmwYwkCZoNZgFGU6SHOgzBzFgiCDCUQjHcwVnSI32KRQnaCQgHdXwqmNGkD6SZPJs7T2kQbPIJ0OOr4f/9pv7lQQjUlBlJAUoz3JsRARPSGDnzCSCPQwc0kAh3At9nMIciXZwJGSygcYZFKQwMYliKwAPPC50Z5k30nt3kQ7r3j879w0sPiHgH6Jonk+wzx/EYj8YIn6Udygtw1MW9AJthPo0HKMniIcMERHC3wmPq01OTIx8GmIIZNJKgjRsmPr8+PT8FKEWAkSLRStzjM0dYw6Et2t3HLktTYVSfGQZlqzHPZ/RpFdwoURlHxS7RfK652SqNK0fbrFv/ZKjCRpUHS+JgdQ1fdHpbmJkUZmdsjTLH+Wy2cFbWkJKByR5k3xvTpaLPScOqq6O26oytKWWNujHMHKl7r8gXOsEcs/YstpmTJEF9XJ9aXTNgJMxNtjqMCqjy2rwRQnhvNvmsW5Ki1pe1cCKF+BiegrOpxNWWU4Sqx8vMEbarKjAwXxPoymJuVHZL0c6VtrEWt66e2IVOkp55vpABbl414cKEuEmGWhy4tirp3FLtbH4/6CujKfwDtrTd1Iu167kubCQ+Wvhan8X1xh0D8px0Nq1SBCB5MPRWWJJ16ia1kbT9TbtacmPoglUc/aT2MF4IjHXR7bpmq+TuFlvMfaoc60bXhDHFrrF/mlH0KUExc3emLQvOSINUUF82VsEgVXgUqHKxW9W5wTdbkisp5bjdnJN4V1r6+gpGrcmeZS6x1BRWekI53gxk01dWuqx7hHgZHePkujrrpnIwhvuoQPFNvImDDX12rgKmqqfrvMSxmyJeSXiUtoLRrlCKUq7Nnl6jeXWuk+yk2yJ8U0/KrjkSYBrD1sZh3kkWkWvbw7rzjnMqo6jbzaZA48iNJ3y3xW4jTdKIkl9nTbq1G09e16Nrrg/GLOzIbb4jusaTohp3+vPi4JtCdvXsNrMYM9gTqOGso70mBEwF+1LaXd0hKUnG9q5hLBfb67GNebmVTivEOCcBV5LDXrrehK19ZM6M37GmRq8qipV6geiXwmjDpp1YtCKp5bHLBFJ1vNvWwHemVIj7+nZOMRF2j8ctccOMNZNL1WKuU1oGb3VGIInFuA8dWIkXhy1yUemCoWC4wOGV4vEbeiaF/Lpqh6t8XQyZS7mbWYLbm/U+bLQaq7xWC9p8BfzJn1frXluNtr+SE1RbOONp3tIRzqxmx0aUHIaqGNFWj8IlclbJtZuWXBFW8CkHz20VO9iVIOUikdvz+BK3bbri+GOrGlupJanbgUu8g51TTCr0Ahrk5i0Vb1gqA3smzPKcGhJib64CtZ7Ne3XU1oQdlFlg9lordyka2mSdz+wRw4/0oNDLbalX9lghuouI5Nnf9F6SDjrVruMWY/3RdUWKVdUS1TjKr5ZYcNwXhUcv9yui5faNM1/PT8TCYy8k4ra1gxzyUOXJgsEO8UbVj8EldFbmXIkyk+crtVo5Z3iwdHSQWZyXb/UVtWEEXlw1Q8/8wD1qNwF2ndQTV9StwmSqShVtcXRQQ7xS9nBCN/IqLQypMVp7WePdgjQq9KZdDG/LS8eVWQbhMlX7MskwK9vmDC8jx4ShDpW0keksuVwOMQF0JYyjElRHWzE7NuojFvEW+hlN0ziYAQRIZxmpNnLDXCP6dnClvLfWZW3uit2MRIt4u6kq80B1XCHAXpaJ4ZpsN9GIo0yIHTFQf+Q+zFW9msVsvO6DczLc7Fhl+dGeGQqpmxdxxhFmFzprd0+1jo8Naj8/HzsKgRXvjPgCy0eLG6XwUSCsD7PVzO+M5iif14ddoeVnJM1Vd7ZqmdxGcWuGCvZePKk8QtC+JNCHG2OY+KVriXohVvxVuJEUPK8ypTue/Dno9wU565MwWtD6WuKFueeUfQrrfq2B4D1JYytq5yjltSDZZ1iM850XMJuh3jVbn+EaOFuap363n/OXqruozqJo5oR3SgUpzqUWNS6qX57bZlhEfiAu99IR3+HNgWtpQ2wZkwSBY3onOuFtDGNCU2eIodiOrLQWE7NVqwIPUbjWtHOWs3vLtcRlSS6FK0ahHiGHtMJ1+563kDCOarkwB5c0b7CMIGuBrfIjFeI7nqhCQdSJcRxCLL5oynywUl9yZufx1BvHZX4Gauy3KbcdMsnb5ssahK4bSacEFzySd8+r0c2rW73cd6LUc97MiSsjClcesbgWu4UV6XgcZop9ZNsKU3KZQXbOITCu4flkabKZnot8y8ZiUWAzZnvtTFrQNmUddTy7i93ljWbMyvTaBu2cYotj29PqWlJly4gct1ueqvPB7FOmQmRf5/fEOBsLU2iWwsFZw35kuteDcSB6NC4wNmJmJFGJs+sK9ZwjX9Xn4ybf9LVPD7FfnLZzj8rmdsiPu41+Dkw78271fpBgq5FkPDss5Nmta3Uqz3q+LyU3aR2ylY+Msi1pCdlrJcg/UgaI3C2PjdvNd5WnKpaQN1lNMqB1c7wzaw6DFrOrZGMqyYiNXMgp8OIg1YVU+fv0NDIypzXK0bjaBzvDHd1Jlub2eHUTW5GW85MDz5G9TyDmitxqgipVMTfCa+12VPEttT2vhGOxNJdtuhUVmx7t0RqzI48cZuxegTfa2YGLwp1Z/A3X93sj7awFewBtWZKqspsE+txS+kDDz+U8dLlLGbNbCzW0GVymfsGutGTJ+9nWpuIdczGCNhT5PCaOhlmus0TzUA2x9hmvOeW4PBpRlC+sNQa6InVcLs94U8oBWqAD4iwraYcuRMoPY0sK7QXSwR4o0Rdj5xKc7+FgAVleaC33lZltZ3qBEgHcE6FNsUzPMJd0sxViOjqHDjnM+SXoAfHe3S8213PbIiHAmO1AstaGXS1yf5MjboSRZrn3hbPEz+UAGXhFjTeCxrWCsLjVs5vhNWtLhCVsrlpxIxl6vTG3I32ogQPGqGKa5enUgRbRXJ0cMlv0XJ6uHVarq8O+lpZVha/R9TEvleGI8QRm55s6zHvcqa61edkpEbeQ3AvuRfiqHTd2u62SVaGErYJpNny97K571ebPYU45GXfyJCWYre2N6qaJsqiLfGBVl9zoW/fU2NopzISKQ3YogGHltkDRQnBmuQ2aTJ9k1RF00gdsRypttMiAgXIFtQh9d0G9Uz4ud5HaXRSys3z0sN2C3jPt8kWOIlo/k+qak1e4PN8dBsUxCn8fkTm7CY+kspJXgmhfvbyrK+pCbloz9kb/6qiFSzujSZm3UterU0nPTSnsRDnaEMOh9fVVH1CrWUNb2c23RwddhN2wlKk6rfrddXZuKn8eGtfoPJBLVkBpOsYzMUeSUiIE3LhuMG+9WutJu7KVdX+4LFfzwxZfUBpqHha2JohyV9/m6kicbpHeLrWeHDEhVCW0breL0GwWsI15MzheI03kk/0O1bLSaKW2z7Dq1G3mJ60DRZrm++vBi7hZzaMdTxlcl3S6N9gozcGZMgZHldIFlFRqc+ueeZ8IzJPkJWymFPxRjIyNtc22Sn9a3shGwszbueJ6J0i1LEvPurtOgvkFb5EU8zdL0K6Sh8uYjgxd7QZ+n/jsZieuu6PLHeeVwoCmn95HK3LZcB3fw+pOOANnyHCuUjxnzcWK8G1x5fZpj2PEdbNsLxIyI1OzDJO1AZc+17GdsR9Qm3VInrdnGwPPY3LPiQyZr1sMd6OqH2K0kxauhlTSLY+qiGixQ5F5udYZ3XqxXLQ7/nQJV8l59CL4WKt5d4pOm5W7Hl0rx6sO5OlarYlD7fEtt0DLtsGX54g+7cOAq2JtuaSXZ/lM3krgOKqVQsvdyLbnrln3yDhzq3QMVo1M2zjC1IVaNqIYmh5qp3Q+JF7lL0mXXg+NWVdz+DLk5Urx+Y1XGgxWGZzBXtbHrgmCTBEUmuAPWH3mbwZ5kuCCxvzrockbo0NaI9zOFjWqyywApmzGLQKkMntGblqrYWGKVqNWtOA9dl4vN86pwOkELCC1OvPnRjnbizwtcitTotrax43bEpWxTDbnuOGmCGNr8dKtjUzb7mCJ7beIaOmyyg2RuNvUztYK+SHrSDNcRrsVESPEwvdJex4RGeubsbLfDo1qi/umZK18j+xsdyQNvyBAYePHboAJvt3JeLrfj1uf92mYEajDsGwR3w/D1pIdIThkvo0gS5lZyFsnYLEbTXWNL/CzdM8uHQfmgjzR9EhChBu6Ww21lpMF1xk3RqDr9Zo/X1ndG91L5BJbRV/fbkuWP0jy3MT5Vqg0mWh1lMazvtg1xiXo+USZYZqwImc7sSd4LHXXAkdiJLJxFqR6Xs9dAeeiKr0YiHLLYcuimSDS7ZrtZxv0jIjlDb9Z69kykHEqdvgb0/XxpSFrAqa30iyeRzdMMpreYm18dYusthXqg26ZujkQR1GBD43i0Q68VQdsQILDYenVmluvZYvPJakYLux+iPzVhd7jbLRuN33oMP5Ota9cYxn2zC0cGMkwR1Bx93biDTqwRc7b4zIiryhTp/m9wgkwnVlDRJqEup3WBELvzYG8DVKA71N660/DLKHVS0TsyjCj/E7B+fnAFGCxttgxGheudpRHMI7INXyorM+EL/JRQYS+fYvXuBh4ykFijs38SijubZHgDaHg8oAPOG2pCSVT0eG6biq64W7kIEVRIs9dLu3n3npmExtBumInAuNjxPLWmOHgO624MhhY9FwKX0PmtNeFp0Vxw0/1bakH267grtpth+6MuouPojVoF0I6ro/RINtkLMJiq5c7jMlh/UTPsHQmXqWjQsL63pE2SNOGFuXFlnUJYT+XbqcqEkgEo4MtLZ5EK6BgZlcKl8upcLU9c/OjdCkPDju6ZAPLORIm0XURsW0T17IZEGKwUIk1c3W4KB0oJ9qwaU/KZy6JQu6K7LclQVmaV6R0kI6JWBXVhh4lJjctGp9zwXLfsONoechqYSPxwNqu38JyUxTB4OwRIxF4pIcDUWsDix+MRSyMGQNWykimBvCREmf+scVDZDxd99ggB/zKZpHhYiIkaXWX7YFxewk30djrYmlUfUKpEs5i9oaL7Wc67Fx9sYRLZafXFFnThDYksFAwVh45c+0o1hS8FcUrc1QXakP7uNgeQZ1Drg5dX/AENvIcLB9rzwdpfh5TztsdtvqZm0WXIC0Vsnecg3zglFs7Yr7rZtk4Y03HGlzdv9BWmLAnqd1qO7oM5ySV6ofdIkYpOemr5iIXhZgr+yjS+mV16fxIz+GVsTJwKsJTslQLPa3Ty5VpViO+PqM1daRP3qC0NMwRp3BeDrDcRiZLMEp2ObmYHg3tARM3O10j/YrqFrnQszNCasMZ18iwkC4kWjCOYommp7ZfiFkxlkpdIBtzE7Ie3XqWR11EMTqgS+ZgNDO23KlLFEMlTu9Y6XIGfaJcS2XNoEjULMcAIRw636+ut74bmtLre5TJEA7kzPHGYhuF414+vdxPf1/eMJTC8E8v0/nAc5f/39ofjm5J9f4kidMz9tPL/7vNysfG4ceJ4H3bP3D8tzv3t39D2n98emm8BEj22Fpusz56blT+lw3az39593giMz7OtaejzGv3cXLSOdF9lzsp/L7tmvG9LbP+vscNPNC303+6tO/PI4eXu5p59Ti/eKoFrh3vfgLw3oEnSVuVd3ZJMR3QBX7idB+30fNsAMwegS8Tr33HKfI9aKpJ5ecZ1eSQ6ZDq5bf/Cw8XsdnUJwAA -->
