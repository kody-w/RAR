---
name: "rar-cowork-cookbook-teams-update-allocate-headcount-to-business-units"
description: "Drafts a Teams channel post on allocate headcount to business units status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_allocate_headcount_to_business_units", "rar_sha256": "9d58024b8c3edba7e7dfd1995f6efe6810efc6a28e7979711d90f5c303920783", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_allocate_headcount_to_business_units_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-allocate-headcount-to-business-units:a362e7a903d74f29202c069d8acf03073eca244f6d94c86439ad3517069a6d2b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_allocate_headcount_to_business_units`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_allocate_headcount_to_business_units_agent.py` is
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

Allocate headcount to business units Teams Channel Update — Drafts a Teams channel post on allocate headcount to business units status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-headcount-to-business-units
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_allocate_headcount_to_business_units_agent.py` and embedded as the fenced Python below (sha256 9d58024b8c3edba7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_allocate_headcount_to_business_units_agent.py` first:

```bash
python3 teams_update_allocate_headcount_to_business_units_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_allocate_headcount_to_business_units_agent.py   # or on stdin
python3 teams_update_allocate_headcount_to_business_units_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate headcount to business units Teams Channel Update — Drafts a Teams channel post on allocate headcount to business units status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-allocate-headcount-to-business-units
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_allocate_headcount_to_business_units',
    "version": '2.0.0',
    "display_name": 'Allocate headcount to business units Teams Channel Update',
    "description": 'Drafts a Teams channel post on allocate headcount to business units status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-allocate-headcount-to-business-units',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-allocate-headcount-to-business-units',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'adb9027c266c675c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/allocate-headcount-to-business-units'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-allocate-headcount-to-business-units', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateAllocateHeadcountToBusinessUnits(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAllocateHeadcountToBusinessUnits'
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
    print(TeamsUpdateAllocateHeadcountToBusinessUnits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V5aZPjRpLlX8HkfJA0yCriBlFtbbYkQeIgCYDERVDVlsINECdxEIdW/30DJDOrNFLPjLbXbFlWVTgiPNyfuz/3QPz6YrdNVFQvX15U384hzk7TOPIryM49aFV0RZWA/4rEAX8ht8ibKnbapqjql9cXz6/dKi6buMjBdLayg6aGbEjz7ayG3MjOcz+FyqJuoCKHgNzCtRsfinzbc4s2b6CmgJy2jnO/rqE2j8HkurGbtoa6uImAAlCcN35lu01886GFZ5f3i5VdeVBQVNC1jd0EAgrZof8ZqOP3dlamfv3y5ed/vL7E4Prly68vbmrX4NHLXSu99IAKi6cq/LsmWrF86qFPagBZqZ2HYFI5AGxycF/6FVgyA488P4Cedz/Wfhq8Qv/xH0lnV2H905evOfT8fX2Z/hzbHGoiHxhq143vQa5d2k6cxs3wGVqknT3UUOU3bZVPsNXAkjz8/Jj5TVJRQn+f3v34WORz6Dc/fn0pgAr2BPzXl58ggMXXl6qdrj9PUsoff/qcFp1f/fjTNzl161x8t5mEAa0/vz3vn2LBwG9D4+C+6t+B1IeLHf/ry3fGTb+H3pOdYObL50sR5z8+BJdVcfNzO3f9H3/6Z2LdyHeTNK6b/5Hcnx+Cp8ABNj0V/+n1DvI/IPhp0IfMf75sCdz6VywBw9+Xe4WeQP0z2Xf8/5PodIqpD8T/VNyfTYD/Dv38T237rya8QsHXF9ZPQZpUtpP6X6Bf31Rlvfr5B+/bwx/+8RsQ/d+KUYu2cu8S3jI7jwO/bt7efv6hvj/+4R8//9CWINZAUr21VfpnMv8M1/s6v0PwOerH388F6+t5khddDn1EOvRrUf5b9dtnyLDT2Pv2vP4CfZ8v0w+GJiPeF31A8F3O1EDX73D86eU3QBc5sKZ1769Blv/7v0P72K2KuggaSAUk0UDAwU2c+ZPyWhTXkPZM6l/UrbDbfc68XyDwdEp3QBF2mzYQV9kxIMCqmDw+WVAE0C//y72T6if3SaqzZiKmt/bOTG/vLPn2wZJvTfH2zpJvd5b85TOkRUCPoorDOLdT6LhQFAiQIKDUeCJeECt1m326TUoABeMHCR1XwkRAdZv6f4N++curvt0X+FwOk5lfc+A3G7z1oMbPyqKyqzgdIHviMWdo/E+AiwHXVEWaOjYg6emftvw8YWdGfv5E1AUU7/e+24KqMCmQQkEM+PsVBEVdpIDqmwnnOonTFPLiCoBYVMO9MAFffJmE/fLLL45dR1/zB1Hj0KMg1TMw4ENh6NOnsvKDNA6j5mvuu1EB/fDrbz9A/xv6r2bdhU9rKKB+3AEEwZ5CoipLEMjcNgPDamgKG4DZ3bO//vbwzKRdDiooyLc4iP37ZCDtW5hMFjzc9e4rYPOkol89V/o9blAXAVyguAFoAQ6oX7/mk4gCDK26uPbfQXxMfkD/7vzHOpNP6ieGwE9BVWT3sfcInZzpFpX3GRIC6AMpYC7w672gR1MJ9/zSzz0/dwcw026+uTAvGqgGeVUHwyvU1sDUSfIvDhA9gZMB8rKbX6D9SgF1sEinql896yKYXeTx5Phn9D4eAyHVDyDGlu8iPkOSD9CESruyy6iya/8+LrAfEQHq3/t8INyGcr+DpvLvTz66Z/w98hb/kw7k0bysns3Lo1+AvrYYghLQ/98O524Cxx3X3EJbs9Ba0o7WI96mtmwy/9HJge7iPvmePN86jndyeqftr3kaAx9Vw98eI4N7iD3GPKiwrUD8HBfHu/wp2au73LgBgTJ5vqqm4La/5u/14RVAA9xUT1QHoEgmdig+FpzevmsagaSd7r/1CtAjBqfcANENla2Txi4U+L53T4QmqqY0ezoCRI0/pRzICzf6nVUQkA4iAsifPDIBDmrIHToJpAvorx6x/zE8njowoIXXukBbkE/+Z8icwhuEaA05PmijpjEAhR/uoqDMBxgDFT8QriO7fCgztcpPBe3JF0U2BcN3Hni+BKE6FSKw3kceAqk2iDSAZQecANKsf3j2Q8+nr4Cy2ZQT90m/d/fTVuj7Qva3KReBjt9qA4jRqQf4DhxA4BUI5olQQHVOapDtmf8MIBAJ93L/+VGxHy3Bhy5f/rA/+PGvbSHuNVj/vee+QFHTlPWX2exRJ9/L5Ge3yGYgRuLSrx8l89OjeH16T7tPH2n3qSk+vafdp3va/W6hB25foL+m7O9EPKP8C4R+Rj4j06td7PpTGD9/AJvVp6X1iZjefs2P/jenPyNjoj1Axc7wUX3eh4ASFFZ+OA1+VKN6KmIdqJt3ErxXk4/AeKbNxEXhVDrr4rt0nmy6k87Dce9kDV7lUxnwppbwsXdKJ/Vr/+VL3qbp60tuZ/5f3jNN7AwCGUAz7btAUoF+q4n9+91H7zXd/H7feE83wBNe8WXKOlAJQZ/8Cn20vK/Q+ybkvsnLW7AL+3lqt6clwVDw38fYj02p47+APWAzlJMZj53V1OU9u+8/KjElG9DYnYh6qiHP7J1W/IMQcBGGfvVHIfL9wk6fFAKofqqfoGw/E78Genqg/XqFgCNBQoIcA9TZggl/XAasU/mA/wEHT+Z+w++bWcXDlt/uMDSP7emvL+9UMl0/2odHEIEJ//c934Txe61+m1ayJ3n3zuwO+b3ffQPmxlNN/u5VODUYb48gffkCiMl/fZmABSUtjcf7Xv3loR6w61unDCQAivlUTz3GDOQYkAQqfznZlAB6/G6B6XHs3cdPF1/+vL3+K1zxxcYpzKdtBsE9mggwBkMwF6EYb267AYIjNO67NkYQAeUxhDunCJyxPZxEaTDGpjzMAVpNns7sp1YzdPIRsOfDEf/6HuDlIRAUH4ykgETGI+cIRjhzF58qJu3TXuChDEMGFGgrqTmK+IFL2djcpxnwB0U9BglIF0dwYB49xyd5z6bzoeXbe4P/7rUHh7wBGs7iyQbMtt25S6OEx9A25fo44uCuj2KoBwBCSAYP5nOfAPM/pj49Nzn2AcQU5KDfBN3ebVrn12ckTIFLEWAkT9TC4vFbzRjDpk3aOUYOU1G+dT7NBCfWqdEktWonnlGec6X1SlsWFH3011taXLiqIWnifh/RZigtcExQMi4472Fmj0hqKovz3dLeLbP0kowSTrc+SRKEvtzzhbxvt0fpvK3E4z6hdqKNrk9CRu3HUu+LOkUdVyWTrL5oqTWMqJ4FcaRhN5Z3aHgnkoZL7FBk22/xIu73O6t0h8X86GTlWULOLoUX6XlFIqdrsxUrE9ZbgUjV08xdbStjNWzVqi89XiippNqVh5IvYCkf56Sc91iQj8SxHGbKiBPbPki3sa0uWLFLM7w0jF3lz6UzVdpctOPMeo9fORwraicpNYNZwqmcEUlzygoDIxAxH1R6Far+NdOvCSGP5GV+FExj1ZsotSFOidQZZrIxiNHcN+7u7Bcizm/T7VWJVrtLtK6a6MbCMp4XjMFsa0rxh+2V1Hc3aR3rRbrUB9PXqtV8cGRvJZjq1exFRTol4nJYKEJsUKIVy62hpWeHCSOhulhJNojLS0y1Ln2pzweenl8Ny9iblNn1uy1xGpHBXoLAN64GO2/FLXoVKzfeRGmvmU0YpJdNrJmripSOFHoZ9atplHLcZpohKtnM3CiEj1K5hNQbEt6QdqmHlbqRhestoZalP6IKiib2gLrzzRK5tsSpcNIW7+Sw7THC2jkXVzlSneOGhk+2UZ5Z3RHbE5dFk3GjYF5c/QzbLrBy1Z52RDRHjIMonotDNct5o+TO8iq3UBHoI4x9PkZEdV7BI75aRzfGIvKFuHRGde/1aqYrwoxb08ZF7q/tTR0FSl43lNXyaKRfByVZcpQh20WZXB0pHVgdZUKEdhZlrvfMQcfIw67KMcmTon1QYmUQ1rciC8Lhtgz8jrzdvK1QWCDvYdlI4FucU96sc3M1a9MVfZYWekhggjQXklQlKxdWT0d+S1aSqm4S190fZZMbDtiplQ6r2i+0g3fiiwOuYnoWb+SbXSfuMrKc+qBaIO1WxMbwCTjUw40Amh91cUPXOny6SsJtI+DCKMT7RbIdjvZ+KS1FtxmGtnA7XwytZpa7V7zzboPEepp+nJecSO+O8alHiotF6Qa6Vi7F8YgFtcheZ0nD0uQmnymSmY3yIZvHHrxPKXxRGuiNvdUz4hae4sxJKU3pMTPD0dmudPk2HrmuQDjZWYnaeYGfZZESXL/pF5thFcDJOUiHkxTgOtvnDBsbhhDi/OpK5itzVM3rCbQ6fJAike0hK+pwihDrup0pt/CqpzqZX1pm4E+7orkezg7CVB5545Ks4CTDrgO9YNgT6cn7k7Go4GupigZPbpY17WxFa7sXk5xic0RRYm59A8mUWHmTF6tmdhjnYH+4pXiiD0x3K+lFrhRARne9rorK3gUei2KS4h+2RxYhLfMmHOpNw7jxdYvL7l7EYl8Ud7FoUfW4uxwztywNyaZ03Wuj6jIvtKFpzzVfHQ6hHOSGvc9wraWVZlt63tHELRRAl604W1NyMDH1+JVMr/DbPKfFUTzX1JHhO1zwKZM5EanihEt6hG/ReHaZm7zZcDpH1R49Wjs6V9z8sKKRmxHntmyJSnfEafSwjCTLEfa0fRG1mZCTe20ehHmoywRe7mPS7ql50M3POzr1R3oMs+x4JuvzPOKKEBFQa80aXHJCHPpgaYNoXbZdo9ZLQU2DpF4zKjJz4DRkLKlVyhUXKVuiXFTmZUET5XCgNfGYbCxYWOmrOvNKMhmEA7dsepACih+3lnoQW6vgWtZBat5B3NRMhVlcCbEySPaFJqkg35Fz4Nr44NbbAuMrspGTfa2JDWL4Fe8m9D4Z9rdKqDpmBjKIwFAybGCO3SdqNvdmN1AuqTaYhYdgF1LUXE2HqNWZxWrfMnMTl7aLHSJYKJ8hsl2OQhevJXMX6ZTNyqCyISf3smTPItqtK9OJRSe84dfByQrBTnyLcdXTVmfkYVNi+UF2y8KRNwFcrHVD17dL9sovaex6Iiym9ZmzdwyYK7VaYZtQT+BlgSytnSbB+UoyLheqkFrXteprObD+bn5Y6n2DqX4qDezp5F0HvNAbq/IBsIQahEv3YPvS0aXi7tJiM25liVa1D9zQBT4qbmde9bHTYMJXgguYZQtLNiz1+5NkskJPUmF4WnLz9LoFzUrHDqCpWeAuvT75ArLVhgzumX1rH/aVfT4rprzjZxHqqlywF2d9vBeCzYUtsXZ06OtVPIdJvC2Ja9wSypozsTSPNVu+sjq/Wy7Y1McC11of1tIcEZVisDGV2t4Ydy2f04E/hp6+UcSDuCKXYbKFWaOo+LDdN3kyuJV4IBDd5oZ0rJe3E+NJ17DpSSVXk1MswZKz7PcY55Q2c4p0YO9aqp2bq5o77sCrdIahF/GcnPpqt+LX6pngumxdeotgVNAq3vSDe0UZ7xyMe8+3N6W944rljAYZFpmi6GHyEdiZBxs/Shl+dmr2xzZCTUNF/fWgXNpcVHeoZGyy3YaMTnvCFJk4GWQNa7Z1h+32CVc0dWf369o41MfjsST5ROePmQ4wifaWJ8SzjMPTG31IyqVpsXEY4OegueKxrgF0Ewvz/WKVWvHB65TO2lLo7mJIpnlGfGRxhG+8Q+ASvnL5LhltI6xCBqFdRyfXrskoeMl6Yd+DXa9vDyobaNQgy1Z2RK9lf/OGcxceElc+CBlDb+nquFjjxmLZhc5pyY4HjjJrVqB4VajXWLdaEmpEzfwKiWT7Wtv9YjWiMHyul9fUyOL+7GkoZ87XdqNexFPZXZfN6JLbbeozF4u8ad5QaFtqfY2a62nNB2DrvbDcKDCCQS2UENGLNa9lXhyJpOYJ+Y5fRumwE2uNqLLysOG3ew6NzW3ik81KQtAZpflFfG4cT9os2qymF/aWJHbbE3rh57yozo3CFptNsepBk7Vu4r1joOl+XM4Eo9oNPCsurVbabKh5tCA4x1inHteptX1ECVJ09tS612eavL/KJxuTXKVTLzwJRNHn1CXlkVdDsW+H01HtdU831FGkMve29xMVg7OiggfKux5gfQjnyIYli/OcP7EJXpeLviV6TuznpIVZRLidHRInHrL4xBiqjmd7r7Qp7ZjA0RglZG80ck/nKZqSMVUsJNLQzpp8jgW5PA7uijc2sbVf1acrjwJfHZtU1N1eampx5aSVuWQsoVHKM4niu7y0x1m95Dfl8kIHxXjcVa1tUsoBJUxv1axOFdZ6a3QTOqXhgDoRSqS4rEOupLSGYLeFh5r6iZ03tK6NyCI11nE+KFsdbphLt2z9Y3PRsLMJ2oab7Bn7bCelbndohU5s1uiJUJe9pHX8uSsT6niW+qTfjjQdOb0eZqyfmp6T4SMpZIgBijQyWIcOxZbr02LUb5l4VbbW8tpLHWkVNy9YWOMQc1U5+KGchovNpUZ36xteJoyNiNLKJNfRxh2uiNJnMUNgBdbiVIZz4kFaH0UCW56JrCWaxckrs6Oxa8NU91Z8tbuci/FqBNtj7EtSVAvz2+VaRXp7cFM2CvfMgttvdJ1Y0Kh5kfx60ep7WAur+VWPbDyoVGJlU1bvhwsv3G7ObSzwTduA+N6420NxtfbazDHZqI+ORtRtuDNBjCwSlY4YHcZWiXJUFJsZfKiEU0OTW9i73Uxk7vQEvb5c2PnhzNKlT/VlsV4c/VIG1tKWg11IhZK3+UzfsKySXp0MpunqlAdZ7QeE2hIMR8O3QDLyAG/wsZHPSoMSctUGpETUJ2yYpR3JWB7OgZhg0I6H5exw5ezKbDXmgqEGfUV27AXpzCO+PAsLz9Ack5IdtmZ5L+6rC2XvLT7aNFdtc9mJ9CE9WDOMiQJVmF95Sb3S/TlAO2fOjYskBE3JlvDoLWhT8JuVekf0skTFnCmXTNQj7Tzg6ZpoyVNLorXCWsoZw3NLxEyW7EyOSAMBA5tfjQFZlCl1cJvB3I1axtzJshm4DYgMvnUbHJAqPLvtz/r5dN1oFw1fX2Kh85PQ5eoe7Q7UDs8XK7+z+gsTdUm8Wlj+LElTVhC4kDcukXC2goN8iCLNFdhE3p7xtGt3hrSDRxnTKWHhiqAfa/FizrM7X423x3rZnCxyPN22e83WrJslbZ29MCvWXODKc9gUFsRNcpQhS2bdwJEDsboRyTE4Ubte9poGxzb4Ct+34yAZvWEBbt7DQTt3Orjbc+oKNsdil1YYJW4Ki9YqWSsDksApfO7wWcRvk5gWWXhxjlfibK7sHIJnC5luYXJwVlWLFfRpbdYHDdsYXsZh9YkMslaHEYrvhNxhDmNP0W5T+/48NOWVellq8Nia2uJ0IuLdUWXXrDrGgrTOS4ReB4oq0/ZsflwkS5+xO4VHnDhqYjOh2vxykZdwvvA567wcCCNbuCxWqyfFkqLVaRafL3i/yyUsPElKhxbriohFecMpQUa3uNPMlK5n4U6aba7meaH4+dkkFKEJL6N4DFNq2dHD0Llblg3E8Frx8Kzge5yjBa2ZEbG8pouqEGao41+cmME2mNA60S4nqePJys8paFPwhN4xPOfzK0MXkax1jnSsGLBNU1plM3UuoRXZ53R4IKLeZY82oXV0R+dsWHHrhUKOFstabVgqLddJ82bcVALjeAKyIq0d2xTLNsY6jGlPpUO6BIof8aCJ3HOUF7gZ9vwGbUW8ot0EtvxQEEY4EjaBefFNq9sXfLEPBhQJmsVW1jr3ZnsHL8XRnCVM1x7tPF+xwXp59UiY7YKV53i3QDnHKDa7BqqEkSMOnw6LcehGOsC1Sle2rOLdwpF3aAK7kQPbwCOyXtFl0yxmNcvhecKQ0iaXYXoZzBI0OS0KGm/XlyBQDWS7vmw2eLTKheWlay5y2Y5edzoq5wxVybjhNel0a42YR5rZ5YCwB1VLGg3t3fkMxzIhk6q548ZwPJ9d6E3ZXnh5RwScvevSElP2cZxvT8vZgWhkneXYBaVGy6zXjJ6MKL7JtC2DNsoux2a04d74IBBGTO65aGECwOAxxTyzWDM8S7tbim5WPqw15JxcLG3iMMYUwtrWzHKPRpAubudcZ+XL/lTmCcGjDUY3SEUdQfG1maYZl+7RWSYw7dedAs8yveg4Ay47jXZs/LwWm7q16LwdF/iNadndbpZv6SC0FrEMm4ZMSWJW7cJyqBhd2GizpEzlFvYyqV65waXp+O3S4fcdHSCcmNjn3fogYnBNqERicNRl2J4klsD6judxiXb7C0VkhBKY2o7mWYTHxTOVutk2XCxeXl/uB8kvX1CEZpDXl+mQ4XlU8C99Ww7HuHx7isbBbur15f/dh83HR8b3Y8b70QFQ6st99S//gtb/eH2p3Bho+Pg8Xadt+Py4+Z8+7n76y1+gJ3HD4+h8Oi/tm/djmcYO71/M49xr66Ya3uoibe/fy4Fn3vV8HmO83M3OyulM5HszwW1QVL5r13fznico93PozPfix4jpNnweOLy+eANwcuzWbzhFvvlVOdn+PAGbPgRPR2Avv/0fod1UX0koAAA= -->
