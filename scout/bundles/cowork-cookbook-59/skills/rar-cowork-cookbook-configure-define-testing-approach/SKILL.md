---
name: "rar-cowork-cookbook-configure-define-testing-approach"
description: "Applies a bulk configuration change to define testing approach from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_testing_approach", "rar_sha256": "8772853e8670629f4718753f10f6c731c220d428bdd049c850cf85f09a63c25f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_define_testing_approach_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-define-testing-approach:14c16b84ae9a9e110f1c7038224f8ed9a0a3b4050f8bfb81e764a54aa8b0034b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_define_testing_approach`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_define_testing_approach_agent.py` is
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

Define testing approach Configuration Bulk Setup — Applies a bulk configuration change to define testing approach from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-testing-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_testing_approach_agent.py` and embedded as the fenced Python below (sha256 8772853e8670629f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_testing_approach_agent.py` first:

```bash
python3 configure_define_testing_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_testing_approach_agent.py   # or on stdin
python3 configure_define_testing_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define testing approach Configuration Bulk Setup — Applies a bulk configuration change to define testing approach from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-testing-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_testing_approach',
    "version": '2.0.0',
    "display_name": 'Define testing approach Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define testing approach from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-testing-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-testing-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '80d324ffacc2507d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-testing-approach'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-define-testing-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDefineTestingApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineTestingApproach'
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
    print(ConfigureDefineTestingApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOj1pLvV2Fq/mh7qC72RXXDEQ8tSAIEEiCE5HZUs++LWIX8/N3fQVJVd4+v515HTMSTo7tZzsk9f5nJ8e9PVtuERfX0+qR5Vg4trTSNQq+CrNyFZkVfVAn4p0hs8AdyirypIrttiqp+en5yvdqporKJihxs58oyjbwasiC7TW9r/ShoK2t8DTmhlQce1BSQ6/lRDq68uonyALLKsiosJ4T8qsgAUyjKy7aBFhfHSyE/Sr1nqI+aEOqsNHLvtEbJqiJNbctJoLoty6JqXoA43sXKytSrn15//e35KQLXT6+/PzmpVYNHT7OHPN78JoB+58892IPtKZAQrCsHYI4c3Jde5RdVBh4BkaHH3U+1l/rP0H/9V9JbVVD//Polhx6/L0/jf2qbQ004amrVjedCjlVadpRGzfACcWlvDTVUeU1b5aOhamDNPHi57/xGqSihX8Z3P92ZvARe89OXpwKIcDPAl6efoaIC/Kp2vH4ZqZQ//fySFr1X/fTzNzp1a8ee04zEgNQvb4/7B1mw8NvSyL9x/QVQvXvV9r48fafc+LvLPeoJdj69xEWU/3QnDGzYebmVO95PP/8VWSf0nCSN6ubfovvrnXDoWS7Q6SH4z883I/8GwQ+FPmj+NdsSuPXvaAKWv7N7hh6G+ivaN/v/N9IpiK36w+L/lNw/2wD/Av36l7r9TxueIf/L09xLow5Eh516r9Dvb9p2Mfv1k/vt4aff/gCk/yUZrWgr50bhLbPyyAcp8vb266f69vjTb79+aksQa56VvbVV+s9o/jO73vj8YMHHqp9+3Av47/MkL/oc+oh06Pei/I/qjxfIGLP/2/P6Ffo+X8YfDI1KvDO9m+C7nKmBrN/Z8eenPwBC5ECb1rm9Bln+n/8JbSKnKurCbyDNKQAKAQc3UeaNwuthVEP6I6m/auJakl4y9ysEno7pDiDCatMGWlZWlEIgH0aPjxoUPvT1/zg3HP3sPHAUecdG7+2Ohm8PNHx7R8OvL5AeAr5FFQVRbqWQym23kBV4eTNyvMVG3Wafu5EpECi6g446W4+AU7ep9w/o67/k8nYj+FIOoxpfcuAXCyxzATZnAFOtKkoHyLoB+tB4nwG8Aiz5AN7xr7Z8GW1zCL38YTEHILh38Zy28aC0cKw7htfPwOl1kXYAF0c71kmUppAbVcBIRTXcEb3NX0diX79+ta06/JLfgZiA7jWmRsCCD4Ghz5/LyvPTKAibL7nnhAX06fc/PkH/F/qfdt2Ijzy2oCTcDAaCOYUETZEhkJltBpbV0BgWAHZunvv9j7snRulyUBRBPkX+WOSa0TvfhcGowd09774BOo8ietWD0492g/oQ2AWKGmAtkOP185d8JFGApVUf1d67Ee+b76Z/d/adz+iT+mFD4Kdb+RzX3iJwdKZTVO4LtPahD0sBdcdaOXo0LOoGBG3p5a6XOwPYaTXfXJgXDVSDvKn94Rlqa6DqSPmrDUiPxskAOFnNV2gz24I6V6RjWa8edQ/sLvJodPwjWu+PAZHqE4ix6TuJF0j2gDWh0qqsMqys2rut8617RID69r4fELeg3OuhsaJ7o49uGX2LvPlfNBOzH5qP6diPaAB1SuhLi6MYCf3/7VVGybnlUl0sOX0xhxayrh7vYTY2WKPW954MNA0QaDruOfOtkXjHnHc0/pKnEXBNNfzjvtK/RdZ9zR3hAAa4AELUG/0xx6sb3agB8TE6vKpuxviSv8P+M7AM8E49qgDSOBlBofhgOL59lzQEuTref2sBoHvojaqDoIbK1k4jB/I9z70ZoQmrMbsejgDB4o2ZBtIB2PV7rSBAHQQCoA8BISIQtaA03EwngywZ3XHzwsfyaGysgBRu6wBpQRp5L9BhjGoQmTVke6A7GtcAK3y6kYIyD9gYiPhh4Tq0yrswY9P7ENAafVFkVuN974HHSxChY30B/D7SD1C1gO+BLXvgBJBdl7tnP+R8+AoIm42pcNv0o7sfukLf16d/jCkIZPxWAkCfPpb274wD4rTK6lvIgaKb1CDJM+8RQCASblX85V6I75X+Q5bXP3X6P/29YeBWWvc/eu4VCpumrF8R5F7+3qvfi1NkCIiRqPTqb5Xw8z3XPj9y7fN7rv1A+G6nV+jvCfcDiUdUv0LYC/qCjq+kyPHGsH38gC1mn6fHz+T49kuuet+c/IiEEd0A4trDR5F5XwIqTVB5wbj4XnTqsVb1oDzesO5WND4C4ZEmd7QB1aIuvkvfUafRrXevfWAyeJWPaO+OnV3gjVNPOopfe0+veZumz0+5lXn/zrQz4i6IVWCNcUgCj0Gn1ETe7e6jaxpvfhzybhk1ImPxOiYWqHGgw32GPprVZ+h9fLhNZHkL5qdfx0Z5ZAmWgn8+1n5MkLb3BAa2ZihHye8z0difPfrmPwsx5hOQ2PHGKl58JOjI8U9EwEUQeNWfiSi3Cyt9oETdWGNlBAX5kds1kNNtR0wHvgM5B9IIoGMLNvyZDeBTeecW1GJ3VPeb/b6pVdx1+eNmhuY+WP7+9I4W4/W9MbjHDdjw73dvo03fq+7bSNka9996rJuJb53pG1AvGqvrd6+CsVV4u8fh0yvAGu/5aTRkFYECdr0N0k93cYAe33paQAGgxud67BYQkEaAEqjh5ahDAhDvOwbj48i9rR8vXv+6Ef6r9H/FSAejbZa0vIk18TAM9TGHQQkWx0mf9dyJhVqETaIU6rO2b7OYx9CkRZGWxdooSpA2kGL0ZGY9pECw0QdA/g9D//3u/OlOANQLnKIBBZZhcJYiPJZmUBqf+CSDsQxF+EBY2mEIzMFx1CVx1nZdlJw4LIU6Pkv56MSiCQen/JHeo0e4S/X23oq/e+UOA28AObNolBm3LId1GIx0J4xFOx6B2oTjYTjmMoSHUhPCZ1mPBPs/tj48MzrurvgYtKAzBH1ZN/L5/eHpMRBpEqxckfWau/9myMSwEJyx1VCCTRS+XBAybKlDIS+JbtYaw1lp6W43bZaRRol9aZIisU7tHXY5HKhyirtHi9uiml8nk56omTpRnVRB2W2IbmbNyWNqRrmyyNIqxHW5NOnIkEqtSC0Mq1VrkGZ1jJIoKbOGWFGNiDXFnuw2WXcRO0PG92Tj+f6Fz0+ntDod93sNK9cTPNZj7Xogl+HCDZDOOBzwXXia8bihR2RNnJ2K11r3vM4otFNX5qbxTuRwkHR+l10pZ+hUERf3jY75fOFubcMY2K6LS8b3l3y7imG4NYnajCZ7TV1Wx9IaRNvLFpWpMIshtQICL8p9moulQ5yXHV7sZPrQiMOBKLC+E7G8yeNwtoiUXSBOBZo+aZkZUpNSOmmTIT9WFh3Xh+uyGKoo3l/wupxVxFyf2epQaaVEtk7WOUJ7nq0dlW6m1wJHl0hhH6r0EGoXTdDORhadY4tE+o7PMyXcV6Uuwj6DTkOyl/fTuMCs6+K6P81zhGBmq1nr1qq946YuOXFl7rSfyEzgx5sZbZPpBUWrEBEvwtpzl4ZWHAgcSyTrnNVLoF8uz2UphrNpJlRHoa2xZXWQWrU8bRcG79RZpE8yGq8NA6kaSTjsp7R3Qsl1Ela1sOgb9ervvHJZyiytVebVU6bTYTbZMzU82NiE3bUUThUrmzlttGHQjTKzcJ8i1kJPHK3AkA8HtoNTr4uG4izjWtVJzIy1rHK/OzSzThG3lTa9TrmTP3GH43kw4cXgdTx/pcTLEBY6kimzXRhgLj2zjf0k3LEIw3dnJj9iK6OkGPk0hI3eDRPlah6X8WSW1tVmd8Src5GBP3hhFedqi9FpITWU3MzJFcPyV/awYsUVvUitCXauwzmiIwVpXmnY9/WYWZDeOaFRooqtiUTp0YXoz5YhZTUzGzTBFNmq0ewonGEJSaxXKnsc5pGJxVh1hYlpv3QM5Si4XioL2CBUymE+Hfan0DrMekM+MoosR83R2a0PB3ovzBZwgu5Y3nbiNlETtEcdkTpL5/XaKoerMp97ipDRk4RveRDn+TWe60chV5ZFdlVbsUl2ahXP0VWFuhFbBujyROV4aVHEzAzDlSv3A+pTvl5dkRgR2mOQrjZI0vruaj6vK9i0jp2fLmdZGGhdvci6IaxJV2dVEjeCtY2js8LYsmXmk+0Mq+BGtcKO3uHG0cQj6ZBMiqTMdquSM9z9dqj0rQ+bcY2hJwQEra2e9ygMd5s8siqRdQQpLQTYtgqXsHCipEy2RE9amzTnyo/hSJk2e3gqrMV4r5N4my6wvbPHTFNScWlqDia1mnndjoWLnnUqa2+cnVafCVu4pEjUtaTD9irx1CZByWgHp2zP4xcnVQ8JPkzQbRl5jhiEzny4SmYQ1p0lmhOT36D0UQ8XKa0aR41CGdDIL6lLmqL0VRMvasKjvRNe5t705F/DuX1g/QuGWaHQwHaxoFBK9VAe30Y7KdHFfr1U9vOToRe7rSCbcHme+RfFlvEiH9Lkwrhb354jhJz5fYFgZATbM1MTgqKcXOrcPM2MmB70+IpqIXxVj0d6riga61jTZZPuY2c1CE7nFqFNXpCMgrcXJthvyCJV9Np1WRa+YNcFV/LLuqV5WaekmkI4rB/q+YUz8LN0lBKCDozCL65LLGO266mUxN1MJTc6Xp2KhjSd/jTj1uTUPKTW/swNmoFX4srb4yVhhotAI43V3FvXrRFr+a7HsLAzV1svq3vrdKrlY71puqNgryz4NDFPm9iXli6GTbrDlSW7vBroteDP9rVaEoSPwlWtxWk22Rzt42q1pkjewGi+jePVgGo4T2zrbVcG+jVBUf+kkixinrEkixmYknl/07KFn273ZXr1YOuUpegUD0KyjGcrOb2KRFSKCViP4q26trvtPBZKKZWrwOGyJCu6nBOxI64fsaW+DwfH9xbUarowcessV4mCmkNuSIPrZ+4+x7SlsbU3p8NSqoytdd3IZ5NQC3p/dmKk1JeIZC7xMMOTQspPuIlyLS4yibbICk7ZUoVskxOzNJ1GRXkrkUlDOiyxgpbqSadxXXCyAMbQ5jUXKVxBqVBkNq4zLNTjEOaD7mdDi+8Xrkp7enuI19TpYkwnQbIZUnFp0RdDQGzOYCI7ChaGfir0IuMSEWOaCyfH3j5B2wUYujRTa5oKngfGHmuHitM4gUW7vhWtgTWCdOI1nTc1rW1ueLm5TfQZ7rYSL5tOeliRq3YLX0KuAxUDzzbNIUKnOsnDl5NH190eVR0NNBdarqZ7Rss3urBpdiXlyHDSc0QhaJlhXA1mdXFA9kmYB+PnrWUFpb+R1kTA96rUb+wId6IUJab+TrrsmN7iZV6j+rlcwUWGovaGi892ZDhlkgUou8Mzmww7ObLyNa2mUyWgNnoRzmUWGxZ1avVWWCfrq+oxZwbtZSOoKEbXirCJ0mXPhoccvcBds1zQ6QnbSbSNG9g6XEftpZXVjKMpBlXaqoSLwrOmm7WD8iqrF4hCb9L1Wo/FQz7My9g1rXWLyLNgzWMHPiwSStnL6BI+NXJiBFGkThlRFBRpcTZZntvNDnrTnR230tEYDaMima92Nqvwk3aY2GoV7p2Yug7YbnfmB7tuvYZzFGqvwUt7o19smmkneYWgSTCRgzDvZ27iWp6MVH2c44cuFCq08ZlqjtVDqzPWkdgwp4jMtHO3JLd4Hk3lkIS5Rie7aUPNZkW84FababVZ5kF5LNV+2xT+Wl+XzbACXdoqx8hWdLLqcKm46XSHH2WyN5YwqW7Mk4Xs+HC2ZPZn2gYZcJ2xSwCN5ary8IuG2q0hUrpqnnm82KgVuQiD9azYMnarYdMySLTSkzfkAr26fX5dzVNNWSXFZiIn1+V8w+64VDVNu0wiFLkI3Z7ftE2UWTtdqOQeIJon9ilLXnSOiswglnYyLnM7ynWNapdq2J7a1ehyvzbhU6R3srMVw8maQydRDKrA+TLQxbx0zhq2wQV7swpEST8rZHVSmtxbkGDAW0UnFNcyYMqJnnKnnbV3CR4/lYZpyrl48firQCzLZdPJZyLikLW+OYj0hSR0fAdriqdVw8Xq4dNuybgxoexa38zM1B1oOvNs6sieKy+l8yXqunjZB6DX03zqoG6PjcsWwwTbtIICn4U8LrfT5Qo4WgmlIrugS06R0lgMi4IVh+S0ybCuX4fp5ZxzhCPs1gxVCIdEvajH8+Tq1NshMRJ/ssit1iNEpodnRhgcm1JW7Fm6V9fHZWFYGKNTMwa99MISjg5NIBtr92yIekofgtkGPfN6FCkamaZLGQAo2WPeCseC1XZ7Ogi9MSUpLZNPOipeo83avsoOorkcj+loZHCCLTd1IpDI6kSwQSVosQDD03pNbXPFlfjjOhQYtOidMxFupjsRQOzBWJ1qjujLQi7kK5n3yw2yDmL62AXcbDe0g1LE0UIqr2B0XGihtJ9tm/bEMysyNLexfJa75gz6US7jY36xzO0wBxQ5dr7dmsq1zJZRUWZt0BuwN5NOS24xKDwcZwNbOfRBTATpeJTCYKNMteRoXLnVzeX8WmDDledlB76lmQOPRjsru2bJVOTmTYNIDa/Q7RlB5b14CLbSKokFpDPn0uV4OgQYSIELI837acGsJD3BpqK33/M4piub6qTZFoPhe1BO1pNMr6qYjsKU33vzKOqiRDInoKk4yIvgaGyU45SYrGhC7FaIUbB+GoEZMYKXOc4YLCjC0jTduqm/qq8kHG3XA0LwF3OeE6na1dKSkJvrqjUW4UohvKV4csuLIKIoM58WZBZe9B0niqmbKgU+UEKMoTY+pWS3dfZaIy82oCDm4dy5+IiNzVF1bS6vdC8l9oRtsKMHAoubCvCipVR4zeKcoCj63jju53oFE1rYU7RCr+MO3WyUDWXSHejdeUaBWTrEL5yfry2GyCiWwSanK+p6pg7TA4uQvduLrKvQCMLukCsKotYmDtv2fGlQvQJ9Zq+mFTVv0OngqgJ56Pbd4ohfaZIvGqTYtesCXSoCwajFjohXdpRtnGDbr6T9Veh4kLqnDTJQK7XLMJrK/c18MWwNOTVDI/HmIdEJoPAn00KhPSIXPFa4TCN7SnCFUJMVHMUCO0xi0ilnZ57wwiUbw3xAbM29ES5gv7moqJMzvjvZmcOeQhh5jafjGHy2Q2clK7DCztK1WjdUImMLN9dLWsRQa5XRq4srKyViXSZEbEQHebVDgoPNRZ0+pVa+ShtTIq7oXKhLF8aOTBFdZ9y5r+L6esAaRoxQJVWqMuBAL4FJrVJMBiS+dil36fXkqPjthLhaYK5YCF6lrUObWEeyKk6O22PH0wLTSKhkzrjTyhIivys6XvIW5RVzt1tpPXdhlbyE65wI90dGE7FoN2F49iTD/MFFWXWCXdNNvnDAi5LemfG8Jip6h2wL1NuuHHVg5thulZZlaFdsTHXroIi2G5tLNjNritvknOcuyWGHuSHs11PequyFMCXhuisk0aCmEgIDhesrYZnHiG/3NJI3UzeKY8GStqUCCJhKwCHGriLw2lGR3JRJsEBFarp1CVuGAQO2IIWJM+c6OOOyNufwvTz3YztwsIAcCpphKKvfKpJ3aC92euRIS5o2pdLuDyRIuyr3TwsGM9Vrt0IbJ6zOuoWSK4NoFfPMeBtd3vWiaDYiIXlh4xFu7HFz/ogMMeoYwgDrqLvVDrt5usd0mQaj27SZdyHfkRwGM94ZXkXTSYeDEaq3GR8jiGDSzibsbL/YIJvNZDvp6XQ+RC6as/MiWx2QDgxe/Ekr46C9uAv7zGDhtHV8u1khsElo3jrs8EkoN5REXEBLVmRkQfUzm52CDndPLP2tL8zzs3F0TgVpVHalmn1nYfBmy8ncdOOkgs9PJghCc0GRLqQNOYl7Fr8iC7uteE+iNMuakqs90e8PZQwmDB3dMD7HLYteWdQa1WqrDbHZ7ubJwHthx52siEC8KCUpegk62HJacOlaKvxZCOdxtujmFOudXP8QSmA0IkknmVrkLo9IdGodwa1qbDPZiZVi6cxOxfUi9I4vuum83O8Zoiit2CUSjqSHSGKq06n0SbiXtwJQIbhcHYypsn5yTfr8wCqLyzUiHWwAc1LbrRcCu00OfG+kPGbFlwNRdhd9up9jOlK2uu8718ChSoxVtpxdRKLMlwO73rhrdEqvFno6wYOKKJKqXC8yFkVyez0YTSaL7iVSfDwXnbZOqBXS8wh7EVlFKziO++WXp+en29Hv0yuGsujk+Wk8L3h89f9b34yDa1S+PUgRDI0+P/3vfdC8f1x8PxG8HQF4lvt64/76N6T87fmpciIg0f0zc522weMj5n/7aPv5X35JHrcP98Pr8ejy0ryfmDRWcPvSHeVuWzfV8FYXaXv7zg0s3dbj/75Svz2OG55uamXleHbxwRFcW24W5RGgXr01xdv9+//4PMrHMznPjb7dBo+jgecndwBui5z6jaCpN68qR20fx1PjJ97xfOrpj/8HnOx7TaAnAAA= -->
