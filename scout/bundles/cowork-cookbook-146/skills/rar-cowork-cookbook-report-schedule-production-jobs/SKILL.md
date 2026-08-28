---
name: "rar-cowork-cookbook-report-schedule-production-jobs"
description: "Builds a structured summary report of schedule production jobs activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_schedule_production_jobs", "rar_sha256": "4bfd76893a786b989abfb54a516d638e22a3924cfeba9b8334c93445efee2cc9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_schedule_production_jobs`. The original RAPP
agent is preserved byte-for-byte in `report_schedule_production_jobs_agent.py` and in the RCI capsule.

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

Schedule production jobs Summary Report — Builds a structured summary report of schedule production jobs activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-schedule-production-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_schedule_production_jobs_agent.py` and embedded as the fenced Python below (sha256 4bfd76893a786b98…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_schedule_production_jobs_agent.py` first:

```bash
python3 report_schedule_production_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_schedule_production_jobs_agent.py   # or on stdin
python3 report_schedule_production_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule production jobs Summary Report — Builds a structured summary report of schedule production jobs activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-schedule-production-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_schedule_production_jobs',
    "version": '2.0.1',
    "display_name": 'Schedule production jobs Summary Report',
    "description": 'Builds a structured summary report of schedule production jobs activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-schedule-production-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-schedule-production-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3ba76a74c8e9067a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/schedule-production-jobs'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-schedule-production-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.429, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ReportScheduleProductionJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportScheduleProductionJobs'
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
    print(ReportScheduleProductionJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZObWJbvV2Fy/rBrsBOxC3d0xAMJEBJCICSBVK5wsYPYd1C9+u7vIinTrqmu6e6IiScvKeDes5/fOeeSv71YbRPm1cuXF92zMki0kiQKvQqyMhda5H1exeBHHtvgH+TkWVNFdtvkVf3y6cX1aqeKiibKM7Cda6PErSELqpuqdZq28lyobtPUqkao8oq8aqDch2on9Nw28aCiyl2wDOyFrrkN9oHvXdSMUB81IdTkjZXUn6Cm8jIX/JyksSvPit28z+pXwNwbrLRIvPrly8+/fHqJwPeXL7+9OIlVg1sv+ztD/clMfee1BqzA5sTKArCqGIHqGbguvMrPqxTccj0fel59rL3E/wT913/FvVUF9U9fvmbQ8/P1ZfqzbzOoCT0grFU3QFvHKiw7SoASrxCb9NZYA8WBIbKnVaIseH3s/E4pL6C/T88+Ppi8Bl7z8etLDkSwJnm/vvwE5RXgV7XT99eJSvHxp9ck773q40/f6dStffWcZiIGpH799rx+kgULvy+N/DvXvwOqDw/a3teXH5SbPg+5Jz3BzpfXax5lHx+Egd86L7Myx/v401+RBWZ34iSqm3+J7s8PwqFnuUCnp+A/fbob+RcIfir0TvOv2RbArf+OJmD5G7tP0NNQf0X7bv//RjqJMq9+t/g/JPePNsB/h37+S93+pw2fIP/ry9JLog5Eh514X6Dfvukqv/j5g/v95odffgek/ykZPW8r507hW2plke/VzbdvP3+o77c//PLzh7YAseZZ6be2Sv4RzX9k1zufP1jwuerjH/cC/scszkAqQ++RDv2WF/9R/f4Knawkcr/fr79AP+bL9IGhSYk3pg8T/JAzNZD1Bzv+9PI7wIfsgUrTY5Dl//mf0DZyqrzO/QbSnbxtIODgJkq9SfhDGNUQ+DvlduUBu9YRMOxzHYj/ycOTxADOfv0/zh0jPztPjEQeUPftDee+fce5bxPO/foKHQDZvIqCKLMSaM+q6tfMCrysmVgWlVd7VQfAxB4b7zOAoc/TFyjKoF//CeVvdyKvxfjrHS2jBzbtF9KESzXY8DrpZoRe9tTEAXDvDZ7TAvpJ7gBh/AgA6iegc50nHcC1yQ51HCUJ5EYVUDoHUD7RBrb6MhH79ddfbasOv2YPIMWhRz2oEbDgXRzo82eglZ9EQdh8zTwnzKEPv/3+Afq/0P+060584qECQH96Aki41ncKBDKrTcEy4CTgVgAbd0/89vvTtoBMBgoY8FvkR95jM4jM2HPfDK2v2M8YSUG2BwwMjJtOhgXoDEXNKyT50Lu8z8I14XeY1w3kegWoR17mjICqBdR5t2SWN1ANwq/2x09QW3t3rr/alXUXMQUpbjW/QtuFCqpFnoD/JjHvi8DmPIuA+d/D4HEfEKk+1BD3RuIVUqZYhAqrsoqwsp48fOvhF1Al3rYD4haUef3XbCqL3mSqe2I8zAMWAcs4T5d+nnwOCjuo06DQvvG+r7Gmmna417bqa1Y/g96qJlc4oAgApkEbuVMp+NszpOowbxP3bj8g6UTp6QX36ZV7DOp/1QPoz3bhUb2hry02Qwno/2djMYnHiuKeF9kDv4R45bA/P8w29T6TeR/t0kQPxM4jRb7X/TfUeAPPr1kSgRioxr89Vt6N/VzzgzZ7dn+nDzwNzDbRvQfiFFhVNYWw9TV7Q2kgMnSHJKAfyFoQ1VMwvTGcnr5JGoLUnK6/V+y74yp3UhoEG1S0dgICwfc817acGEhVTcn0NDuISm8ybB9GTvgHrSBAHdge0IeAEBFID2C7u+mUHKgJ8siv8vT78mjqgx5uAdKC5tJ7hQyQD1NM1CAJQTMzrQFW+HAnBaUesDEQ8d3CdWgVD2GmfvQpoDX5Ik9BmP7ogefD7xF8l2USH1C1XKsBtuwnQHW94eHZdzmfvgLCplPO3Tf90d1PXaEfy8nfvmZ3Gd8xHKRyMlXiH4wDgRRK63uwTUhUAzRJvWcAgUi4F93XR918FOZ3Wb78qQn/+O/16fdKePyj575AYdMU9RcEeVSvt+L1CnAAFDAnKrz6Wcg+v+XV5+959XnKqz+QfVjpC/TvifYHEs+Y/gKhr7PX2fRIjhxvCtrnB1hi8Zk7fyamp1+zvffdxc84mEA0GUHlfK8ob0tAWQkqL5gWPypMPRWmHtTCO6QCJ3zN3sPgmSQAsbNgKod1/kPy3ksrcOrDZ+/IDx5lDeDtTm1Y4E0DSjKJX3svX7I2ST69ZFbq/fPBZAJ3EKfAFtM0A0wOmpom8u5X7w3OdPHH2eueTQAG3PzLlFSfoKkZ/QS995WfoLdO/z46ZS0YdX6eetqJJVgKfryvfR/sbO8FTFbNWExyP8aXqZV6trh/FmLKJSCx400FO39Pzonjn4iAL0HgVX8msrt/sZInQtSNNZXf6L0YvIXjJwh4DuQbSCGAjC3Y8Gc2gE/llS2oc+6k7nf7fVcrf+jy+90MzWMG/O3lDSmePnj2e2A5SEmQEKDSISBKAUNw/Ygn8Ozf7QSf2wG0gVYE7Cds36WpOYNb9JyymTlj2b5NEhaJUi6Fzz0Ms3AGIxzfsy3GnuM44TA4QZCg1HqY4zCA3iMov03VPJpE8ma+hzMo5rg4hZEkwaA0ZjGuRdCW5c7mc3pG+y5A/+9bY4CLTz0fek1GfG9KJ3s81f3txaYIsHJF1BL7+CwQ5mTZpmoP4Qq+JcywP5CaHl81x93EudfsLvwJw8+xe4U1LMZ5YmR5Ik49bseFeLwdSmW99eMTfDaZdUb3R1Y7FdgsTTIi4aNF5eENhah0SJz37iqXklbuFjFfYuVJIdN9merdyaoue1u9zFeVfIuNxKoVGPFjkymj/d4iLhemOkoiWsYHtRmNYlUUl21H1NcBdsDoZNdGkaPbedVrMXwuj8aFuDmdQ9pGkCApVVXHuRHO5u1hDbvpISbdDKcXN3JEVJ+4Xkb6FKR6qWxY/Ho9pVVaBc3JwbdGWhrzc5nVJZfB25ZtN3FQegv7qK8OYiLBjrSXF14814/waU4qt5Gk5WOjG9VBGzysAuupJGA316WOJMc0WDpueiqXZnEqrzVftYqVw1dUX2ZpW6OIhl5NKdUTMmXLw/pEUod+sYXtZs1ejL7cF7eRDvlbEAvNLaHy40VZVo1zM3ZI3juSrfSXhmPFrKfokh8vREUJXovJayMliHNaSzQappozoiVvqx3KjH0bxag+M8Iqj0UqnzcSfd7X4gy2AqxC6WGMyys1yytx9MmyJ/DcIFHjFMhij6jO4ijowYCrrSdeLTRibtuTTc4TQ23nzkJOOeqC2m6DV4qzb8mROpuH+dlwMyIqh7o7zY+qdLruiLqX4FJpCuE0qmu9pk1rwc27uTyUVHxjrXxwMQlupJWCleVYFrPCLbpIXZ1mkllJ2Y6XF35hX2NJc8y6Pl7KDN2aV9hhXNOhz1jRyDdMH2/ibYfIc/p4yS0pXpvalnT5Gclxs5FaFsWe8y16p61UDOsPlYMshx3m+UMHul70Sp5Sa0E0KhIMp11BMHC6onaDK5IUd6tMHVkTSWvYxWporHGbBYYebhijOQV7x5CZHN5uDBsRtwGREARjkUgTj4o1N9mMDQSLWS1O6Lj2dyeTGwy9WirryyaglNvCPFftkl3EEqavxX0WV4sVLV54Pd7HY4+pZDSW3umkVIfgZnGDgq+qtdJvKoKCXYOyOZkhTN3nhFkXR9IJ3iIm2e2N9bDC7bmyvKmFRWy6eLZAeoTHTIt2eButVNgfuYZ3OCG9+Iyy3duYSNM6pqLldT10kupgM6vI9c11CCX8sA+UtNEt+tKFyg3hhuOQUadVcyWEjBvnWm7jJHfF9mtPR8dIY2WfmmsuSd663FQulnW40TThjHJpVbeeTY3ApBJKHyuUqbRFh8VEfwqjQuZK6bbFD+c4CyzWsIfisiAxaZ7nM4M+7MqUW5MsteGWmNqVl3NKnZxx3ifabr9WManDrrlWk8w8PoZj5Aa4Oq7yWNujp+OOwjU5ncE6d9A3cSh6GKsz40WGc/SEpUR+KISluDfPEpoQ5jU9STV/rNLmNFrYxlvfDqxEM7LIHRf2AOKtTmm+ADnJSNk2swTsmHrzw+CNZ47FuRE0S9FysZsvxm7MzmtGEGpqzdCzlRbgne/D2oroFI6+YmzNL+31mEuObdwO26XFwh2vjXQiHZC43KC9vEza1SbiYkPaJi1wdXU+aMboZNV6pd5Y51xsiSOdKqnoqubcwmAtFjDOLkq9lOn9OHD1sF+sypmEHMWFv+40Hs6p9VlRRhrNdV2QWunGbbh2gQt2JqAVb+ZLZsE2G0JKUWt5OTaG4YVh5sDnnj0NJSdSF4GQ2KgyqD7zr1nLGGdlE6OpY+WyOabLI437q0JeoMddpLgXZg6rB5T2M97Y8q5MyRXjn8Z1CAsA+2PMG/rdwGmFqnWzuVErc7lqdubZFKNwocYdmaBIL98QFYk2cNv5QsL0q6iZA7gNK5cmUCXS2YPMXovDIva021Hodc2p0qNx2rLYzqYtoegFhdUcNo3TSs0sXh/qNN7uDiBAzK7elLq3liUDDFEsHsVhNVdmQefFp7rKt5fjUuv04ujuWEqqPcE1ttpMu8G40+EnLVFXlYoXqbKAm2NUSrGmMgRezhu/EeoNWXemnxQx7UeXFDO5djMX+iurzZUjnEgGZySz7ZwOVvbxgtEyN1ScaIVHxiPbdd/EAQYQ73YJbbOx0u3KWrTF4kpxoZ0dr1Y7R+EdJuD1mo1Rsov8Q28QyzXmXLiLPjoWncKzwqLJWb7vESfE5vRC0wyPmZ0dUXDUfVHy8kViksqZzTRiJJtuUCQ4b1hny8+5TWk0RYDF8vWEyqN1E3BGmyFor51Df4Hy9ml9rBfL2CZFc5AvF1+X6EVceYKSWvO5ylukBmaRS75K51t+1gqXVhBSW5SvMnu4HoYzefYXFGKWJXvdqZLO4eGuKS4HmWmVCDTvYVjeEsU5b5yra4KY2t5kqaJ8TtlqrYG0C4yp5Ca+quu1WBaG2PtjW/HkikqYbm+xeurQnRmUflfiNcMVWxvrAziPnYwRtZgXxtPZmR85PRX7ubPhV4WBDoEDKkoWifSy2xq+uRgucRzO1FkyFrwBcE/R+tFpzJDBG1VXdXETaTtX6ZCzaVAcgrEYn5O8vCq37C7jSGVW7/bxPjs26PF0FJe7VZbDNOx36uHW8Ya64mcDxs3OFxXnQ3h5Fg0t604xihtyhZJOic+o7sJYcnTZFUxluyJ2voRJxoMcBrCGB7c+JCRtc17ql3Y3NJW071Wqh42yv9nHXRcdTXkg2vEYFuehIviCvaxAx4WRVlcTHEFmOt+ceyLaoGuDDHaqW2ihXoYeczhmVRoxgmbsFmAkS0FZubrsrBe3a/xmzWMjgqMQVIjZLV42SQXmif15l0j8zgtk1NONXkvGs7ANRSOTtGUVzzJCByFykCu3WEfeJXQbFkkGHQYTAD/IQ5p2Nl6uGTmNKFPg1XMxhp6UepmalbzQnrmdoB8rRRGq3PRxGtmMRZGX3CVWtGtLgrBlJGwlCufBEDB4JzbJFcBWg2OhortGqlCHU5rMBLLWzVrccj6aeEZMWlUc2tu1PRrGtXPdY6g6DWxuduFSD900dY0Z1zPZMBxJuLRgudud7dONmcU0YaT6CpUVgqKzQyNsZD5rdVSq5I5Wr9ICR2wWidqlfYrl8MJQl7y/7TRpZelSfGvTeb7SLQk7FhsyDhrWUAxnWfT7kjH73ovEZp5lgc0dg/ZWjQ59tRh2jxcj3wvujIwFsbOwON+QCyLP8X7hsfSGWF4sNil2aL5fy4OWHLGgSRueubCXYr9Zzw96plW+gwW4B3rndsVWdrrGjh4p6OX1ctwqeLhV6qWIt8Wa787ebIORQmbY63IhRgrNXBV4s7+G3RZRlWvWoNoFt/ZXfVY7eif2sZRbY+AVJkDGFXFDd2GKm0yd81fQ9pi7643a1zMZvvoJ3q5X8hqna8o6CsZC9FaBojPb24KumWNKz/bOfL4/3yr+rMfnkxu2Ptlrt14gFoLRiE1aXM9Gn5XLXS/pGaxvZ7JJSBtF4ZnK1bNNwFfG+cT2uyV7Inf8ArfFPhBRIV8HoTh4pSlmOhhcGINVTIHW2X2wvJUde1usDqtSpkCzeYk5Ti9AeEQUsuRBq7uAj9qxC2bOpbHPzXFTDBe7v4rluKGWLRXZDuhTcwLMaLWC7k8o6KjPY7RRuf5k3nT0ypiYlih9qzEbSRxAGaGMDUdzduJfty6+ODheZzU8DvfH+YqT0evGoxeEKlcdpeBi54aO2ZMzmkHH5dXGUOJAyFd2U5Qrv5WVAi1LbkZZYPSm1LUamM6V7we6rtIiVvP60tpYqa7J4YzwGkymiTo/lFd78BkbX1N9oOSYzZsXe0XYt9xb0EjORXPWxVt47Yw+TONqqdeSVzCMLQWE4646dujohSx75rnEhHBO17R9a9hK4mBXGDpOvcrdBQuQE0Guu5uJIyDbkbwJqhpVaVWd71WZ2jEojsu+mSr9McO3RU1hxzpYGdY1n18P5+zAzQXkIuqXMSZtJlzwUQQGGjg8dmIsCbsdLm3PDOcHujHAB2+zLHfjBTnN/NVOqZLZDnZpObC3SgZmq9hbhrdGa/bneTjbuWZCj1nGGv4x7puZvJA3YGIKDj6m2ASqLVKBdkNxe0UE0CKax0sYz8160GcLHKNoWuviapZ5FyOuUSPcrrC1o2J7xiUWS2k/a8hYufFutgypGzqz6YRaDRelXSPUAGf7uq/akoeD1GSjdghHA74S1KpZrXD1IO3dFiXo8+JWstTY2KKFdd3FM9veRl1eEPAQzkmCumZrc4X7m/UtSPOARVy7y2agi+wTopHmlzZfCyhfoRmz6I0cd2t/EMX9lSU0USVHtz3jJ7Yj/WwTeUjZg1pjI60kDfNN02yFRhZUry+WPNKJY5JFplfVLOxxQWVszWTREaeYQWSRdGEERg7RDtc8IGs6kw0SkWQ7CY7HVbqLN4i+s5qVkxrLUTsf+K2gN4hKCQt332ISScMnU9dnpsH7mt8WTerRKDVwdrfu1tjNzHNyTKOBYt0EHtZJhRigiz2YdoiEODarGZBcjdgeUhIFDRV91fLw5i6PwVzwaWNZe6LY5T3LdDZ7thNGKBicBv5GtgbBoKf+qMlhUe/gKiVXl6WNHzzBjm8H01MarBEWsx2jj7W8pxiMrVBX5ZYpe15EDlJtWBud0de9yAksPJTwSZYYa137qxxx4rGiiqxZ0wuGEdtBaXl2LtEekQgciCnapouM9uy2BTYqQC4E5q23B+JCd/aAboD3ZQHp9MElG9qkTsOJAs1fRIFJBYFntmAaQOWtqlQNfEWQtSz4oobjbp8yqGxSXKDypsdb50DsuKPlCu5VTbvjMG7LDOctpUZdWjF73xMRY2UpS/0sbHRYzuj5/ERywzow6Gu9ww0MtGjuvKTRCyI2TFuNAaVT/VE5wStmWeWnGRKwYK7vs0hL0MONuU33boJXNNaCXHYemskDjm+3w7XcBzN5I15hejXzvPzMZEsCXizoJrLmVwYJb4HYnxctD8DHYjOV2IrFSU24FmO0LVakS3WbseG8wLa7hDu0SG0EdOnEnloTI0zpBLaDlx2Onxcmd8GdbOnbl1ytnTSh8GhY4ju5HdEc9t2a1NJd2HJns7B4OcX5OmxOiJWIGnLszDqae6Bas/NbkfSqz+IHfmZtbgKhnXU7FyRjkdHIjTUpPZbXKr8DPXXiyfmtay/ELYwdvNtopGsOlIqwshTzMBFuNJZ9+fQynSk/T4b/1de702Hd/9qZ4eN47+390P1QGEwvX+68vvzLEv3y6aVyIiDP41S0TtrgeYj4385EP/+TlwrT5vHxvnR6iTU0b6fnjRVMv+nzEmVuWzfV+K3Ok/Z+KPvpxW7r6fcO6m/Pw+eXu0ppMZ1kP/g9T7m/NflTB+9l+pWA6aWM50ZW83YZPM+HP724I/BK5NTfcIr85lXFpOLzDQXQDHudvaIvv/8/Qp1AJDwlAAA= -->
