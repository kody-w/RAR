---
name: "rar-cowork-cookbook-teams-update-start-production"
description: "Drafts a Teams channel post on start production status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_start_production", "rar_sha256": "65541fbd34d047a7f028c045b5932f566ee20de3ae1d8d8015db44333eab8ae3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_start_production_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-start-production:1e4346fff2b900c7477cc8a21cd7d77c4a415869a6c9241a8343e560f9deda97", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_start_production`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_start_production_agent.py` is
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

Start production Teams Channel Update — Drafts a Teams channel post on start production status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-start-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_start_production_agent.py` and embedded as the fenced Python below (sha256 65541fbd34d047a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_start_production_agent.py` first:

```bash
python3 teams_update_start_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_start_production_agent.py   # or on stdin
python3 teams_update_start_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Start production Teams Channel Update — Drafts a Teams channel post on start production status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-start-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_start_production',
    "version": '2.0.0',
    "display_name": 'Start production Teams Channel Update',
    "description": 'Drafts a Teams channel post on start production status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-start-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-start-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3f56a45a2c24b1c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/start-production'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-start-production', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateStartProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateStartProduction'
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
    print(TeamsUpdateStartProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716e5OiWLbvV+Hm+aO6x6yUp2JOTMRFRBQElZdgV0cWj81Deb8U+vR3Pxs1s6qmu+fMRNy4ZlQmwl7vtX5r7U399mQ3dZiVT69PKrBThLfjOApBidiph7DZJSvP8E92duA/xM3Suoycps7K6un5yQOVW0Z5HWUpJF+Utl9XiI1owE4qxA3tNAUxkmdVjWQpUtV2WSN5mXmNO1AMN+qmQi5RHUJhSJTWoLThoxYgjGfntwvWLj3Ez0qkaCL3jEDhdgBeoGhwtZM8BtXT6y+/Pj9F8Prp9bcnN7YreOvppoGee3YN1EHs7kMqJI3tNIBr8g6aPXzPQQklJPCWB3zk8e2nCsT+M/K3v50vdhlUP79+SZHH58vT8KM0KVKHAKkzu6qBh7h2bjtRHNXdC8LEF7urkBLUTZkOHqmg4mnwcqf8xinLkX8Mz366C3kJQP3Tl6cMqmAPun55+hmBpn95Kpvh+mXgkv/080ucXUD508/f+FSNcwJuPTCDWr+8Pb4/2MKF35ZG/k3qPyDXe/Qc8OXpO+OGz13vwU5I+fRyyqL0pztjGL0WpHbqgp9+/iu2bgjccxxV9b/F95c74xDYHrTpofjPzzcn/4qMHgZ98PxrsTkM639iCVz+Lu4ZeTjqr3jf/P9PrOMoBdWHx/+U3Z8RjP6B/PKXtv0rgmfE//K0ADGsitJ2YvCK/Pam7jj2l0/et5uffv0dsv5f2ahZU7o3Dm+JnUY+qOq3t18+Vbfbn3795VOTw1yDNfTWlPGf8fwzv97k/ODBx6qffqSF8vX0nGaXFPnIdOS3LP8/5e8viGHHkfftfvWKfF8vw2eEDEa8C7274LuaqaCu3/nx56ffITqk0Jp7+Q/g8F//hUiRW2ZV5teI6mZNjcAA11ECBuW1MKoQ7VHUX1Vxvdm8JN5XBN4dyh1ChN3ENcKXdhQPaDZEfLAg85Gv/9e94eVn94GX43rAobfmBkRvNwB8+waAX18QLYQyszIKotSOEYXZ7RCIb2k9SLvlRdUkn9tBIFQmugOOwq4HsKmaGPwd+fovJbzdmL3k3aD+lxTGw4ZB8pAaJHlW2mUUd4g94JPT1eAzhFSIIWUWx44NsXb41eQvg08OIUgfnnIhUoMrcJsaIHHmQq39CMLwMwx2lcUQsevBf9U5imPEi0ronKzsbr0E+vh1YPb161fHrsIv6R2ACeTeQ6oxXPChMPL5c14CP46CsP6SAjfMkE+//f4J+W/kX1HdmA8ydrAN3JwFkzhGBHUrI7AimwQuq5AhHSDc3CL22+/3KAzapbDpwTqK/AjciCG3b+EfLLiH5j0u0OZBRVA+JP3oN+QSQr8gUQ29BWu7ev6SDiwyuLS8RBV4d+Kd+O7690Df5QwxqR4+hHHyyyy5rb1l3hBMNyu9F2TtIx+egubCuN56cDh0XQ/kIPVA6naQ0q6/hTDNaqSC9VL53TPSVNDUgfNXB7IenJNAULLrr4jE7mB/y2L4a3DQTTykztJoCPwjU++3IZPyE8yx+TuLF0QG0JtIbpd2HpZ2BW7rfPueEbCvvdND5jaSggsydHEwxOhWybfMU/95aLjPFuxjtri3eORLg6MYifz/G0AG1RieVzie0bgFwsmaYt3zaJiQBrPuQxWcBm7Et6L4NiG8g8k7zH5J4wj6vuz+fl/p31LnvuYOXU0J80JhlBv/oYjLG9+ohgkwRLQsh6S1v6TveP4M3QDdXw12wjo9D1WffQgcnr5rGsJiHL5/6+3IPbeGnIdZi+SNE0cu4gPg3RK8DsuhfB5Oh9kAhlKC+e6GP1iFQO4w0pD/4P0IRgZi/s11MiwDOA/dc/pjeTRMTPfwQG1hnYAX5DCkLUy9CnEAHHuGNdALn26skARAH0MVPzxchXZ+V2aYWh8K2kMssmTIk+8i8HgIU3BoHFDeR31BrjbMKujLCwwCLJ/rPbIfej5iBZVNhly/Ef0Y7oetyPeN5+9DjUEdv+E7HLSHnv2dcyAwlzBxB6CA3fRcwSpOwCOBYCbc2vPLvcPeW/iHLq9/GNV/+s+m+VvP1H+M3CsS1nVevY7H97723tZe3CwZwxyJclDdW9znewP6fCuxz99K7Aemdx+9Iv+ZYj+weGT0K4K9oC/o8GgTuWBI2ccH+oH9PLc+k8PTL6kCvgX4kQUDdEE4dbqPDvK+BLaRoATBsPjeUaqhEV1g77sB2a0jfCTBo0QGjAmG9ldl35XuYNMQ0nvEPgAXPkoHKPeGce2+jYkH9Svw9Jo2cfz8lNoJ+N+2LwOgwhyFnhh2PNDXcPSpI3D79jEGDV9+3J3dKglCgJe9DgUFmxccWZ+Rj+nzGXnfD9y2V2kDN0S/DJPvIBIuhX8+1n5s/RzwBHdfdZcPWt83OcPA9RiE/6jEUEdQYxcM7Tn7KMxB4h+YwIsgAOUfmWxvF3b8QIdbzlVDp33UdAX19OB09IzAuMFag+UDUbGBBH8UA+WUAEI7hNfB3G/++2ZWdrfl95sb6vtO8bend5QYru8d/54zkODfG8kGf7630reBqz3Q3ganm3tvY+YbJI6Glvndo2Do/2/3/Ht6hfgCnp8GJ8LOFEf9bUf8dFcF2vBtQIUcIFJ8roYRYAzLB3KCjTkf9D9DlPtOwHA78m7rh4vXP59q/6rkXzFAEuTE933cmaGoOyWnU9elbRxzvakHr0mbxCh6MrMn7gwnMZsmSAJQE9SfecCzZ1OowRDBxH5oMMYG30PdPxz8n43ZT3di2BtwagKpJxRFYr7jEaSHklN76qM47aIk5VAzAvepyQQAHPUAYQPMoz0axSjPIUmCIIDt0DYgBn6PWe+u0dv7XP0ejXvZv0GUTKJBX9y2XdqdYqQ3m0KrAYE6hAswHPOmBEChWJ+mAQnpP0gfERkCdjd6SFQ45sEhqx3k/PaI8JB8ExKuXJHVmrl/2PHMsKfmxpFDZ1ZOfKY6zc71dWPkHDYWt43XZBOt1zvt2Ajo9oqZF3J9FkQ+YddWMD0EMwhFixmTToVV28z9IFTTlTpt+q28lc5SsHRNudu5NL1c7rX5RBTVo3oQ0ULB9CTRot4TneJCHuiKNqiUbM9hnLta247JJM2V7mCcw7HVc30XSeVeO+A2F+zEsBBxCq0Vq1v2RWuw56snEpytZptxyiQdtq80NQXYqaC4+JBTerHMZqu8wkHbUyOvPcXjdUX5bZrOrO4ESsFYL3jtHB/nWK3ZcVnadL3MS5uVNjxopLThCTbflZfYiuU5Fm8jKm5MohIiCsvzLE+YuTfBxJhszdy+Wq1nU+KyaEp90bXrTVDVrnhVrs1xMjlA1fZJs7TjXJMToUzZSVWg+GyZZSPPxk/mbFHIboH1SaSIsRp0281ORsOth6XbmNsIhmih6cpEZbarnK1mT7iDVTi1Pj1sR65yXl4bVTseTVc6UZG96gzSTtmZHx2MXK6xc7pR9D5K9y5UdmllPlau1eMRczi7lQiZcVersRRUCn9xnLxYHCrTbVn7sBFF7CifW0IOKzE6Erp9UM/Wgp5p+UXJFyancqqykqfzSVrkRJ9va78mKX21XqB9Q0w3pZle2TJ16sBra/K6yUIjmcezFDpDibZT9RJxPL7Ww8AGI8U0il5W2pgMgCebqqXbnODSknc4O2dSInpdwreN1V4M5eqKpF9JB/xknTp9m1OLhXolFhtRn4VV33oEii1HTSE2V1o+16QFNmZopcd+zihNPMeNeHnQDu227s4pOlU2eUlJR2pCjXi5mKkmORHwzXy0SkngWiPDSqNio41JTu4Lxx8vTjMu256wSd4XBKCFtG4V52LIUYzpXnyUuoNaYIfcOO0pqxlblRxE0YKXNDdFs5mD7UJ9rWCOqDWsZmaO6rqR1sfLiytMHDUOJEo54FrAAUFdLhkmcBSD1xKMO2uVVkcMqeC8KmdMmayjMNb16zFV4u2K613AkgRb7E4lhWl5hpkp60YUmax3yhJLw9MU8ya8sGXCg7Ok0iR3jqu1I3vrMRuPnaubHTGmHY27ZZOR7GbjOdMFapjVdKKKZGvE+O4MAnTsdHIJe+FRs/oTHgigVI1eaCM/bVanvDhl+mxc7YSNsBMLqe7RMRnKtSGWs+Uun4XOqadrqS5FUuMJ4orZ8jp2DZL0DFFazeIuQr1yAxLDr+vNPuWyc1buTn3nxrsUyIIkzk3JUDOn8Du7L71sZVhZtixAxml7ejQvo9I4bkRsazJrzm+ylIwNZ65vrlVHK7qdKaOZuWNX2XlvJDrKTwh/d0aBexVCQbtcTvY+PPZH8RDH8SS1LC1fjlnP5FgMoxKNr11KjfIOxaSqmPEpy++d2PQKUuKjnpfGfrw52B4vN36haMdJ5GHztO3xtrPmzGyOO4ejbmlTciWOiw2/y1fyJDzUzdUdLyZTml5bfuiiq6PvB6TO7VZpqCpJWKaGbqcL9KKdNqgejru9VRRsAVSUdmRny5748+5sz2yKUtl1NJV62sV3TF5f+MhNqENI0f5V7jZqKjqYmxZu0k+P/XWeMld2Eex1TVwcNycCXYzz3O75ZUJRkhuK+4uSoMQFdyyuxs3j2Sr4pTWf1eJ6XaAXOUkO4sbhzCOxCnVmqaqBUqeJI4a5FvRGGjbmaud21bo47PCEMapSuxa9S+G7RbGRrrvdROx6hxr5qTOityxQLM7n7fyKjUbgLKUbwessIulRYd6J4uKElVQGxoe1tjPd0bWZzhnO3ywhOJt0Va/oZNXRUkvu/c16Tub+crMnu671DeWi7lnTOntrEz91RmLo3CktKIxLPMbTkhEa2aqi7YSGieyFbm7Q5VxyxFwkhEIRSuI6N9ZblNAOteox6SENN9kW26dBNhOtLpvk6zlra13VO96cRo/10gC7fT6P13Y0VvLiuF+VYQrQhLSWM5Xm9jKe0atisWjyWHOCfBsXPVVTod0d2t1+L7g7i2HOh+VJMJtzldE79xRK5DXpeZMlOH5tr0fWNS1L66ztdZWkCNsRsJhvakBkkxgnuWqheFwx3+ddvFjOrGLrOnQ/jZxoFfK2sZo4vn7imXjDb06FS+T8iT91jspl2lWgLw3p52LMSieN0BsJev1iAFGYFmjsaHNhldq70oFI5gRZJexFkLsEL0+DWpdYb13xZSOG1MgJQl5qDqVgF0Z+Upn1qlq04eYiLaMTxKTuAHwBr+oFMa/0TBfSTJBM44gVa9yS62MiRBclWHJXGh+ZzlVosO4QbKJDv5zHpGoQXlRjhMOzreCx+EEwMikKlDGcRRzWVwmUtlCBpY6j68bFsyZHL7Ws03jHlfNxMam1s3KSiUOABjVDlbixnund9NoXHBHueWrHOCBVRA11CtOGg0l5ZTreEnsgaAzOzDZog3JRL2xtwZH4mSIaxobTddtnI/FU9GKcMvuiLc6Kvzo50XSWqeew3zNmPh7jc6wld6OzfZVX67k+ixnOuADPcxZxzh8xwVmiBn/SYmqy9sZpOb2ONeykZgVYNeutvLFHDKpcpgsVP2PTlk9G19m2Ks/4JJX7HW41CiqWWD2jcicA1kHabw4zR5yysDyuGDO/BJa33fmiEZ3TYIyGei4HvJoH23XWmDnu60rVx5GemYxsaJ4sN24p9edVsvXWKlaE+t71jcKC2KDqgl5kZmsaWxKzGkN3PK8x1JPdFjrBCDzThw3lmHyiSsdqk0fbWGdWwnGU7ZebGtPnizQ5To7bg8vkbjLX1vMkZ3VukgvZuDB9OHz4DiZutb7K6vWKbkSfmBL7JgesVHMYuZ9k/aRX9OuZzo5qcwwm7sY8CfOQC7dm0gTEYR/QEV24XREQubSFAyUFA0Wecz4G1dEsz3LWX1qmrLa0sDJhgbcajHa17Eo+ri6VdsAMUHVqaUxTKeWMczGZ4VUz1hKQMwd6Z/ke20xMw77i1oWfuj3BEHwbOyLXHlYs2dQkNtP1enXledzzNgVnJyLnjcU0S1Lf1atcIsbEZXbY2EKxUfirKGmBMpE5ZcsF+5zw1te9ZJxJVL8a152K9uesMSqSmcxHJ6Itt5WFHkrg0NNsziuWPKax3ZLA5JXvrFVSNnVxbxxmomks1TU/M/gRo2UroDLOZs7hZ2rEpJ15TFh6AuJzFIBtsZTW5wPIMS2N4xqQLKHmlR0WDLG0HdIUyzi3Lma9Oh1PVtxfV8fd1vJhjA0pUR08l3Bh0+7cDbB17uJcd31vESObWjTRtapg9LjZ1bWtvSTst0ZJBeJpQswxRpEaYE2Xi6FFiqE2cdP1Qg9mbjPb8RPVG03xJJ4rQZiGpGNKRTx36RUmNrOFuR3rcL5F432w3jQXZYeSUk5u6YU03UZqf1x6FDFaZMJEbwsjlfn9PPRqbyeS8tItHJQVVpa1kIOJtDTPJIMbh5MMKqaC4yNsUyO3VG3f79WZcvF0a0Eyy8wSjFZbzfHZlpyy+Fzc64EijY7p4eKmu5KLZBYt6LFySZb56Uoq0Tz3E/5onI1+TOXV0Zu0C7mfVAe4k52gTVkeFYY77RXzEnk1bcpx6rJn292vZur4HE1GCwyODye/ga3jOsJc+zSD4xoOsZ0wumN9WKcNvV00k/Go9vp42syjZrVJyaS5VAsXNyWQFQLLw/0qm13xlDyfiWBteTza40d6seyEjUh4Y9drGdrLML3pTSqhOa06svbWNZtwHTTjBJuDbm13W3tvmMlsdJACYqZMlItu+afmQmC71GwXfjzTjKDHBH9qjVbyKZtmrDwG2LE7eefSOqz6pqvbbcVWlYNmI/ki0II33cLparxa0+ON748rY9fNbd442tAanyyA2c+mZZpgPmHP06rEaTiATedHZXEg9vpok2aHQPSWs240F6cCeR5nK0oILjLbHg1LE6p5rqAUCbFmxa1iaRrgLEkt6AMM5bTrNXXqdW3jRXv+6lEJhcqriGQwBW7xJBITiI09o7RTzpvLlXTKpUs3WrTitMN7sqrmCjtukhMZjHX3Qqzco7yurPLqEezqCmB2mZ08clpprPJsOVf18f46H3Vt3TKXIyMv223YHE52Z8WZ7yjt1st9ampOiHG5WqlbfW5g5ormOo4zcXIbExd/tfcSatSjHWc6NdjiTEUG80qkpxJW+6Aj61k2zanTvqHb5ard8tNkmqbuBo7RCQn37FJXp4G7oY8JaTJHltgK3JRVJhQIlxvOaQ/+pJgobkhKjBsXfrtPl5udVG4wBc5gLOPxEu2SVbRiStndCzWJLqqLVoltSV1iIgWuDxha37CHi9pGvDHVO32MURQ99ucRn/k146mLg8aPp63GmvMr53K8tXE5d1/v3OSwOO0tjZOWnj1OsbnsKY3KaeOxdArlCWuzJgmmSumkDdpcuQ0QamKnqj1HSFhQjc6rYxuvjuueioN2YVPKaqS4XrTDrqumtynCOBPTUDLhtHOa0Bznz8CuAtt5ZVnb8SqMJCwiF9JkYoww2u2X7c5zPO7MUtZmURV8o+CXw6xMY5NySZTYE6AM9WOYloSxv67ivpkTAQnYncRD2DFnW3QBgp2XKoGy352tcSKgfr2HHYsEvjpXZmcCS5fUGcw3tVeGyx3Lok3vqdvdCVRweJ61Mn7wZzPUIcok9HsrZPxpm47QYpUwDi6TjnvxRRwbTdBDez6EXmosPIKgo8r07AWRXBPHnNLL8cjHRZc9tdtpJGMzgRAtVTqbgBOtgN8tjINnetE4r4z5RC5W/dJuGquZ7UuyDYUxf8z44BzPJ00b5dS4Wep71HYx7zpZlr23q5RkUstkG1N50jJiQtioalk5vZotIpS8yJm0yEWOd5LwFPYnVJpKtanj5NGV2wOeTnGU0FPtRBvFfhnYSutp03ans6AP6d1y7h4weSSw9IW+zCuJMS71dllXjEtkXdad/aK3lWTPu9su2i9WXemc9PNOTbPW7mMyTiuyPwkkWmOFVy38dpRxDds3MWBHsCh8K5c32HgZrUbWYYY1e8r3KgrupBcud23pTIB7s/XSAcloCefWVm8TkKAAn6YM3efxZQcnv1K42GK/pPaW7WSL9YFNN5fF3CSUdaoDxbvm43K0ydKyOZLThUCZ9o6jPOM62Y0ZMfbMY5WIe4Z5en66vXd9esVQiiCfn4bz/Mep/L99rhv0Uf72YENMUfz56f/d4eP9IPD9Td3tiB7Y3utN+uu/qeGvz0+lG0Ft7sfAVdwEj8PGfzpY/fwvT3oH0u7+tnh4lXit399i1HZwO4WOUq+p6rJ7q7K4eVA4TTX8P5Hq7fEa4OlmTpIP7xS+V//x1uGtzh4mDHdub2gT4EX3BcPX4HFe//zkdTBOkVu9ERPqDZT5YObjfdFwBju8MHr6/X8AgJgHdO4mAAA= -->
