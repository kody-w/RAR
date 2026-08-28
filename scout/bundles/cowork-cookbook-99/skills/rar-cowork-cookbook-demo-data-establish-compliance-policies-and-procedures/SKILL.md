---
name: "rar-cowork-cookbook-demo-data-establish-compliance-policies-and-procedures"
description: "Generates and creates realistic demo records for establish compliance policies and procedures in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_establish_compliance_policies_and_procedures", "rar_sha256": "93fc5828b3755da1a6680730ae27824f8b20cfa5945d1308bf0bcba142a9b41a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_establish_compliance_policies_and_procedures`. The original RAPP
agent is preserved byte-for-byte in `demo_data_establish_compliance_policies_and_procedures_agent.py` and in the RCI capsule.

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

Establish compliance policies and procedures Demo Data Generator — Generates and creates realistic demo records for establish compliance policies and procedures in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-establish-compliance-policies-and-procedures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_establish_compliance_policies_and_procedures_agent.py` and embedded as the fenced Python below (sha256 93fc5828b3755da1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_establish_compliance_policies_and_procedures_agent.py` first:

```bash
python3 demo_data_establish_compliance_policies_and_procedures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_establish_compliance_policies_and_procedures_agent.py   # or on stdin
python3 demo_data_establish_compliance_policies_and_procedures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish compliance policies and procedures Demo Data Generator — Generates and creates realistic demo records for establish compliance policies and procedures in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-establish-compliance-policies-and-procedures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_establish_compliance_policies_and_procedures',
    "version": '2.0.0',
    "display_name": 'Establish compliance policies and procedures Demo Data Generator',
    "description": 'Generates and creates realistic demo records for establish compliance policies and procedures in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-establish-compliance-policies-and-procedures',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-establish-compliance-policies-and-procedures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9805adacacd0a624',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/establish-compliance-policies-and-procedures'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-establish-compliance-policies-and-procedures', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataEstablishCompliancePoliciesAndProcedures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataEstablishCompliancePoliciesAndProcedures'
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
    print(DemoDataEstablishCompliancePoliciesAndProcedures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abeiWJruX/Ge/hCZRcRhkilq1VqNiiCDqCBTRq6TzCCjDCJm53+/G/WcyOys6nuruj+0seII7L3f4XnHvfHXF7fvkqp5+fqihW454908T5OwmbllMFtWQ9Vk4KvKPPB/5ldl16Re31VN+/L5JQhbv0nrLq1KsJwPy7Bxu7C9L/Wb8H4NvvK07VJ/FoRFBW79qgnaWVQ1s7DtXA8MJoBuUeepW/rhrK7y1E+fROqm8sOgb8BtWs7cWQseetV11oWlW3Z3Il3jpmVaxo/5aV51s9YHw01ata9AxvDqAtph+/L1p58/v6Tg+uXrry9+7rbg0csKyLRyO5d7F2X5IcnuKQhbBrsPMQDB3C1jsLIeAWoluK/DBshRgEdBGM2edz+0YR59nv3lL9ngNnH749dv5ez5+fYy/Tv05axLwllXuW0XArjc2vXSPO3G1xmbD+44Idf1TdlOagPQy/j1sfI7paqe/W0a++HB5DUOux++vVT1ZAVgkm8vP84AQN9emn66fp2o1D/8+JpXQ9j88ON3Om3vnUK/m4gBqV/fnvdPsmDi96lpdOf6N0D1YXwv/PbyO+Wmz0PuSU+w8uX1VKXlDw/CwJyXyXJ++MOP/4isn4R+NnnM/xfdnx6Ek9ANgE5PwX/8fAf55xn0VOiD5j9mWwOz/jOagOnv7D7PnkD9I9p3/P8T6TwtgVO/I/53yf29BdDfZj/9Q93+qwWfZ9E34O15egHe4eXh19mvb9qOW/70Kfj+8NPPvwHS/08yWtU3/p3CW+GWaQTi+O3tp0/t/fGnn3/61NfA10K3eOub/O/R/Hu43vn8AcHnrB/+uBbwP5ZZWQ3l7MPTZ79W9f9pfnudGSDXBN+ft19nv4+X6QPNJiXemT4g+F3MtEDW3+H448tvIGeUQJvevw+DKP+3f5spqd9UbRV1M82v+m4GDNylRTgJrycpyFXtPbabEODapgDY5zzg/5OFJ4mraPbLv/v39PrFf6ZXeMqQbwFIR28fqfHte2p8e0+NbyDVvX1Pjb+8znTArWrSOC3dfHZgd7tvpRuHIEMCSWowJWwuIMd4Yxd+Adnpy3QxJdRf/jWGb3far/X4yz3ppo9MdlhupizW9nn4OiFhJmH51NsHdSW8hn4P2OaVD2SMUpCSPwOE2iq/gCw4odZmaZ7PghSUCFBfxjttgOzXidgvv/ziuW3yrXykXXz2KDwtDCZ8iDP78gUoG+VpnHTfytBPqtmnX3/7NPuP2X+16k584rEDJeFpNyChqKnbGYjDvgDTpvID0rQb3O32629PyAEZUPJmwMppNJWsaTHw4ywM3vHXBPYLRpAzLwS4A8yLumq6qVql3etsE80+5AVMp6Ep2ydV24FiWYdlEJb+CKi6QJ0PJMupwgFnbaPx86xvwzvXX7ypDAIRC5AQ3O6XmbLcgdpS5eDPJOZ9ElhclSmA/8M7Hs8BkeZTO1u8k3idbSfPndVu49ZJ4z55RO7DLqCmvC8HxN1ZGQ7fyqmwhhNU9zB6wBNPDcFU+O8m/TLZfKr0IGcE7Tvv+Nk0BDP9Xgmbb2X7DBG3Ce/tAhBlnMV9Gkw++denS7VJ1efBHT8g6UTpaYXgaZW7D3L/TIcx9QKzqRmYPTuZqXj2GILOZ/8LW5tJPZbnDxzP6txqxm31g/2AfWrSJvM8+jrQUTyITSH2vct4z1HvqfpbmafAh5rxr4+Zd2M95zzSHxA1ALnlcKcPBAOwT3Tvjjw5ZtPcVftWvteEz0CrewIEtgRRD6JicsZ3htPou6QJCO3p/nt/8ARz0hw466zuAZj+LArDwHP9DEjVTMH4tA7w6nAKzCFJ/eQPWs0AdeA8gP4MCJGC8AJ14w7dtgJqAmijpiq+T08nowIpgh7YZga64PB1ZoJ4mnyqBUEMWqdpDkDh053UrAgBxkDED4TbxK0fwkyN81NAd7JFVQCn+b0FnoPfI+AuyyQ+oOpOWflbOUx5OgivD8t+yPm0FRC2mGL2vuiP5n7qOvt98frrt/Iu40dpAKkgn+r+78AB/tcUDw+dMlkLslERPh0IeMK9xL8+qvSjDfiQ5eufdgs//HMbinvdPf7Rcl9nSdfV7VcYftTK91L5CsIKBj6S1mF7L5tfJry+fITdl+9h9+U97L4AAb58D7s/cHuA93X2z0n8BxJPV/86Q1+RV2QaklMQrQCh5wcAtPyysL/Mp9Fv5SH8bvmne0y5OR9Bnf4oVO9TQLWKmzCeJj8KVzvVuwGU2HumBrb5Vn54xzN2QCEo46nKttXvYvpesYGtH6b8KChgqOwA72DqBeNw2jnlk/ht+PK17PP880vpFuG/tmOa6ghwaYDPtPUCFgDdVpeG97uPzmu6+eN+8h54IGME1dcp/j7Ppi758+yj4f08e9+C3Pd5ZQ/2YD9NzfbEEkwFXx9zPzarXvgCtoHdWE+6PPZVU4/37L3/LMQUdnefmXqD6iOOJ45/IgIu4jhs/kxEvV+4+TOZAOSmSp927ymgBXIGoG/6PAPWBKEJog0k0R4s+DMbwKcJzz0oqcGk7nf8vqtVPXT57Q5D99ic/vrynlSeNng2omA6iN4v7VRUYeC5gCG4f/gYGPsfalGfVEFyBM0QIMvgkU/QGO3hFEEELuqSJI1QOOKGGEVj84j2MMSPXIKZEwGKI7QXIZ7vuegccxlvjrqA3sN/J95FOkmKua5P+xQ6DxjKJf0QRzzcD1EMDSg8RAjAkabDOQDtY2kGMutT/Ye6E7Yf3fIE0xOFX188cg5mCvN2wz4+S5gxXMqmvG3iMRQZxecTTSNMPRYFJjeNeiOF/TjunQoplhruSjafVjmi27f2nEpINtLxIJCcgC93bRGGSM6YOzfT7WrdZYKLLUUitDL4dsIsP2G5Ct96o37SgxTR2jEb5WjLpb6YqZ0gLeuirNIElDOJvG4jwS12nI3mIm3o+bnWDMk3LzsY1qKdIme5fHXgYTU4hnrgmkarTVtpjDQ9WufI8ozeWS3nxbrFq1oidOlicomh1XgTqVZB0tfjkNq23JjXuZkg0EWvr1GpI0xUnmiLSBnfwudRyhh1crkOqZQKIOhRyTKx4Cyb2Kbm1yfB4G/wsht6jWwXhtoe8lxNiby38ExMCbSuq7pYs+U6OihX36oXdi8Y5zprvUq6eooUt712u1nuuB4ufhSLeql12rnbyidJt/g16gRN58r6wR/xrmioldAFSLA9ibwjqjtfvvGlo1zXUr0VPXFtactE1Jis7vylpxy3WB80QqRuxiWBi2LL7g0ksZjer09t4guEvV3kru4FDof11x1Rr2xo02m1IcmENyLnY2AS62Yl3vb4doBXnMwl7Roj3RPaLDB535epVlzMlSEyJ99LuDIiT9pIn/mjmhobd57qki32Aas2BJmT5O3mkH0YsOMRV2T0NpIEBe+LK9ZkstOEu8N59CyRN7Coc5I6Oe7sNsaU83ZJBwqBBmajoDxkpQsCQQMxrk0O2hgRNhiF3d4GxGcUyD5fSzglRVPrrVSSdb29XiXhSJ+S2iaSvNuEe8iFgxJB11B/lvorvc26uR3KVnJMY14Tl2u6USUFKhyprgtspcstX+i2uG0jCNGoFeS0RO/Dawi62DkkL8MUgVcLiFudhPGUOdpwutCrOXHdXmACgpKMP1zDM02FuyWHqcBZ5im27wNDcExdybNzZ5wNG1FNCce8lb1pquuJA1YiFUwsR1Xke6chtGBYFwzwuFO26YMFJBC7ZdQO60Voh91xzwxSGWPsiVQqt95gaauJ/QI/bPaS1yzW3WAMXK2NkuQCjObFKj1cdsTRSYLdaNCMi/iHkJKWG+vgYnLVEutjqKbLVc2X9oW3zgMOggvSVKcrz5G7rkv/0GJYdNUNkyol1RcukAVt6DlWyOVCHCNfxk2HEQ3fPI+wsBdjd+9p20bJz+olmW9a5+rthTN6Olsmd9nRwlo3dlrNaDmThRmP5TV7QDVnXBxaZdHsVZ8XtdK6QMN5FVUdsoSi+so5MBzKN0201qHKodptATt+1ZUuhtedRddopYWZaxjlFTKFWifwk6YvT4ZOmXysqYbFKIc1id6Ww3F+8zOLWd3maSES66xvOCKIYwcmM+vk5DWzh9WkORKHM7H20A2xkTTDNkVP9xqnhdYJcc1SOb/I7NZZcmWA1TWmcYugTtTMgMX18SCXeuH4LnbLFZaQI3Nclojrx84qdEJTTkQ3V1Y3FDM7scPs4grX6CI/izdLgGDVDRYVh2x4J3DKw1UI4kBgDjYBb5yLKaElYvsL+ggFvQvL67NvrXQhJRisVfKy3h/gvCuvg0es5qO+kvFjQo1mHLPxSjlt55iNcet+u4mk5YrZaeJR1zCnnENlv9AP103h6CcSLm7oyN26jZ0romoXp5t3S3hnLvC8soxxYu/VzAI+VnMHaxeJo/o6u9HygfOxZh23Xtex41IJYD7erKpOk/qOs88+t9E9Lj8Ias+xhLSRDK5Qg7qOT9ZB6Mxe0H0fyqR9f7Yts1gEWrsLPPUmGNFu3t445dY0lNiVDuRfrBrTtQVL2DdL7S/IcNa0U1YwW+/kUFxMcnyCkmg77HA0YXED3wGJ2H0ijN1IRxFL6KIuigIdX4SSKlj6eFnm9UDUxkUa5uJ8cWo1Ntt5DrW5Lc/LI4X65FlX2c3uFoW3rajUBIezh048y2tsJfPb8rjWS2Pwit2BZxk61/Vm4Rb1fFVLPo+ch8NxLclaoZzVs50gBxMMmrm+WLhMbxwuVE1LF8hg51IZ2MVKH+nGCUnrHJ9QdXOwUcPU/QPRXbco0S1psmzOZ3Q08I2boavkZjHHBSCVOFiX+ySovloHKVxzMj3F8CvFtjv75u2hoOMcn8BOB7/36FAz9TFK2vQ4H6XKFw1esHQUssgI1/BeUUB+gdZnPhPwc2PTPaHL57jUT9TJYOXwPHB7jMlZyzgW+4O1ONBHzerqqkiXqOBZ5NnwshzEPWvUjbtmgmph7FL1tOQNa2stIgFPKjY9UiTYdoj1stxv2lMYK3tuF5OF5IySHjhke9GvXJetE7/RK8MwS6xKnAFPinl+XPZsVlziCNmFly1WaEhy3EN2rFxSrYUU0D8mczQxxOv6KovcBVFDuvALs3bY6NZ1OrdLs+Z4GUmMKdYcg950Q162C4gKSTUxRSIYt4dU2ZTR1l1k+I4qO+WgJlvbr6WIw3Z6X4rakuvTrKIPKORKltbrwxjT1NAiHjmIarjxWp6+OuhRPh6PG8dZkDbUjrUzcMuGqRWrnmPzHna5euMjLEwGMBMHXryC676zDiNr7Jw9i/lCaZEsRRpYoJnXaMOHR5rZIrCOwtQ4tzFnXPV7MeowlOOuCGntwgxFLpypURCp9DkWnrYnGXHUmpG94Azr6z5FOG0b2ylEmkO+iNnW2PDXQfCX2x61pNFcwOl2n5kb213PydQY4d2NTFC+bbVOIhZFb/OxIBmYQ60GXM1E93o425IKnOGSWBy+zdLauuimaqNeb+ydLiIN7Wb2BQKz64IdEpVxraLdb0Vg9FEtkCMbN1lJJuyxx409p4ZOWWeEM0h5Y1z3CUsaq/Ol0MOq9wM5364HN2vxjTyKjKyVcLJSdrrmHz3XybgYO5Soqvap0B1vOTsucMW6pEvuJCztfnvgRj9frujNpffKzXkB5QMhGHqWt7eTdnKd9LqOOIng89shSaDF0YYqf6tijg6VEoVjnewkdtFJZ8bJOrOxeE/dNLJh3C4OxUiOLzYNu/IzYkVUBL2wiKmy6R0SHUQ0owA2snTkh4juKio6S1o6vwmu2ufIhvG4pQpnOmLpl940Dd6DNnETW4bDXddDZueqNNj5Hr3u59piWQa3FJrPZeFQ1WlTHXOxlAh/5QwJsriWMewqeM2lnqXcWLzRMQdtRzgmyHPZMa1yNIsKG00PrzWyqg8seq6wyzJiqXQPGg5FQEp5WGEapcQGaHpb46jX+724FmrFvOXLxvfbVr6scPe6io8tyc1vkb8U9aCrJXZx5R0lWvYQ1W2I2wqEIl1lZz1AD8W4YfB53xD7ONtFImbaBU4Sm3y+3eqXeh/XSnOyl4khrdI1cPlWBxM2ixrFr01Mh7kdw6QjVMohlrVLd5PnqYMSGHlZOsesWAiQ5fftsj02l3Zdr+H6XDNkevOszcaTBg2ikZ0Ts3BRjcrYkxS6RaiwrlgrrBnR9BGD5ddYh9BNjBhjfdlssiCJFWxVDUaoxyvRcBX0PCyv+5ujrnbE2Ik1Q21lVFigh3gbs2ZS5yZN+4KD0LdWtrl6oS6427wIvMVoQ422QUStueE8aZv8Togxic9721mbBxCn+TnlSR679FlLeM4l0jnqdNhZlItQ57jpKJJfZGCDJRh5FGzMwzo6L82lm5TonkNUKF51dmu1Rp9DwRWCGlpIEOuKwbhbjjfbCHsmzwI8GdgghLfyzReMQTEgwm/3iMm0Lk9eY3htyCaVX+FO3R4dQAgp2f1C3DH8PhactZ57JdOrIxv1pHvGnTqNMc70HdVVfYtIljFYCC8hZI/MFSppIpGkcSqveG59Ou2HoxDkNuhKAsIVo2MeEEGqMxJvEMqCD4agpVQ4PDZE5I4IHfDOhTAQK1uZhXDFBBUXLnZB4+aGEcpWgKH2soPYTsoLPmcMGF4LDGWGJEOVJYHuMVJiLnJwligDWXDb9UKIHUiGU28f+vxW71euEpGcniriIr9BZmGjm73pB73GJQSIc1EQiO08VllKLGnrQPvz8WLtGwJv+wUoqk5I8Ie5KqjwEjVO0nrPYMRFtRnikOaazuH7tmpjCjoZW3qMqLk/7Mq06TMbKWluwDFrD9JEa6HXhF6VjhUwSTQEY4mZ15wVmfK8DC7jngkQflU5bSvGu9vR0vWM4Ehyy4yMAKln2IAZG6aSNJHVdISG1Iy1dFwgELyck0JX7m4hZqfUtkGxeH3iDCY28XXRNRRm5VTLM9bWRW8xYaPkFeduAQ2fgkvGYcP+OOeDntGvdsrBHKFv9vPELv2UCUfOUK+8iNxgCVtmMhvrWasz0Hpe2/OcCBuRoJi9Xg3lpeSzPb12QJe0vaxrimbnS4/xfcKdU7cTNQhFbC+xVU4fxIuU6gJUCavrHAI5ex+5LGjO+mK4YH3h96slC7YEgzEX25N/AeVnVR7sFaeumZAujfUuSBJ9faNoRU9UsoWWuC1RORWV/TG9cV4oAxgO2k1BlHXVQUfZu9iwVx3FDDR2DpEIzLbt4h3K8L1uEjha4dR1c9wTUEKCHieCsF0b8su22m/hHcU58nrgHQa5LEC7AixNNnK3iwV5YW/zA4qM+BJvGMalpNIsyJ4iAum2URiTxPjNvA8GiRH0YU/ECLs4REg15OSOIQN+sWahQwopegW71dEX5gy0QQVMj0zFAh2i26NYzx3pjaxRDJrNoS054gHt3rZdDjuBRKE3C+av7EqVV7uAidRuT1cr/wZzLi/TCyya31bMiB+xgqqMehF1VEo1SOQvVJzcRelqN7RiAktQEnRzOUK4gxLb4TG04+LEHrGtEeCXIrouRkVqMM5VcxeiyGa+ukgwX1ZmFhcLLbukBATv1uH+qDdoN8qCXLE7H+2JLWjU0KTvdsWYrc7QodrXTJmzJ0ShdhXLV6TC2abTAylwVd6fjgjGeH6SHzGYwo4Xr9R1xpQGPpGMJFjB2S6DgmEBgu5KH1HG5XBCxItVxq6bZBnKzX5dn1bFdW1ADkoqZOYgYrFS2pJN6BqzGWmV9UQu76MdHZNqOwxhAIeREK1wGTku5KrDtXIJ3+pq1/pFTuLpdQWkCtB+T0RBS2i+v/K564WuRCs4b9ZeWEBcK+4vxqUICyTEqJKlb3U+7Has14iDK93WxN52vcrZmMuyHKOFBbbc5TE8BNcGlvpddQmZ66lVioHpAx0de8GGgQezdOS3uBSz7Mvnl+nY+nn4/N98Xz2d/f2PHUE+TgvfX1jdj55DN/h65/X1vyvoz59fGj8FYj6OZNu8j59Hlf/pQPbLv/byY6I5Pl4XT+/grt37KX/nxtNPpV7SMujbrhnf2irv7wfFn1+8vp1+pNG+PQ/EX+4AFPXjdP2pMLh2gyIt0+ll7ltXvT1OqMOX6YcU08ulMEi/38bPw2tAYAQ2Tv32DXRAb2FTTxA8X6lMp7vTO5WX3/4vBZl/D60mAAA= -->
