---
name: "rar-cowork-cookbook-scheduled-brief-manage-service-assets"
description: "Schedulable morning-brief email summarizing manage service assets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_service_assets", "rar_sha256": "aafe6f3b7760b143e1068c72d92c0d0df8bca4f5a4653b9bd556503eef405cce", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_manage_service_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-manage-service-assets:5db4454485a24812f0231fdd578e3aa76302f79ed5252c74b124cb1267c10977", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_manage_service_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_manage_service_assets_agent.py` is
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

Manage service assets Scheduled Email Brief — Schedulable morning-brief email summarizing manage service assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-service-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_service_assets_agent.py` and embedded as the fenced Python below (sha256 aafe6f3b7760b143…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_service_assets_agent.py` first:

```bash
python3 scheduled_brief_manage_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_service_assets_agent.py   # or on stdin
python3 scheduled_brief_manage_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service assets Scheduled Email Brief — Schedulable morning-brief email summarizing manage service assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_service_assets',
    "version": '2.0.0',
    "display_name": 'Manage service assets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage service assets for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '23c11e3b9485f363',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/manage-service-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-manage-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefManageServiceAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageServiceAssets'
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
    print(ScheduledBriefManageServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjyJblX6GjP2RVExliX+LZMxsk0L4iQIjKskgWZ9/EJqCm/vs4kiIys6vq9auxMRulZYSE3M/dz70O8duTWVd+Vjy9Ph2BmSIzM44DHxSImTrIJLtmRQR/ZZEF/yN2llZFYNVVVpRPz08OKO0iyKsgS4fttg+cOjatGCBJVqRB6n22igC4CEjMIEbKOknMIujhdSQxU9MDSAmKJrABYpYlqErEzQqk8gFSgDLP0jIYkLJrCop/IFBU4KXAQaoMKeoUcSBih8D1VwCiuHuB2oDWTPIYlE+vv/z6/BTA90+vvz3ZMQT/ph1wxoNKm5v84128cJMOEWIz9eDSvIMOSeHnHBRQpQRecqAVj08/lSB2n5H/+q/oahZe+fPrlxR5vL48Df9kqN5gRZWZZQU1ts3ctII4qLoXRIivZldCA6u6SEvEREroz9R7ue/8hpTlyD+H7366C3nxQPXTl6cMqmAO3v7y9PNg+5cn6Ar4/mVAyX/6+SXOrqD46edvOGVthcCuBjCo9cvb4/MDFi78tjRwb1L/CVHvcbXAl6fvjBted70HO+HOp5cwC9Kf7sB5kTUgNVMb/PTzX8HCCNhRHJTVv4X7yx3YB6YDbXoo/vPzzcm/IujDoA/Mvxabw7D+HUvg8ndxz8jDUX+FffP/f4OOgxSUHx7/U7g/24D+E/nlL237VxueEffLkwjioIHZAUvmFfnt7biXJr98cr5d/PTr7xD6f4Q5ZnVh3xDeYIkGLiirt7dfPpW3y59+/eVTncNcA2byVhfxn2H+mV9vcn7w4GPVTz/uhfLVNEphxSMfmY78luX/Ufz+gmhmHDjfrpevyPf1MrxQZDDiXejdBd/VTAl1/c6PPz/9DkkihdbU9u1rWOX/+Z/IJrCLrMzcCjnaWV0NXFMFCRiUV/ygRJRHUX89rhbr9UvifEXg1aHcIUWYdVwhs2IgO1gPQ8QHCzIX+fq/7BuTfrYfTDoq3+no7UaRb3dCfHsQ4tudEL++IIoPZWdF4AWpGSOysN8jcF1aDVJv+QFZ9XMzCIZKBXfikSeLgXRKCP8P5Ou/JentBvqSd4M5X1IYHzO4sS1I8qyArA3J1hz4yuoq8BkyLeSUIotjy7QjZPhR5y+Dj04+SB+es2EzAS2w6wogcWZD7d0AsvPzwO5Z3EB+HPxZRkEcI05QQGdlRXfrOtDnrwPY169fLbP0v6R3QiaRe7cpR3DBh8LI5895Adw48PzqSwpsP0M+/fb7J+R/I/9q1w18kLGH9j96DtRwedxtEVihdQKXlciQHpB+bhH87fd7NAbtYEdCYF0FbgBumyHat3QYLLiH6D0+0OZBRVA8JP3oN+TqQ78gQQW9BWu9fP6SDhAZXFpcgxK8O/G++e7694Df5QwxKR8+hHFyiyy5rb1l4hBMOyucF2ThIh+egubCuFZDRP2srGDy5iB1QGp3cKdZfQthmlVICeundLtnpC6hqQPyVwtCD85JIEmZ1VdkM9nDfpfF7+15WAR3Z2kwBP6RsffLEKT4BHNs/A7xgmwB9CaSm4WZ+4VZgts617xnBOxz7/shuImk4IoMzR0MMbpV9i3zNn86UXx0fUS6zSC35o98qQkMp5D/rwPLoLMwm8nSTFAkEZG2iny+J9gwZA323ucyODY8xAwV/zFKvLPOOx9/SeMABqXo/nFf6d5y6r7mznF1AZWRBfmGP1R3ccMNKpgZQ6iLYshm80v6TvzP0NkwLuXAYbCAo7st7wKHb9819WGVDp+/DQHIPemGYoDpjOS1FQc24gLg3DK/8ouhrh5xgGkChhqDhWD7P1iFQHSYAhAfgUoE0OPQuzfXbWF9DHG5JfvH8mAYraAWTm1DbWEBgRfkNOQzjECJWADOR8Ma6IVPNygkAdDHUMUPD5e+md+VGQbfh4LmEIssMSvwfQQeX8LcHDoMlPdReBDVdMwK+vIKgwDrqr1H9kPPR6ygsslQBLdNP4b7YSvyfYf6x1B8UMdvDQDO6rfs/eYcyNhFUt5ICLbdqITlnYCPPL338Zd7K773+g9dXv8w7f/09w4Et+aq/hi5V8Svqrx8HY3uDfC9/73YWTKCORLkoPzWC+/V9/lea58ftfb5Xms/gN999Yr8PQV/gHhk9iuCv2Av2PDVGgobUvfxgv6YfB6fP1PDt19SGXwL9CMbBm6DNW11Hy3mfQnsM14BvGHxveWUQ6e6wuZ4Y7pby/hIhkepQCJNvaE/ltl3JTzYNIT2HrkPRoZfpQPXO8N854Hh+BMP6pfg6TWt4/j5KTUT8G8eewbihSkLHTIcmGD5wJGpCsDt08f4NHz48bx3KyzICE72OtQXbHJw1H1GPqbWZ+T9HHE7naU1PEj9MkzMg0i4FP76WPtxmLTAEzy8VV0+KH8/HA2D2mOA/qMSQ1lBjW0wtPHso04HiX8AgW88DxR/BNnd3pjxgyzKyhxaI+zIjxJ/T9BnBIYPlh6sJpijNdzwRzFQTgEuNWzGzmDuN/99Myu72/L7zQ3V/YT529M7aQzv75PBPXUG7L81wg1+fW+9bwO6ecMYBq2bm29j6hs0MRha7HdfecO88HZPx6dXSDvg+WlwZhHA2bu/Hayf7ipBW74NuBABEsjnchgZRrCaIBJs5PlgRwTJ7zsBw+XAua0f3rz+9VT8r5jglXYsiqIpiqNNguJwwsUIEncdh2Y5QJomy5AY4bI8cGiCJmyWsnCCsuEPhrVxjGdZqMkgKDEfmozwIRbQhg+H/9+N6093ENhCCJqBKKbpAsYlLZZlMAunSIBjDGezhMMTNuZgjstZtkm5tEkxNGnxlkPTDI2RALgURts2GPAes+Jds7f3ufw9OndWeINkmgSD3oRp2lACTjk8azI2IDGLtAFO4A5LAozmSZfjAAX3f2x9RGgI4N34IYHhmDhYNsj57RHxISkZCq6cU+VCuL8mI14zrdPIkv01WsRo25LMgVRzFSuUaaovaHw+c/SFkIigt6dntSilqlue8K0tR/VMtXFxL8/5sUvE/LUvuVJXzxeFnwvUVvKshO6c1CB0g6aN1SGYYPrO6Gj1qOVa46xWUjU1NC2+RiatnxK1mBKqdVHEa11plxVJjvhCj0IK65bhMe5TE002Fq+tZ2nRq+YJ9W1uStdinYNkutXMQFsb11o+RZ0B1zZdpgYabpZ2jRuzeK7WahLak9J3V+RJs+y9zOyUHBvt+rwDTV9QstHxIHW5QxA7h9gIOHiKjY0pUSlmUhQOL53o+eJQnpmMcKnQNasJXmvHhJ4lZ3p9OlHurpzFvo+DsbDE1UqN12I02p1cXC23E+1SF6rYFdk6lEqTOCzaVlnTp2oZrVZb5oIR9SHYcIm2w0A/t/CKnbbrmrHcgF9xqpVupNFydi5ztROvDqVHjtFn8pHRj6eJoZdCZKqNMbLSFWV2SY33ucHS7fww39FLB5uME5+axcy0w6lzKozk09JIsGsa5it9MkoS57ph8FWsZk08WgdNW8vmtbMxrNvtmfP0nGy9ZKSooDrXtDktuaOqEZ253KNWaLYqiTaYcdG9vdjuU3kabR1lqU2NzhGIhmZihunWBlEDUeh2slZE646gqdEhaYlMXVsFDAJxtUqPBnTtp+tYZUPKX8VytQ7LM0ANVTPZrWxpS1OlwdKrgFTvBPeE7ROqUq6qim7rc9GmfcCo4kJX2NnUb/gzhU8kIWYvsxmVs8oUGyUlqaW7trgUkz4BvT+2EzcmzskG28xMaW2cAHFRNd3At7qmbV34X9d00ukjvOf0ecIrOrVeMmsUnfHcmAXuonZWUsPPR2Hg7AvKRyMdiBGj4TjlHpYZ11Sndlr5Eb7QYwPDF/nULtQLvqhni4xQxHNWRW1SlcdAOlfH1Dt2S6Mju5gVji2jqZf52Q4YbzU77AB9OSvTC9tP8Esyq311MjuIoQyTGZ95aqC6gREd55NN0M7adCNr4irLg26n7OzdMqB4NrVX66vjosRkQxABhqkRlfnSOljJIRZGi3BNnIprc3TmKb0hE2DmVWTHFb7rO0kV7Uss7hqN5UftyZzRlc0VEj2nNbR381URtCedosaTUD2e5cqIeA1r91Mp3O1NIQNVeB7bE5eJjZHfqrgCs0moR5twnotL+RIuV5P0crGvi3F8KqKzu2cndZo7WEJOFvnO2ivepeNCTbZCX7Frz+1X8bRk9ITfmqO+OPnrRDa0EyusVM60dpx5kFdbvTiVOzayCxebRLp1PKzHsriRyIMKfJpTjhEdMLoWmLVyXVToImYI5bhR96NkJ11Uc6mteX+bC4UhTyegImqaaPLMsU3GswviKurHoEoP9NnxTtu5aShAPNFekkvkLtmYNBGPV3F+MRyNWdXLSTuf1WjewSI47WhmtEpKnHEoGlWDtI8ldqrAIwzRrIzlWBx3SrEJ9uMdPcEbJmwV4tiDSC/2nl+LRE6NuLM7BtGcRwO/czGQFOODHIyr1LBNILLXNFWyXKHUqJW3M3WWLBYUbDSTyyzaxzunAaofRh1IcrCHzDExbHIRL3d6DfZkqW2S6rILHZJn0mWJYjY4OLWhCQIlzuNxqXeTdhJnh1Upx+edlI4Xx6iJzHy3qWrSszSHTFcHf3oUGth8i1Cx8dMyy6tMJvtmPzmf1ZhcFMV+Q6ginIgTdhN49RaMp85BLW17dyivJzIqE5qs5fn5ZHQmwLQ4JXuK3etVa8MmcjCZDa6EBZ/x+VImNHdWdSWfKvZk0jPbSS+HLEcc1gsrrcfkWV2ykbqPmobEz3s4LIw43m5ij+EAKiltQC1Orp7GBJUrQuBN9/iCvtJZuil2q+t00cT9Jd9Qou2OeWNDJYDoZHu8ahLKU8/rLV0y2WUyy+fxXlenXTxRTotmojLiNZ6K57NCjt34YHrXlb+t5qoyOyWiLTQgW6tKRflbbM/2Tm0uqNFOrFzfK7dLVN7g4mnCia0SKpfCnMbXTj85F4YFB9zIdJZues8UBEM26hK3mQ71sy26kSJlZW0sW9mcjfQcUq10NY97UnNW+xlvVnOSq/XtSVxCCC6cjiXmuCgIbS65GbW354ZiBZYv+kdjrRNug7EzIS7maylxYmMp2dVJz9WAKZZ5NKKO0hgefARNsQhs3ypHV0AxqWjlJSCSwFocNi6h8+BCjpelIgio4qJrc+SZirhIzfX4woaZP4opJZ0pKwefYhuVjAVJJ2bJNaG2tpeCldHNjs6SqBtxFDfY8rpKz7OtHsv4JSPOcLhIx2E2V4UscWG7x1A4+SVHzFcV7eztmsAq0QhsazTrNF/Ej+16ITnmRuJmdkLmluCGVaVL+0tUaE1vEqNk6vF4J1/i/CSM8MpKz6nkzOh51s7UPo2qA1OmTIgRi+aYbGZqPK92oURmnZpwiqYpQW1Kdlv2dCuMvZ7LjtHVL+xsnk3L1nKkYqyutguvc6aYMdUIeTE+FMCtZj5KbtLjvF0sj4elmjas4fIJ4amuk4qRWYNjLk6E5QLwM3wzhw2kvTDMemGumXQyJ0c9vdVH+UXwjqfqeNXwMWqECjOT52LTQ84jhdKx1nuS6S6KxbinTdZ6dIIVDcFixky+WiqRzbaNGdQYdxhvyqtgZzOv7/bk9Jzn1D5caCvlPI6YsxKs1jEDUmehbpfneLGyxxfCIHI8j9vauXLXNp6cePVyEUMmPvjcjqnHR13rcGYznh/yxdK+ZMyMty/6jHTVpS14u8PoUtNyuY0i8zhZXxLbXAp6vicmx8rexVK0A4deZUBJCQe8nMSHcH7svXS52LpoRF4WiX4ilYvEESsWCFSRRJzv7jbHdreM6XWHHc7yskpWRRT48YKWuchmpyTV+lKnSMvr5ZycIsoVKiZ0dtYxudJzXYn8qk+OUaIT7dSS9vgshvzho2PtjGb2dkcYOpquFtdsTFu7orxujhJvMsvlkbB2C3aFa33jOHy84aZoZgSBz20kZsxSnXXdWdcTxtGNSM0mjS6dDvmWYVxCLNATHJXm55GMJ0l6NUdLyWGXKVVITb0xtJmFTrzU0zVDwvFrghYUIclhGyleJs0c8rjBxL2xc6Yb3dakcmHn234Ps+Iw3rkOT+P9zMPZK185wrIrlpuRzByLtNbqXZvrzIERm3nuQM5aCempIDxYvWs4eCyFbROF66u2PbBcpuoiV+Wq0mNCrEl+2q1XKlrxPezUqFyFh51xwjKlWfHaJt4mXXkWWMmQ0OOqYHJMzJx9t4y6I8i2dNOsSt5KuShbemnspglecfFp6Uz1s7bS9svsSGORZ6w8OCn20h7t1XNCCQVOXqce51ByOMdo97A1BXIx0ldNmDdBatX8sjqqFBQJJkS/8g+6OyaVdaPwSkFOy1kly0D2NXQMj+aCNFprgQGHLY1xs646yAJNa4xmr+RoY+prS+7A/qivEk44qruZwJ5h5z1Nd9IGn0atXmyWsbiPKK6PVlidkibXqMe9OrMwQeTG3mXUCV6xDfOKN4SpvTpkl/PGQGu590X9NJ3OprRKe2lQrpVZ6KVTccJuN0SxLFKU4LEpJwGlDieUfehb30tD1dFCd5ttPHN8pJWQzgEjFmx2yHvjipqLja/TnGNtV3xetQ0cwslT6IHGrHQSbTGuttDCUVFCx/haEgtyNHXYgrbFqVuTy3I7bSwgOnYrB5maOwRNJ6GrdnXMYHDuPFAJ2i4Wuxmsx8Lmti1+Dnmcwk/0FjvZmXwyIyNijP1kbgYjlJREShbP41641ByZXm1aBA7ZSuK43uzQxt3U1kZjZ82lLncgD0fm+kCXzrwR2hGzWwONrbaWeCVEQqtoYqLF4mjnUaQUYzFZs52ecVzQ8/CFttroUHjXonBHuDKakRp/RpmcZnUcD71ixXOBsQJXfXOlx9h07hu9OBn3XgkMb0HazXSfTMzjeSPqJBeUy8QXsAVjc74YyPiYVnbS1qt3ByqO7DngSgyrSbug9LM3rnVg1ewpvNoCaPDokkxWHhuzgDPaPtyMU9hHhLZDxcbcnMl+KTVjasLXMyLxmoN71UXXcITy3MiAnKxb4MQV2Y1HyWhRK+hWm5wtZrLccwuAsqJ83RAnoZ2zl3U7pngpITZ8iM9RtOa0ZmShaz/01yvviGIhEMxLN+ZK1y9tkSRTel7Vi7o3QycbG60Unqd8a1hmy8dTwIqN1imqz+3zWQM2VOeQfT3F0Gt/Hi/dID/12H5aL3rbijb+OhwHir/gxSTRWOncnPZ0RxiMv1iIm0u7JykLcik8L8M+mFb8eNdPwMw+ycpVT5qFQNgWT56XnbS/Vn2ahrrtmmMOE8WTd24CXaO0M48Wu5GDjvp+I/SOyB/m5xKPqp6DQ2d5uB6mceVNlPEUZw1qNhXa8nTFZR8dlVNcP5KLo9tyuTs+qmtSaq5G3VYFYGfsVKjaiPRGSxY72vR6fK6m+64x+rgnUbUzFgWOAUrhdifQpQwR6sveZhnO4KlotbBHcrLYCSPBnrAUNet9b87Zs0V/WnsbpWj27CgCZ56eFeuy9+bz8Xkby9t+Qk7IrOdXkKtPNYOyrbPuFxv+xDSzBVU77Yp39cjr5VKYlGy+upKYrRvkOTkI+GlPlfycVs0mQuchlkZrw+HVHk1D0SYS8nolO8FMHffETD2Uq4gRllzXrYM3HMbYkNNNlzvngss2KYpd5rGg47MrPdpyE11nYydGJWbqV/aWdPt23I1qty79sE9Y+zBCu46vfGnLk920bJYmmk2mkOmzUJEkglol7aUofQ4f6bslpEwqlLFQI1vN9vhcpzBewCSpXakVp+9HOFZ000BLqnrv0Y6d0xFOLotGK8uQX3IL1Qv1y34y3ZdctgH+XB4J3nYqe6HQ49zRAG1vRmaSkL01PDMlR+ASszKFc3hQjrNjfNYPI7qgd6m9AKLPufC4Tfh7N99xsAyFxl4orWOOmw1lE4tL2nmk2l7GqZJkEt1xqxlBWiGWrQyyzE3RYBOR6jrRYjO291gKbYErLN1pKhe2w7jJgWg7WskBu9nbVELty4YBBdsLmCzYHFPb2ArOyvNpGBSoupgqoziPdzXqEPtyYrthc52vBEX0TachROm4hTUtSKxrlAvOXIpM2K3crUgRrTNnWTTfHRgrShgS1McVQ4bYnF5XnctYq4MgPD0/3Z7tPr3iGEPjz0/DI4HHjf2/fU/Y64P87QFHsgT//PT/7kbl/abh+8O/221+YDqvN+mvf1PTX5+fCjuAWt1vJZdx7T1uUP63m7Kf/627xQNEd39SPTytbKv3BySV6d3uaAepU5dV0b2VWVzf7mdDr9fl8Dcr5dvj0cLTzbwkrx63jr8zZ7jysKTK3h5/cfM0/GnJ8CQOOIFZgcdH7/Ek4PnJ6WAUA7t8Ixn6DRT5YPTjgdRwF3d4IvX0+/8B/TsiBZonAAA= -->
