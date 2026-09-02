---
name: "rar-cowork-cookbook-configure-manage-project-quality"
description: "Applies a bulk configuration change to manage project quality from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_project_quality", "rar_sha256": "1d6f3f9c00d76744889494a1f80bd56aba81f67aa4e8766873e4d604cefddaf1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_manage_project_quality_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-manage-project-quality:3b92c43de9e10c06ae5d7762a0e546f5ed9b283b6d2ed0c827c5445cf273c6e2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_manage_project_quality`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_manage_project_quality_agent.py` is
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

Manage project quality Configuration Bulk Setup — Applies a bulk configuration change to manage project quality from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-project-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_project_quality_agent.py` and embedded as the fenced Python below (sha256 1d6f3f9c00d76744…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_project_quality_agent.py` first:

```bash
python3 configure_manage_project_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_project_quality_agent.py   # or on stdin
python3 configure_manage_project_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project quality Configuration Bulk Setup — Applies a bulk configuration change to manage project quality from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-project-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_project_quality',
    "version": '2.0.0',
    "display_name": 'Manage project quality Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage project quality from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-project-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-project-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc59b91fe812ac6b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/manage-project-quality'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-manage-project-quality', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageProjectQuality(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageProjectQuality'
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
    print(ConfigureManageProjectQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaeZOi2Jb/KkzOH9U9ZqUge754EYOIyKKCICJdHVksF0HZFwV7+rvPRc2sqnnd815HTMRYkZkC9579/M45l/rtyW2bKK+eXp8M4GaI6CZJHIEKcbMA4fNLXp3gn/zkwR/Ez7Omir22yav66fkpALVfxUUT5xnczhVFEoMacRGvTW5rw/jQVu7wGPEjNzsApMmR1M1c+K2o8iPwG6Rs3SRueiSs8hTyROKsaBtE6HyQIGGcgGfkEjcRcoargjupQbAqTxLP9U9I3RZFXjUvUBrQuWmRgPrp9Zdfn59i+P3p9bcnP3FreOuJf4gDljf+2p29fucOdydQPris6KExMnhdgCrMqxTeCkCIPK5+qkESPiP/8R+ni1sd6p9fv2TI4/Plafi3aTOkiQY93boBAeK7hevFA4sXhEsubl8jFWjaKhvMVENbZoeX+85vlPIC+fvw7Kc7k5cDaH768pRDEW76f3n6GckryK9qh+8vA5Xip59fkvwCqp9+/kanbr2bhSExKPXL2+P6QRYu/LY0Dm9c/w6p3n3qgS9P3yk3fO5yD3rCnU8vxzzOfroThq48g8zNfPDTz39G1o+Af0riuvmX6P5yJxwBN4A6PQT/+flm5F+R0UOhD5p/zraAbv0rmsDl7+yekYeh/oz2zf7/g3QSZzAD3i3+h+T+aMPo78gvf6rb/7bhGQm/PM1AEp9hdHgJeEV+ezM0gf/lU/Dt5qdff4ek/ykZI28r/0bhDeZoHIK6eXv75VN9u/3p118+tQWMNeCmb22V/BHNP7Lrjc8PFnys+unHvZD/Njtl+SVDPiId+S0v/q36/QWxhuT/dr9+Rb7Pl+EzQgYl3pneTfBdztRQ1u/s+PPT7xAgMqhN698ewyz/939HlrFf5XUeNojh5xCEoIObOAWD8GYU14j5SOqvhiKp6ksafEXg3SHdIUS4bdIgYuXGyTu0DRrkIfL1P/0bin72Hyg6fkdG8HbHwrfHhrcHFn59QcwIss2r+BBnboJsOE1D4MKsGRjeQqNu08/ngSeUJ75jzoaXBryp2wT8Dfn6z5i83ei9FP2gxJcMesWFrgqQBqQQUN0qTnrEvYF534DPEFshknyg7vCrLV4Gy+wikD3s5UP4Bh3w2wYgSe67dwCvn6HL6zw5Q1QcrFif4iRBgriCwuRVf4fzNnsdiH39+tVz6+hLdodhHLnXl3oMF3wIjHz+XFQgTOJD1HzJgB/lyKfffv+E/Bfyv+26ER94aLAe3OwFQzlBZGO9QmBetilcViNDUEDQufntt9/vjhiky2BBhNkUh0OBawbnfBcEgwZ377y7Buo8iAiqB6cf7YZcImgXJG6gtWCG189fsoFEDpdWl7gG70a8b76b/t3Xdz6DT+qHDZNH7RzW3uJvcKafV8ELIoXIh6WgukOhHDwa5XUDQ7YAWQAyv4c73eabC7O8QWqYNXXYPyNtDVUdKH/1IOnBOCmEJrf5iix5DVa5PBlKevWoenB3nsWD4x/Ber8NiVSfYIxN30m8ICsArYkUbuUWUeXW4LYudO8RAavb+35I3EUycEGGcg4GH93y+RZ5yz9uJPgf+o7p0IoYEHIK5Es7QTEC+X9tUwa5OVHcCCJnCjNEWJmb/T3IhtZq0Pnejd1YQTvcMuZbE/GON+9I/CVLYuiYqv/bfWV4i6v7mju6QQAIIH5sbvSHDK9udOMGRsfg7qq62eJL9g75z9Aw0Df1oAJM4tMACfkHw+Hpu6QRzNTh+lv5R+6BN6gOQxopWi+JfSQEILgZoYmqIbcefoChAoY8g8ngRz9ohUDqMAwgfQQKEcOYhWXhZroVzBHYMt298LE8HpoqKEXQ+lBamETgBdkNMQ3jskY8ADujYQ20wqcbKSQF0MZQxA8L15Fb3IUZ2t2HgO7gizx1G/C9Bx4PYXwOtQXy+0g+SNWFvoe2vEAnwNzq7p79kPPhKyhsOiTCbdOP7n7oinxfm/42JCCU8Rv+ww59KOvfGQeidpXWt5CDBfdUwxRPwSOAYCTcKvjLvQjfq/yHLK//0OP/9NfGgFtZ3f7ouVckapqifh2P76XvvfK9+Hk6hjESF6D+VgU/31Pt8yPVPj9S7Qe6dzO9In9Nth9IPIL6FcFe0Bd0eKTGPhii9vGBpuA/T/efieHpl2wDvvn4EQgDtEG49fqPCvO+BJaZQwUOw+J7xamHQnWBtfEGdLeK8REHjyy5Yw0sFXX+XfYOOg1evTvtA5Dho2yA+mBo6g5gmHeSQfwaPL1mbZI8P2VuCv6FOWfAXBip0BjDdARtDnukJga3q49+abj4cbi75RMEgiB/HdIK1jfY2z4jH23qM/I+ONxGsayFk9MvQ4s8sIRL4Z+PtR+Towee4KTW9MUg+H0aGjqzR8f8j0IM2QQl9sFQwfOP9Bw4/gMR+OVwANU/ElnfvrjJAyPqxh2qIizGj8yuoZxBOyA6dB3MOJhEMECh/f6ADeRTgbKFdTgY1P1mv29q5Xddfr+ZobmPlL89vWPF8P3eFNzDBm74lxu3waTvBfdtIOwO22/t1c3Ct5b0DWoXD4X1u0eHoUt4u0fh0ysEGvD8NNixiiGD622AfrpLA9X41sxCChAyPtdDozCGSQQpwfJdDCqcINx9x2C4HQe39cOX1z/vgP8k919xj534BB4AFmCoj1IuIAOapiYuCkiCCkkQsN6EwT0qmIAA9ZkJ7ZMEQfrhhMZ9CkygEIMfU/chxBgbPADF/zDzX+7Kn+77YamYkBQkgAVUiIesj6IBTdEEwTAswRIuFjKoF5CU67kMFlK06xKAoSmKoXFABBRK+CAMAjfEBnqP9uAu1Nt7D/7ukzsEvEHQTONB5Inr+oxPY0TA0i7lAxz1cB9gEyyAtFGSxUOGAQTc/7H14ZfBbXe9h4iFLSFsyM4Dn98efh6ikCLgygVRS9z9w49Zy/V2Y28TqaMqGXUdTun4ttie6Hpnjay+XC+pVp+u0mp1tTqjvfC0nHg61u12ZDHFreWKC1FrvLdxVbvyZLjhk/WJ0SJ0yTcOoGt63TPacbUVOOM4vyq20u8U9Nznp1PFWMtmaWFN556VxG52SaWacudAfp1kl2WuMkF9PhOlmdcxWp8UJZ26xiIoTqq9vFTSdb8QXVZdYmI/v+Zn5VD54T7dOsmeOnWrTpq0WCu5lpIc5XC1TXhP3ReJz1u1HRlp5c90CoRePV5fnR6014oxnZ4NM5ywY9YqN3PZVpR+AWEUU7Q63uZJUSmd7PTz45UI44rL5sFEKbb+UVMCqJh/PkuCI+1n+kmiSqM0yJ3CkKurE7NYdSrSkmp0TRlzLd85gqH5ljGyKsPR+2pbqvs0TIGutJQok8fI9cDGN+g2PVMicElb1eZibEmnYktXE345rtartbzjS4s5T6qVGZ8qbeyTQrkvvMihJgbrd8z02u52gKulnD8zbZ1GdeGLLNPY5tlvljvSVYo+xA7ZyVYaIwKq17idsAPBruPz6wo1ZhQxck7BIadm+6DZl5iLnQhj25GdK8toNXZ6ocKaLVEpFzsh7KyMeL64bGkeW8goR+FZaVdHdZUpJIHOJDPQz6amVlnGzryFl+pN2RCsqE4bf4YVKTUBzlFc7M14HW9bW6wzNllXo36fopP+XKuqOC6XyUJPI84eq4LlSBRBKC0Qs6VFXNkuUBaHvmYvkeSN0vVaj7gOUFFUKgDtgEZWGOZca5cqLzWZ1YSOyxkZpvJxNZtSET+xMnMfF6XelqU+uv1oSZvlXkJoTEYt1MvsyuxmzEq7bKmOqTar+aytxro+ydA+DM1wxHeBSFLxtfJcViateuMR1spIsG3QuPpmoWBKs1Nifjk5cRNVDS/7/hpvmxlbVmB0vICtuSbmDjjNFQwG1zo5T7ssaZVU7JK5T6wb69AQ0oqjDGK70TFik8yJSiQWgZBwRVsTVji1OSNRpbyIr9rsuIexwYyTTTrHxsru2tN6Z4pg2U9PR6Z2pfNsIWb53JbGc8KQijorQ3deZP6mRqc0mfK7q6e4gR8yNrvqc2x5PQdSpoXXc+qMZcvftf14YXA+NhY5b+doVrAmCal2Os8Rp5Wxm8vjaHUdT7stZqKluVND5pKW+mWjXi2Tkq+xXW7dcRMyZ1ty8+PYVI0+FrozOwo1TUq2O4LY2cphwfbFBk5uwdnsW8yayFvXt/DNaNNS1TXjXZsqAzepi4VSjRIqZl0h2qqg75b7Y0EsbFKqrqlcBECNpTF/WhCJ7Tmo1OmjUSwYxSaNthoz3S5F1knkadswM1JZVMJy70qMf5kQ0k6fxAnlbEJpLQrUxj6crAnXBMAhuspeb+sydt3UVpZ6Gx8PnOT1qtL6c8+ZHUeg7a1i1V6D+WKd7ZRJntaMSQZCv5yR14TbOb4jBJRpaq0nnjFhVcKcLEx6ObpOr4AZMWM/ZSStBpfspBuj6XI+F5XgROGmKY+WHMUEUzX0D4bi5mdTaFPxGm4NRS5nspepC1e1ABcUVBj3ts9HOFfLvZNkeNaNF7bEKIcCta5i0Xtak60IEeW3h6Ce1bLu2doqS6Q4JY9Lb+edlgehNZaMPBM7gHpu0va0P1tcMIoTimJnicryFHmxkU6iheKjuaXOwNS4ZPZ1NV9Oitn0TB+q49E+iztiLi88baMuVLsvQTsB6Xq7CzqnlRzctidsqJk16dsOoxvKstgfvabViEvFuMeTSK6964ZacCg5T0gCY9eiNm+zqkrDPQ423KKQ0gxHN+F4fihDmiKU+VLLR2wOY1B3mhoAAOc5lG/1hCp4XlwJbOJEu8RQMZ8qYdqps+vY7l3DMvddK8TGbGurl7lVe0qhXOVyIyva2fBjw9Amq7mIlTZQsFmbYOvGWPM2Wc6MtE6XJX/Cl5boladxGW9QgBHXmTPjRduzx+2hJHXSkX2hTlC2cAhbnTr9fhTL54lGEsuYYEHl+fMpSu7iVS6pOxdn0RN/Cnq4RZ3rqYcbu+3ebjs0q2XVOaopF88WW+G8Ylsrpy1TV87eJTBQb1bNL7m2VebGfD5SStKUtRk7qkZePEN3Aaw6kbhMlfnx3BELdLFJt+0kPjLHykiCguG4daVkjsHJnJQq5kji0/o8329Cu7LxgzU5kuhYxq6ddKnxKsbMBJed1W6BC6HfcIsttNlusatkhcsZns7LrK1MayWIdct5pwIrrR1aXATKlIsjvViFhSKtev9URJaPgYKxV7PYYM1zXR77NFfsGd+viKnDGcxsJp0zqVhhWXlhNdQo9VCoA87dhvOFVZpOjMV8n3qRdJpRs3jH5KG+Yurr3lkYQpNfaS22BPkAm2RpT1nVNML7SF0JdFqdr0vM4rJTw67Ela+3O/uco+tSFQJGNd1NutOz/EzaVryNJFokUDFfFJnmU+06d+Mp6QpZMfPnOpNv/YwVjZMw7eayRR16H91OWj6blvah4q8byRQyh4jaC31d5VTixvHRuCzmm0DcWE1uTA/CPvUClKTTY7EgRWEjCbsDTjcqvZ9T+MIe5aR4zU7lYaTLJzwIGIpzgjhPLkv0kvVXlDbZtX0+y1MjnM7XJ4HmKJRWKTyytbpZ96ad+MCjF1jft6ZX+viSdmJS1MvzjsYnmTttInTEVSZRR03H8/lB4BbLabWcZwd5X2wuWpMHkrmXm3KVRYpaEIHtKHiQ7JOcB6YlN90hXTJcummjbhxVvLCKCwtdWFiZTonVmJwa2o5pGLLA/TLp03i9VRN9310v8/VhwecaXbU7bJofTkZ0CLQCVSzumGqpKBqor8iXgHXacis6l8P0uJ8fCoFW5XWWHkfFiojkOVujocE7SdBwbNIZI67NRH6fCbvRyXH59Sbmj6usmO9gsxMXEsnn6mVj0KfVcoQd2FxEI16XNlaaWAvVIP1j5aD6hOyiLbs2iT5qyd2G3vTRKHLJSC9AUMcVq22tiJOVSbAIon15VlzYJrF6gWFiIjRnucQ7D0jXpVWiEmZu1s6MVUiSP1+xinOwpdOIGsBqW7JMx+kJqgyr3bI8LXT2Wrnr9XiHHvfjixFCztp+tWL8nsGWjbwe9VI6K7SpuDgd2HWk5mmHitxaTWZKVOa025+UtdvbhKIbBG4evFrglgGDCqohXcra2TntbkEaJbUcReSkyppru1zEw8GfQoVGuplbgsFPSwvOwsLIbGVBg1dUQvtTM144CZ9TYH4u42AdC0Qen4BMGkeLbMFeszddvY/wy2TOh2RWaqfivN2ulBNxlOZM5y2v2VYLBExJTFmmthMg0OdjPR/LCr+teu149Pq1Pj1mejdZGhDztvs2kC8il8+VhOiSDeZx2EkpF97q0AtMd1z3OTdKqws/QiW9ZimF4IMJuZ40vKwnZbTA7WXZ8L4/n8Hh/1jhXjnzeHmj95sowYhilE05bXq91n3tLuLclbxqLwlhKhwmm8PSyZTx5go0w1ZSxtgm9XLeX5Y7vu6XkiOpdOwt0fi0HOnH49qs+msQHEfUhsNMh9a5ucRPduNE5LPQJgEhlnMZIsiBJCaBl6AdsxOsvE7MtAb5pV7u11Nm5++KIrPkacDuLqnlF6s6IUhZa7TpxNDapir5yV6fcqhpMcvMC62qS2bBVJzrnLAE1BStrzTW4zxs5PA2EYkxsMr5ORgV+PKC1estO0ku/vUc0gJjy7hvLvzW1ERxcq0rHcf9nbPlBZde4l2BUSmHZjOzXqSz3iTmMwnbl8G1pjxHRXeaPa6sxYndkgdfOm6Py2xGEvpkaY8njM4KW9x1an/erUaMTclnqprMOLLnW8IYywzFTnd8uMV8kz1GrCvBwXg1C7gNTvfWWEFpbHdBV0c280AAq+RhfM3Xq67z24BuGZLSNHU/VoMwZATtMnfFLPDGo31IUPsd2tDFAp/7OCU3tUrrcj8nIowSsPUhhwAOwZcLbXYpYLvzRda2ujGbc1RAoJLXHZt+Jmi6TQhJHZzwmCNmdQq6YNFdjy4bzM4Z6B0xL3EVVybr6YHF/cZy+40uQkn6E0wRYtyph+pkCeneGXPYfCS7GwZsD1tj3KYJcRjb9UVb+M5Krgm3H7eEFjO0S5xP8nhyFnATzm5ToxupPbONaK+e2dOyv+ykkTUFG80m6l10blyCXmN42oyrcOIHvuRsxSMLO4Rp2UkLtBvNu4sWgDAHkzLGVasapkspNrm2VSVPxJvKu+4tqjy66PUw2mMUhovbdhx0Bd7z+4vcM/M1Djqi7vgw9qOT5O9rr3YWeeQWWb2JWSdsqyL1hQMsNFdhHEZA2aGymZW9DxscgfaPl2NsaGc+77BTUAkHlpr7m9VoOfJRxvMqmg/X3MWqRO8SN+u5o4XUaHw2zegyni0XelhytJCe5u25G6dMzPMc09Wcrsup5u04rl4s416sarVnL+uy3JEzba0WKrE2I2W/GcMpauUt2Qk2USIvWp1lyrRhrvUp31GzJhldnXw2brd80FVzNCSSq6GGth/QoDoFaRi2HOsr66Vv64w0ntZKNUW1ZLZFiTWzWMEI7Ec8ChF3avbjtPJ3lKGLAn/xvGOVT9oA1ymywzeA3KIo3gUVHGTcA16PZDRQsyO1hhFlBmchmV7MZtTkcljhezziNoZG7FmRRP3mNNKOqFnzjsVa11GGxUy4ofONN+JWfou3XpSfz15wZo1aYfDAGaM2rPDtnp5O1MNiRJPjxo1ITmT1kYxvrld3csbXsxNrlDBDULXX7EtPlgFspVN2Qm9oJmEZwO/hzJUvHMCz7BY1JXEB5xPdBgclFMuUaMmKgXHOV+xxJfJs6O+VEUcb5y4i5sX4MFEqog5DurOFlZitNmtNp7TVadTBrhez49F2B4GNw1YEpgp9d7ysKHFVRZyp7xeGLi3x1SxV00W+mezdtmi4nvIAbPPtY9X6wVrrdjm3mxYCi+MtweodvbYjgtDqSVFdVDiCn3TN4BJfmnWhy2UasZSk8oyt2ulxO1tDLeQ+I7arpLUWpY5izaZnRBqXVl1Sz218Z1yN8ZX1DWD0IxnMWlKFs04Ep6VondB1QWfz8aY4jY9YAPbKcW+rywpXFbXEYYVszLFyEnItx0OnTcGEzg7k1VQvPuBwU7i4qjkn9L27KWdbUcnoqze1s42cbcFm1RVjeWTm40O28oNY8PHzct8F+47Sxpw4H42i+qQcOO7p+en2nvfpFUNphnl+Gt4PPE75/8oh8eEaF28PSjhN4s9P/3dnmPfzxPf3f7cjf+AGrzfur/+6kL8+P1V+PAh0O1auk/bwOLb8H6e0n//ZyfGwu7+/ph5eU3bN++uRxj3cDrbjLGjrpurf6jxpb8fa0MxtPfw3lfrt8XLh6aZUWgxvKj4YPn2chb81+bAyjIfncTa8ewNB7DbgcXl4vAR4fgp66K/Yr99winwDVTEo+ngPNZznDi+inn7/b0tVplWCJwAA -->
