---
name: "rar-cowork-cookbook-demo-data-scrap-an-asset"
description: "Generates and creates realistic demo records for scrap an asset in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_scrap_an_asset", "rar_sha256": "13ebdae6702a16dc9c525108969694fcb437a3b0274d65f83e6aaff19f6cd873", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_scrap_an_asset_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-scrap-an-asset:14918e5d730080e7cfeaa2c472650031745dcfa21d14381689b8746c0a5f74e6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_scrap_an_asset`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_scrap_an_asset_agent.py` is
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

Scrap an asset Demo Data Generator — Generates and creates realistic demo records for scrap an asset in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-scrap-an-asset
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_scrap_an_asset_agent.py` and embedded as the fenced Python below (sha256 13ebdae6702a16dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_scrap_an_asset_agent.py` first:

```bash
python3 demo_data_scrap_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_scrap_an_asset_agent.py   # or on stdin
python3 demo_data_scrap_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap an asset Demo Data Generator — Generates and creates realistic demo records for scrap an asset in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-scrap-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_scrap_an_asset',
    "version": '2.0.0',
    "display_name": 'Scrap an asset Demo Data Generator',
    "description": 'Generates and creates realistic demo records for scrap an asset in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-scrap-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-scrap-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '81759bb7d868f0bc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/scrap-an-asset'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-scrap-an-asset', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataScrapAnAsset(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataScrapAnAsset'
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
    print(DemoDataScrapAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOi2LbvV+Hm/aO7L1UlM5gnTsRDRAUUFBXQrhNZzCDzPPTr7/42atZwu/uecyJuxDOjMhH2mtf6rbU39duL2dRBVr68vhxdM4XWZhyHgVtCZupAXNZlZQT+ZJEF/kF2ltZlaDV1VlYvH14ct7LLMK/DLAXkazd1S7N2qzupXbr3a/AnDqs6tCHHTTLw1c5Kp4K8rIQAsZmDxZBZVW4NheACqgCtlfVQ7aZmWt+X1aUZpmHq39nmYZzVgBI8LsOs+gS0cHszyWO3enn99R8fXkJw/fL624sdA65AqyWQujRr8zgJY1N2EgWIYjP1wdN8ALan4HvulkBWAm45rgc9v/1cubH3Afqv/4o6s/SrX14/p9Dz8/ll+lGbFKoDF6ozs6pdYLSZm1YYh/XwCWLjzhwm++umTKvJNOC61P/0oPzGKcuhv0/Pfn4I+eS79c+fX7J88iVw7OeXXyDghM8vZTNdf5q45D//8inOOrf8+ZdvfKrGurl2PTEDWn96e35/sgULvy0NvbvUvwOujxBa7ueX74ybPg+9JzsB5cunWxamPz8Y52XWTtGx3Z9/+Su2duDa0RT3f4nvrw/GgWs6wKan4r98uDv5HxD8NOgrz78Wm4Ow/juWgOXv4j5AT0f9Fe+7//8b6zhMQYq/e/xP2f0ZAfx36Ne/tO1/IvgAeZ9BRsdhC7LDit1X6Le3457nfv3J+Xbzp3/8Dlj/UzbHrCntO4e3xExDz63qt7dff6rut3/6x68/NTnINddM3poy/jOef+bXu5wfPPhc9fOPtED+OY3SrEuhr5kO/Zbl/1H+/gnSAGI43+5Xr9D39TJ9YGgy4l3owwXf1UwFdP3Oj7+8/A5wIQXWNPb9Majy//xPaBfaZVZlXg0d7aypIRDgOkzcSflTEFbQ6VnUX46SsN1+SpwvELg7lTuACLOJa2gNkCmGQD1MEZ8syDzoy/+x76D50X6C5mzCvTcHQNDbHfDezPTtDnhfPkGnAIjLytAPUzOGVHa/h0zfBbgHBN1TomqSj+0kC+gRPrBG5YQJZ6omdv8Gffkr5m93Pp/yYVL6cwqiAEAUMKndJM9KgJ3xAGAXoJI11O5HAKEAOcosji3TjqDpV5N/mjyhB2769I8NkNrtXbupXSjObKCwFwLY/QBCXGVxC1Bw8loVhXEMOSEAetAlhjtoA8++Tsy+fPlimVXwOX3ALg492kc1Awu+Kgx9/JiXrheHflB/Tl07yKCffvv9J+j/Qv8T1Z35JGMPzL/7aWo8kHhUZAjUYZOAZRU0JQEAmXucfvv9EYBJO9C4IFA9oRe6d2LA7VvQJwseUXkPCbB5UtEtn5J+9BvUBcAvUFgDb4GKrj58TicWGVhadmHlvjvxQfxw/XuMH3KmmFRPH4I4eWWW3Nfe820K5tRDP0GCB331FDAXxLWeIhpkVQ1SNHdTx03tAVCa9bcQplP7BFVSecMHqKmAqRPnL9bUZIFzEgBFZv0F2nF70NWyGPyaHHQXD6izNJwC/0zSx23ApPwJ5NjincUnSHaBN6HcBBkZlGbl3td55iMjQDd7pwfMTSh1O2jq2u4Uo3v93jPv+ON0MPVxaGrk0HPOmJpigyEoAf1/GTwmFdn1WuXX7IlfQrx8Ui+PfJqGpMm8x1wFZoEHs6k4vs0H71DyDrKf0zgEMSiHvz1WevcUeqx5AFdTgvxQWfXOfyrm8s43rEEiTJEtyyl5zc/pO5p/AFaBMFQTMIF6jabqz74KnJ6+axqAopy+f+vsT3dNloPshfLGioEjPdd17oleB+VURk//g6xwp5ICeW8HP1gFAe4g4oA/BJQIQXoCxL+7TgblMLn2nttfl4dT2IAWTmMDbUG9uJ8gfUpfkIIVZLlg6JnWAC/8dGcFJS7wMVDxq4erwMwfykyD61NBc4pFloC0+D4Cz4f+M3ucb3UGuJoTpn5OOxAEUEb9I7Jf9XzGCiibTDl/J/ox3E9boe/bzt+mWgM6foN4MGtPHfs754D8K5NHIoNeGlWgmhP3mUAgE+7N+dOjvz4a+FddXv8wrf/87w309455/jFyr1BQ13n1Ops9utp7U/tkZ8kM5EiYu9W9wX2c/PXxXlgfzfTjvbB+4Pdwzyv07+n0A4tnMr9C6CfkEzI92oagHoEPnh/gAu7j4vKRmJ5+TlX3W2yfCTChF0BUa/jaRN6XgE7il64/LX40lWrqRR1of3csuzeFr/F/VgeAytSfOmCVfVe1k01TNB/B+oq54FE6obkzzWm+O+1c4kn9yn15TZs4/vCSmon71zuWCU1BYgIfTNsbUCRg2qlD9/7t6+QzfflxV3YvH1D3TvY6VRHoXGBK/QB9HTg/QO9bgPteKm3AHujXadidRIKl4M/XtV+3fJb7ArZa9ZBP+j72NdOM9Zx9/6jEVDxAY9udenP2tRoniX9gAi583y3/yES5X5jxExKq2pz6HWizz0KugJ4OmIo+QCBioMBAzQAobADBH8UAOaVbNKDDOpO53/z3zazsYcvvdzfUj83hby/v0DBdP9r9I1vuG8d/MopNrnxvoW8TQ3Miuw9Md8/eh8o3YFU4tcrvHvlT3397JN3LK8AT98PL5L8yBC1uvO98Xx5aAPW/jaOAA0AGUJSg9c9AzQBOQK98Uj0CqPadgOl26NzXTxevfzrD/lmJv6LEHGVc0qFxBGEQl7Y91zQxm6AxikQQHKUJ0rE9E0MdlMAZlGLmFkMTlI2YpEcTLgWET3FLzKfwGTp5HKj91a3/8jz98qADHQAjKUCI4q7lmC5FI5iJUo49t0mMRBFmToEfwrMtAqdN3EIwmnAo0mNwlzJNz0PnHmU7DI1P/J6T3UOZt/cp+j0Gjwp/A1iYhJOqmGnajE2jhDOnTcp2ccTCbRcFxtO4i5Bz3GMYlwD0X0mfcZjC9LB3ykww1IGRqp3k/PaM65RtFAFWbohKYB8fbjbXTArfWnJgwSXlsdVtHtW9pDlb19CcC+2oSJqQUTI6tyttqPby0Bwj4WgKccjV0h51pcseOXpVBPf4suK20jLOG1oZEaK3hk7t7A3b4LNIKThWUHNHlA5VYA/rWrtqRHG7rveirq12c62M8muibRmm3u9HbSZdkqyI4m1/nY1SLaGIEIumRpV8LEXacRiGBhfQvR9ua2tFSkOhDfQYmto5d0x6XF2q2llfinKndsUFkVVqfyIZph1z2Gtv8UyqSK+1UkIO1BaNskjMXOFYhZSe10cNrVKzwOrj+hBcSFzdzXrtYogOxuaUFZnXW1RfrRwmwnPjFPpFEmtV1K52sVLddDV0rl4kx97NihXHFBxHbk+27Vn6sYmZXOfJMVNzTU/QPhLLdE1VBYLNV1kGOyZ2M+bG9ZQEGeVKa6ZQ2rMwwhXhd5hxLPT+JFEBPxwja+/ZJF9ccitwKOw4t3tiMbi6fmWrLONapqnQoIrtNUnIi5gyro64Q5VDS+f4mds7bqFJG+IaIuXZMcmVtZFGDpc7b7PZ8kG1Wg/WLS6XWHmuUs5M2rWliXLqWQtW8Mz2NOyyzREuzoKEBKfiIhRzvi5FKqUKfLxKjed01BnfLZExxGi6Paf9uky3+c3ZB0lvpeJKS6z2SiY7wrkpgh9idqOEcr0na1UrK5SHjWZBnklX9Gudb5TjvjyKo61bRLH21sbOI05970jZabSxIbicYF0Re24ZztHlVjnPA3+Y0WlZ0PFFQ7WApOVr51endiB349pchzK3qm57KeeSq1lluSwaZLxSsi1DXq8hCSfIdc6dyI6ExR7mAiYQ160sCwo582b2fhipq+edWpjrnPWKuo2FZ9IiuqpUa0hVR9tc9dMujopaK7QLoujbDbZdXoSU6G88LlLFXqdGYhuVxk5jcoUQSACuYj8IqaLOFnUa7KgLF7bVRi8EnVjhncZWGn+W9eiquiKPC3jGCysZzcL0whGcvpAScaMlyobvbFchcS7c3cp5N8t9bJnwqaoc+VBEDsOpD0VinB8SBtbbql9bCzJNcuu6ESz5svVuFF0fm/OOMg3YmHEYYuurFdzOkk6qdG0mxrZRFCM/tBfQT0ge1c/oZo3MeEUi6k42TG7DnYmlPe8YRz476xRtt0iA9HC50fPML/aXVXxbnXBNcXXkeNMqpB3mfrlmZpvDloJbXk1n8FyUhdjWCMLRpN1mHg8h4pRbN9G8dqMHEq9eNd3bBBFpWgpjHq9nLtd75FK01GbcaqW3OhQXMAJl/P7AwMKWs9TrtugVgyXWHpytCNwx2fNmbLnuoAQzrm0jzxa6mZRlKtYwxraZZSLZr4fOb63DwjpeC9ePNWy4ZF6+4pKDwSsIKiantWNTxy4KEFRoi/ki5UL7Gm/cK8FI/kk/MB66181akhsvUU85FjilmLZLuB0uzmK+GC761b6ejG5z3l8M2TNFa2W2powuqU3cIV6LuwGTbfqTxRLeZm8s/aMK9sIbHTPZJdYtbyLC1/NhL+RSGNtHkzBlere4rbNdpLqVVVU0z6LpFd5ure6M2acgPGeUGg8zN+B7NEm3W9GICybpaBU/LvhFwit2sGnOK2m2aDp8rrarcFfGM4EQ2bMnpFuti7WTU9dHWgj4rjuxyipX6z67yWaoSdaFP9r0pUv4RS4eBPQ0yit2fTJ3jJQTKH2K68VxgY3VMLJmo/dmamIE019TMSbUxHU8zwhpgPLkKREX3G7QGqXC5kwa6+qZKXBx1K/7Llv5WbTfJ20aLPtr5zjzkeaIy1lQmVkbjqcZYfYkHKf4jII9UU33ActcGm4VoyTpNNKhEy+LZX1EIsm6jtIYhgt1S9pUcZJZzOi8/aiIRR3xBnusyUbQTM5Zy6m2OqUaQXM79SKgNjIey8DJ8mxzlc5K46crdi5lWE6LYeHzXm9ezmcmDGGKxyKz3bCtmM72J20bY3NMrsLZwmpUIrwWxAa3A2LVyyhZcwh1LGsTWWutYEboMhhVYrdXerwSsHmcp2sV9618ZDf6ZSSrzO9vwWxUbMojm2xcYGTljNrGs0I/MiS+mneiSmk5QMU9RWT7ZExh5jwXb6EnauNK8GsDvV7TGBevsrlBWU+uIlGQSGN+W9LnQ3w47tkIOY24mhdYwrkbDiEYx4y1WiL8xM+kiLQvCCxxOseeZVM2PG0xwngsD1cmP2/js3yyeenQHjSc2/gXkacYXkwqBjvV5JE3l4eCIwbJ0K5oIWAXebyG4tAdDvy5Z1j4YNV1gw66vw3VkVvEBOi9WZigyHLFKJkiNML1kAwnkh6uw6WJ+cVMwdDdAZaO9RHelBZ26cvxLMvnSuo2dE1n1OoSO7gwXwtd6DBotlaiOeN2PUvxaDBEOXO8zBXKjgXhSEnHsufP5CWv1/h+qSyblhsX9Co52sgRv8hkqJqFLmQ5S+4W2I0apThlD1IzRL1j3ayQnmdDFIwHFs3jGe0PSJbixxpLbpFf2APLhkSrtMOiwqwdldThIN1WecTMd8jsVM+IU96Oe17Dlwa/0aPRCweecOJydzTh7W3rXOBKR4+Wd8L6mN4ZAhWDTu9iWHIQG3HN8ku31lFSEFk+zFlMYg2yoDWp0aJqOefNQKgOKCKp801MzXYjFZbryj86ZsZFpsHkGhnHiurTKlpy6/xcUFvfZFfCxUGxRazkK4vET40IchhkmU7HZwIt8eXi7C6iPVE2ugxAJ0wMlroERbUxVjIS2pWtJIlQ+f1+lNHBF5XooFhsFQtxLwsBAAdxdtYVNx4SOo+ROCEX7mkvmvrMFqyAMk9haam7fbRqdlg506qDISVgGr7seo6Y3YTjzhZDAj3r64GX/f1uVuz025narMBGeHdKTixmGoFo8arDprdrGigr47ITTkoznE9uupcO2VIoubjqqpOOGm7FHUuNTncpr0UFNceqGo538ArJrvnal0EiqSMxlD26XWpOeUsCMcSx+bnRwazC4nOrXw5FTm3CXR0RlHGw0Z0t0LC2V2sJJhFSubbEeeGKthYdbSN0wvMlZUNkKdxskfVPzbzzdjP0JiDnXhuLYzRGdrOqCJZaJLfMq3kDCRdimVxjC81nIHWuXgdm4xMG42tze0QEhMW8I4Yu9HixFfXa5eescUnXB9bCBUz3x52Pkedc2dSmm3nHTN1LwhyU1znTrDKNFw7hWrpgh3V8SJUr7V8lS463B3fNj2JRafjMyDaK6UZcHEf10VLC3brDm1ksOxK/u9HkuhujgXHzXbsQQ2cOGrYYny0W9OQDcylyWvZNmk/Zet3ACGhPe263hxOV4iphkZW4PcBC4oDtddklmij66izGtyVbrkRt3tRsPa81uUU00iQXiysmaXgSkDt2w7QxGWmGccmbVEZqgaMPs+KUyqvDAnRZZy8RsmwX1sCJm8tlKfvUbmVEBEugGmhWFVudd9jJH2G7PJqeOx7nauecL8sLu8rEq9au0gUWSYOzOHGxIA4CGDXH8rA7pehFXfuJ5roZdpKGnkD4/oC0440thoIkEQIRjG3aqTZZeHx6pqmoKEpSXvBLtTRcsMPnjX1s7EDRXa6b+jiPFNhbxlZsBEajwcteMI11RngF46BKrdNNuSoW0RwPugN6nqH0dJLc7bSBtLsdqsu+tabI22alCnurHj2HU850EknjbTn6XQKPe19L1DWpk3v6lrObslnnNWZ6u77jPDi9RnSvhKsinMHTeK4uz8GYSAWDtx2mr+GiGVp4ufWdVoFzBqEInPTO2oWdHy0YF4LxQu0p9ubhjmaX+JnCVgFDV6U1tmy5Xc+l/c3mXMxwx3rRtP2w3PcGTsPcCfa1INb1dpZuYCmNmdSlSNIz5nB4pKX5jbNM10ejwyAjq31IUqv9IVY9u2KPTemKe2oRHi+7pWhhqs73JWueHcUVbrnaL8iTQsh+oxxmq8jeuEyFIA1ul3R6qRaF4V4bZ6kSDSur5qCdFPnoDFjrnglajQN1FKjTbtf61rEhHAbmSvbYtXTQJumMmK8Vil6K+eomr7dud4C3dNtK8Knd9tQgC1epktlTLeubUmEwe7mIfEZjTI4ynVQI9WBW6wSNoXhSz0oPtm1buJ7XRn92uyV/VPfGjfIMlqlFzMLH3eniuA3aEZcQzmCMyMZqpqPzGUAbKmiMZsdtsdlZISirMSq3ZuoNxpk+u5yPBewtDmkXlbm54Dc2wQO0NlqH5C+tCrh7cg8gBMyb3WyLeMdbEy7BeGOUoa4OEQsrV7kfyfN6kXCYf7rh1aaPUmJ2XY89v99gB09hO61cW11iNatVavTGHi8RxnaC9Tbba6wTjtcjhs/QwVWXC1ZfY+yK4SWj6jpbWiyzOii2S3h2UYuibg5BeyM1ZpUfUns/40qzNok5jmJiYAXbVsRORlaQib0KkcNMmqf4GgykOU+cjG0268o+0mGYp7DSEHGbouwrTPCKYOMHkO/LGr8tkP1tqSGExKRypqwGmKtcBped3hjRZO+0B+7Mddb2VhZJs8IPFCnjmkvukDl+pbVCvZgBfmC0ztmeT5SC+/5p0bJcSGRLbzZnC0IZ+dDfC/1st8lmkq/Zace4ERzSYlssLPTA7E9X2uA2Lr/IHBhe2ntufrWqdlS8umqJMsHdxpxTuxBZMY3i0UfCNRczVQ9keM3whk7fHAmWKV6vDzLu0n3RkXgw0/mEjJ2282akYVtdsWZKmMeMqPUuPTuoNaHmIWsysnpBHYyDdQbdCEPh2WpGXQu6D1sfRkrmovsmx11WBZgnNjhFaP1STW8GvibsZhfBo04nKB4OIHomPJeUpgxWQZgiLqLsDzcf9jvXzw7X8KrD293+QNfDSj1ZfT1gzsnyWuvohI68782S1Vf5Wkbxxp6fRJrbdIy96a0zShj4sLztNh0rGhzPGJgvju5SCaUSQMpwQdkxH8/c5Qqvllcr6qmzLC1LxfB1h17YV2uBwIRbdXt41pyTDpTQyU8bCbFG4WSSzgJp58mqYXRiW7WDW3oDn4H5iaxtMjuDrZC7VVYbpjiYN1g8KY5TzWpPYMmZsfWVM4srWoDMM+EoIBi+6U7VnEVsWKiUwttlTETfrPFsb6xhrxwoa7um4pQOGCWg5wsSHiVLiiSWZV8+vNzfrr68oqAPEB9epiP758H7v3KA649h/vbkgFNz6sPL/9554+Ps7/0V3P0Y3jWd17v013+u3D8+vJR2OClyP+qt4sZ/Hi3+txPUj391mjtRDY+XwNObwb5+fzNRm/79kDlMnaaqy+GtyuLmfsQM3NlU03/6qN6eB/wvdyOS/PG24Kk0uDbt+3n7Ww3uhFWeVe7L9L8ypvddrhOa9ftX/3kSD6gHEBgwo77hFPnmlvlk4fMd0HTYOr0Eevn9/wH2vVnOwCYAAA== -->
