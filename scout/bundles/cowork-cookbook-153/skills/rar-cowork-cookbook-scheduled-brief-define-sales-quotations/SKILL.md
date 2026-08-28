---
name: "rar-cowork-cookbook-scheduled-brief-define-sales-quotations"
description: "Schedulable morning-brief email summarizing define sales quotations for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_sales_quotations", "rar_sha256": "aee091c88f8fded8b064f60b7bc917e895f2c0ae25c4b4c50f8b28108fca9c31", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_sales_quotations`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_sales_quotations_agent.py` and in the RCI capsule.

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

Define sales quotations Scheduled Email Brief — Schedulable morning-brief email summarizing define sales quotations for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-sales-quotations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_sales_quotations_agent.py` and embedded as the fenced Python below (sha256 aee091c88f8fded8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_sales_quotations_agent.py` first:

```bash
python3 scheduled_brief_define_sales_quotations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_sales_quotations_agent.py   # or on stdin
python3 scheduled_brief_define_sales_quotations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales quotations Scheduled Email Brief — Schedulable morning-brief email summarizing define sales quotations for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-sales-quotations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_sales_quotations',
    "version": '2.0.0',
    "display_name": 'Define sales quotations Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define sales quotations for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-sales-quotations',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-sales-quotations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b3e67fc242e2cb4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-sales-quotations'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-define-sales-quotations', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDefineSalesQuotations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineSalesQuotations'
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
    print(ScheduledBriefDefineSalesQuotations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjxrrmX+HW/dDtq+4CsUn0CUcMQqANgcQObkebHcS+SuDxf59EUlXbx8f3Hk9MxKirowRkPvmuz/tmUr++2F0bFfXLlxfZt3NoY6dpHPk1ZOcexBTXok7AryJxwH/ILfK2jp2uLerm5dOL5zduHZdtXOTTdDfyvS61ndSHsqLO4zz87NSxH0B+Zscp1HRZZtfxCO5Dnh/EuQ81duo3UNUVrT2BNFBQ1FAb+VDtNyW4jies4pr79T/AlCYOc9+D2gKquxzyAOYAgfFX30/S4RXI49/srASIL19++vnTSwy+v3z59cVN7ab5Lp/vrSah1ncJ5EmA8/v6ACO18xAMLgdglBxcl34NhMrALSAz9Lz62Php8An6r/9KrnYdNj98+ZpDz8/Xl+mfBASc9GgLu2mBzK5d2k6cxu3wCtHp1R4aoGLb1UBlG2qATfPw9THzO1JRQj9Ozz4+FnkN/fbj15cCiHAX9uvLD5P2X1+AMcD31wml/PjDa1pc/frjD99xms65+G47gQGpX789r5+wYOD3oXFwX/VHgPrwreN/ffmdctPnIfekJ5j58nop4vzjA7isi97P7dz1P/7wV7DAB26Sxk37b+H+9ACOfNsDOj0F/+HT3cg/Q7OnQu+Yf71sCdz6dzQBw9+W+wQ9DfVX2Hf7/xN0CmKrebf4v4T7VxNmP0I//aVu/92ET1Dw9WXtp3EPogMkzRfo12/yiWV++uB9v/nh598A9P8IIxdd7d4RvmV2Hgd+03779tOH5n77w88/fehKEGu+nX3r6vRfYf4ru97X+YMFn6M+/nEuWF/NkxzkPPQe6dCvRfkf9W+vkGansff9fvMF+n2+TJ8ZNCnxtujDBL/LmQbI+js7/vDyG6CJHGjTuY/8//Lyn/8JHWO3LpoiaCHZLbp2Yps2zvxJeCWKGwj8PDgK2PVBUY9xIP4nD08SFwH0y/9y7+z52X2yJ9y8EdC3Oy1+e5DgtzsJfvtOgr+8QgqAL+o4jHM7hST6dPqa26Gft9PSJeBGv+4BqThD638GdPR5+gLFOfTLv7nCtzvYazn8cmf5+MFVErObeKoB818nXfXIz5+auaAw+Dff7cA6aeECoYIYQH6aeLpIe8Bzk12aJE5TyItrYISiHu7YwHZfJrBffvnFsZvoa/4gVgx6VI4GBgPexYE+fwbaBWkcRu3X3HejAvrw628foP8N/Xez7uDTGifA80/PAAn3sihAINO6DAwDTgNuBjRy98yvvz1tDGBAbYGAH+Mg9h+TQaQmvvdmcHlLf0YJEnJ8YGhg5Kws6naqYHH7Cu0C6F1esOj0aOLzqGhaUK5KP/f83B0Aqg3UebdkXrSg8LVxEwyfoK7x76v+4tT2XcQMpLzd/gIdmROoHkX6Vu6mQWBykcfA/O/h8LgPQOoPDbR6g3iFhCk2odKu7TKq7ecagf3wC6gab9MBuA3l/vVrPlVLfzLVPUQe5gGDgGXcp0s/Tz4HLQCo4rnXvK19H2NPNU6517r6a948k8CuJ1e4oCiARcMu9qbS8I9nSDVR0aXe3X7+o+Y/veA9vXKPwfVf9AnvtRxi773FvaRDXzsUmePQ/+dGZJKb3mwkdkMr7BpiBUUyH/ac2qfJ7o+OCzQDz2VA7nxvEN7o5Y1lv+ZpDIKjHv7xGHn3wnPMg7m6Gggj0dIdH4QAsOeEe4/QKeLqeopt+2v+RuefgNPv3AWcBNI5eejytuD09E3SCOTsdP29tN89WntTcoMohMrOSUGEBL7vObabAKnqKcuengDh6k8Zd41iN/qDVhBAB1EB8CEgRAzyBlj3bjqhAGoCzwR1kX0fHk8NE5DC61wgLehP/VdIB4kyeaAB2Qm6nmkMsMKHOxSU+cDGQMR3CzeRXT6EmVrap4D25IsiA/H7ew88H34P7bssk/gA1fbsFtjyOjGu598enn2X8+krIGw2JeN90h/d/dQV+n3d+cfX/C7jO8mDHH/E73fjQCC3suZOqhNFNYBmMv89Th/V+fVRYB8V/F2WL3/q4z/+vVb/XjLVP3ruCxS1bdl8geFHmXurcq+AIGAQI3HpN98r3iP/Pj+y7fM92z5/z7Y/wD+s9QX6eyL+AeIZ21+g+SvyikyP+Nj1p+B9foBFmM8r8zM+Pf2aS/53Vz/jYWJZkNXO8F5y3oaAuhPWfjgNfpSgZqpcV1As75wLnPE1fw+HZ7IASs/DqV42xe+S+F57gXMfvnsvDeBR3oK1valvC/1pY5NO4jf+y5e8S9NPL7md+f/2hmYqAiBsgUmmzRBIIdAMtbF/v3pvjKaLP+7m7skFWMErvkw59gmamthP0Hs/+gl62yHcd155B7ZIP0298LQkGAp+vY993yo6/gvYmLVDOYn/2PZMLdizNf6zEFNqAYldfyrsxXuuTiv+CQR8CUO//jOIeP9ip0/CaFp7KtNx+5bmb0H6CQIOBOkHMgoQZQcm/HkZsE7tVx2oh96k7nf7fVereOjy290M7WPv+OvLG3E8ffDsE8FwkKGfm6kiwiBYwYLg+hFW4Nn/bQf5hAGMB1oXgGP7PkLN3eUyWAae7y0dhMQDEnEWjkvNF/6SIgLURWwfJVzcwV0CCZYOupwjy8C1KRebA7xHjH6bqn88iYbatrt0F3PcoxY26foY4mCuP0fn3gLzEYLCguXSx4GV3qcmgC6f+j70m4z53sxOdnmq/euLQ+Jg5BZvdvTjw8CUZi/MhSNEDrUgg7C6LJcIVQ5Zbi8Y1B/JzXkYzlaBdLejVzSxoEmHIpujFsdKpTq61/OKitdElKPKqbfPM37bZLLk85IpIo1qDMt+P8u3TUfI9E4qYE3tvIO+T8oDtVDL8qAJdaJxy9QuDT1T8w2aKIVyQao27Q6YgRGtlMnuwWFvlr0Y54qSqa46Og5mDRwPX0Q37lWDREo51uNWOqR92A2WRcSlQZyPTWNUmknBh5jnRelcWTq+JTSk9Ky2vQrrkpj1ynIh5vtqcdri3chV8Kk/w+yhiA6KNlR9dBjqVk7nbaA7NtPIuhuZFnw+Yugl6OqVVvlSlooZnooGGlodPhfWa2W5YcUqr9iycnNiGP1dNqbMTddIDtcS7hqbgrNTXSfzu7RpNVY+cXoq2Tm3T/d8ixBZNy9agRt5H7X7yE99ux0y2UsurqxW1ooQG34UGwLZldahdLgjX7HK/qA0oTfSZWaWdWuSuj9zJWQ1dLJh0WFdDOVeM52dser89YmwU9SQFdfby2YwQ5RqneulWnHCrLVUDW2HvZ45WSwql1lG6/uLuW+ROVfrfKdH3olN936Txcoiw9FGE+BK4PfycUX6JYLvkaiOLaaoRadi5oGg9oboOydjHIuNzBxGt9MNow9IVhcxV3K3c/Mok4OkWZmDBp2+bnlmV2k63mykckHsPb0+zjetypWKhmRMaip4sYNBSTre7DwqCNx2b/nlhHFIoZ+7PNvx66C73URWdfO4NIk4bY/+eWZTnrHEuK4qDiIBC2xKmrOtFpkXc5R25y7dY9Y+ar0ymXtGghA1aXlGr6cichJurlui+yDEsbA7hXAfBe51WcxF7qiX8FWocxYPAgWm2EK8uJRKoDuf3jdtLzlXTYjTueql1nHQ5Wqul9rlTJgX2GoEsPdcb46Km+yL0dwF3C6xiawHctDiYu6WvnhWCIzHxWIpEPp1cyxqZz+vYq5fpefN2YkkTrGsTWKEgMA8JN6tjh2xXRm0nPK7oqzG0zo2xf1mCadSxiEwr43jQrkpM1+Jt4gsWhS72APwZW4O8Fbfc1tssBbCcq44u/LkVAKolVeG4OyDGwfIBkb9nVNLw84ND4F2PgtdU3fO3oSN4ugeQmnd9rusumaUaypHk6iZpd5ezFXIBGRqwTF+kGtSODHidiFzclUVx+4aSGdqroC9nRqjiwXZykLZJToccfsR8FPVwBJZNLew63WcJw5zoSMNmRJsrHPQco+sPE2vWS45oo7Y+IqVHEqsPdu3Yq7CpSlOUarLUWhaZNgI6xHfdIdhnjS1SrhNKM1IsBOytGZx7jcXfrhJVcnmc5PasYx01C3l7NRBMbMk8kpnW+q0ZYSS4WChKKONbsy9KBILTUqQbhc1ojfyF11X611WWqRuqrNSCZ3CufFHyeUd17nM7G7QSqEbj+jJE4tjawkZDs8JxTaP5+5Cj3x9tMWdRwttMBfCvEkzqsjVIOaLreXcYBKHWaoQFxS7Tpc3slge5CMiFKQ8qnigM64lxukJJDl3Uq1LbG0vZW+JvipIe3KkYtQ524ObF+UWu7bNtc+8bH++kKds1AZWqQ72ziU3QXYZnTHiFgWXbOTz6qCi5Pm4Xq61VQmCb58QGr2KSOUs8VeU1nPHbHHdZ73TJsdX21Y8dO3OrNStqfBsimxFlLviHc9yhiG65XpFyMjFy6MzvD1Js253kEXUcHWfdwZ3bS6wYNvyR+J4OojjWBOEl9co3h2O0m6fb+z2Nu+wPkGK4dDnIrGxx/2Mox1hE1lLbLlkXP7I96VomMYhjphFowXVAZ41ydgFWBpgKhzzGBrOWG3FLJnlMsW43XmThBFSlvZWYInUkkymTJHOm68y2qnJU12m7FJHGL7Y6y7MMtbKvGSLIi4RO/FVyg01RRUOcw6Ps7PPlrvFivGS9bK62HmTMSUXwltlSK7eLabIJRmH2z2OhjcEQTyzLBqccqME7wbE42Y3janEojobF0ApprcQK8fdWAilF0KB8LqNUQjLtOuruZX54zVfYKquWnm/wvPl/mJd+AyJ12zDnU5SpmBnmBOMxOJ9XyvrfoH7MuoozjbD98cDelBL7abogpIfMBfFMzzEpewiUclifrqFe/kWE3a+t6WbkdbDQuA7e7CLE8nOrs65oqvG0o+nVpW11Yplx5t08jZZbZt7ELQYnc0nuj6cGJUpKlO7rfUO/JgsqzmCoRksNnRMqo5EXFSHMk7a3THyQy9kT/RVP5TkXhEsoumdIaHdTWTX541/KSVNz9Eisq44l+Fbky7RdbwZ6yDkyFZRLUfenHuhZ+SMZs/6DLeRNNqTjMDxbH8V6YIOUDt26RxpqdNGYM6dHjQD5lW86Fmjop2EJjpcA7IDdMCZ43JeCDv+LNpUGp+MY+96x0jAVUCi7A4rkXNCbcgUjeMEcPFN4WxWDDb0utW1LBZ0QFfR1gvzjFfDaM6qqp0z2eFSjYc0p8+HfpZIgXFx4gVVyEk0nhmsxGB0RbXDkl/VJ9W9cOOg0YqyIjTMELNok6tpa0hnqw3GpPDhmRvwB+x2vV4raV7J6+587BtUkRmT9NK8l0k8j/lSo4IsPy96q7pxg5irs7TtKBcNUfLiuhg9cgSiXQcGXyXVWYjDduZ2GFOnFk/D0qaQeVbg1mwg3dxuVNGKv9U7llxLxdxRxvTQH+FooPOYbU1zfuAMyc3lAsdSFN4dNBIx+y4U8T0Bmpf50TP4VseHC75aN1zICLN5cGhX6CbOrgtP5XZRnVyIKFQbjFM34szKSvVmXcNoNDk22nTZbSVWsn0iU2xgMwOlFCpZLg68vIL5OKci5XhUBlerSSlVw1FWzqhurDilsobIovGMx64cIyXZ0diUsX0A+xuSC0h9KEe+Evz0avGqwpbNeNAz29RvHE9LBFpepSidrQoVLhruiJbKLD/Q12LYOyKf3ACjZPpe2yogUHPWy6uKwJoOO2czhlIRkjnPSMaj5zOrxReCubY634mNyxZL04PhdtsyJuEwnwNvbSuxTRCcMlfHS78/wpyKLdKolbMgBZV0hekS17rEtjhQLWglvC3OrFa5gEfceakqiiVzW0HjlY0Ug34yVBq26rNlQxIX+dASPb65sMQqwoLb6PN1ZfskWixJjb8Yuyr1U7B3KxPer9YBvUfW/Z4W8vDinN2ANog6GVczT5Dl2/mUa3SWyPxJrcpxGJB+ubJKdSac5zsn3gtLPvUGpDEPOrtvbqq9wKmkzo+nmL0wmVIKZIjaYFuCIR1PqGF2CkrUNzOMmO9SXBO0vgzDsqkvFhNZh/XAGafAwEWCsaJhNNzB391yAuSWUsArG1kPKdYSGKP0mIjMC3vHHpf82iZSDWwAwxmRooVNYWSE2AbeNLuwW6xYWAmHPHRuxdiQfC0iOlbtcNMVqIOxTKy1nl4R1cwvSDtWwW6TCqCOb9aXKxdL0Sic7aOGj3J5HveMcCTEnt/P0dNUdTUvF2jaDxnLmKkmZyEe3C+OdBnJLLfmLqcWVd2dTN529fl2uByR5SqyC8Rj8cIy9mWu7fcerF/7CI70gUMiQ1pt4Y3Hs+aM3HQNb91o9iJHxjB4LWco81xjUtIrtpGyTjYLfW05pZH2TeoH15VYENuWMmqSmFdYOh7aYJd3S3EtLozZzYNrzN1yrmiIkleGpk413Y64qTF7W7jkXBpbkbCUbkOjC7G8NCO+VhLF1zpYJxbharHgqtbLugO9sxSJ9SoiUgSWPMxm2yWP305SuA63YN9fj26wCtITtVXS8CwuwgCZeeKyX/WV3J27235WIxq+XG2Eq9csRNhVa8KwB2TpbayeUBEjWevZ9oZuRXLbmdkS03fUNq9ymOqafkb3VapvUkqDYXZLLWIfpRZ9jhGSTh6ElncPh3m6pCmBLbehNeNPsXP2XVZQ/LXN9yR7iXf7VTlStXur6NDFF264X49bimEOp8GZr9zVIJ/w7oIT8xRsvfSx99y1wLQDNQiX0Dx5t1Vd6+dDtChH350vhgurJ+i+i/aStcqp9dkhsry/kbRQ8RlpjvJpCTZTnrdqkFjq19z6fAhSCkO4YIcdFh5o0I+pLpZr7yRua3GJuutVEi61pc2QNtUzkb1FEWfMbWPmz2ctTN5uyCWlNc+N4NUxWnFUty6F5faGbK0uaKhjxKEL49KG/GbHOUwvjoJjADbiA1skfRPhe/4mLcaoIzoC5A4ZmFZH0/2o1ha+ZeCN5fPIMeIvm9iL9tS2VuJ5fHTSfNZ0Sbjz1/R2b+cOsr8p7ngYKFUZYTbcSpdTLfK76MqPRsI4M/6GmfuBNQiakKkbmm+x8MQx17TheDMi/PnxGJB5jy3a5elKrahiXYAW1F7CPmkO+HG3DuOLP8xih3czfX05mwp75DwbzucrwZO6gb3AsGcwMiIgbA+qZa1jJ4+EuXN6zbGG2PNLwx03DHCCl85uRHa5bjTG3dcpEuDzQeRhg/YWXp34WeB1LOUy242IhXg2493VZt34m01fXOllLhQiN8wYxCcB/i0f59nJ688blbk6/KWusk7DziQpYJpPHBEKKxdaJZl2hAH/XaltkSNCv6LRrU9zq6tSU0ixDVzMTCTaAiGmUhsC8dtEPF0Qo5Etj1LHWaRFaKA4hVffaIHpsO4Umaee93oqdJml4Vlwiyl51zlaf7uwEdbNekwufHXd23BIrTUKWQQkE3WUVu22HiIiQY9LN29+PXWCYVFGfzVgUt/dxsPsZnX4wkC6KxKZs7NnnquYBkSueUibBUvtttwUaOIf04okAI0zfQXSDbezUF/JyakiZ2KW+1dVwrRynGHbouiPSUfsHXI5jzsLy2SEq5ZRIZXtJacVRFwEIb0pBpEtZKuTeRETT+dLcp1TjhmlCMhh3e2dwL+SrhcLMt2s7dNiF3gEGSqoe7rgBR+j+/p2wrJtRnOXkAGF85y24TqjNpqorindko8kPa5QXQ7PM23h2slqMLwhLcS8U8VLfTxu8wDLV9iVGpYwLZO8OOh4PleEiLokSK4vwb6cuHmIbp0SSoeTvYQI15GhxnPpomajzw8BKFopWAo1yYW1cGbn1TjrDNrFV51br4sFraZSWXTn68UkZW+zXLme2nkSscc2/dLEZ+XayTrxKvsl2uBu15vEFr5usZsEkpdJaJr+8ceXTy/T0fTzgPnvvk6eDvv+n505Po4H31473Q+Xfdv7cl/ry9+W7OdPL7UbA7kep6xN2oXPw8h/OmP9/G++s5hAhsf72uld2a19O5xv7XD6A6SXOPe6pq2Hb02RdvfD3k8vTtdMfwfRfHsear/cVczK6YT8n1R6PGpK322/tcVdJ/9l+muF6TWQ78X2+2X4PIL+9OINwHGx23zDSOKbX5eT1s93IdOR7fQy5OW3/wPtQOHg8SUAAA== -->
