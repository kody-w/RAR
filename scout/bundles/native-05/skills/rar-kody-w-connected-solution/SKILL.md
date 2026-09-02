---
name: "rar-kody-w-connected-solution"
description: "Turn an agent stack (a folder of BasicAgent *.py files + optional metadata.json) or an explicit list of sub-agents into ONE import-ready Microsoft Copilot Studio connected-agent solution: an orchestrator plus one connected sub-agent per agent, wired with InvokeConnectedAgentTaskAction. When an agent.py carries its compiled CapIR (t2p-capir/1.0) \u2014 or one can be recompiled from its seeded data \u2014 each sub-agent ALSO gets a REAL deterministic capability topic that runs the same steps as the agent.py's perform() (trigger -> the user's real query -> filter the seeded records -> branch -> respond, plus the document for artifact capabilities); only the data is mocked, so flipping the in-topic Table() to a live Dataverse / SharePoint connector is the one-line move to production. No code deploy. Bot names are auto-capped to 42 chars and orchestrator channels default off so it imports and publishes fully headlessly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/connected_solution_agent", "rar_sha256": "23c5edf7914db69119e2463a528c4d6a2dee964b94f5f6b90f9dffbd1d58c9af", "source_kind": "rar-agent", "source_commit": "b4ba983328bbb00340c62a83332318dc0ffc22aa", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "connected_solution_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/connected-solution:92a19ce22c7e7a8150289b8865aecffd635f579a7647be205ab5780a11128a3d", "kind": "skill"}, "version": "1.0.3", "author": "Kody Wildfeuer", "tags": ["copilot_studio", "connected_agents", "power_platform", "deploy", "integration", "converter"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/connected_solution_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `connected_solution_agent.py` is
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

Connected Solution Agent — turn a set of agents into ONE Microsoft Copilot Studio
connected-agent solution (an orchestrator + one connected sub-agent per agent).

WHAT IT DOES
------------
Given an "agent stack" (a folder of BasicAgent `*.py` files + an optional
`metadata.json`) or an explicit list of sub-agents, this agent emits a single,
import-ready Copilot Studio solution `.zip` shaped as:

    orchestrator bot  +  one connected SUB-AGENT bot per agent
    wired by componenttype=9 InvokeConnectedAgentTaskAction components

Instead of cramming every capability into one base agent's instructions, each
agent becomes its own separately-registerable connected agent (the unit
OneTrust / Agent 365 govern), and a generative orchestrator routes to them.

Every bot is a GPT agent (gpt.default instructions + code interpreter); no Azure
Function / custom connector. AND — when a sub-agent's source agent.py carries its
compiled CapIR (t2p-capir/1.0), or one can be recompiled from its seeded data —
that sub-agent ALSO gets a REAL deterministic capability topic that runs the same
steps as the agent.py's perform() (OnRecognizedIntent on the agent's triggers ->
Question for the user's real input -> a Table() of the SEEDED records -> Filter by
the real query -> branch -> SendActivity, plus a document render for artifact
capabilities). The control flow is real; only the DATA is mocked, so flipping the
in-topic Table() to a live Dataverse / SharePoint connector (binding.connector) is
the one-line move to production and the same logic runs unchanged. The emitted
package uses the exact structure of a real exported Copilot Studio solution, so it
imports with no code.

PROVEN LIVE — and the two non-obvious fixes baked in
----------------------------------------------------
This was imported AND published end-to-end into a real Copilot Studio
environment. The live test surfaced two things static checks cannot, both now
handled automatically:

  1. Bot-name 42-char limit. Dataverse rejects any bot whose display name is
     longer than 42 characters (error 10004). Bot names are capped to 42 here,
     keeping a trailing "Orchestrator" intact.

  2. Orchestrator publish + channels. A headless `pac copilot publish` cannot
     do the Bot Framework / M365 channel app-registration, so an orchestrator
     that declares channels fails publish with a 409 ExternalServiceException.
     Channels are therefore OFF by default (the whole solution then imports and
     publishes fully headlessly). Set orchestrator_channels=true only if you
     will publish the orchestrator in the maker portal (where the channel
     registration + consent happens) to expose it on M365 Copilot / Teams.

USAGE (as a RAPP agent)
-----------------------
    perform(stack_dir="path/to/my_stack")              # build from a stack
    perform(subagents=[{...}, {...}], solution_name="MyPack")   # or explicit

DEPLOY THE RESULT
-----------------
    Autonomous (built in — PURE Web API, stdlib only):
      perform(stack_dir="my_stack", deploy=true)
      Imports the solution into your Microsoft Copilot Studio (Dataverse)
      environment via the Web API ImportSolution action, then publishes every bot
      via PvaPublish (SUB-AGENTS FIRST, ORCHESTRATOR LAST — a connected-agent root
      409s if its children are not published yet). NO pac CLI, NO subprocess, NO
      binary — the IDENTICAL code runs in a local brainstem AND an
      Azure-Function-hosted brainstem. App-registration credentials are read ONLY
      from env (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET /
      DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file
      (credentials_path=, ~/.rapp_deploy_settings.json, RAPP_DEPLOY_SETTINGS, or
      ./local.settings.json) — the secret NEVER travels through chat.

    M365 Copilot / Teams exposure:
      regenerate with orchestrator_channels=true, import, then open the
      orchestrator in Copilot Studio and Publish (handles channel registration).

Self-contained: standard library only. Drop into any RAPP agents/ directory.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "capir_mode": {
      "description": "How to build the deterministic per-capability topic inside each sub-agent (the topic that runs the agent.py's perform() logic on STATIC synthetic stand-in data): 'auto' (default) uses an embedded CapIR, else real seeded data, else SYNTHESIZES static stand-in records from the agent's inferred data shape \u2014 so EVERY agent.py maps to a self-documented topic; 'static' uses only real seeded data (no synthetic stand-in); 'embedded' uses only an embedded CapIR; 'off' emits instructions-only sub-agents. Synthetic data is the swap-for-live seam (Table() -> connector).",
      "type": "string"
    },
    "credentials_path": {
      "description": "Path to a local.settings.json-style file holding DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE (under a top-level 'Values' object or at the root). Used only for deploy; the secret is never echoed back. If omitted, env vars / ~/.rapp_deploy_settings.json / ./local.settings.json are tried.",
      "type": "string"
    },
    "deploy": {
      "description": "When true, AUTONOMOUSLY import the solution into your Microsoft Copilot Studio (Dataverse) environment and publish every bot (sub-agents first, orchestrator last) \u2014 no pac CLI needed, stdlib only. App-registration credentials are read ONLY from env vars (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file \u2014 NEVER from chat. Default false (package only).",
      "type": "boolean"
    },
    "environment_url": {
      "description": "Optional override for the target Dataverse environment URL (e.g. https://yourorg.crm.dynamics.com). Defaults to DYNAMICS_365_RESOURCE from the creds.",
      "type": "string"
    },
    "orchestrator_channels": {
      "description": "Declare MsTeams + M365 Copilot channels on the orchestrator. Default false (headlessly publishable). True requires a maker-portal publish.",
      "type": "boolean"
    },
    "orchestrator_name": {
      "description": "Orchestrator display name (auto-capped to 42 chars, 'Orchestrator' kept).",
      "type": "string"
    },
    "output_path": {
      "description": "Where to write the .zip. Defaults to <SolutionName>_connected_solution.zip.",
      "type": "string"
    },
    "publish": {
      "description": "When deploy=true, also publish the bots after import (default true). false imports without publishing.",
      "type": "boolean"
    },
    "publisher_display": {
      "description": "Solution publisher friendly name (default 'Default Publisher').",
      "type": "string"
    },
    "publisher_name": {
      "description": "Solution publisher unique name (default 'DefaultPublisher'). Pair a fresh publisher_name with a fresh publisher_prefix to create a brand-new publisher.",
      "type": "string"
    },
    "publisher_prefix": {
      "description": "Customization prefix for the bot schema names (2-8 lowercase alphanumerics, default 'rapp'). Use a FRESH prefix to mint brand-new, isolated bots + a distinct solution instead of updating ones that already exist.",
      "type": "string"
    },
    "solution_display_name": {
      "description": "Solution friendly name.",
      "type": "string"
    },
    "solution_name": {
      "description": "Solution unique name (alphanumeric). Defaults from metadata.json id / stack folder name.",
      "type": "string"
    },
    "stack_dir": {
      "description": "Path to an agent stack folder. Each BasicAgent *.py under it (or its agents/ subfolder) becomes one connected sub-agent; metadata.json (name/description/features/starters) shapes the orchestrator.",
      "type": "string"
    },
    "subagents": {
      "description": "Alternative to stack_dir: explicit sub-agents, each an object with agent_name, display_name, description, instructions.",
      "type": "array"
    },
    "version": {
      "description": "Solution version, e.g. 1.0.0.0.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `connected_solution_agent.py` and embedded as the fenced Python below (sha256 23c5edf7914db691…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `connected_solution_agent.py` first:

```bash
python3 connected_solution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 connected_solution_agent.py   # or on stdin
python3 connected_solution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Connected Solution Agent — turn a set of agents into ONE Microsoft Copilot Studio
connected-agent solution (an orchestrator + one connected sub-agent per agent).

WHAT IT DOES
------------
Given an "agent stack" (a folder of BasicAgent `*.py` files + an optional
`metadata.json`) or an explicit list of sub-agents, this agent emits a single,
import-ready Copilot Studio solution `.zip` shaped as:

    orchestrator bot  +  one connected SUB-AGENT bot per agent
    wired by componenttype=9 InvokeConnectedAgentTaskAction components

Instead of cramming every capability into one base agent's instructions, each
agent becomes its own separately-registerable connected agent (the unit
OneTrust / Agent 365 govern), and a generative orchestrator routes to them.

Every bot is a GPT agent (gpt.default instructions + code interpreter); no Azure
Function / custom connector. AND — when a sub-agent's source agent.py carries its
compiled CapIR (t2p-capir/1.0), or one can be recompiled from its seeded data —
that sub-agent ALSO gets a REAL deterministic capability topic that runs the same
steps as the agent.py's perform() (OnRecognizedIntent on the agent's triggers ->
Question for the user's real input -> a Table() of the SEEDED records -> Filter by
the real query -> branch -> SendActivity, plus a document render for artifact
capabilities). The control flow is real; only the DATA is mocked, so flipping the
in-topic Table() to a live Dataverse / SharePoint connector (binding.connector) is
the one-line move to production and the same logic runs unchanged. The emitted
package uses the exact structure of a real exported Copilot Studio solution, so it
imports with no code.

PROVEN LIVE — and the two non-obvious fixes baked in
----------------------------------------------------
This was imported AND published end-to-end into a real Copilot Studio
environment. The live test surfaced two things static checks cannot, both now
handled automatically:

  1. Bot-name 42-char limit. Dataverse rejects any bot whose display name is
     longer than 42 characters (error 10004). Bot names are capped to 42 here,
     keeping a trailing "Orchestrator" intact.

  2. Orchestrator publish + channels. A headless `pac copilot publish` cannot
     do the Bot Framework / M365 channel app-registration, so an orchestrator
     that declares channels fails publish with a 409 ExternalServiceException.
     Channels are therefore OFF by default (the whole solution then imports and
     publishes fully headlessly). Set orchestrator_channels=true only if you
     will publish the orchestrator in the maker portal (where the channel
     registration + consent happens) to expose it on M365 Copilot / Teams.

USAGE (as a RAPP agent)
-----------------------
    perform(stack_dir="path/to/my_stack")              # build from a stack
    perform(subagents=[{...}, {...}], solution_name="MyPack")   # or explicit

DEPLOY THE RESULT
-----------------
    Autonomous (built in — PURE Web API, stdlib only):
      perform(stack_dir="my_stack", deploy=true)
      Imports the solution into your Microsoft Copilot Studio (Dataverse)
      environment via the Web API ImportSolution action, then publishes every bot
      via PvaPublish (SUB-AGENTS FIRST, ORCHESTRATOR LAST — a connected-agent root
      409s if its children are not published yet). NO pac CLI, NO subprocess, NO
      binary — the IDENTICAL code runs in a local brainstem AND an
      Azure-Function-hosted brainstem. App-registration credentials are read ONLY
      from env (DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET /
      DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) or a settings file
      (credentials_path=, ~/.rapp_deploy_settings.json, RAPP_DEPLOY_SETTINGS, or
      ./local.settings.json) — the secret NEVER travels through chat.

    M365 Copilot / Teams exposure:
      regenerate with orchestrator_channels=true, import, then open the
      orchestrator in Copilot Studio and Publish (handles channel registration).

Self-contained: standard library only. Drop into any RAPP agents/ directory.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/connected_solution_agent",
    "version": "1.0.3",
    "display_name": "ConnectedSolution",
    "description": "Packages a BasicAgent stack into an import-ready Copilot Studio connected-agents solution zip, optionally publishing via the Dataverse Web API.",
    "author": "Kody Wildfeuer",
    "tags": ["copilot_studio", "connected_agents", "power_platform", "deploy", "integration", "converter"],
    "category": "integrations",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import io
import os
import re
import sys
import json
import ast
import base64
import uuid
import zipfile
import logging
import urllib.request
import urllib.parse
import urllib.error
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

# PUBLISHER PREFIX. Kody, 2026-08-27: "make it aibast for now."
#
# Env-overridable rather than hardcoded, because this repo is public: a bare "aibast"
# default would stamp every stranger's generated solution with a publisher that is not
# theirs, and a solution carrying the wrong publisher is a real problem for them to unpick
# in a tenant. Setting RAPP_PUBLISHER_PREFIX overrides it; unset, it is aibast.
_DEFAULT_PUBLISHER_PREFIX = os.getenv("RAPP_PUBLISHER_PREFIX", "aibast")

logger = logging.getLogger("connected_solution_agent")

# BasicAgent base — use the RAPP runtime's when present, else a minimal shim so
# this file also runs standalone (python connected_solution_agent.py <stack_dir>).
try:  # the RAPP runtime's base when hosted; a minimal shim when standalone
    from agents.basic_agent import BasicAgent  # type: ignore
except ImportError:
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        class BasicAgent:  # minimal fallback
            def __init__(self, name=None, metadata=None):
                self.name = name or getattr(self, "name", self.__class__.__name__)
                self.metadata = metadata or getattr(self, "metadata", {})

# ============================================================================
# Embedded Copilot Studio solution templates (verbatim from the proven packager)
# ============================================================================

DEFAULT_ICON_BASE64 = (
    "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"
)

SOLUTION_XML_NATIVE = """\
<ImportExportXml version="9.2.26023.151" SolutionPackageVersion="9.2" languagecode="1033" generatedBy="CrmLive" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" OrganizationVersion="9.2.26023.151" OrganizationSchemaType="Standard" CRMServerServiceabilityVersion="9.2.26024.00146">
  <SolutionManifest>
    <UniqueName>{solution_unique_name}</UniqueName>
    <LocalizedNames>
      <LocalizedName description="{solution_display_name}" languagecode="1033" />
    </LocalizedNames>
    <Descriptions />
    <Version>{solution_version}</Version>
    <Managed>{managed_flag}</Managed>
    <Publisher>
      <UniqueName>{publisher_unique_name}</UniqueName>
      <LocalizedNames>
        <LocalizedName description="{publisher_display_name}" languagecode="1033" />
      </LocalizedNames>
      <Descriptions>
        <Description description="Auto-generated publisher" languagecode="1033" />
      </Descriptions>
      <EMailAddress xsi:nil="true"></EMailAddress>
      <SupportingWebsiteUrl xsi:nil="true"></SupportingWebsiteUrl>
      <CustomizationPrefix>{publisher_prefix}</CustomizationPrefix>
      <CustomizationOptionValuePrefix>10000</CustomizationOptionValuePrefix>
      <Addresses>
        <Address>
          <AddressNumber>1</AddressNumber>
          <AddressTypeCode xsi:nil="true"></AddressTypeCode>
          <City xsi:nil="true"></City>
          <County xsi:nil="true"></County>
          <Country xsi:nil="true"></Country>
          <Fax xsi:nil="true"></Fax>
          <FreightTermsCode xsi:nil="true"></FreightTermsCode>
          <ImportSequenceNumber xsi:nil="true"></ImportSequenceNumber>
          <Latitude xsi:nil="true"></Latitude>
          <Line1 xsi:nil="true"></Line1>
          <Line2 xsi:nil="true"></Line2>
          <Line3 xsi:nil="true"></Line3>
          <Longitude xsi:nil="true"></Longitude>
          <Name xsi:nil="true"></Name>
          <PostalCode xsi:nil="true"></PostalCode>
          <PostOfficeBox xsi:nil="true"></PostOfficeBox>
          <PrimaryContactName xsi:nil="true"></PrimaryContactName>
          <ShippingMethodCode xsi:nil="true"></ShippingMethodCode>
          <StateOrProvince xsi:nil="true"></StateOrProvince>
          <Telephone1 xsi:nil="true"></Telephone1>
          <Telephone2 xsi:nil="true"></Telephone2>
          <Telephone3 xsi:nil="true"></Telephone3>
          <TimeZoneRuleVersionNumber xsi:nil="true"></TimeZoneRuleVersionNumber>
          <UPSZone xsi:nil="true"></UPSZone>
          <UTCOffset xsi:nil="true"></UTCOffset>
          <UTCConversionTimeZoneCode xsi:nil="true"></UTCConversionTimeZoneCode>
        </Address>
        <Address>
          <AddressNumber>2</AddressNumber>
          <AddressTypeCode xsi:nil="true"></AddressTypeCode>
          <City xsi:nil="true"></City>
          <County xsi:nil="true"></County>
          <Country xsi:nil="true"></Country>
          <Fax xsi:nil="true"></Fax>
          <FreightTermsCode xsi:nil="true"></FreightTermsCode>
          <ImportSequenceNumber xsi:nil="true"></ImportSequenceNumber>
          <Latitude xsi:nil="true"></Latitude>
          <Line1 xsi:nil="true"></Line1>
          <Line2 xsi:nil="true"></Line2>
          <Line3 xsi:nil="true"></Line3>
          <Longitude xsi:nil="true"></Longitude>
          <Name xsi:nil="true"></Name>
          <PostalCode xsi:nil="true"></PostalCode>
          <PostOfficeBox xsi:nil="true"></PostOfficeBox>
          <PrimaryContactName xsi:nil="true"></PrimaryContactName>
          <ShippingMethodCode xsi:nil="true"></ShippingMethodCode>
          <StateOrProvince xsi:nil="true"></StateOrProvince>
          <Telephone1 xsi:nil="true"></Telephone1>
          <Telephone2 xsi:nil="true"></Telephone2>
          <Telephone3 xsi:nil="true"></Telephone3>
          <TimeZoneRuleVersionNumber xsi:nil="true"></TimeZoneRuleVersionNumber>
          <UPSZone xsi:nil="true"></UPSZone>
          <UTCOffset xsi:nil="true"></UTCOffset>
          <UTCConversionTimeZoneCode xsi:nil="true"></UTCConversionTimeZoneCode>
        </Address>
      </Addresses>
    </Publisher>
    <RootComponents />
    <MissingDependencies />
  </SolutionManifest>
</ImportExportXml>"""

CUSTOMIZATIONS_XML_NATIVE = """\
<ImportExportXml xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" OrganizationVersion="9.2.26023.151" OrganizationSchemaType="Standard" CRMServerServiceabilityVersion="9.2.26024.00146">
  <Entities></Entities>
  <Roles></Roles>
  <Workflows></Workflows>
  <FieldSecurityProfiles></FieldSecurityProfiles>
  <Templates />
  <EntityMaps />
  <EntityRelationships />
  <OrganizationSettings />
  <optionsets />
  <CustomControls />
  <EntityDataProviders />
  <connectionreferences>
{connection_references}
  </connectionreferences>
  <Languages>
    <Language>1033</Language>
  </Languages>
</ImportExportXml>"""

CONTENT_TYPES_XML_NATIVE = '<?xml version="1.0" encoding="utf-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="xml" ContentType="application/octet-stream" /><Default Extension="json" ContentType="application/octet-stream" />{overrides}</Types>'

CONTENT_TYPE_OVERRIDE = '<Override PartName="/{part_name}" ContentType="application/octet-stream" />'

BOT_XML = """\
<bot schemaname="{bot_schema}">
  <authenticationmode>2</authenticationmode>
  <authenticationtrigger>1</authenticationtrigger>
  <iconbase64>{icon_base64}</iconbase64>
  <iscustomizable>0</iscustomizable>
  <language>1033</language>
  <name>{bot_display_name}</name>
  <runtimeprovider>0</runtimeprovider>
  <template>default-2.1.0</template>
</bot>"""

BOT_CONFIGURATION_JSON_NATIVE = """{{
  "$kind": "BotConfiguration",
  "settings": {{
    "GenerativeActionsEnabled": true
  }},
  "isAgentConnectable": true,
  "gPTSettings": {{
    "$kind": "GPTSettings",
    "defaultSchemaName": "{gpt_schema}"
  }},
  "aISettings": {{
    "$kind": "AISettings",
    "useModelKnowledge": true,
    "isFileAnalysisEnabled": true,
    "isSemanticSearchEnabled": true,
    "contentModeration": "Low",
    "optInUseLatestModels": false
  }},
  "recognizer": {{
    "$kind": "GenerativeAIRecognizer"
  }}
}}"""

ORCHESTRATOR_CHANNELS_BLOCK = """
  "channels": [
    {
      "$kind": "ChannelDefinition",
      "channelId": "MsTeams"
    },
    {
      "$kind": "ChannelDefinition",
      "channelId": "Microsoft365Copilot"
    }
  ],"""

ORCHESTRATOR_CONFIGURATION_JSON = """{{
  "$kind": "BotConfiguration",{channels_block}
  "settings": {{
    "GenerativeActionsEnabled": true
  }},
  "isAgentConnectable": true,{publish_on_import_line}
  "gPTSettings": {{
    "$kind": "GPTSettings",
    "defaultSchemaName": "{gpt_schema}"
  }},
  "isLightweightBot": false,
  "aISettings": {{
    "$kind": "AISettings",
    "useModelKnowledge": true,
    "isFileAnalysisEnabled": true,
    "isSemanticSearchEnabled": true,
    "contentModeration": "Low",
    "optInUseLatestModels": true
  }},
  "recognizer": {{
    "$kind": "GenerativeAIRecognizer"
  }}
}}"""

GPT_BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>15</componenttype>
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{bot_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

GPT_DATA_YAML = """\
kind: GptComponentMetadata
displayName: {display_name}
instructions: |-
{instructions_indented}
gptCapabilities:
  webBrowsing: true
  codeInterpreter: true

aISettings:
  model:
    modelNameHint: GPT5Chat

  extensionData:
    lastUsedCustomModel: {{}}

declarativeSkillsMetadata:"""

BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>{component_type}</componenttype>{description_element}
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{bot_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

CONN_REF_SET_XML = """\
<botcomponent_connectionreferenceset>
{entries}
</botcomponent_connectionreferenceset>"""

INVOKE_CONNECTED_AGENT_BOTCOMPONENT_XML = """\
<botcomponent schemaname="{schema_name}">
  <componenttype>9</componenttype>
  <description>{description}</description>
  <iscustomizable>0</iscustomizable>
  <name>{display_name}</name>
  <parentbotid>
    <schemaname>{orchestrator_schema}</schemaname>
  </parentbotid>
  <statecode>0</statecode>
  <statuscode>1</statuscode>
</botcomponent>"""

INVOKE_CONNECTED_AGENT_DATA = """\
kind: TaskDialog
modelDisplayName: {display_name}
modelDescription: |-
{description_indented}{inputs_block}
action:
  kind: InvokeConnectedAgentTaskAction{input_type_block}
  botSchemaName: {child_schema}
  historyType:
    kind: ConversationHistory"""


def _connected_inputs_yaml(params):
    """The orchestrator-side typed inputs for a connected agent, from the source
    agent.py's perform() params. Per the Copilot Studio connected-agent schema:
    `inputs` (AutomaticTaskInput list) sits at the TaskDialog root and `inputType`
    sits INSIDE the action block. These populate the connected agent's Inputs
    panel and let the orchestrator pass the params when it delegates. Returns
    (inputs_block, input_type_block) — both '' when there are no params."""
    params = params or []
    if not params:
        return "", ""
    inlines, props = [], []
    for entry in params:
        pn = entry[0] if isinstance(entry, (list, tuple)) else entry
        required = bool(entry[2]) if isinstance(entry, (list, tuple)) and len(entry) > 2 else False
        name = re.sub(r"[^A-Za-z0-9_]", "", str(pn)) or "input"
        inlines.append("  - kind: AutomaticTaskInput\n    propertyName: " + name)
        props.append("      " + name + ":\n"
                     "        displayName: " + name + "\n"
                     "        isRequired: " + ("true" if required else "false") + "\n"
                     "        type: String")
    return ("\ninputs:\n" + "\n".join(inlines),
            "\n  inputType:\n    properties:\n" + "\n".join(props))

INVOKE_CONNECTED_AGENT_DEPENDENCIES = '[{{"type":"bot","schemaName":"{child_schema}"}}]'

SYSTEM_TOPICS = {
    "ConversationStart": {
        "display_name": "Conversation Start",
        "description": "This system topic triggers when the agent receives an Activity indicating the beginning of a new conversation. If you do not want the agent to initiate the conversation, disable this topic.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnConversationStart
  id: main
  actions:
    - kind: SendActivity
      id: sendMessage_M0LuhV
      activity:
        text:
          - Hello, I'm {{System.Bot.Name}}. How can I help?
        speak:
          - Hello and thank you for calling {{System.Bot.Name}}. Please note that some responses are generated by AI and may require verification for accuracy. How may I help you today?"""
    },
    "EndofConversation": {
        "display_name": "End of Conversation",
        "description": "This system topic is only triggered by a redirect action,\nand guides the user through rating their conversation with the agent.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnSystemRedirect
  id: main
  actions:
    - kind: Question
      id: 41d42054-d4cb-4e90-b922-2b16b37fe379
      conversationOutcome: ResolvedImplied
      alwaysPrompt: true
      variable: init:Topic.SurveyResponse
      prompt: Did that answer your question?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: condition-0
      conditions:
        - id: condition-0-item-0
          condition: =Topic.SurveyResponse = true
          actions:
            - kind: CSATQuestion
              id: csat_1
              conversationOutcome: ResolvedConfirmed

            - kind: SendActivity
              id: sendMessage_8r29O0
              activity: Thanks for your feedback.

            - kind: Question
              id: question_1
              alwaysPrompt: true
              variable: init:Topic.Continue
              prompt: Can I help with anything else?
              entity: BooleanPrebuiltEntity

            - kind: ConditionGroup
              id: condition-1
              conditions:
                - id: condition-1-item-0
                  condition: =Topic.Continue = true
                  actions:
                    - kind: SendActivity
                      id: sendMessage_4eOE6h
                      activity: Go ahead. I'm listening.

              elseActions:
                - kind: SendActivity
                  id: yHBz55
                  activity: Ok, goodbye.

                - kind: EndConversation
                  id: jh1GMT

      elseActions:
        - kind: Question
          id: PM68ot
          alwaysPrompt: true
          variable: init:Topic.TryAgain
          prompt: Sorry I wasn't able to help better. Would you like to try again?
          entity: BooleanPrebuiltEntity

        - kind: ConditionGroup
          id: KNxYBf
          conditions:
            - id: DPveFP
              condition: =Topic.TryAgain = false
              actions:
                - kind: BeginDialog
                  id: cngqi4
                  dialog: {bot_schema}.topic.Escalate

          elseActions:
            - kind: SendActivity
              id: GrVHEW
              activity: Go ahead. I'm listening."""
    },
    "Escalate": {
        "display_name": "Escalate",
        "description": "This system topic is triggered when the user indicates they would like to speak to a representative.\nYou can configure how the agent will handle human hand-off scenarios in the agent settings..\nIf your agent does not handle escalations, this topic should be disabled.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnEscalate
  id: main
  intent:
    displayName: Escalate
    includeInOnSelectIntent: false
    triggerQueries:
      - Talk to agent
      - Talk to a person
      - Talk to someone
      - Call back
      - Call customer service
      - Call me please
      - Call support
      - Call technical support
      - Can an agent call me
      - Can I call
      - Can I get in touch with someone else
      - Can I get real agent support
      - Can I get transferred to a person to call
      - Can I have a call in number Or can I be called
      - Can I have a representative call me
      - Can I schedule a call
      - Can I speak to a representative
      - Can I talk to a human
      - Can I talk to a human assistant
      - Can someone call me
      - Chat with a human
      - Chat with a representative
      - Chat with agent
      - Chat with someone please
      - Connect me to a live agent
      - Connect me to a person
      - Could some one contact me by phone
      - Customer agent
      - Customer representative
      - Customer service
      - I need a manager to contact me
      - I need customer service
      - I need help from a person
      - I need to speak with a live argent
      - I need to talk to a specialist please
      - I want to talk to customer service
      - I want to proceed with live support
      - I want to speak with a consultant
      - I want to speak with a live tech
      - I would like to speak with an associate
      - I would like to talk to a technician
      - Talk with tech support member

  actions:
    - kind: SendActivity
      id: sendMessage_s39DCt
      conversationOutcome: Escalated
      activity: |-
        Escalating to a representative is not currently configured for this agent, however this is where the agent could provide information about how to get in touch with someone another way.

        Is there anything else I can help you with?"""
    },
    "Fallback": {
        "display_name": "Fallback",
        "description": "This system topic triggers when the user's utterance does not match any existing topics.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnUnknownIntent
  id: main
  actions:
    - kind: ConditionGroup
      id: conditionGroup_LktzXw
      conditions:
        - id: conditionItem_tlGIVo
          condition: =System.FallbackCount < 3
          actions:
            - kind: SendActivity
              id: sendMessage_QZreqo
              activity: I'm sorry, I'm not sure how to help with that. Can you try rephrasing?

      elseActions:
        - kind: BeginDialog
          id: 5aXj5M
          dialog: {bot_schema}.topic.Escalate"""
    },
    "Goodbye": {
        "display_name": "Goodbye",
        "description": "This topic triggers when the user says goodbye. By default, it does not end the conversation. If you would like to end the conversation when the user says goodbye, you can add an \"End of Conversation\" action to this topic, or redirect to the \"End of Conversation\" system topic.",
        "data": """\
kind: AdaptiveDialog
startBehavior: CancelOtherTopics
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Goodbye
    includeInOnSelectIntent: false
    triggerQueries:
      - Bye
      - Bye for now
      - Bye now
      - Good bye
      - No thank you. Goodbye.
      - See you later

  actions:
    - kind: Question
      id: question_zf2HhP
      variable: Topic.EndConversation
      prompt: Would you like to end our conversation?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: condition_DGc1Wy
      conditions:
        - id: condition_DGc1Wy-item-0
          condition: =Topic.EndConversation = true
          actions:
            - kind: BeginDialog
              id: dn94DC
              dialog: {bot_schema}.topic.EndofConversation

        - id: condition_DGc1Wy-item-1
          condition: =Topic.EndConversation = false
          actions:
            - kind: SendActivity
              id: sendMessage_LdLhmf
              activity: Go ahead. I'm listening."""
    },
    "Greeting": {
        "display_name": "Greeting",
        "description": "This topic is triggered when the user greets the agent.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Greeting
    includeInOnSelectIntent: false
    triggerQueries:
      - Good afternoon
      - Good morning
      - Hello
      - Hey
      - Hi

  actions:
    - kind: SendActivity
      id: sendMessage_abmysR
      activity:
        text:
          - Hello, how can I help you today?
        speak:
          - Hello, <break strength="medium" /> how can I help?

    - kind: CancelAllDialogs
      id: cancelAllDialogs_01At22"""
    },
    "MultipleTopicsMatched": {
        "display_name": "Multiple Topics Matched",
        "description": "This system topic triggers when the agent matches multiple Topics with the incoming message and needs to clarify which one should be triggered.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnSelectIntent
  id: main
  triggerBehavior: Always
  actions:
    - kind: SetVariable
      id: setVariable_M6434i
      variable: init:Topic.IntentOptions
      value: =System.Recognizer.IntentOptions

    - kind: SetTextVariable
      id: setTextVariable_0
      variable: Topic.NoneOfTheseDisplayName
      value: None of these

    - kind: EditTable
      id: sendMessage_g5Ls09
      changeType: Add
      itemsVariable: Topic.IntentOptions
      value: "={{ DisplayName: Topic.NoneOfTheseDisplayName, TopicId: \\"NoTopic\\", TriggerId: \\"NoTrigger\\", Score: 1.0 }}"

    - kind: Question
      id: question_zf2HhP
      interruptionPolicy:
        allowInterruption: false

      alwaysPrompt: true
      variable: System.Recognizer.SelectedIntent
      prompt: "To clarify, did you mean:"
      entity:
        kind: DynamicClosedListEntity
        items: =Topic.IntentOptions

    - kind: ConditionGroup
      id: conditionGroup_60PuXb
      conditions:
        - id: conditionItem_rs7GgM
          condition: =System.Recognizer.SelectedIntent.TopicId = "NoTopic"
          actions:
            - kind: ReplaceDialog
              id: YZXRDb
              dialog: {bot_schema}.topic.Fallback"""
    },
    "OnError": {
        "display_name": "On Error",
        "description": "This system topic triggers when the agent encounters an error. When using the test chat pane, the full error description is displayed.",
        "data": """\
kind: AdaptiveDialog
startBehavior: UseLatestPublishedContentAndCancelOtherTopics
beginDialog:
  kind: OnError
  id: main
  actions:
    - kind: SetVariable
      id: setVariable_timestamp
      variable: init:Topic.CurrentTime
      value: =Text(Now(), DateTimeFormat.UTC)

    - kind: ConditionGroup
      id: condition_1
      conditions:
        - id: bL4wmY
          condition: =System.Conversation.InTestMode = true
          actions:
            - kind: SendActivity
              id: sendMessage_XJBYMo
              activity: |-
                Error Message: {{System.Error.Message}}
                Error Code: {{System.Error.Code}}
                Conversation Id: {{System.Conversation.Id}}
                Time (UTC): {{Topic.CurrentTime}}

      elseActions:
        - kind: SendActivity
          id: sendMessage_dZ0gaF
          activity:
            text:
              - |-
                An error has occurred.
                Error code: {{System.Error.Code}}
                Conversation Id: {{System.Conversation.Id}}
                Time (UTC): {{Topic.CurrentTime}}.
            speak:
              - An error has occurred, please try again.

    - kind: LogCustomTelemetryEvent
      id: 9KwEAn
      eventName: OnErrorLog
      properties: "={{ErrorMessage: System.Error.Message, ErrorCode: System.Error.Code, TimeUTC: Topic.CurrentTime, ConversationId: System.Conversation.Id}}"

    - kind: CancelAllDialogs
      id: NW7NyY"""
    },
    "ResetConversation": {
        "display_name": "Reset Conversation",
        "description": None,
        "data": """\
kind: AdaptiveDialog
startBehavior: UseLatestPublishedContentAndCancelOtherTopics
beginDialog:
  kind: OnSystemRedirect
  id: main
  actions:
    - kind: SendActivity
      id: sendMessage_OPsT1O
      activity: What can I help you with?

    - kind: ClearAllVariables
      id: clearAllVariables_73bTFR
      variables: ConversationScopedVariables

    - kind: CancelAllDialogs
      id: cancelAllDialogs_12Gt21"""
    },
    "Search": {
        "display_name": "Conversational boosting",
        "description": "Create generative answers from knowledge sources.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnUnknownIntent
  id: main
  priority: -1
  actions:
    - kind: SearchAndSummarizeContent
      id: search-content
      variable: Topic.Answer
      userInput: =System.Activity.Text

    - kind: ConditionGroup
      id: has-answer-conditions
      conditions:
        - id: has-answer
          condition: =!IsBlank(Topic.Answer)
          actions:
            - kind: EndDialog
              id: end-topic
              clearTopicQueue: true"""
    },
    "Signin": {
        "display_name": "Sign in ",
        "description": "This system topic triggers when the agent needs to sign in the user or require the user to sign in",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnSignIn
  id: main
  actions:
    - kind: ConditionGroup
      id: conditionGroup_ypjGKL
      conditions:
        - id: conditionItem_7XYIIR
          condition: =System.SignInReason = SignInReason.SignInRequired
          actions:
            - kind: SendActivity
              id: sendMessage_1jHUNO
              activity: Hello! To be able to help you, I'll need you to sign in.

    - kind: OAuthInput
      id: gOjhZA
      title: Login
      text: To continue, please login"""
    },
    "StartOver": {
        "display_name": "Start Over",
        "description": None,
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Start Over
    includeInOnSelectIntent: false
    triggerQueries:
      - let's begin again
      - start over
      - start again
      - restart

  actions:
    - kind: Question
      id: question_zguoVV
      alwaysPrompt: false
      variable: init:Topic.Confirm
      prompt: Are you sure you want to restart the conversation?
      entity: BooleanPrebuiltEntity

    - kind: ConditionGroup
      id: conditionGroup_lvx2zV
      conditions:
        - id: conditionItem_sVQtHa
          condition: =Topic.Confirm = true
          actions:
            - kind: BeginDialog
              id: 0YKYsy
              dialog: {bot_schema}.topic.ResetConversation

      elseActions:
        - kind: SendActivity
          id: sendMessage_lk2CyQ
          activity: Ok. Let's carry on."""
    },
    "ThankYou": {
        "display_name": "Thank you",
        "description": "This topic triggers when the user says thank you.",
        "data": """\
kind: AdaptiveDialog
beginDialog:
  kind: OnRecognizedIntent
  id: main
  intent:
    displayName: Thank you
    includeInOnSelectIntent: false
    triggerQueries:
      - thanks
      - thank you
      - thanks so much
      - ty

  actions:
    - kind: SendActivity
      id: sendMessage_9iz6v7
      activity: You're welcome."""
    },
}


# ============================================================================
# Packager: orchestrator + connected sub-agents, with the 42-char name cap,
# 100-char schema cap, and optional channels (default off = headless-publishable)
# ============================================================================

MAX_SCHEMA = 100


_CONNECTED_INFIX = ".InvokeConnectedAgentTaskAction."   # 32 chars (incl. both dots)


_MIN_ACTION_BUDGET = 26   # always leave at least this many chars for the action suffix


MAX_BOT_NAME = 42


def _cap_bot_name(name: str, preserve_suffix: Optional[str] = None) -> str:
    """Truncate a bot display name to the 42-char limit, keeping a trailing word
    like 'Orchestrator' intact when present."""
    name = (name or "").strip()
    if len(name) <= MAX_BOT_NAME:
        return name
    if preserve_suffix and name.endswith(preserve_suffix):
        budget = MAX_BOT_NAME - len(preserve_suffix) - 1
        head = name[: -len(preserve_suffix)].rstrip()[:budget].rstrip()
        return f"{head} {preserve_suffix}"
    return name[:MAX_BOT_NAME].rstrip()


def _sanitize_schema(name: str) -> str:
    """Lowercase alphanumeric fragment for a bot schema name."""
    return re.sub(r"[^a-zA-Z0-9]", "", name or "").lower()


def _pascal(name: str) -> str:
    """PascalCase alphanumeric fragment for a connected-action schema name."""
    parts = re.split(r"[^a-zA-Z0-9]+", name or "")
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def _xml_escape(text: str) -> str:
    return (
        (text or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _indent(text: str, spaces: int = 2) -> str:
    pad = " " * spaces
    return "\n".join(f"{pad}{line}" for line in (text or "").split("\n"))


def _yaml_display_safe(text: str) -> str:
    """Make a one-line value safe as a bare YAML scalar (no colons/quotes/newlines)."""
    clean = re.sub(r"\s+", " ", (text or "").replace(":", " -")).strip()
    return clean.replace('"', "").replace("'", "")


# ============================================================================
# CapIR -> deterministic capability topic (the 1:1 conversion)
#
# A converted agent.py compiles its perform() to a CapIR (t2p-capir/1.0). When a
# sub-agent carries that CapIR, the packager emits a REAL Copilot Studio topic
# that runs the SAME steps perform() runs: OnRecognizedIntent (the agent's real
# triggers) -> Question (the user's real input) -> SetVariable Table() of the
# SEEDED records -> Filter by the real query -> branch -> SendActivity, plus a
# document render for artifact-producing capabilities. The control flow is real;
# only the DATA is mocked. Flipping the in-topic Table() to a Dataverse /
# SharePoint connector (binding.connector) is the one-line move to live data, and
# the same filter/respond/document logic runs unchanged. This is the opposite of
# an actions:[]+modelDescription "gamed" topic.
# ============================================================================

def _yaml_dq(text) -> str:
    """A YAML double-quoted scalar: robust for Power Fx expressions and message
    text (escapes backslash/quote, encodes newlines)."""
    s = (str(text).replace("\\", "\\\\").replace('"', '\\"')
         .replace("\n", "\\n").replace("\t", "\\t").replace("\r", ""))
    return '"' + s + '"'


def _pfx_str(value) -> str:
    """A Power Fx double-quoted string literal (internal quotes doubled)."""
    return '"' + str(value).replace('"', '""') + '"'


def _pfx_safe_text(text) -> str:
    """Strip literal braces from message text so Copilot Studio does not parse
    them as variable bindings (unparseable {...} fails publish). Template tokens
    like {Topic.X} are added AFTER this, so they survive."""
    return str(text).replace("{", "(").replace("}", ")")


def _capir_topic_fields(records):
    """Stable union of record field names (the Table()/filter columns) when the
    binding omits an explicit field list (recovered / recompiled CapIRs)."""
    fields = []
    for r in records or []:
        if isinstance(r, dict):
            for k in r.keys():
                if k not in fields:
                    fields.append(k)
    return fields


def _numeric_metric_field(records, fields, hint=None):
    """Pick the field numeric-threshold queries compare against (e.g. "assets
    above a 30% failure probability" -> a real `Value(field) >= 0.30`). A field
    qualifies only if it parses as a number in EVERY record (so Power Fx Value()
    never errors). Prefers probability/score-like names and 0..1-ranged fields;
    honors an explicit binding `metric_field` hint."""
    if hint and hint in (fields or []):
        return hint
    if not records:
        return None
    numeric, ratio = [], []
    for f in fields:
        vals, ok = [], True
        for r in records:
            if not isinstance(r, dict) or f not in r or str(r.get(f)).strip() == "":
                ok = False; break
            try:
                vals.append(float(str(r.get(f)).strip()))
            except (TypeError, ValueError):
                ok = False; break
        if ok and vals:
            numeric.append(f)
            if all(0.0 <= v <= 1.0 for v in vals):
                ratio.append(f)
    pool = ratio or numeric
    if not pool:
        return None
    for pat in (r"p_?fail|prob|likeli|risk", r"score|rate|ratio|pct|percent|conf"):
        for f in pool:
            if re.search(pat, f, re.I):
                return f
    return pool[0]


# The load-bearing perform() constants (t2p-capir/1.0 CAPIR_CONSTS). The topic
# reads these off the CapIR when present so it mirrors the agent.py's numbers.
_CAPIR_TOPIC_CONSTS = {
    "example_take": 2, "fallback_take": 2, "pdf_records": 3,
    "pdf_prepared": "Prepared for {customer}",
    "pdf_footer": "Synthetic demo data - no customer data was needed.",
}


def capir_topic_action_name(capir: dict) -> str:
    """The custom-topic schema suffix for a capability: Handle<Pascal(key)>."""
    key = (capir or {}).get("key") or "capability"
    return "Handle" + (_pascal(key) or "Capability")


def capir_topic_data_yaml(display_name: str, capir: dict) -> str:
    """Render a capability's CapIR into a REAL deterministic Copilot Studio topic
    'data' YAML that goes INSIDE the sub-agent: OnRecognizedIntent triggers ->
    Question (slot) -> SetVariable Table() of the SEEDED records -> Filter by the
    real query -> ConditionGroup on the match count -> SendActivity, plus (for an
    artifact capability) a SetVariable that renders the document from the matched
    (or fallback) records exactly like perform()'s artifact step. The synthetic
    records live IN the topic and the control flow runs deterministically; only
    the DATA is mocked. Structural 1:1 with the generated agent.py's perform()."""
    capir = capir or {}
    consts = dict(_CAPIR_TOPIC_CONSTS)
    consts.update(capir.get("consts") or {})
    binding = capir.get("binding") or {}
    fields = binding.get("fields") or _capir_topic_fields(binding.get("records"))
    table = binding.get("table") or "records"
    records = binding.get("records") or []
    customer = str(capir.get("customer") or "the customer")
    response = _pfx_safe_text(capir.get("response") or f"Here is how I handle {display_name}.")
    # triggers + grounding facts + the artifact doc come straight from the steps
    triggers, facts, doc = [], [], None
    for step in capir.get("steps") or []:
        op = step.get("op")
        if op == "trigger_match":
            triggers = step.get("queries") or []
        elif op == "knowledge_lookup":
            facts = step.get("facts") or []
        elif op == "artifact":
            doc = step.get("doc")
    prompt = None
    for slot in capir.get("slots") or []:
        prompt = slot.get("prompt"); break
    prompt = prompt or f"What would you like help with for {display_name}?"

    # Power Fx: a real Table() of the seeded records, a real query Filter, a real
    # count, then a real branch -- the exact perform() path.
    recs = []
    for r in records:
        if isinstance(r, dict):
            cells = ", ".join("%s: %s" % (f, _pfx_str(r.get(f, ""))) for f in fields)
            recs.append("{" + cells + "}")
    table_pfx = "=Table(" + ", ".join(recs) + ")" if recs else "=Blank()"
    conds = " || ".join("(Lower(ThisRecord.%s) in Lower(Topic.Query))" % f for f in fields)
    text_clause = "(%s)" % (conds or "false")

    # numeric-threshold support: a query like "assets above a 30% failure
    # probability" sets Topic.Threshold (number, %-aware) + Topic.Direction
    # (ge/le) and the Filter does a REAL Value()-comparison on the metric field,
    # not just text containment. Falls back to text match when no number is asked.
    metric_field = _numeric_metric_field(records, fields, (binding.get("metric_field")))
    threshold_actions, filter_inner = "", text_clause
    if metric_field:
        num_re = r"\d+\.?\d*"
        thr_pfx = ('=If(IsMatch(Topic.Query, "\\d"), '
                   'Value(First(MatchAll(Topic.Query, "' + num_re + '")).FullMatch) '
                   '/ If(IsMatch(Topic.Query, "%"), 100, 1), Blank())')
        dir_pfx = ('=If(IsMatch(Lower(Topic.Query), "above|over|greater|more than|exceed|at least|higher|>"), "ge", '
                   'If(IsMatch(Lower(Topic.Query), "below|under|less|fewer|within|at most|lower|<"), "le", "ge"))')
        threshold_actions = (
            "    - kind: SetVariable\n"
            "      id: setThreshold\n"
            "      variable: Topic.Threshold\n"
            "      value: " + _yaml_dq(thr_pfx) + "\n"
            "    - kind: SetVariable\n"
            "      id: setDirection\n"
            "      variable: Topic.Direction\n"
            "      value: " + _yaml_dq(dir_pfx) + "\n")
        num_clause = ('(!IsBlank(Topic.Threshold) && If(Topic.Direction = "le", '
                      'Value(ThisRecord.' + metric_field + ') <= Topic.Threshold, '
                      'Value(ThisRecord.' + metric_field + ') >= Topic.Threshold))')
        filter_inner = "(" + text_clause + " || " + num_clause + ")"
    filter_pfx = "=Filter(Topic.Records, !IsBlank(Topic.Query) && " + filter_inner + ")"

    grounding = "\n".join("- " + _pfx_safe_text(f) for f in facts)
    ground_block = ("\n\nGrounded in what you told us:\n" + grounding) if grounding else ""

    # artifact (op==artifact): render the document from the matched-or-fallback
    # records, exactly like perform()'s artifact step (hits[:pdf_records] with a
    # data[:fallback_take] fallback). Materializing the real downloadable file is
    # the live-data flip -- a Create-file / Convert-to-PDF flow over these records.
    doc_actions, doc_block = "", ""
    if doc and fields:
        cells_pfx = ' & " | " & '.join('"%s: " & Text(ThisRecord.%s)' % (f, f) for f in fields)
        source = ("If(Topic.MatchCount > 0, Topic.Matches, FirstN(Topic.Records, %d))"
                  % consts["fallback_take"])
        document_pfx = ("=Concat(FirstN(%s, %d), %s & Char(10))"
                        % (source, consts["pdf_records"], cells_pfx))
        doc_actions = (
            "    - kind: SetVariable\n"
            "      id: setDocument\n"
            "      variable: Topic.Document\n"
            "      value: " + _yaml_dq(document_pfx) + "\n")
        prepared = _pfx_safe_text(consts["pdf_prepared"].replace("{customer}", customer))
        footer = _pfx_safe_text(consts["pdf_footer"])
        safe_doc = _pfx_safe_text(str(doc))
        doc_block = ("\n\n[" + safe_doc + "] " + prepared + ":\n"
                     + "{Topic.Document}\n" + footer
                     + "\n(In production, a Create-file / Convert-to-PDF flow over these "
                       "records delivers the real " + safe_doc + ".)")

    hit_msg = (response + ground_block
               + "\n\nI found {Topic.MatchCount} matching record(s) in the "
               + table + " data (synthetic demo data - no customer data needed)."
               + doc_block)
    miss_msg = (response + ground_block
                + "\n\nNo matching record in the " + table
                + " data; here are reference examples to ground the answer."
                + doc_block)
    trig = "\n".join("      - " + _yaml_dq(t) for t in triggers) or ("      - " + _yaml_dq(display_name))

    # intake: ask for the value to filter on. We intentionally do NOT read an
    # orchestrator-passed `Global.<param>` here. A connected agent can only
    # reference a global it has DECLARED as external-settable, and the solution
    # package format gives no reliable way to emit that declaration — referencing
    # an undeclared Global makes Copilot Studio's topic checker throw a
    # PowerFxError ("Identifier not recognized"), which blocks publish. The
    # orchestrator still DECLARES + PASSES the typed inputs (see the connected
    # action's inputType); the agent's generative layer receives them, and this
    # deterministic topic captures the value it filters on via the Question.
    intake_actions = (
        "    - kind: Question\n"
        "      id: question_query\n"
        "      variable: Topic.Query\n"
        "      prompt: " + _yaml_dq(prompt) + "\n"
        "      entity: StringPrebuiltEntity\n")

    return (
        "kind: AdaptiveDialog\n"
        "beginDialog:\n"
        "  kind: OnRecognizedIntent\n"
        "  id: main\n"
        "  intent:\n"
        "    displayName: " + _yaml_dq(display_name) + "\n"
        "    includeInOnSelectIntent: false\n"
        "    triggerQueries:\n" + trig + "\n"
        "  actions:\n"
        + intake_actions +
        "    - kind: SetVariable\n"
        "      id: setRecords\n"
        "      variable: Topic.Records\n"
        "      value: " + _yaml_dq(table_pfx) + "\n"
        + threshold_actions +
        "    - kind: SetVariable\n"
        "      id: setMatches\n"
        "      variable: Topic.Matches\n"
        "      value: " + _yaml_dq(filter_pfx) + "\n"
        "    - kind: SetVariable\n"
        "      id: setCount\n"
        "      variable: Topic.MatchCount\n"
        "      value: " + _yaml_dq("=CountRows(Topic.Matches)") + "\n"
        + doc_actions +
        "    - kind: ConditionGroup\n"
        "      id: hasMatches\n"
        "      conditions:\n"
        "        - id: hasMatches_hit\n"
        "          condition: " + _yaml_dq("=Topic.MatchCount > 0") + "\n"
        "          actions:\n"
        "            - kind: SendActivity\n"
        "              id: replyHit\n"
        "              activity: " + _yaml_dq(hit_msg) + "\n"
        "      elseActions:\n"
        "        - kind: SendActivity\n"
        "          id: replyMiss\n"
        "          activity: " + _yaml_dq(miss_msg) + "\n"
    )


@dataclass
class SubAgentSpec:
    """One connected sub-agent (one agent.py promoted to its own bot)."""
    agent_name: str           # e.g. "loanoriginationassistant"
    display_name: str         # e.g. "Loan Origination Assistant"
    description: str          # routing description the orchestrator selects on
    instructions: str         # the sub-agent's gpt.default instruction blob
    # The capability's compiled CapIR (t2p-capir/1.0), records already injected.
    # When present, the packager emits a REAL deterministic topic INSIDE this
    # sub-agent that runs the same steps as the converted agent.py's perform(),
    # instead of leaving the behavior to the gpt.default instruction blob. The
    # instructions remain as the persona/router fallback.
    capir: Optional[dict] = None
    # The source agent.py's perform() params [(name, description, required), ...],
    # declared as typed INPUTS on the orchestrator's connected-agent action so the
    # Copilot Studio orchestrator passes them when it delegates (the agent's
    # "Inputs" panel) — the contract, structurally, not just in the description.
    params: Optional[list] = None


@dataclass
class ConnectedSolutionSpec:
    """A single solution bundling an orchestrator + N connected sub-agents."""
    solution_unique_name: str
    solution_display_name: str
    orchestrator_display_name: str
    subagents: List[SubAgentSpec]
    orchestrator_instructions: str = ""   # synthesized if empty
    publisher_prefix: str = _DEFAULT_PUBLISHER_PREFIX
    publisher_unique_name: str = "DefaultPublisher"
    publisher_display_name: str = "Default Publisher"
    solution_version: str = "1.0.0.0"
    managed: bool = False
    orchestrator_schema_suffix: str = "orchestrator"
    # When True the orchestrator auto-publishes on import. Leave False so the
    # import itself never depends on the (slower, fail-prone) publish step.
    orchestrator_publish_on_import: bool = False
    # When True the orchestrator declares MsTeams + M365 Copilot channels. This
    # requires a maker-portal publish (headless `pac copilot publish` 409s on the
    # channel registration). Default False = fully headlessly publishable.
    orchestrator_channels: bool = False


class ConnectedSolutionPackager:
    """Assembles a multi-bot connected-agent solution zip from a spec."""

    def __init__(self, spec: ConnectedSolutionSpec):
        self.spec = spec
        # publisher_prefix is the one untamed length input feeding the schema caps
        # below; bound it to Dataverse's 8-char prefix limit so no schema exceeds
        # MAX_SCHEMA for ANY direct caller (perform() already caps it). Mutate the
        # spec too so the CustomizationPrefix stays consistent with the schemas.
        spec.publisher_prefix = spec.publisher_prefix[:8]
        prefix = spec.publisher_prefix

        # Connected-agent components are named
        #   {orch_schema}.InvokeConnectedAgentTaskAction.{Action}
        # and the full schema name must stay within Dataverse's 100-char limit.
        # Cap the orchestrator schema (reserving room for the action suffix) so a
        # long stack name can never push a component name over the limit.
        suffix = spec.orchestrator_schema_suffix
        base = re.sub(r"stack$", "", _sanitize_schema(spec.solution_unique_name)) or "agents"
        orch = f"{prefix}_{base}{suffix}"
        max_orch = MAX_SCHEMA - len(_CONNECTED_INFIX) - _MIN_ACTION_BUDGET   # 42
        if len(orch) > max_orch:
            keep = max(4, max_orch - len(prefix) - 1 - len(suffix))
            orch = f"{prefix}_{base[:keep]}{suffix}"
        self.orch_schema = orch
        # Whatever room is left after the (capped) orchestrator schema + infix.
        self._action_budget = MAX_SCHEMA - len(_CONNECTED_INFIX) - len(self.orch_schema)

        # Assign a unique schema name + connected-action name to each sub-agent.
        self._children = []  # list of (SubAgentSpec, child_schema, action_name)
        seen_schemas = {self.orch_schema}
        seen_actions = set()
        # Children need room for a ".topic.<Name>" suffix within MAX_SCHEMA. The
        # orchestrator schema is capped above; children were NOT, so a long
        # solution + capability name overflowed the Dataverse 100-char limit.
        child_base_max = max(4, MAX_SCHEMA - 35 - len(prefix) - 1)
        for sub in spec.subagents:
            base = (_sanitize_schema(sub.agent_name) or "agent")[:child_base_max]
            child_schema = f"{prefix}_{base}"
            n = 2
            while child_schema in seen_schemas:
                child_schema = f"{prefix}_{base}{n}"
                n += 1
            seen_schemas.add(child_schema)

            pascal = _pascal(sub.display_name or sub.agent_name) or "Agent"
            action = pascal[: self._action_budget]
            n = 2
            while action in seen_actions:
                tag = str(n)
                action = pascal[: max(1, self._action_budget - len(tag))] + tag
                n += 1
            seen_actions.add(action)

            self._children.append((sub, child_schema, action))

    # -- public ----------------------------------------------------------

    def package(self, output_path: Optional[Path] = None) -> bytes:
        buf = io.BytesIO()
        overrides: List[str] = []  # /data parts for [Content_Types].xml

        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
            # 1. solution + customizations (connector-less, empty RootComponents)
            zf.writestr("solution.xml", self._solution_xml())
            zf.writestr(
                "customizations.xml",
                CUSTOMIZATIONS_XML_NATIVE.format(connection_references=""),
            )

            # 2. Orchestrator bot (router) — instructions list the sub-agents
            self._write_bot(
                zf,
                bot_schema=self.orch_schema,
                display_name=self.spec.orchestrator_display_name,
                instructions=self._orchestrator_instructions(),
                overrides=overrides,
                is_orchestrator=True,
            )

            # 3. Connected-agent delegation components (under the orchestrator)
            for sub, child_schema, action in self._children:
                self._write_connected_action(
                    zf, sub, child_schema, action, overrides
                )

            # 4. Each sub-agent as its own connectable bot — now carrying the REAL
            #    deterministic capability topic (1:1 with its agent.py) when a
            #    CapIR is present.
            for sub, child_schema, _action in self._children:
                self._write_bot(
                    zf,
                    bot_schema=child_schema,
                    display_name=sub.display_name,
                    instructions=sub.instructions,
                    overrides=overrides,
                    capir=sub.capir,
                )

            # 5. Empty connection reference set (no connectors in this topology)
            zf.writestr(
                "Assets/botcomponent_connectionreferenceset.xml",
                CONN_REF_SET_XML.format(entries=""),
            )

            # 6. [Content_Types].xml — every extensionless /data part listed
            zf.writestr(
                "[Content_Types].xml",
                CONTENT_TYPES_XML_NATIVE.format(overrides="".join(overrides)),
            )

        data = buf.getvalue()
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(data)
        return data

    @property
    def bot_schemas(self) -> List[str]:
        return [self.orch_schema] + [c[1] for c in self._children]

    # -- bot writers -----------------------------------------------------

    def _write_bot(
        self,
        zf: zipfile.ZipFile,
        bot_schema: str,
        display_name: str,
        instructions: str,
        overrides: List[str],
        is_orchestrator: bool = False,
        capir: Optional[dict] = None,
    ) -> None:
        """Write a complete bot: bot.xml, configuration.json, gpt.default, system
        topics, and (for a sub-agent carrying a CapIR) the REAL deterministic
        capability topic that runs the same steps as the converted agent.py."""
        # Copilot Studio caps the bot name at 42 chars; keep "Orchestrator" intact.
        display_name = _cap_bot_name(
            display_name, preserve_suffix="Orchestrator" if is_orchestrator else None
        )
        # bot.xml + configuration.json
        zf.writestr(
            f"bots/{bot_schema}/bot.xml",
            BOT_XML.format(
                bot_schema=bot_schema,
                bot_display_name=display_name,
                icon_base64=DEFAULT_ICON_BASE64,
            ),
        )
        gpt_schema = f"{bot_schema}.gpt.default"
        if is_orchestrator:
            # The connected-agent root needs the channels + isLightweightBot config
            # or its post-publish provisioning fails with a 409 ExternalServiceException.
            poi = '\n  "publishOnImport": true,' if self.spec.orchestrator_publish_on_import else ""
            channels = ORCHESTRATOR_CHANNELS_BLOCK if self.spec.orchestrator_channels else ""
            config_json = ORCHESTRATOR_CONFIGURATION_JSON.format(
                gpt_schema=gpt_schema, publish_on_import_line=poi, channels_block=channels
            )
        else:
            config_json = BOT_CONFIGURATION_JSON_NATIVE.format(gpt_schema=gpt_schema)
        zf.writestr(f"bots/{bot_schema}/configuration.json", config_json)

        # gpt.default component (instructions)
        gpt_folder = f"botcomponents/{gpt_schema}"
        zf.writestr(
            f"{gpt_folder}/botcomponent.xml",
            GPT_BOTCOMPONENT_XML.format(
                schema_name=gpt_schema,
                display_name=display_name,
                bot_schema=bot_schema,
            ),
        )
        instr = instructions or f"You are {display_name}. Help the user with their request."
        zf.writestr(
            f"{gpt_folder}/data",
            GPT_DATA_YAML.format(
                display_name=display_name,
                instructions_indented=_indent(instr, 2),
            ),
        )
        overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{gpt_folder}/data"))

        # system topics (one set per bot)
        for topic_key, topic_data in SYSTEM_TOPICS.items():
            schema_name = f"{bot_schema}.topic.{topic_key}"
            folder = f"botcomponents/{schema_name}"
            zf.writestr(
                f"{folder}/botcomponent.xml",
                self._topic_botcomponent_xml(bot_schema, topic_key, topic_data),
            )
            zf.writestr(
                f"{folder}/data",
                topic_data["data"].format(bot_schema=bot_schema),
            )
            overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

        # custom per-capability topic: the REAL deterministic behavior, INSIDE
        # this sub-agent (1:1 with the converted agent.py's CapIR steps). The
        # orchestrator stays a pure router and never carries one.
        if capir and not is_orchestrator:
            action = capir_topic_action_name(capir)
            # keep "{bot_schema}.topic.{action}" within the 100-char schema limit
            action = action[: max(4, MAX_SCHEMA - len(bot_schema) - len(".topic."))]
            schema_name = f"{bot_schema}.topic.{action}"
            folder = f"botcomponents/{schema_name}"
            zf.writestr(
                f"{folder}/botcomponent.xml",
                self._topic_botcomponent_xml(
                    bot_schema, action,
                    {"display_name": _xml_escape(display_name),
                     "description": f"Deterministic handler for {display_name} "
                                    "(seeded records + the real user query, 1:1 with the agent.py)."}),
            )
            zf.writestr(f"{folder}/data", capir_topic_data_yaml(display_name, capir))
            overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

    def _write_connected_action(
        self,
        zf: zipfile.ZipFile,
        sub: SubAgentSpec,
        child_schema: str,
        action: str,
        overrides: List[str],
    ) -> None:
        """Write the orchestrator's delegation component for one sub-agent."""
        schema_name = f"{self.orch_schema}.InvokeConnectedAgentTaskAction.{action}"
        folder = f"botcomponents/{schema_name}"
        description = sub.description or f"Delegate to {sub.display_name}."

        zf.writestr(
            f"{folder}/botcomponent.xml",
            INVOKE_CONNECTED_AGENT_BOTCOMPONENT_XML.format(
                schema_name=schema_name,
                description=_xml_escape(description),
                display_name=_xml_escape(sub.display_name),
                orchestrator_schema=self.orch_schema,
            ),
        )
        zf.writestr(
            f"{folder}/dependencies.json",
            INVOKE_CONNECTED_AGENT_DEPENDENCIES.format(child_schema=child_schema),
        )
        inputs_block, input_type_block = _connected_inputs_yaml(getattr(sub, "params", None))
        zf.writestr(
            f"{folder}/data",
            INVOKE_CONNECTED_AGENT_DATA.format(
                display_name=_yaml_display_safe(sub.display_name),
                description_indented=_indent(description, 2),
                child_schema=child_schema,
                inputs_block=inputs_block,
                input_type_block=input_type_block,
            ),
        )
        overrides.append(CONTENT_TYPE_OVERRIDE.format(part_name=f"{folder}/data"))

    # -- xml helpers -----------------------------------------------------

    def _topic_botcomponent_xml(self, bot_schema, topic_key, topic_data) -> str:
        schema_name = f"{bot_schema}.topic.{topic_key}"
        desc = topic_data.get("description")
        desc_element = ""
        if desc:
            desc_element = f"\n  <description>{_xml_escape(desc)}</description>"
        return BOTCOMPONENT_XML.format(
            schema_name=schema_name,
            component_type=9,
            display_name=topic_data["display_name"],
            bot_schema=bot_schema,
            description_element=desc_element,
        )

    def _solution_xml(self) -> str:
        return SOLUTION_XML_NATIVE.format(
            solution_unique_name=self.spec.solution_unique_name,
            solution_display_name=self.spec.solution_display_name,
            publisher_unique_name=self.spec.publisher_unique_name,
            publisher_display_name=self.spec.publisher_display_name,
            publisher_prefix=self.spec.publisher_prefix,
            solution_version=self.spec.solution_version,
            managed_flag="1" if self.spec.managed else "0",
        )

    # -- orchestrator instructions --------------------------------------

    def _orchestrator_instructions(self) -> str:
        if self.spec.orchestrator_instructions:
            return self.spec.orchestrator_instructions
        lines = [
            f"You are {self.spec.orchestrator_display_name}, the orchestrator for the "
            f"{self.spec.solution_display_name} workflow. You route each user request to the "
            "right connected sub-agent and never answer specialized questions yourself.",
            "",
            "Connected sub-agents you can delegate to:",
        ]
        for sub, _schema, _action in self._children:
            one_line = re.sub(r"\s+", " ", (sub.description or sub.display_name)).strip()
            lines.append(f"- {sub.display_name}: {one_line}")
        lines += [
            "",
            "Routing rules:",
            "- Read the user's request, pick the single best-matching sub-agent from the list, and delegate to it.",
            "- Pass each sub-agent only the inputs it needs; do not paraphrase or pre-answer its work.",
            "- If the request spans several sub-agents, handle one sub-agent per turn and confirm before moving on.",
            "- If no sub-agent fits, say so and ask a clarifying question rather than inventing an answer.",
        ]
        return "\n".join(lines)


def generate_connected_solution(
    spec: ConnectedSolutionSpec,
    output_path: Optional[Path] = None,
) -> bytes:
    """Build a connected (multi-bot) solution zip from a ConnectedSolutionSpec."""
    return ConnectedSolutionPackager(spec).package(output_path=output_path)


# ============================================================================
# Build sub-agents from an agent stack (agents/*.py + metadata.json) and validate
# ============================================================================

def _humanize(name: str) -> str:
    name = re.sub(r"_stacks$", "", name or "")
    name = name.replace("_", " ").replace("-", " ").strip()
    name = re.sub(r"([a-z])([A-Z])", r"\1 \2", name)
    return " ".join(w[:1].upper() + w[1:] for w in name.split())


def _humanize_class(name: str) -> str:
    name = re.sub(r"Agent$", "", name or "")
    name = re.sub(r"_agent$", "", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    name = name.replace("_", " ").strip()
    return " ".join(w[:1].upper() + w[1:] for w in name.split())


def _safe_literal(node):
    try:
        return ast.literal_eval(node)
    except Exception:
        return None


# Class-body literals a converted agent.py embeds. CAPIR is the compiled CapIR
# (perform()'s spec); SYNTHETIC_DATA holds the seeded records (the build keeps
# them OUT of the CapIR binding, so we re-inject them); the rest let us recompile
# a CapIR when one was not embedded.
_RECOVERED_ATTRS = {"CAPIR", "SYNTHETIC_DATA", "KNOWLEDGE", "RESPONSE",
                    "DOC_NAME", "CUSTOMER", "TRIGGERS"}


def _parse_basic_agent(py_path: Path):
    """AST-extract (display_name, agent_name, description, module_doc, params,
    recovered) from a BasicAgent .py — `recovered` carries any embedded CapIR /
    seeded records used to build the deterministic capability topic."""
    src = py_path.read_text(encoding="utf-8", errors="replace")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    module_doc = (ast.get_docstring(tree) or "").strip()

    cls = None
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and any(
            isinstance(b, ast.Name) and b.id == "BasicAgent" for b in node.bases
        ):
            cls = node
            break
    if cls is None:
        return None

    self_name = None
    description = ""
    params = []  # (name, description, required)
    recovered = {}  # class-level CAPIR / SYNTHETIC_DATA / ... for deterministic topics
    for sub in ast.walk(cls):
        if not isinstance(sub, ast.Assign):
            continue
        for tgt in sub.targets:
            # class-body literals the build stage embeds (CAPIR = {...},
            # SYNTHETIC_DATA = [...], KNOWLEDGE / RESPONSE / DOC_NAME / CUSTOMER / TRIGGERS)
            if isinstance(tgt, ast.Name) and tgt.id in _RECOVERED_ATTRS:
                val = _safe_literal(sub.value)
                if val is not None:
                    recovered[tgt.id] = val
                continue
            if not (isinstance(tgt, ast.Attribute) and isinstance(tgt.value, ast.Name)
                    and tgt.value.id == "self"):
                continue
            if tgt.attr == "name" and isinstance(sub.value, ast.Constant) and isinstance(sub.value.value, str):
                self_name = sub.value.value
            elif tgt.attr == "metadata" and isinstance(sub.value, ast.Dict):
                # Walk the dict node key-by-key: the metadata literal contains a
                # non-literal value ("name": self.name), so literal_eval on the
                # whole dict fails — pull the literal keys we care about directly.
                for k, v in zip(sub.value.keys, sub.value.values):
                    key = k.value if isinstance(k, ast.Constant) else None
                    if key == "description":
                        dv = _safe_literal(v)
                        if isinstance(dv, str):
                            description = dv.strip()
                    elif key == "parameters":
                        pv = _safe_literal(v)
                        if isinstance(pv, dict):
                            props = pv.get("properties") or {}
                            req = set(pv.get("required") or [])
                            for pn, pinfo in props.items():
                                pdesc = (pinfo.get("description") if isinstance(pinfo, dict) else "") or pn
                                params.append((pn, pdesc, pn in req))

    stem_name = re.sub(r"_agent$", "", py_path.stem)
    agent_name = stem_name
    display = _humanize_class(self_name or stem_name)
    if not description:
        # First paragraph of the module docstring.
        description = re.sub(r"\s+", " ", module_doc.split("\n\n")[0]).strip()
    # Statically infer the SHAPE of the data this agent works with (the dict keys
    # its perform()/helpers read & write) so we can synthesize matching static
    # stand-in records — no execution, no domain rules.
    recovered["INFERRED_FIELDS"] = _infer_record_fields(tree, exclude=[p[0] for p in params])
    return display, agent_name, description, module_doc, params, recovered


def _stack_subagent_instructions(display, description, module_doc, params) -> str:
    """The sub-agent's brain: self-documents the agent.py end-to-end — its purpose
    and its FULL input contract (what the orchestrator passes to delegate). Generic
    for ANY agent.py; no domain assumptions."""
    lines = [f"You are the {display} agent.", "", "# Purpose"]
    lines.append(module_doc.strip() if module_doc else (description or f"Handle {display} requests."))
    lines += ["", "# Inputs the orchestrator passes you"]
    if params:
        for pn, pdesc, required in params:
            tag = "required" if required else "optional"
            clean = re.sub(r"\s+", " ", pdesc).strip()
            lines.append(f"- {pn} ({tag}): {clean}")
    else:
        lines.append("- No structured inputs are required; use the user's request directly.")
    lines += ["", "# How you answer",
              "- Run your deterministic capability topic and ground every answer in its seeded records.",
              "- That seeded data is SYNTHETIC stand-in data for your real source system, so you load "
              "and run end-to-end with no live connection. Swapping the topic's Table() for the live "
              "connector takes you to production with no change to the logic.",
              "- Stay in your lane: if the request belongs to another connected agent, say so and let "
              "the orchestrator route it."]
    return "\n".join(lines)


def _contract_description(description, params, limit=850):
    """The orchestrator-facing routing description: the agent's purpose PLUS its
    input contract, so the Copilot Studio agent knows what to pass when it
    delegates. Self-documenting, generic, length-capped for the component."""
    base = re.sub(r"\s+", " ", description or "").strip()
    if params:
        ins = "; ".join("%s (%s)" % (pn, "required" if req else "optional")
                        for pn, _pd, req in params)
        base = (base + " Inputs to pass: " + ins + ".").strip()
    return base[:limit]


# t2p-capir/1.0 — the load-bearing perform() constants, mirrored so a recompiled
# CapIR carries the same numbers the agent.py uses.
_CAPIR_SCHEMA = "t2p-capir/1.0"
_RECOMPILE_CONSTS = {
    "word_min_len": 3, "example_take": 2, "fallback_take": 2, "pdf_records": 3,
    "pdf_prepared": "Prepared for {customer}",
    "pdf_footer": "Synthetic demo data - no customer data was needed.",
}


# Envelope / structural dict keys that are NOT data columns, so schema inference
# never mistakes the result wrapper for record fields.
_ENVELOPE_KEYS = {"status", "agent", "data", "parameters", "properties",
                  "required", "type", "name", "description", "items", "enum",
                  "error", "result", "results", "success", "ok", "count", "as_of_utc"}
# Objects whose `.get("x")` calls are NOT record reads (input kwargs, env, etc.).
_SKIP_GET_OBJS = {"kwargs", "self", "metadata", "os", "sys", "environ", "params", "config"}


def _flatten_record(r):
    """Flatten one record to top-level scalar fields (the Table()/filter columns):
    a nested dict is merged up one level; lists/dicts are json-encoded to strings."""
    if not isinstance(r, dict):
        return {}
    out = {}
    for k, v in r.items():
        if isinstance(v, dict):
            for kk, vv in v.items():
                out[str(kk)] = vv if not isinstance(vv, (list, dict)) else json.dumps(vv, ensure_ascii=False)
        elif isinstance(v, list):
            out[str(k)] = json.dumps(v, ensure_ascii=False)
        else:
            out[str(k)] = v
    return out


def _infer_record_fields(tree, exclude=None, max_fields=14):
    """Infer the SHAPE of the data an agent.py works with by statically scanning
    its code for the dict keys it reads/writes: `rec.get("field")`, `rec["field"]`
    and `{"field": ...}` literals. Excludes input-param names + envelope keys so
    only genuine data columns remain. 100% static — no execution, no domain rules."""
    exclude = set(exclude or []) | _ENVELOPE_KEYS
    keys = []

    def add(k):
        if (isinstance(k, str) and k and k.isidentifier()
                and k not in exclude and k not in keys):
            keys.append(k)

    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == "get" and node.args):
            obj = node.func.value
            if isinstance(obj, ast.Name) and obj.id in _SKIP_GET_OBJS:
                continue
            a = node.args[0]
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                add(a.value)
        elif isinstance(node, ast.Subscript):
            sl = node.slice
            if isinstance(sl, ast.Constant) and isinstance(sl.value, str):
                add(sl.value)
        elif isinstance(node, ast.Dict):
            klits = [k.value for k in node.keys
                     if isinstance(k, ast.Constant) and isinstance(k.value, str)]
            if "status" in klits and "data" in klits:
                continue  # a result-envelope literal, not a data record
            for k in klits:
                add(k)
    return keys[:max_fields]


def _synthesize_value(field, i):
    """A clearly-synthetic, generic value for `field` on row i — typed by the field
    NAME's TOKENS only (token-matched, so "age" never fires inside "message"). No
    domain knowledge. Deterministic (index-based, no RNG)."""
    f = field.lower()
    toks = set(t for t in re.split(r"[^a-z0-9]+", f) if t)
    if toks & {"prob", "probability", "score", "rate", "ratio", "pct", "percent",
               "confidence", "likelihood", "fail", "risk"}:
        return round(0.15 + 0.7 * (((i - 1) % 5) / 4.0), 2)   # 0.15 .. 0.85
    if f.startswith(("is_", "has_")) or toks & {"enabled", "active", "flag", "bool"}:
        return (i % 2 == 0)
    if toks & {"date", "time", "utc", "timestamp", "datetime", "created", "updated"}:
        return "2026-01-%02dT00:00:00Z" % min(i, 28)
    if toks & {"id", "guid", "uuid", "code", "ref"}:
        return "%s-%04d" % ((re.sub(r"[^A-Za-z]", "", field).upper()[:4] or "REC"), i)
    if toks & {"count", "qty", "quantity", "amount", "price", "cost", "value", "age",
               "days", "years", "hours", "num", "number", "level", "index", "size",
               "total", "kv", "voltage", "pct"}:
        return i * 10
    return "synthetic %s %d" % (f.replace("_", " "), i)


def _synthesize_records(fields, n=5):
    """Generate n self-documenting STATIC stand-in records over `fields` — the
    synthetic data that lets the topic load and run end-to-end with no live
    connection. Generic for any field set; swap the Table() for the live connector."""
    fields = [f for f in (fields or []) if f] or ["id", "label", "detail"]
    return [{f: _synthesize_value(f, i) for f in fields} for i in range(1, n + 1)]


def _resolve_capir(recovered, display, agent_name, description, params, capir_mode):
    """Decide the CapIR a sub-agent's deterministic topic is built from — the
    topic that IS this agent.py's perform() running on STATIC stand-in data, so
    the Copilot Studio orchestrator gets the same result it would by chatting the
    brainstem and invoking the agent.py.

    Policy (capir_mode):
      off       -> never emit a topic (instructions-blob only)
      embedded  -> only when the agent.py embeds a CAPIR literal
      static    -> embedded, else recompile ONLY from real seeded data
                   (SYNTHETIC_DATA); do not synthesize a stand-in
      auto      -> (default) embedded, else recompile from SYNTHETIC_DATA, else
                   SYNTHESIZE static stand-in data from the agent's inferred data
                   shape. Maps EVERY agent.py to a self-documented topic."""
    mode = (capir_mode or "auto").lower()
    if mode in ("capture", "always", "run"):
        mode = "auto"
    if mode == "off":
        return None
    synth = recovered.get("SYNTHETIC_DATA") or []
    embedded = recovered.get("CAPIR")
    if isinstance(embedded, dict) and embedded.get("steps"):
        binding = dict(embedded.get("binding") or {})
        if not binding.get("records"):
            binding["records"] = synth
        if not binding.get("fields"):
            binding["fields"] = _capir_topic_fields(binding.get("records"))
        out = {**embedded, "binding": binding}
        out.setdefault("customer", recovered.get("CUSTOMER") or "the customer")
        return out
    if mode == "embedded":
        return None
    if mode == "static":
        return _recompile_capir_from_meta(recovered, display, agent_name, description,
                                          params, records=synth) if synth else None
    # auto: always map — real seeded data if present, else a STATIC stand-in
    # synthesized from the agent's inferred data shape (its perform() field reads).
    records = synth
    if not records:
        fields = recovered.get("INFERRED_FIELDS") or [p[0] for p in (params or [])]
        records = _synthesize_records(fields)
    return _recompile_capir_from_meta(recovered, display, agent_name, description,
                                      params, records=records)


def _recompile_capir_from_meta(recovered, display, agent_name, description, params, records=None):
    """Build a CapIR for an agent.py with no embedded CAPIR — mirrors T2P's
    _compile_capir shape from its records (real or synthesized), KNOWLEDGE,
    RESPONSE, DOC_NAME, TRIGGERS plus the parsed metadata. Same structure and
    perform()-parity constants as the generated path; only the source differs."""
    records = [_flatten_record(r) for r in (records if records is not None
               else (recovered.get("SYNTHETIC_DATA") or []))][:10]
    knowledge = list(recovered.get("KNOWLEDGE") or [])
    triggers = list(recovered.get("TRIGGERS") or [])
    if not triggers:
        triggers = [display] + ([re.sub(r"\s+", " ", description).strip()[:60]]
                                if description else [])
    response = recovered.get("RESPONSE") or description or f"Here is how I handle {display}."
    doc = recovered.get("DOC_NAME") or None
    key = re.sub(r"[^a-z0-9_]", "", (agent_name or display).lower().replace(" ", "_")) or "capability"
    fields = _capir_topic_fields(records)
    prompt = f"What would you like to ask the {display} agent? (a keyword, id, or value to filter on)"
    binding = {
        "connector": "table",
        "table": "rec_" + key,
        "library": display + " Library",
        "fields": fields,
        "key_field": fields[0] if fields else "id",
        "row_count": len(records),
        "records": records,
    }
    steps = [
        {"id": "trigger", "op": "trigger_match", "queries": triggers},
        {"id": "slot_query", "op": "slot_fill", "slot": "query"},
        {"id": "ground", "op": "knowledge_lookup", "facts": knowledge, "into": "Grounding"},
        {"id": "lookup", "op": "record_lookup", "source": "binding", "from": "query",
         "into": "Matches", "take": _RECOMPILE_CONSTS["example_take"],
         "fallback_take": _RECOMPILE_CONSTS["fallback_take"]},
        {"id": "respond", "op": "respond", "template_kind": "standard"},
    ]
    if doc:
        steps.append({"id": "artifact", "op": "artifact", "doc": doc,
                      "from": ["Grounding", "Matches"]})
    return {
        "schema": _CAPIR_SCHEMA,
        "key": key,
        "response": response,
        "customer": recovered.get("CUSTOMER") or "the customer",
        "binding": binding,
        "slots": [{"name": "query", "entity": "StringPrebuiltEntity",
                   "prompt": prompt, "required": True}],
        "consts": dict(_RECOMPILE_CONSTS),
        "steps": steps,
        "expect": list(triggers),
        "triggers_owned": True,
    }


def _subagents_from_stack(stack_dir: Path, capir_mode: str = "auto") -> List[SubAgentSpec]:
    agents_dir = stack_dir / "agents"
    if not agents_dir.is_dir():
        agents_dir = stack_dir
    subs: List[SubAgentSpec] = []
    for py in sorted(agents_dir.glob("*.py")):
        if py.name.startswith("_") or py.name == "basic_agent.py":
            continue
        parsed = _parse_basic_agent(py)
        if not parsed:
            logger.warning("  - %s: no BasicAgent subclass, skipping", py.name)
            continue
        display, agent_name, description, module_doc, params, recovered = parsed
        capir = _resolve_capir(recovered, display, agent_name, description, params, capir_mode)
        subs.append(SubAgentSpec(
            agent_name=agent_name,
            display_name=display,
            # description carries the input contract so the orchestrator knows what
            # to pass when it delegates (self-documented, like the agent.py).
            description=_contract_description(description, params) or f"Handle {display} requests.",
            instructions=_stack_subagent_instructions(display, description, module_doc, params),
            capir=capir,
            params=params,
        ))
        logger.info("  + %s%s", display, "  [deterministic topic]" if capir else "")
    return subs


def _load_stack_metadata(stack_dir: Path) -> dict:
    mpath = stack_dir / "metadata.json"
    if mpath.is_file():
        try:
            return json.loads(mpath.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def _orchestrator_instructions_from_metadata(meta: dict, subs: List[SubAgentSpec]) -> str:
    name = meta.get("name", "the agent stack")
    desc = meta.get("description", "")
    lines = [f"You are the orchestrator for {name}.", ""]
    if desc:
        lines += [desc, ""]
    lines.append("You route each user request to the right connected sub-agent and never do their specialized work yourself.")
    features = meta.get("features") or []
    if features:
        lines += ["", "End-to-end flow this stack supports, in order:"]
        lines += [f"- {f}" for f in features]
    lines += ["", "Connected sub-agents you can delegate to:"]
    for sub in subs:
        lines.append(f"- {sub.display_name}: {sub.description}")
    starters = meta.get("starters") or []
    if starters:
        lines += ["", "Example requests you should expect:"]
        lines += [f"- {s}" for s in starters]
    lines += [
        "",
        "Routing rules:",
        "- Pick the single best-matching connected agent for the request and delegate to it; pass it the inputs named in its description.",
        "- Calling a connected agent gives you the SAME result you would get by chatting the source brainstem and letting it invoke that agent.py — each connected agent's topic runs the agent's deterministic logic on its seeded sample data.",
        "- If a request spans several connected agents, handle one per turn, show its result, then continue to the next.",
        "- If a required input is missing, ask for it. The seeded data is synthetic stand-in data; do not invent records beyond it.",
        "- If no connected agent fits, say so and ask a clarifying question.",
    ]
    return "\n".join(lines)


def validate_connected_solution(zip_path: Path) -> bool:
    """Structural checks that the connected solution is import-shaped."""
    ok = True
    with zipfile.ZipFile(zip_path, "r") as zf:
        names = set(zf.namelist())

        for required in ("[Content_Types].xml", "solution.xml", "customizations.xml"):
            if required not in names:
                logger.error("  X missing %s", required)
                ok = False

        bots = sorted({n.split("/")[1] for n in names if n.startswith("bots/")})
        logger.info("  bots: %d (%s)", len(bots), ", ".join(bots))

        # Every connected-action must reference an existing child bot.
        actions = [n for n in names if ".InvokeConnectedAgentTaskAction." in n and n.endswith("/dependencies.json")]
        logger.info("  connected-agent actions: %d", len(actions))
        for dep in actions:
            child = json.loads(zf.read(dep).decode("utf-8"))[0]["schemaName"]
            if f"bots/{child}/bot.xml" not in names:
                logger.error("  X action %s -> missing child bot %s", dep, child)
                ok = False
            data_path = dep.rsplit("/", 1)[0] + "/data"
            if data_path in names:
                data_text = zf.read(data_path).decode("utf-8")
                if f"botSchemaName: {child}" not in data_text:
                    logger.error("  X %s data does not invoke %s", data_path, child)
                    ok = False

        # Every extensionless /data part must be declared in [Content_Types].xml.
        ct = zf.read("[Content_Types].xml").decode("utf-8")
        data_parts = [n for n in names if n.endswith("/data")]
        missing = [p for p in data_parts if f'PartName="/{p}"' not in ct]
        if missing:
            logger.error("  X %d /data parts missing from [Content_Types].xml (e.g. %s)",
                         len(missing), missing[0])
            ok = False
        else:
            logger.info("  content-types: all %d /data parts declared", len(data_parts))

        # Each bot needs gpt.default + the system-topic set.
        for bot in bots:
            if f"botcomponents/{bot}.gpt.default/data" not in names:
                logger.error("  X bot %s missing gpt.default", bot)
                ok = False

        # No botcomponent schema name may exceed the Dataverse 100-char limit.
        schemas = {n.split("/")[1] for n in names if n.startswith("botcomponents/")}
        longest = max(schemas, key=len) if schemas else ""
        if len(longest) > 100:
            logger.error("  X schema name too long (%d > 100): %s", len(longest), longest)
            ok = False
        else:
            logger.info("  schema lengths: max %d/100 (%s)", len(longest), longest)

        # Copilot Studio rejects bot display names longer than 42 chars.
        worst_name, worst_len = "", 0
        for bot in bots:
            bx = zf.read(f"bots/{bot}/bot.xml").decode("utf-8")
            m = re.search(r"<name>(.*?)</name>", bx, re.DOTALL)
            nm = (m.group(1).strip() if m else "")
            if len(nm) > worst_len:
                worst_name, worst_len = nm, len(nm)
        if worst_len > 42:
            logger.error("  X bot name too long (%d > 42): %s", worst_len, worst_name)
            ok = False
        else:
            logger.info("  bot names: max %d/42 (%s)", worst_len, worst_name)
    return ok


# ===========================================================================
# Autonomous deploy to Microsoft Copilot Studio (Dataverse Web API, stdlib only)
#
# Self-contained so this one file, dropped into any brainstem, can BOTH package a
# connected-agents solution AND import + publish it into a real Copilot Studio
# environment — no pac CLI, no third-party packages. App-registration credentials
# come ONLY from env vars or a settings file, never from chat, and the secret is
# never echoed back. Same proven path as the T2P deploy agent: service-principal
# token -> ImportSolution -> PvaPublish (children first, orchestrator last).
# ===========================================================================

_DEPLOY_AUTH = "https://login.microsoftonline.com"


def _http(url, data=None, headers=None, method=None, timeout=300):
    """Minimal stdlib HTTP: dict data -> form-encoded (OAuth), else JSON bytes."""
    if isinstance(data, dict):
        data = urllib.parse.urlencode(data).encode()
    elif data is not None and not isinstance(data, (bytes, bytearray)):
        data = json.dumps(data).encode()
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read().decode("utf-8", "replace")
            return r.status, (json.loads(body) if body[:1] in ("{", "[") else body)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, body
    except Exception as e:  # network / DNS / timeout
        return 0, str(e)


def _extract_dyn_creds(creds):
    """From a settings dict ({IsEncrypted,Values} or bare), a Values dict, or a
    JSON string -> {client_id, client_secret, tenant_id, resource} or None."""
    if isinstance(creds, str):
        try:
            creds = json.loads(creds)
        except Exception:
            return None
    if not isinstance(creds, dict):
        return None
    vals = creds.get("Values", creds)
    cid, sec = vals.get("DYNAMICS_365_CLIENT_ID"), vals.get("DYNAMICS_365_CLIENT_SECRET")
    ten, res = vals.get("DYNAMICS_365_TENANT_ID"), vals.get("DYNAMICS_365_RESOURCE")
    if not all([cid, sec, ten, res]):
        return None
    return {"client_id": cid, "client_secret": sec, "tenant_id": ten, "resource": str(res).rstrip("/")}


def _deploy_creds(kwargs):
    """Resolve app-registration creds for deploy — env / settings file ONLY, never
    from chat. Returns (creds_dict, source_label) or (None, None)."""
    candidates = [
        os.path.expanduser(kwargs["credentials_path"]) if kwargs.get("credentials_path") else None,
        os.environ.get("RAPP_DEPLOY_SETTINGS"),
        os.path.expanduser("~/.rapp_deploy_settings.json"),
        "local.settings.json",
    ]
    for cand in candidates:
        if cand and os.path.isfile(cand):
            try:
                c = _extract_dyn_creds(json.load(open(cand)))
                if c:
                    return c, cand
            except Exception:
                pass
    c = _extract_dyn_creds({"Values": dict(os.environ)})
    if c:
        return c, "process env"
    return None, None


def _sp_token(client_id, secret, tenant, resource):
    """Service-principal (client-credentials) token for the Dataverse env."""
    code, t = _http(f"{_DEPLOY_AUTH}/{tenant}/oauth2/v2.0/token",
                    data={"grant_type": "client_credentials", "client_id": client_id,
                          "client_secret": secret, "scope": resource.rstrip("/") + "/.default"},
                    headers={"Content-Type": "application/x-www-form-urlencoded"})
    if code != 200 or not isinstance(t, dict) or "access_token" not in t:
        raise RuntimeError("service-principal auth failed: " + str(t)[:200])
    return t["access_token"]


def _dataverse_action(resource, token, action, body=None, method="POST"):
    data = json.dumps(body).encode() if body is not None else None
    return _http(resource.rstrip("/") + "/api/data/v9.2/" + action, data=data, method=method,
                 headers={"Authorization": "Bearer " + token, "Content-Type": "application/json",
                          "Accept": "application/json", "OData-MaxVersion": "4.0",
                          "OData-Version": "4.0"})


def _import_solution(resource, token, zip_bytes):
    """ImportSolution (unmanaged, overwrite) then PublishAllXml."""
    code, r = _dataverse_action(resource, token, "ImportSolution", {
        "OverwriteUnmanagedCustomizations": True, "PublishWorkflows": True,
        "ImportJobId": str(uuid.uuid4()),
        "CustomizationFile": base64.b64encode(zip_bytes).decode()})
    if code not in (200, 204):
        raise RuntimeError("ImportSolution failed (%s): %s" % (code, str(r)[:400]))
    _dataverse_action(resource, token, "PublishAllXml")


def _find_botid(resource, token, schema):
    qs = urllib.parse.urlencode({"$select": "botid,schemaname",
                                 "$filter": "schemaname eq '%s'" % schema,
                                 "$orderby": "createdon desc", "$top": "1"})
    code, r = _http(resource.rstrip("/") + "/api/data/v9.2/bots?" + qs,
                    headers={"Authorization": "Bearer " + token, "Accept": "application/json"})
    rows = (r.get("value") if isinstance(r, dict) else None) or []
    return rows[0]["botid"] if rows else None


def _publish_botid(botid, resource, token):
    """Publish ONE bot via the Dataverse PvaPublish Web API action. PURE HTTPS —
    no pac/CLI/subprocess — so this agent.py runs identically in a local brainstem
    AND inside an Azure-Function-hosted brainstem (no binary to ship)."""
    code, r = _dataverse_action(resource, token,
                                "bots(%s)/Microsoft.Dynamics.CRM.PvaPublish" % botid, {})
    if code in (200, 204):
        return {"bot_id": botid, "status": "publish_requested", "via": "PvaPublish"}
    return {"bot_id": botid, "status": "publish_failed", "via": "PvaPublish", "error": str(r)[:160]}


def _publish_connected(bot_schemas, resource, token):
    """Publish every bot — CHILDREN first, ORCHESTRATOR last (a connected-agent
    root cannot publish until its invoked sub-agents are published)."""
    if not bot_schemas:
        return []
    orch = bot_schemas[0]
    order = list(bot_schemas[1:]) + [orch]
    out = []
    for schema in order:
        botid = _find_botid(resource, token, schema)
        if not botid:
            out.append({"schema": schema, "status": "not_found"})
            continue
        out.append({"schema": schema, **_publish_botid(botid, resource, token)})
    return out


def _run_deploy(zip_bytes, bot_schemas, orch_display, kwargs):
    """Import + (optionally) publish the connected solution into Copilot Studio.
    Returns a result dict with a human `summary`; never includes the secret."""
    creds, src = _deploy_creds(kwargs)
    if creds and kwargs.get("environment_url"):
        creds = {**creds, "resource": str(kwargs["environment_url"]).rstrip("/")}
    if not creds:
        return {"status": "creds_missing",
                "summary": "NOT deployed — no app-registration credentials found.",
                "how_to": ("Set env DYNAMICS_365_CLIENT_ID / DYNAMICS_365_CLIENT_SECRET / "
                           "DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE, or pass "
                           "credentials_path=<local.settings.json>, or place "
                           "~/.rapp_deploy_settings.json. Secrets never travel through chat.")}
    publish = bool(kwargs.get("publish", True))
    try:
        token = _sp_token(creds["client_id"], creds["client_secret"],
                          creds["tenant_id"], creds["resource"])
    except Exception as e:
        return {"status": "auth_failed", "summary": "NOT deployed — service-principal auth failed.",
                "error": str(e)[:300], "creds_source": src, "environment": creds["resource"]}
    try:
        _import_solution(creds["resource"], token, zip_bytes)
    except Exception as e:
        return {"status": "import_failed", "summary": "Import FAILED.", "error": str(e)[:400],
                "environment": creds["resource"], "creds_source": src}
    published = _publish_connected(bot_schemas, creds["resource"], token) if publish else []
    npub = sum(1 for p in published if p.get("status") in ("published", "publish_requested"))
    summary = ("Imported into " + creds["resource"] + " and "
               + (("published %d/%d bots. " % (npub, len(published))) if publish else "skipped publish. ")
               + "Open Copilot Studio, select that environment, open '"
               + orch_display[:42] + "' and use the Test pane.")
    return {"status": "deployed", "summary": summary, "environment": creds["resource"],
            "orchestrator": orch_display[:42], "publish_enabled": publish,
            "published": published, "creds_source": src,
            "test_in_studio": "https://copilotstudio.microsoft.com"}


# ---------------------------------------------------------------------------
# RAPP agent wrapper
# ---------------------------------------------------------------------------

class ConnectedSolutionAgent(BasicAgent):
    """Generate a connected-agent (orchestrator + sub-agents) Copilot Studio solution."""

    def __init__(self):
        self.name = "ConnectedSolutionAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Turn an agent stack (a folder of BasicAgent *.py files + optional "
                "metadata.json) or an explicit list of sub-agents into ONE import-ready "
                "Microsoft Copilot Studio connected-agent solution: an orchestrator plus "
                "one connected sub-agent per agent, wired with InvokeConnectedAgentTaskAction. "
                "When an agent.py carries its compiled CapIR (t2p-capir/1.0) — or one can be "
                "recompiled from its seeded data — each sub-agent ALSO gets a REAL "
                "deterministic capability topic that runs the same steps as the agent.py's "
                "perform() (trigger -> the user's real query -> filter the seeded records -> "
                "branch -> respond, plus the document for artifact capabilities); only the "
                "data is mocked, so flipping the in-topic Table() to a live Dataverse / "
                "SharePoint connector is the one-line move to production. No code deploy. Bot "
                "names are auto-capped to 42 chars and orchestrator channels default off so it "
                "imports and publishes fully headlessly."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "stack_dir": {
                        "type": "string",
                        "description": "Path to an agent stack folder. Each BasicAgent *.py under it "
                                       "(or its agents/ subfolder) becomes one connected sub-agent; "
                                       "metadata.json (name/description/features/starters) shapes the orchestrator.",
                    },
                    "subagents": {
                        "type": "array",
                        "description": "Alternative to stack_dir: explicit sub-agents, each an object with "
                                       "agent_name, display_name, description, instructions.",
                    },
                    "solution_name": {
                        "type": "string",
                        "description": "Solution unique name (alphanumeric). Defaults from metadata.json id / stack folder name.",
                    },
                    "solution_display_name": {"type": "string", "description": "Solution friendly name."},
                    "orchestrator_name": {
                        "type": "string",
                        "description": "Orchestrator display name (auto-capped to 42 chars, 'Orchestrator' kept).",
                    },
                    "orchestrator_channels": {
                        "type": "boolean",
                        "description": "Declare MsTeams + M365 Copilot channels on the orchestrator. Default false "
                                       "(headlessly publishable). True requires a maker-portal publish.",
                    },
                    "capir_mode": {
                        "type": "string",
                        "description": "How to build the deterministic per-capability topic inside each "
                                       "sub-agent (the topic that runs the agent.py's perform() logic on STATIC "
                                       "synthetic stand-in data): 'auto' (default) uses an embedded CapIR, else "
                                       "real seeded data, else SYNTHESIZES static stand-in records from the "
                                       "agent's inferred data shape — so EVERY agent.py maps to a self-documented "
                                       "topic; 'static' uses only real seeded data (no synthetic stand-in); "
                                       "'embedded' uses only an embedded CapIR; 'off' emits instructions-only "
                                       "sub-agents. Synthetic data is the swap-for-live seam (Table() -> connector).",
                    },
                    "version": {"type": "string", "description": "Solution version, e.g. 1.0.0.0."},
                    "output_path": {
                        "type": "string",
                        "description": "Where to write the .zip. Defaults to <SolutionName>_connected_solution.zip.",
                    },
                    "deploy": {
                        "type": "boolean",
                        "description": "When true, AUTONOMOUSLY import the solution into your Microsoft Copilot "
                                       "Studio (Dataverse) environment and publish every bot (sub-agents first, "
                                       "orchestrator last) — no pac CLI needed, stdlib only. App-registration "
                                       "credentials are read ONLY from env vars (DYNAMICS_365_CLIENT_ID / "
                                       "DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE) "
                                       "or a settings file — NEVER from chat. Default false (package only).",
                    },
                    "publish": {
                        "type": "boolean",
                        "description": "When deploy=true, also publish the bots after import (default true). "
                                       "false imports without publishing.",
                    },
                    "credentials_path": {
                        "type": "string",
                        "description": "Path to a local.settings.json-style file holding DYNAMICS_365_CLIENT_ID / "
                                       "DYNAMICS_365_CLIENT_SECRET / DYNAMICS_365_TENANT_ID / DYNAMICS_365_RESOURCE "
                                       "(under a top-level 'Values' object or at the root). Used only for deploy; "
                                       "the secret is never echoed back. If omitted, env vars / "
                                       "~/.rapp_deploy_settings.json / ./local.settings.json are tried.",
                    },
                    "environment_url": {
                        "type": "string",
                        "description": "Optional override for the target Dataverse environment URL (e.g. "
                                       "https://yourorg.crm.dynamics.com). Defaults to DYNAMICS_365_RESOURCE from the creds.",
                    },
                    "publisher_prefix": {
                        "type": "string",
                        "description": "Customization prefix for the bot schema names (2-8 lowercase alphanumerics, "
                                       "default 'rapp'). Use a FRESH prefix to mint brand-new, isolated bots + a "
                                       "distinct solution instead of updating ones that already exist.",
                    },
                    "publisher_name": {
                        "type": "string",
                        "description": "Solution publisher unique name (default 'DefaultPublisher'). Pair a fresh "
                                       "publisher_name with a fresh publisher_prefix to create a brand-new publisher.",
                    },
                    "publisher_display": {
                        "type": "string",
                        "description": "Solution publisher friendly name (default 'Default Publisher').",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        stack_dir = kwargs.get("stack_dir")
        subagents_in = kwargs.get("subagents")
        if not stack_dir and not subagents_in:
            return {
                "status": "needs_input",
                "agent": self.name,
                "message": "Provide 'stack_dir' (a folder of BasicAgent *.py + optional metadata.json) "
                           "or 'subagents' (a list of {agent_name, display_name, description, instructions}).",
            }

        meta: Dict[str, Any] = {}
        if stack_dir:
            sd = Path(stack_dir)
            if not sd.exists():
                return {"status": "error", "agent": self.name, "message": f"stack_dir not found: {sd}"}
            subs = _subagents_from_stack(sd, capir_mode=str(kwargs.get("capir_mode") or "auto"))
            meta = _load_stack_metadata(sd)
            fallback = _humanize(sd.name)
        else:
            subs = []
            for s in subagents_in:
                dn = s.get("display_name") or s.get("agent_name") or "Agent"
                subs.append(SubAgentSpec(
                    agent_name=s.get("agent_name") or dn,
                    display_name=dn,
                    description=(s.get("description") or "").strip() or f"Handle {dn} requests.",
                    instructions=s.get("instructions") or "",
                    capir=s.get("capir") if isinstance(s.get("capir"), dict) else None,
                ))
            fallback = kwargs.get("solution_name") or "Connected Agents"

        if not subs:
            return {"status": "error", "agent": self.name, "message": "No sub-agents found to bundle."}

        short = re.sub(r"\b(Agent\s+Stack|Agent|Stack)\b", "", meta.get("name", "")).strip()
        unique = re.sub(r"[^A-Za-z0-9]", "",
                        kwargs.get("solution_name") or meta.get("id", "") or fallback.replace(" ", ""))
        display = kwargs.get("solution_display_name") or meta.get("name") or f"{fallback} Agents"
        orch_name = kwargs.get("orchestrator_name") or f"{short or fallback} Orchestrator"
        orch_instructions = _orchestrator_instructions_from_metadata(meta, subs) if meta else ""

        spec = ConnectedSolutionSpec(
            solution_unique_name=unique or "ConnectedAgents",
            solution_display_name=display,
            orchestrator_display_name=orch_name,
            subagents=subs,
            orchestrator_instructions=orch_instructions,
            orchestrator_channels=bool(kwargs.get("orchestrator_channels", False)),
            solution_version=kwargs.get("version", "1.0.0.0"),
            # publisher controls — a fresh publisher_prefix mints brand-new bot
            # schema names (an isolated, clearly-distinct solution), instead of
            # updating bots that already exist under the default 'rapp' prefix.
            publisher_prefix=re.sub(r"[^a-z0-9]", "", str(kwargs.get("publisher_prefix") or _DEFAULT_PUBLISHER_PREFIX).lower())[:8] or _DEFAULT_PUBLISHER_PREFIX,
            publisher_unique_name=kwargs.get("publisher_name") or "DefaultPublisher",
            publisher_display_name=kwargs.get("publisher_display") or "Default Publisher",
        )
        packager = ConnectedSolutionPackager(spec)
        out = Path(kwargs.get("output_path") or f"{spec.solution_unique_name}_connected_solution.zip")
        data = packager.package(output_path=out)
        ok = validate_connected_solution(out)

        # autonomous deploy: import into Copilot Studio + publish the bots
        # (children first, orchestrator last). Creds come ONLY from env / a
        # settings file — never from chat.
        deploy_result = _run_deploy(data, list(packager.bot_schemas), display, kwargs) \
            if kwargs.get("deploy") else None

        capir_topics = sum(1 for s in subs if getattr(s, "capir", None))
        msg = (f"Generated '{out.name}' — {len(packager.bot_schemas)} bots "
               f"(1 orchestrator + {len(subs)} connected sub-agents, "
               f"{capir_topics} with a deterministic capability topic), "
               f"{round(len(data)/1024,1)} KB. Validation: {'pass' if ok else 'fail'}.")
        if deploy_result:
            msg += " " + deploy_result.get("summary", "")

        data_block = {
            "solution_path": str(out),
            "size_kb": round(len(data) / 1024, 1),
            "orchestrator_schema": packager.orch_schema,
            "sub_agents": [s.display_name for s in subs],
            "capir_topics": capir_topics,
            "deterministic_topics": [s.display_name for s in subs if getattr(s, "capir", None)],
            "validation": "pass" if ok else "fail",
        }
        status = "success" if ok else "error"
        if deploy_result:
            data_block["deploy"] = deploy_result
            if deploy_result.get("status") not in ("deployed",):
                status = "partial"
        else:
            data_block["deploy_hint"] = ("Pass deploy=true to import + publish into your Copilot Studio "
                                         "environment automatically (creds from env DYNAMICS_365_CLIENT_ID/"
                                         "SECRET/TENANT_ID/RESOURCE or a settings file via credentials_path).")
            data_block["m365_exposure"] = ("Set orchestrator_channels=true and publish the orchestrator "
                                           "in the maker portal for M365/Teams exposure.")
        return {"status": status, "agent": self.name, "message": msg, "data": data_block}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    target = sys.argv[1] if len(sys.argv) > 1 else None
    if not target:
        print("usage: python connected_solution_agent.py <stack_dir> [output.zip]")
        sys.exit(1)
    out_path = sys.argv[2] if len(sys.argv) > 2 else None
    result = ConnectedSolutionAgent().perform(stack_dir=target, output_path=out_path)
    print(json.dumps(result, indent=2))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7y8Z7ejWJYo+Fe0oj5kRBNx8S5r8q1BgIQcIIxcRU0kHiSc8Cg732+fA7o24kZmd79Zc6tWlATn7LPP9k71xwerrsKs+PDrh1Xm9pN9FLu+V3vFh88fXK90iiivoiwFr426SCcW+G/gpdWkrCznMvloTfwsdr1ikvmTqVVGDje+/Y+HvJ/4UeyVE2iSjRCseJJ4leValfVwLrP00yQrBnBel8eRE1WTOCqrAUxZ21/GM8pJlFbZRJHFSZTkWVF9KTwLoLiJnCIrM7+a8FkexVk10avajbKJk6Wp51Se++URxyyuh6N/Hc7JCif0yqqwKnBuHtflJEu9ly0vx05ycJ3x0+dJGxXgVRtV4WSRNtnF45/Wj/c0rPLCOcMRD5N96L2QZ7i+YxVFBAgQgYs4WQIwBaB4K19ok48Vln9xrDwqYPQB+TT5WmMISgwEGXECUGxvUnjPu/wiS0Y4pee54PtAxKdNnuWEr5Dn1royCTyw1ppoIreeuF7lFUmUAupGDoCdW3YUR1U/qQDxnEkVWtWkqNMSfPImpZWAfyovB9vvT56u80s50MXPiuTjJ4B/EQUBINOX/zUuqkuvAAsAe+LJFchOP7wA7Acn38He0R5uVLjl8NIurBTgDT4VXplnqfv5zpNhtZs5dTLcxR8kpKgi33KqF8wBTT/9ExAq7u+rB1pE5STJnIsHwJTZxI+jPI/SYHwfpV/uNzUsO/YA8kCkLCBsjTcRwNbGK0pvAk/00Co8NQMS9yQT4PDojhBgypc4ApxJMrAL7M+LzK0f+S4PcucCPLw8zvqHyRTIYwrICChYAPLVVTZwOgfXBxsJbOKAg8C71H0rkeAxODUuARzfquNBE/zhLkAx7sJ/35PXNtATsG3i1zGgQAg0AmhZGfcPQGG9zkpy8PXDr//69+cPYF/84dc/PjixVYJHH55lV3/Ui1GGwbbYSgPwPu+BIUjB90dGg0cAmWe2l17sf578x39cWqsIyk+/fk0nj3+jLfjmRsXkt8n97QOQwI9fPzy/+Prh06vltX3X729R+sOOp3dvdkT+JM2qV+cMpBifvAL1CqHhr/CqwWD98fbp8DfiVdXgiF/B5xTI5rA9r6uvHz6/t3o8YVg8UOBh4O27ywDLS7D0DlUtsiYCUvHLM86//LWx/LmZ/Prhx9PeHAyk55dnQozHPJnSP8Zn30aUJ25U5rHVP317se2fgY4AMbwLdPnnp4cf6PDn1/TlwYDerxMhcqp/gV2fJ1za/xuw8Y8/3/Dr+d7fsaV0wVrVqsKPzys+vV3xxGz3wevAPcqPn379kQDP3H3DS68oMiBrn99n2lse+a/EczzQz+rU/XXyR+n++fXDn99hXdslwPvbi7wNJvnbCOBjCazOaMy/JcAQ/AaI8vGNTL+8A0I9GPmvg8/NwJfvbj5Qdjglziz3DvvbkyyAQ75b7FtxbA8+GGwI68RKo5sHVo1XfbUUmBTv13cv869/fwcQYDa43L9SquHPHZT26W6vherxdk+vXmTv+drcnSk/whxQehisZOp+1Gt7XKfnnvPxfdF/Af3bT09z08/vb36N8m8/X/WiH799fL7ty8PnO4EPD4DlUf5xfADESgLWKfYmf7jpn0BOgT8EQvzwrm0Zxf2V7j3f5vXDVyf9BMQoYL+9EbdhE1CkqBwgAVfrffz+9WAQnOrTKCDAiaXvGbVPP5e5t1b70aG85fazv5lwjyb9tRl5UnPA+Z9Z7v+xbn/9ALzyqzhyVO3B/9r1wJqHUb9fOSQQ/1bgToX3ADZ9BKd8/Wp/vAvr1xLSB038z/Hrf46fP4HXd0yGfwcVfaTD/fr3F5+exeLloDqNgDi8Oelf/w/35WR9uSFf2H8/w/y5wf9bsr/CJnKfcRkl85F5DwWIVCwgEV8/TF6QfTnyUT9+yuN3VP4HEjypwh9Ph/75SgaeDhrinxHK90e9Doy+fQfwzqtX1/lzorxa/gP815o0mMo3sF+/vFv0Z3s7fPg8SueoSKNpHlVlINcb4QFmCgD+Ibh6x3w9k/AuB3cL9CgTbzXmiViffwLgrQ27f/lu7ZuLvln/TPfPP/iFu778Nlz7r8C9sVk/kPmvdj6Fub/ZWRZ//DnXn9YNAjqzAN0/ffoZLYYIfrDSb4A9PrzLN8ixhv8MRu8tjH88x9PFEPVXRQYC8Me8CgRrIDUJX1Z8ywvPj7oJyKWASRkSGPdL6rUTO6u+h1qCmyTWYxrwEaRzEcDWqob0xIk9q4j7L+6Qj6XOS5L66R6GgXgeRG7fA6xzIJRDRgMOK+85mxXfs+ExSAKWxX3MtZ7yh18K4E9/mdyRfngL8Ps7/fbaHn1vjCY/BDTfb39Uz2+COOPMtfFNNafrhS6J2jdVE2eLw6eHOGu94uOnT//6lfn3Xy79/DNEX6vMT5B543yEOxnUp7c/6NLLvjfK8RPYj2u+Bz95H/4ra5oDE2UNqfI7JkJ9fPdxsCGv9mR19RQkv9WQugJZyrccvHhtEcHmh/dMy5/fnqsb357eP9yi/E1qNabPvz2j+fD44eOrs34Dn19jN7j/xoojsNV754iP9+UvG/4xZsFplmR1+Zgm//qY1N4rPN+VcaAn3ozyPEj8a1gfnTCK3cJLJ35UlNXnt2k0SHWrTw8TvgBJ3VB18SaKvD7eCyhe2oBE33oNrPSqQa3KsVb1pPmpB6zHfQswQ9Ur3bkj/w3YhYH3wJsUNbDF48OPAyE/j5nXx2diAty/3W1B+ek5Afv86OxAZvf1h8znDb/vkAdWPwdpr+l6zyvG4sbg2so6+Yi+ieLLASIAZVVAg8tBnR+Dv88jrNdOPykDAOIjkKe5l3rFYKsmv/wBODmGV3/+8kSbP2Ivff9+f95t0zvRPQAKEHvDJugOaHSvf75XhBuxfQ/SH69v/ee9NGf9TZHr00+BFUNg+HFAZWDfJxhFMOIzClBaTR8mu7uMjwXEP37JrRIk14CgQP5HdvziW1H8y58P31cq3gjJd6HtQGbot8kYeQEivFn6XAFJEqvonyOz1xwfkPxmx9kYgX9X2XgVod0NxK+j4R6U8fMPK0Gu+O1iD2u+owBQkJEGE/THXW8c9J3tA4RnaRgDgfvzH0+s7W9PhZ1fJ/8qH14b3bdC++8fNr9m+bD99fcfFr8RhVeb/vLMv1GUH1FqnmXjnm8M0gFY+ko8vn4Y5OONW/jzTckMZDaT30bSOI734+7HfOe/LFovsvGvF8sxFGbebPrB4Lwrgo9p16cxQwMkerZF3pBSvFePeXWffCjZWvFr1N8pQryD7rcwGtK6AWdwoAoo+ojdbyC0HOuuj07jxUGM7qPP6uJ7H/I3RbPvS2jANURFlo5V58FZJYC1jjUUWD86oyt5diDCUeY2C17/hlPkN369EGXj20KA/5vn6SKviQZsiDJ336+JumJqvDg2Rb5zS01kTQYsAHKAruWo3p/emp0fKJoM6HldnpV14T3TVPeqn4TjI4VfFZjvde/XJvu/dcPhjkBuBiCJdQHedOCbFY9KtwGowYZnJeXkCcG3l3kv/79/+i8l/8DGDk8GcgxfX8jy54c/P7+prHz49cM//vGqnaQ7Q+QFfHoVJaOnNcKonBgZiCmAb/pdXy3W64fE/f2pL/AUas8LoOlDU+DsjYCH0uvv//clc/svLfxjgHQ3hL8/TIwQnJIVURANZV+NU9XH5hqADyjvXIAv+NIMR4DjH8mp8YvB/gFt9f45+f1nwB/yfsDyawpoaUXp0HzwBt2xigjItDU0h+y+8r543dBaAWnPvawz/FPnD8PVx3bWnSDO2KXznLryJoCOAxuHzt7noXWTxUNHZCBTeYniGMQ4xdg66UdhAqT8dQD2+++/21YZfk3vLQZ8ci+jlfAQPz03zL58GdKJOApCYKY8J8xABAIij/+c/NWuEfhwxmgvBgqNXailrsgTEEqNjaTyVWY1+f2PP++kH7ADoc4EBHuRPzTqqoEdr7g83ODOjydmgDsPKILc8n7SW7pN2nBQ16i652SDaxrbPGBp0UbAqD8S8b75Tvon7t7PGXhSPtIQ8Gk0OsPaUcAGZg79s4fJwp88Uwpc97E7NAkzkAgCi+mBXDB1+nua+MzCsdgGzFrpgwi0LsFVB8i/gzx2JE4y2ILq98mGV4GlzeLB3AICjceD3Vk62MMn8Uxfdf2+ptMnEA8TeQydgQew8rCwSm9cN7TvBonIiuf9Yw9uSJ6HHpU38Gj0paPkvZQNn/Kke+3oKQQdjcNoIwd2ft8p/llz+Gv6s+7wmKB/F53+bWv4011JJM6YLIyJoIj61/TLq7+v6Txq7g3hR5N174gAL/+zNtDv/zFq7VPXfEDqsSMEpPJNT+j3/0Lv/PNdK+9He0k0SkgJnEo8lH3e9NO/c53PdPl9SBZ/n5ShNXQvrfLXp1D0DbFA1D8B6H5HMt2cfuHmwDmO75/Jdt9/76rb/dgWB/vSqupz7zf2b3rsL8vLAZPFi047hZUkQ3lkEL/+dfw/ysWAmj1I44jDL+WbmvvnsYMOVPWugUPT/bFpn7UgOPQGYa68uAfECgCVQW5kx69vet/3cVSINAI3VFLPKGrAD/hRboG/mwQZwGyo8YxGBcSaY5I1NKHfEBNE46N9yAbFSUYZE8crDVQc2DmZq8bTkUFePTy5oDdlTujekQZ39wpgKMC/n/4JQrkJdxuCgXRWp3d6whMH4DmkuU8d74cJJwtPitaOEw0vMgUIV4JQy/HenXEYFOyvhhw+/4/GGwYrZVX/n843fE3/CwMOSqoB/IKhqeYuAB3ByVn6sh4sfhyBGKYZvqbbockzkHQIcL6fiBh7y8Oog/U8gwBkdlili6IgCq/nImb3oQm7v5vntxMVL0MTOrDxg1I04KKPkxPWy9xE4Y3VwNfjE4A7r+cn7g7wseQ58eOsHaRrOO3VZIXAGdxfTFYAK/J/MFrx0Y5SF0B6eH70aQxY/mbeYtSf50mVOAvA6SN3gUyDWDbw3PvVBosHtBNEHPfsdGDIa7971xagDqMPudN5iEaLQaV/YhA/3+cxnqxneS8+pPf5j1FXVU3ZifJkvdiJz2XkR3yrNgNL0y+Z3URDHcyPOoCQDYLjIbR76zz+q3+PAWoLJPmO0tBqA/r7VLZ0QcbiAhZ9Af/z5HTHm37vGl+lP3fyjTwElmjQvALIzxBAtoNRGrOSIRgfdG2Mih5ji8+DiRqo0X5Nw7EB6r7NpB69BzpOyHwZU3AC+zJMw4DTALceXslM4Q2R9DDxcrd8LQhtvOfG1Lg3eioKxlkajKVvYFYex2sAgwfF/Dim0BMUQRDi0/eDOW9mckCA9twMuXjeKOEW0HAQdQ0fv35422IaaAnOeLjfCHt404F6zqCg55keYFWfB3UmvwOJBBJzZ8Dj2t8fifiIgjua/xHhGfBsXpsVF6BHQ+L0BHMC0H/0SIX1LJzfBTKP4EYT6HpODO5dvgwaDeWJ8hnbx0IagbATsQPkA2GH7hVN5Hhi53j5Y3Q2wuOfIAx0HIJbD1gab6LMZoNPf/JIo0cEjAPO8jmiqAaP8mqc6RHgz4eaANv+JmcdrVXkD0WAR2jtkIf8NI19Lyv92A6XuIe6d+CPoF4TePSqaTnY13CcVChHezemsGPQD5aMHHpSLngyJrmjlJg6CIZA5Dd6rec879NP1f5+/vPk1dOcym9DdaUK4SqDk/7bY0D56W3i/Y+JXUfxo1O1HqPOt+Ce+3z/+uPh4eHPz5Pxf/79efKmoQwO2/Tq8xH/GPz3U8A53EkQ1bVynBiSCByxbq6Nd25zP5h7Kf9/HJAbM4hH+6iamjjZe/aEUxdDq8mNI3tk6kuV6T0yvFz/8+si0XMVYfEoZKOreBK/l2rRT0dIPz4boWdQr2tDQylmAPmI8OMxz3mK5dxVcZTzF6n2nkK4J5ADGLWxHptHk4/P0bI+mS003fg8UTReEnVD4wxFm6w53XhpS36fxxTZC2CgvmMtc5w5feqTDGqavhgbYPV6b2iSyMpQu53wa0B48BmIBfCzQyly+PoEEbhpCyD/lHuBuy8EgOiCB6HXGGWO3jcaAsV7beA5oRxdkfVcvR6Dzy9PseeXIVkdkoCX3JH7zqK9rnmNdxiylbGd8wTyuSj38f2qHFDB917ci28T+AnMmzXPJbnvNz9V6D69U6J7gvTx+zLdb58n/xt+GDqxj22ib0/7xkTu82gMvt01CeBlGAt5rg+R8hPEB3ik6sObbZ9es6P0wKHVRBZ3oja4rGawzFUIMokgfOpf3aG9Z52eS3DP2gZY8NgBuvuEn9vez4+m/FHeM2AT73Hhj33/QUC+07QhMHpWgHvE8Oyc3hjee6qte7H/ZQhYx3LWWBBMXatwQfAAZGioLgCbAWKIIssfQx0QO7yY2hJ+KU0Nk7LAigEL7n34NQUe5/M4tfJXE7JDEpgMiUY5DNQCNQE2aQikx/Ha5/G+4dvbmXkJBNbj2NFgke8lw9fZCoDy5YeMBejDMDn63Vz36E7fS2nezV/ugTHQId3ggK5Oyn4IrIcjR7p9AewY2z2/Tn4ZgrRfJh8f3fane6A81BYS23Pdp2zu870tMUaPr7K0x8f6UQZuQF+cRP0pOHw+5ym5eS5mvSThPgjQntK9scrwJNcglBnE+fiSaCZWXt7Ti6Hs++Up1RkjOECTf46DtuDcX+74j1HB98hOPoJY/UdKgNz4l6fLvt7+Aw3Ausz3f3msprzOuL+MG16KLyBqeT7maT591NXWyr8AFn0Z4+sSKODk41PuBLK6l1RoENGhJgJEaBgiS4OhdP29cflR3IaRgcck7Eer8aWsehCMjS0FEJYNydfkf2Q3/5sGc/LxPpxiDaz6EgNnGE9+2VkxSJl/mWT2EOmPJrV6rKlmg28yS0D1kapDFnu3nf98be8ARe99+qFQPDiSYbJtqIxm98zv8+gYmmHWHv5LGwxev2tk79FtEYGM8j1m3EH9yIKxbn63jpxpKLKyUUx9fXxqXf0fxCNvApHXrZrn8GLy8fXM48+mI57HHLIn9z9JRyV5E379d/zxiyMe6f3x/w+pes8NP93s7gtfBjgmT9M6/jBJNnmaX7iHma+4O8ykeVY6sPcVrb/VRfwjn5Wnaf2hsFcMBvup9FNZRQAE9CWbfc03U1uDvPQheJiEVZWXv8LwwP+sCB6cInlwe+CIIqd8cLLk0zPao+F7X7WejerYpXxXUN/13z/eR7jnh5NNeY8LoLfhwnPW+FgFew31B/q+5G9PMjrYuKHoNGRsw0h0NGSi1j0L+/KYhT0ufZ8fP4yEvsOR15L+plbw8Se/wvk8+eX1pl9A7p9X79veV+NQ7+p8Mdap2iKq7nnkUDp/y8D/6ymmkAFK/+sno1nvnv1ImJ/YmlfZz+cJoH/2w/TUxPKHmuKjBXry9KORAjy58+x1SWtoGD3CGAp07/Ljh8m4H7F7zopeZix9YE5BoPfEludRxR+m6X759FeU8H4mAu8c+The+/6Br8+bqNbww6Ifpj7HnY/VkZ9MhALuAv0bImbr1Vzo87K/ucodyI+X4cfafHS7G9/Ho56MzGDt306ZYl+YyThm6YydjjgHGgtipGKYkfluKPTuXwGyM2BIpMnLLYbR1pcbfH4eW72LETTUmL8fW33dWn2eUs1S770p1XcJ8e5M81+w9o0M/TXEv4H0RjReE+y16R0t7Jvu2yRygVO6//71sZH3c1SeShZ/Eau9/UXtHeLDRBzC/+9/JHYPpCKgxENKVZXPuQ3w+/eNn547WD9pYf7zu8t8HHCHX6EG+0CSQUJYwgChYkh5Pt2D8/JHw//ulZ+qSz9emYvHwuLY9gI3f/mJ2Esj83UDc8yAhpLmPUa86+B//wdtr7C0igJYKoDk43j4XwjH4wqAxeCsHyfI37kwAPbo0Nz7ry4f39+RHjUdqND955R/fHii/fD5PjRwH2QAG/5ilAOc+tyC/zaAsoYN48DF+CvtUVS/PbV6Xr0Khgr2t3sG9uHX0UV8AJuBjFtxdBt/J3pvTn8AiL/MrwAIIKX+Ug6jA0PvDkAa7MaA9CVK3VcHDI8jd1w/fPj1h6GXL8+/wWYxC2UdD8Mc2qMtBiURjGFthqFIy3N836Vw0idp1qIpgrY9DCEtm6QZxEJRFGMs3AWn3Q3e42kwOhAX4PlMwb+buPlwXw6EGSMpsB7DHdJzfZpFCdemWBRlPYygcIvEGIdwKQtzPY+lCJslfNKnbBbxWdf3bRd1ScZhLX+A9zgBcj/g29O0zROt7+1S4OsTkJQMDpSwLZbBcYyxbRtBcAJxKMwCD3AMRxnXQXzfwTDL+vC89ZHeAzvudxgEDhjs0iua4Zw/Hvk3yBNFDBUHolxw9z8epnoas9dnkH/EbEj6jn5rgttqduP5RbA1rtcqs5hbq3FiEhQ6stogwkZE5kGxP1C8hIXNRVPSUskK5UptLuneXwQc5/sVBnstW2VKGrMQ5Jk2cjvJ4gVdwvM5jhrtzvbl6cm83Hy/82HGhyFDkrfwRvMXtyUrzxOJkW5wE2ryTKWP3tkJ0ZO4vdUY5RvTaoZqlatIqoN2yIFa4+c17Ik4OZch3W8x64xbCybRnTCZXsMWzjIM088kfFaZIwkvC2PpqGlQsCwM29UiXishpDEld0p9uDkbJNts05kaLAq561lfR9DpTiX4WZMvsD6bbzLBcwVuj3heAjcW7NfwvsGxi3bab47qPFUq1CgpgWILh0qOCyJZrJuKnlVwc7RN1SBVKUZ2mrhDEHd35pkCnmkdrKLnPms6k6nVnKc4+8hXUWQVlwqCZ4fDQag2/rZbi9QNPpEQjEFygxfeGWLPUrLdOphEdDDk2xWH36DW3IYJ55qw7gqYTrPTftfWjUzBlXwsoHi9OXIasb3Oud60HKmyakhvyIVv4nLZQ17axUjiHPk+p1YH+QZJ5wpj9Q1CcqznzbN+nlk0X5wh3RPEaYZwu9DUDgYUXpYGjfNHsYVmfuinjTjdLVl/kc2Xl0hYAfpYK/HG8aVQG4iC6q3KX4OGk3L5Ot3bq0BKjMU2KlQI7h2WakySZG4i0vmGYnXTOCEWvrsj+WgKt2eLmHm3PQRzGDSda3Cg5twtsM+EdisV2uin3VGab2etHGQ5MBFu3lwdQ20NkLBAB9dVcUVMhPpUQEfD54SdaC8Zll0iG3ypCD4O02yGXeDrHPEuCczgUms5jaNx+sGGCsxwmzO09dJyRe33qpTEqFCvgo00d0MqWsP1lOG2eymzIwSh/fRMTFsthzeimKZHLr8ohEosZhGmYHCLCepxrjQtx2vz6Ohv4eXNF64ce4L2Ur65TCvIv/ioSci1OWUVn8k63d6qR3q6p5cEqavQOq0yHg4MaEVtYC+9cFutgxrK2WzOqoT04dnsDT+oOXID07cbHhyOM+K8qqb49QAuCcm7zLjwaMEn2HJpcawj8K1IwB2hToG4X/bGaiPhMJNj8F5Y3zCZ149wmCFn5sJ12fRyzYSuxi98RvDQ7Sw7gRRs8w2ryaXXSWrZtyEHTw94q21NjEPXIQarpIVnsEojSprtBEQ0SIbJlaSJThwIInuWgeskh7BoWWd0DFHnhMsRYW6SuyBZZEi0OjUqhfC4athsy6R+e6jktbHT0Cva35QgzRpWYcNLZZPIsU8kr6KAoQg3RAVNb4y0yOra87Z7z+9rS73RFcQSRiRvuCNHLY7hiRCy7bVfC25IItIWW2ELToCluPQb4jQTW3mK47AHBUjJulkfLRD4GixEncN0kk9uc7YgNmTuU/4aI0x/d0qELkbZ6Uxxp5f+0JGM5bXcqWd2pRRMTYKCkrWBMKmA8aszA5ecIsHXkPflwDryttDMbQOeN66HtX4OLxJt0fLl6gAliKGQ2/nKWkLqhtKgq6ucvJUv791Zbm1WBZm1eKNtayeeHtVMzI7cQuGvaiTVjQCzjSp7+prgkjVudk5AnZIM11q+3sBTGZoyxDKAWwnyLdVDW5y5emJ8WxMW5jn2Omdn3jmQW4bpEe643VxUw5Qqfb0Ma1/zrrs9ftFjb3NzyQqDGmypiUyxliFgL+SUD5xbuxTSfsVf0djNMQmGM7nJz5Cdb7Y3koPDnBPL6UBgk9xu+i0icsdzSIaqGxftzIXkiF7lAXw4y1NX6tZTg6MYQb11W4FZiKGEsGS78tW12qLz7XG7T8tjWEj+4VpDp2CVt51cgWid5eojd4GXF0451EuL3Fxil5v2vM2RnEeoiwOBMEd40xhhwk9pBmIXMgPDza20/U3aBUs0uW4tbh/w1HbedkYIjA8uSm20NWgZPvu4HUMItCNYv1dJPd468QpNrWy7zbMbWnRLfyFQArGjUDLOokZX29RsFjl93N0cbbk7blTgc0zILPgGiEpdMJysnvkjrHBeO6c4jT0vHR6KQqkS+2N18lXG7Oh2pioIru6ROccfyI10hvbW2e+804468vB2KjG9Nk9OzIw4tdfFWWRJug1m8xIJlJS2rrsrMDFteoAb45xSDOozhS7bF5HUV+xcrkiEDXV0tlNhHwkyBFYom5gqmUVO01aMOaFToabHN+sCrvzyzMSwm2AFVpzOIrO5nZgpQrTNTqp5jjhLRGxODyVJLlm1bpGE9wJDI9wrh7Wczvb5Kp7H0MaR4NVm51s0VNyO5RTOIiB+EOxu5iZNnbAdxcBqmoZ2B8OMmuBnnKuvV9aaH7q+wyFTPnr+ToEaGNrDPgglYBsG/JMomgafqw2rkuSJcV2/kndMD0P4CUGhkjk1OHpWdhzetJ1ImjOy2uHAsewbdHUSSmNXwo6HH3L0pJLNjFfZDeto0GGp9oHBJaXC7ID3IB1IrnyAElTgNuQwHhyw5+s1PbGeT+FFm+q7m84iKuOeepbgerGDFx4wduoh7YVbDCINQq2JGTNbE7lXH6iGofkrTwlqeGgkhgXqiUe3UoeWRpRe1NuKBUbUTBHbhD0lvig0C895d07Ob6kmpHPKVGJb8W66dAPBp9NVAjQLgq2bdhJMirImxC2kipcjrwgJjXE8N0fl7drvMq30DaoLd/Np7XBoxE0NmVeMPQPVh+1s2nGUgF0Rh9+Tp2O2EkROtREi85pNnDHWjt5xzRQyMyQ9m7frDheXScSEa9YmOrJE4WAWQHEM+wExZ1RXBYqUKcq0v+224gEReponuRV1og5AUYJtx3DnW0ydtsnGP6qXOQe3M4vzgeOZXY1jg+eBw/RL50ZiB3QNHY9ngXJ1OOXqCDtMVUH1TysBpTsl3uFLEK2fvOAAQxeaYNNNQ6MsAQP5cFlufm6J26b06T5tTtcaR+ElXAPRPU7350jNgwa51DuGbyDWmzY4JNAyBEHJfLMV10bIUC50Um7dEvHbdR1zapJCOzVVs1KdwrCYmpCzvRDkEt2BMMdPTaPnfRXeWAIEBwf1QEsudw1px85VxYc2uQ+ZJsL2zE09qn0D3/D1TcAFil6oVS4WsCcsZZFfLuGlkx7Pu26z0bnpgm+5rUR23IGbHi0MohZFwKmMZAqSZHHTlijDAsSO8HZFwRgD+5U2NSmNazWgRw1NMS7r6Q3Tc/mhIJYe7Ku3npV3qXpG7HPMQDyMNAY7pdUGV09a3fh9T6dUihO9Uze1xXQ3puPYjjGCmd5c1QZCoQu5cW28hPfsArHU1kmOt61ZEGsKREeQU81Szw8NB2b5RvUgFab8eTOFg6zo6D5YQI3k+yTwQsKanG5JddWo84pmboUOXSCY3oshj0lrzslWHE+ry44zeWN5FXxPgPwgaUUDhtdrlGGmiYCYHcIhBYjdjit/fsYHT6oLAsQB95oCV9j4vC0zUHEKEssPfBGVrECcb4IGhndFsQ1EO7AZWDYSg1ClqqdZCYhoHUJBeIhzfHXMV7Nwyh4IaKkim2NyYDhPuFx9GYa9ZElXl62szTJ/R9KQA6uinMyMm8soGgKiNNhvyjM7xQTpgPoVtCb4xl8fUPsMNWq8IX0X3awpO2B9DZhq2iebdJGSPod6bKnYxQoKg03NJ2mvSHxkzFjIwS4Fu4bowp46UxbGjUY7RHCjCQimlwJxdiCFxJqtwTbwluDW1zS6ETPVkOo9QbHTZXOmoP3UOiAGQd3oXbCm9LW+4kS+WJxQgcczV8FhQkYl14r3rbZYnkgiPedQg5/nRg/7Pdc6TSAsG5I7lxxtwGs0F7sp8Fpdc8o1hI8ZGDrYTSsuD5IKE/hlvgmNjoJb0RNyuMQLjlLk1NguqhMZitz+7KkBVIVXrUhhPFvR1LkhpiKfMzMSeL3pUXBSskOsvctdzGmNuuihPBARUsgNNwW5X78+N5i/nfUutGMP4QVJhPxEirALefPddkPAdUvWHvBEqQRV5gbINGcmGnxpOCDZKXqwOD3o8D1NKFPocsnIFqSsurmFrSthsgvx1tMbOGq1tAOCQKCwLxcEwVROgSh7v3X0rSiR8D71SSRrePwGT8tsa7RzkKOxChyVC9JjT1xsUTBcrBvSgI3NpdFhGqPdElgisYabTEE812EPhwZFYWgLGQytXWy/XeFoJ9klO2Xrs0CG0oGTV1ZkZFx6qN2VZIZDCIELKG+JCb8hbzNFcNo5t2rnVUqdGjgoEQ0KloUH0qn9LYoN1aE0v+523F5VO4lKUXVJUzhO9zeVEa1qgRQSS14qEs7c5Zo8uV7KGgkOs6eM9W4NBUO07s0gx+BonOHjg3OFnUt0Qw6HdZOuNVJEs6VPxUVnFRFs9QZ2g2zFVG8Hhr3azBqWYBzSIU8h4YXakJ4j8WmrA/MneSBWuepqWK9Ywr8ANVJxihMtIYPPVz5paPpKp9C1pTaM2khQd6NYf483+I2GQAzoMGt81zUwyrC1VG/5aBUGSXZsjicYhXxfvRgs1EwNhtnKjurBMKRKdtPZ5CH0FvAhJVUih9R2HcFsBYP8Ij/AIM/IyWwHiADEVwoRJ2ihCsirTkJ9syBC3qz8wigcZjsFIZHPS627C1BYPcJ7mm1sVN/ORRXe7jaYy/Bce6DZ9YKeJcZJ4al2sTfr6RmjaMVzE0LMST8x+7BZeTBV2uIFaxTUteq4RR3BpIgptAOcu9K5nS6U68EgJXNnu2opbuVFd3QLxRNMTCG9Lt/4Vb9XoNlpfdl34Z6nl3BWnhqjq0O2VpX8UGos1/XzaxFcgAfIxUMisOvTMpNNXLitup26XKI8BuJDeyMj7Okao/MGOOvZClZX/fG289a3tN+RinG7ODNXQ4I+8m9I7jIUjhXnGWNL1PI2TZZxNV30c7kxT9tzJUMZxuPadtHpnaoll4suQVvOR5OqnUn7VMJOSE0Cd3fd5ZSoXlQTofyV7Nxgn0WgeA3yrOaaFenUm/WOizUaCO/o4EDECOCKv3azekOfEC/TSGx7QS+KsmRvOza2md080anYSTRcIlB0RUsnGkEW5PzsBax9pHO5nNaGEsqiUAcBErLRXhdx3lDlNr32VLPZLdpNsJyd4qjnHbrUgJsUGtetGzfwXBFJ5oeIPVALEjioNiBVtN8Su/O8swg7YbSwYeJq7XO3Vuzy5JQ7HnQ6etBGDk85SgDXwGz67IhE1rXBNdMVbEfSoZtAs/uVCftWz2Oy4ikReS42AYnWFCRt/Ezf6+2hz9h0daFQQPxqRUnlwokyWJHZayVfm40AoXMp5Gql3Nsq6e9Sgw5D9+Qs1WUWeafTarmStmlC1yTBmM3FqI76YS2dXKw2LmhOCurU2DfHIvNiQad4+cjqkaeTcu5v7fNCgexo7xE1FGVJq631LoAWritoeK2Eojvv4EjbbqgVIA99EKTz3G2S+VrrndOFpaUIuWG+pPO7czC3N0a3TXs1O55IaR7rtzw/bcnSPoc0iJxS3rr6U45RqkO/WsY8fpIV+LBF9vLtKO3rqEyz2c4qdW021Wg5ZTUuPin2qVHL5X4jRwTpnFt40XUZNl+ApG+FpVpUzDtmc4a0FXkwg9vitDa2yR7iMjzVLo2cHqYy8LDJQnZIrL9pV2+5VhKm4BnJLvh2o6kBzc9z13aXcld6TQOib4oJT10PaYbQ0N6tWhw9KkG7bKqR9nbdstd2fVqJFoWbSYySGbmiuR3Isi472uKdLb8W8XniGefpuYEE/qDudlHvhPDajisz3C+LpLlclQzbIdVMICl5aXkHeZE48CwXj8nKFkQ0dDqKWUD68dhaSKMbMn7dzYSrsYHkFDfs4HBo7T5nvIpWiF29Ucx8Sks5JZPWKelzzNhUqpSQp8gkLrAcwAi3RAHkmOxVK97gotY3hxWRud4co9elB8IS2EpdtJ2T0hZOpRN7jJeZVJOyPEXn13UYrOcgCyntkjNpj2B8uZ8VcxCYmSDQRMVwGobC2ZRbFiWSuXWxy0ztLywT7XvdnnadQt0u++RoqAZ/i/jtftpQXSsdqhmCrW5VRDv0YcMq2Lxzy+t+5ha9dqkND1hJkm6E3BUDj0LOcn2B5wdd2BiI3nlFrkXkzlOVpLtNz8yGjDWfdOstu83NNBX3nlpq7bay9oslIumsFu/ZWtPxDX3gKAtW5jdhDs5NSZ3Sd8tzf2VjS66Q/dKjj5hkX/mVzh8Wyt5eFtbJJ/P9qTrlvb4ivPgqsmYUy1esn4pnsdXC2lxmeLn3a5GwITFNs0ij17OyOdjYodko3vnq7oSExRzOBgez7lUImuW1WvTkPL7pSIZud3NJSJus37TyxgVMoylXqn3I35wqGKku175YpAlR8xGr+Y6UcXgPoeKiaMObgy9zV4v13Qzd7Yz+QugOUaVzyDVPclX1Z5yabQ/9Nj3b5aJN7WTrJ1V+NGWsl0qPDYOe2EAqtjng6E5LVAnaZx6tz+M6jgIlaoPbabvODemcsbv5nkg84gICOkFFaQNqyQPdr3tvAZJhB8G8GHL0bns6t+wi5ADwcLntoVUbHDKkc4O+m9JcK6fX5mTrzHa9lESLK3BT6vFmX98Sm3EEqcPmCH45HGpWTM5aoMQyPT/v0ONmtxcwjD4g/V4oDzs5hR1kh5hyE7mn2RzDhNNuSc95sV7HBQXyDkO+zQh60yNejnhAcW0eI33+2G0ullBpZ1UUHD6dFrQqmqJao1dhsZFtxmK0cyl7F80xNJnLOMVCe7zKg32WbhYmAEJVamHETLDGXOiwXFkkIoNEiPc1ENrBiKJ6VsYKLRWpQHWukrzbI6GHiXa2E7KLLnOnmXUI54HaWFF13i1NmqjyaXPoF+jJ0jqguvrWip0psGlia1Tt5eqIIo2tqZ3PXMTCWKxkje/QzJ6xO3ijUlVv7reMSs5xH0ezG7aEGKzDj9AeX3NzTi0ZZEptd+zRAM5PMqXZ9riz16wqJI4G0pReOB4b9KCtMBfnwxb1oFZDWte4ICud6ewiszUQQDdHY02xNC2t431yJTK0gnXZR0uF8Al2z5n701QsELaKW8mJgsNe2W9WuZ6YZ8JwSo0qEcI4pPtwwTVIXpHoqtQva3IWXaf0fgMZ5+0h0hQVFjdbSL/4uWset8cSkUTKzXLBN7NL5rqRcYTTRRzLJoazuCTjSqJnfOHwi5zZeF1D5+5C481TaB83UQm1Idxwa0J1a2FRer6zuPmJfMRVqVFC6jZbFKm1TaeLpJjeGPd02CYieHaVrvFau+1Kcq6SOqS556khnrar1TorGEwNKCzpPa2TYtspZLZTtGNyXB6n/k3BFNorCh3nmoxe4nvz1kAatfTYGpYSj+Rvuo5J0DKXm07aVGy99ogrCx+FHWPNTWilKxV9KOC4FqZmjNVmJEWhsp/l8pLmCrRZFeYu2GWXuE5cWaL9JGiOXpFSy05dbSkm5bZyvsov0aE5La7CMo7UQqu6kz0P95dcZQ8o4wAr5mY2ReyIObd1ndt5fdkuMluNxdJt9mnE7Dr75joYc4v70NqFJRt153S3zfqC7874TKmPu+XRPqjOhed7IhOcXU8gbsNlOy/Ypoo+4+XzdVcsjhdUXwWH9ZQ0q0uy3hLn6wLDl1QBgsysjTE9APzjUYJd5LXixqejeSvKsO7nZpA6l4YX6naXECCSXt9KWzq1eY7LWGYvrzBsEfoWDnexc8R9LT4gc8IU5ouDxjS6IMYhjbVRL/f4enqbnR1GND0eRA34YSYoiwzxKGeDrFQRLam6r2WucnDicDhWfHvh9xm+qPb6hk0TNvM9ZpFAOypm3ABWiuxEqg1h5NRWlkpHOwv2ImnEmes4dU8oKw04AYferVZLeofSJi8VomErRdWct9ZJmZ1a5eLxs/PCjk5XxmfznCKXRUBo6XHjmFIRr5KVxt1Surk5dSYrB8gF2lzFN8OSjlcfnq0iXKlnjG7otWYvOl+PUCHbX7TteoUxF9Vt9YPY76Zoy8i4a6606a43mfZgqFJRJPsZnyw5jbHhfHE9NEi8qcv+sl/MIsGllrKk5DAVOW1m7Vepfc5vjYPuE1PaUzIMcnJg5rYCpERF1UY04euWSeiakxd1NPz/YCyqihb3MZwHXSym+u4Qr9xVxDgyX+9BIHVsCYwHiaQbY+wxaBb5IkU3/FVacclVkBYIXTPqcXNqUbzd36yONZy9S82CkBFzK0XILdES2g2kULvKPYeBVuhZHOq3zJ+VCMiUq9vc1LcGz/rCbr82dTk4SzfRIvOVeiOE9boESTBI71IBkS4oOxOwq2XapF23iWeWxcFNOLrQrqGyOM/qtt5rznl2k5Im2iKbC3sLmENX5uvUps1EpFEpulxXiLDyICUrliyI3Vczgel2sOfFPrA4Aev4unY7SLbmmO2Op0QNjqLTIYiAPa8OLFJqyblElu3R1NBo2bBnTJPm3tYGBjCqEgbJMX46xYv8dt0sTaGRAJOornE3BDT8bNHmUo2VKVfdMGUc+wTtdup+X/uzIOWMnQPRZXteLrSrZrOiEq6QPb6c2pJUaJFbtoosyVagn6KKVFcbXtKmxdUO9ObsZaFNt9EFiO0WopqtPt9Pj6pAMMhSJGano6OSKJLRm1qgEoRpOoLmp9w5leG02MVNz8bnaSqbonWF7MwlsWWD6905h5BwJdSUt8ELjHDWpLc3BZ5Yn5cCbDpNgUHK3MCajW5XMBNxtGbbFAir4I60wi6KZk4sl9DtcjitbkdLAdFkB7VL6iAdK2XhVDKi5Ydqs+5iex2mEO6lvM97EtXyzuJg5AdfxRN5dojwPuxBsq3NuMquzx2nFpukCDzWiLjF8XSwq2OoT70w9ZVEk9RptT9U/lKwZep6iIQmvs6F7DZXb6udZS8vAUbp642sUmJpVYRU92WHMevzFgRQMzTiVs70KNOiXon40audI0pWwor27IxGQbY9K5oj6VSdL0oxbMqFuSXTbd8HUgdtBKcqQYJi18q889bkpUFqEXUMDu+gcnE5rXhV8QlN3qWrBJeYhb63Cei88X0umSlM2l/DCtevWjifHwlZWu8369yBImy6saszbCHWnpCnOj/3jRy5iMJsR8mnkLf2a+EisiKikKhfH7yQEnMjaOmZUS/V8IqHvqZvlFaTlpRTbzWFBYEvm6nJwV+AzIXCW1a8NWzo8W6MYCIkbzYWsidu67CJ5Lr0JcXZNVIz42hTjLypsFVX3ZYL4HVZmRW93ZL0ejOPleM18+cnNA9J2mNaxHVOtZKhmCVj+ELA1GmXgnTOmsJKh+jHzvBP2JJO1wsr1ZaHGsIJhjgfj3WyOqyO+v5kSvGx7RN8Vu4Pdbf0y62OLGanLTY7yYh7xGjJOW7NeWfbPX7gFv3l6KoL2bre9rus5gmLXdrKjKHKaAdbcd+i2I4IgU+HD0gbdYV59M98PTUN63ae3/a2LGPTdp5Mq87uKRmnGYye+nvy6GJqQrsqV0jTM7qjgqqd5YelsuVa5Uox1UwS54bYHyKXpvml79v0dmEq160qkqTtNaeshMMYCTIzzJvDlMGzi00gDoHQxDY3dqeloF6OZXiFimkas7rreTl3ltbhPrPlekMXOmrTRFB2JoQaV2xeJkBpbuuiEIzqLKyPhYYGMc8dWyWGdC5eEKV9m6kgbL906x260v35yrTyJW5ZZHBsUzGg4UNnm4clgfJnmw7R2Um0k9TAr36GHdK1WUEH3l8HcHiTSyevxV7rlK3VqchiUS3RJCGd7toUnuIlJ/R8tVZwQW9pt23x7cVf7tyzVQYVXGf+0ko3fXmhljqLKhiIXv3YqpbHjXnMZmDtxSe6DbYkip2V0Ks1lM6wa7ardcpM8FMIX7i6q5Kojq+l3RjxwSGu/PXYbMt52lqy7wbhZeb3fIFdbyUc5PrGsmanK5AX67gxbutZZJk0sqrUBUXNNxmItq3p3pXL0DRBAAl8G9MEx91Z4NymOKX48RxVEJLUs2bmX8m9JlzLzF2XooaDzEwKWkCGEpM8nKc9c6tbBH45JvV8yS3MvtvLdo2vjwcp5Hyn9Dc+tky7GwXibYdEZTzazGkpMi1VlERIL/vDdXZijmyVe97cm6n6ejozKRCs9bCNoTG922waOFJdZH1dUhectspyc7tqJ0vCrOV2EZC8SC9ie8bPFq2ggLTDOzQzRthvAV92kLNTwp7ana+n2V70UeCVIzYtL4Xn7FJ8NdPdbK93mp2g0NzsCn8ZniM5jZvVqUpOt8i83I7LbHo0TiR1LfbrZgX82tKI/Z67EXsg1Aa6UPeYSTPrqZO5h62qq4YFUpnVfnmeQtTutEsb73jlt840b/B5VmGMcKimNJAKOmywaLa8Hvpu613Pah0CweB0ddls+gI9lTzON9Va3yRCn9fXywKqZjFhzw4iyEmDbnlcG/JOstpNvEw2S7Q+CvLsvG1LalZ1U73fF1u8soJzFtmeSsA1Qc6Lg5/2R4M8kbVfcBx/zM7ErGXlvVv3G3Ud+rcZvkLbuD5q8ZSjM9pEVxZXcX65q+2VWbNr2Fyk5qVLLzCv6ERhbTJ3C2IUxeyVEjuqV2+3azEIFjMnKMXz1bla540sz88UsJfOucKD3oCcE8PM6OR6gptp367yaOHFZIOXN7cVLUzFZiuMam06uUS8Yyxv4sZLVrEmOAtZhSr1WvlhO4WRELcQfrVJ5CLl7NN+NzMECeF3LgEbHa2uYIPu1KtZXrmUA2lx1bFX9FQ716nllN3NWmoyfzDT2fHKzOxDzh74DSeQ68U51JyUXc9K56Az0nWNUayOYqcllcN+lfVy1C5Tdw0siZDUsYDPULLUMOoWYdd1Q69zw2g9diu6W5/nE/WEdmdW8+dWS+eawwRlO1dd8uxx2Mn0O7KPrzoSSzeQ34RT4AdWSL0LTstFNzcdVkpPqG2iut1spzcyPGd9p2wSZHOYC/q+i019OT8XClziq7NArqiDq+PrQ3oRj1nk6cUeyCBBpBRL2elcmHsqmgeaSEfHGxd6EsLOgkQsE2O2JgQQI4ToslSbPQgg1hW+jmY5LRORcyLX271iWFBiCvWiu52swGtjcpUHdAKz4datpVvqGB4tQSvbY243f4+U8xXvQGU4bzhViDOTvS1MJLwSdLepbTirQPZwUVWRV4N0uT64VzSvNH0G5RRioLVIS6GwTmMkSjDt4Bq85e3kadCHh2pZ4NY6Lw57Y3e4CLN9jtAVaURKh3kshiBCEF29KJpf1vh+o9naDs9CrjqT0fQmFfMb2kSswHFLaLfC+t4xp3a4Zb15Vsp22xiLRTO9Qpp9kgq0rDOFavNuadGqsUKsbmbtu7kESSCZ1HkZSKgt8yvakW5KS8QdYN7Sv/qhxSYg/Ds4+zWL+P55aYlTCFy9dhOU3S7cGs0uhbY114xBcklchIFkGDEIUlEOgi/TrA0rqZlKkaaEMKU3vS0her9obvARcuk9r8b9kaVE5Xqxl1HM4VhGscacZeW2UYMo5zEhi7ALXQoklRQZPMt6I3C3kepcEwG9qWIuOOtj3906Z2Uvt/T0pBcH9jbzZkhYB35+1KaLqDS1qJ2nG1qfrjbOBj2Zi7rXKVZyLgLutOcd7jA3/+TcEvFELomltT6ViRyGGHTgsCu5aAwHSjqd11YHFJlCQQDkc3+eEsurr1ppGdV6RS2b42yBF30aFqnSlh27DFp5ftApEYgvlGL6zIfzZTmL5cWaMclF6AZ05GWs0HAbGtJI5nxWU3ZTY9v+wFk6ic6hfa4e3KM3XdJStuaOIn0Vy+kBrQ4GEiDhni8XZVbGAUvKRau6hiC7u4wSrotiHtnFYsr4ArFGprwJrVedesDmy33vSostyWTLueqZkTEni6WM9rLIyP1RM3xqnetAHuuzxx70+YnqZ6aTRYmzTBLRz6OkkMkSP3tX1lsZ+poyaLIT00JMJATEfHxPn1ZJvKFVPAyUMpjTekCbM8M82fxawLu0gddqyhxPWDR16DIydxq5EnIe1lqxq/WcpN0ZdIRqjV6IbnohkEAkvUIUIrchsjzjjuYlkiJ9s87QK9lgecPUKKFhriVb8dmfQxgpszWdHLVembpauNrtFwFERTreQMAcLjdSbp8w/6wGsCJS17CWgBayxVTlFZRj1rDvF3DCCWcdT1ZKBZE7s9tjLXTbU9os1sUkmcOO0RhZml6qc71IFg6M71FTz45ZiZo7Gl9KzjK6hInkn7dBs6lJs2dqgT+cI2mdu2yezi63fVbosL8X3LTGNpICreZVI4F0hrE2i92ua/CrpkvH1rgRdbwkSmNz1hZ72la3q2UFO9NEx5wazxhb0CHZO8/X5rKRu20JiYVSl8I2tpwDK12hWzo7pKy8jBtnlYmqfLgQKwuCdAXebYQNdpKNmPfWrq6vtKlrEzZJIqRhEIiSlmSX0et4cdtSs3h+0NywdzjCP8/U6zzBPXi52svHPTtNaqlttQvEuAtV11192QKWKNwVCRHPm1JWTMfn/SoMt3rWB9ZuWtB83TZkPT0tlUUZ8GGh0poGocL5cmYss7sWTnxch+0p5YSSmfXuSrVvfr6ITAbnSntTBMq86c1N5cbaHgPZJOtMeTZCqAqfz06b2uwXaa6f1Xgqn892yU+t9EpNk4RNk5bKnb1h0TFK0wJtlAh+ZYV1cFhG04tQl8pto5lNXgs7UUjKcGciMOFbPT3HVLcA3vBYuZ0y9S4+q6WnHeMfRY8lFUVTC7xQpif/ego1OTs4h/4kqMusWoZE5i7m+goniYuikSmk7+dJSK1t5VLidpg4HOWWhHVmOxeTU26Jnjv75B22FowsT2ukDaUru5vZiwoLLoodmGEGd1MCYs7imqBOQXfdiZmbxZ1XhcDvY5Qg7pJ2qsbsXmCgq54aV5FJCFWEV+aanNc7RkxxRTwQp+PGKi9VZUFZtcbnu6CeLTpzebX3V31mqIRLJhbem1Eyla9ZAm/Ds3UhBGtzZFF2Q8xUrGtmVcvNMjpD0Qyixby/pQsVb5fshqLTC0lXs1NCHCCN3llqL8hh6RkhSWLTDl/z4dlGKY3Z3qZrFYqMLl4fJAQvW5lhkKsPR2S07PS+6Fyl0dvWsi92vNpbdrOJ4Yu3USDBmuI9KdGzGqplIaKsHgtTFWQYW6s4Xo870ha2PmqU9ZISp0c984ipDmuwCyzdhkmv1r6H5ZVxngF7gk37whbsqIqYzF6tLs5+flXs+QxE54QdMStisfKDDb8Rzox2Wu7wBM2M7fV6Hgo1IeolnKzll4AMqQtIRmxkXZ6LhU8jOo5h9P9L0VkrSAoFUfSDCHALB3f3DHeXBr5+2UkmGLqnea/q1jm0JTaGILoqyMf3g+efdpBI1RLT1k/jOjhgeWIgqdg3CaSWOu9nyx38sqdl1hLzxMh9GRApx5FFsj3ishaoPr2j4CIGqQzCYFPmeAhUU4ghRCp0j4EWOop5dS2gKaTjeLFuwmlBCebT7bzwemjM/dcaDJM6f62AzM3B8N4AAH85derLobzlrMu1K0Zdtv1/VghNKwOg8J9uii7euAtCUJ/+BE0BdVbjvz+OfPr2zRwnrpH4MLHtxTH5aykLB4QTIpFlTBzo/i3P2WtTozUiTjPk/UQPz0v4S1AM0RhC7WRZtW3WTQrq4Oo1kmhozIz2ylTDrkQZPofWemNiAlNKCdusEB5+4AHzIAoNcgWF7ElxRPfk1qDXpnmaBBHntILcrp5Zps3lcG9/mUoKYXt+DIIKXsgFh+6gu4GXzu9L8SRDpETsaY+I8bMuiD0pQ1VhNu9k3CSoY24ej25IkKTetJLFORVgj5BMZ5JcaGc42zkXDXJdkTCXKFajEsmEPPHoZ7Yt7uy2OJ98Lf/Pb5v24UmzXMnQRygrscoCSwnnbO1PEfyaM+z07yqQ7glr04jkLrjTwXDS6C+OzjvB33t6Yx7IUTH3zppuWbwRkTvQxUg3e1wfCT06cnzMCqvKRHTtoyfYTUcOur1BK8JBGRVsdOAb2EYskYtmZAJ/pKG5kUN0QrMrQkLbBvnoVq1/M2boGI+DHfJkBJRtQvmPZJzBUkzdp1ItdzdbH07H9Rr4242y4xfnD2bX85R5rmpC1YdHW9EBB2sEcZDPLQ7NhfAxW+M7xkSGBsU/pHQ9FmvJIf0E3B68bZLYyTHxGpNLnyHBAqVTTHitBuhR2Y1TUBQiB9yWYxHwJCgN36RQR45Rypwqolf9GWJgprfQOIiWl6TdG62YlMQgwZQUpV0ARcy7hBTqDSAjIdG026BmN058UlxTj5VWvSSL8G+R9jB9yZxOBVAULfkA7+7OlX3N96H7wxlNq6SZJadZMgNbOAaVBsDVllZ7kwyHPgezCsO0MNzK8Tn1RANn20rzGBsxIZ2VdxqAlm/ZV2kevji+BjaSnliCd+c7PVZuyot55S6B5Iw3AnyfajsICONPle9ctpL6Z8lBNSxYZuELW+802eLr+ZHf/Pf991fvfjnc4aO5OkvlvPjE3PP99i9kdSGG0vwp/0EjnI7cnt+oUzCW+sr23U4V9gv+igMtFHr+20cXSCZB5F448PVXTzMGVQEc9WAlwFIB526AB5uThQLYM7lTu25yQMi6HC8BGIbne1yTg5pY1JPvEUSjyLL9sw68QXkPKVx/2F63vo+v88xD8gGnGI+IwXfDD2er7Ek3jXKeSI98UuinzMSMiR5XyP4RXvmXZ8gxY7CVRnK+5T/0t+ybWhyuDsykIS/VGAYeXJzzzV9QtB4z6Zj1NYehG82wXuDIz7y5s/AKmX56BDEPxgzkXwMBLvvnHWFZhbb5ejCGJj7T7BcbJuWQwM1QRI8z+QEe6FF9Q7grO6WofY2m6zRL9JCSfpoujsGlpzo8FqQTYJXQUmy74fk2Hyxu5ZCceVzv6E5vgs5fhlBjcPwNRCjO6tMLsbMTXMd1Vra0NbMpKlcFhuWjnNktShXAY2JUQWPdqGLhbTzRsP5NQ5Bp26t//jReX7MC+NhoQActCe+K4/723ix3jpbJ+nbr9i9KiOIv2Rhscujfj1GP95wQwIgJKJMHwi2t98OPJRIhCgbs6Noi37g1nAzhBsFcibscjjLWmzBQISQ4mFbao8pQ7IwAAloSChpb+09uoeQ9CaPuwm6yCNgwFNNjn6Mq9VEr7QPd7cyNZP0+5NFJJgOy6dfhKZJX8Ny8trenr6a7S3N8ldCEf47tQeWGdqK0+Q9RT72Ucu+v+o5Fkz9wje+rWqzfXimYCJLYtEB2/NM/ZkE1f0JplX7o9W9ZmmiY95XMmvWLYZ6kHftninP3TevRRT1sicU62v66BuSARdedwfm5dNNn9y7W8unokdqH0WClvwJ5ikCHMBg5Xjmx8FBsmHW6n87Zq7KO+z89Km1sjKpAFB7RDA+DejC/OEfMnFCoqZrbvdb6zIuJwpaI7iCYLi3hlf0c+XVIxcUXAsHFXz/vYhor2W9OCb1LimtlD5vwNRo4kwo7z/PSd1MeyJ3Y9aQBWG9RMDzueP/UtQmS/zg7oCj2rPPKEbJjnO99VZsqjvj29p2ngi3iMf31z/fgBzsoO+OQb+Y0Low+gGXj/jnjloDl4isVIGoKxMIzaq4Ks0xESo4wzHv8Ta6IcOFJ+Z50CfTNkrQo+5q5ipIBQhfN7cr8J0HR3Bu4yWqKWnyHPcZSLl8PyfuHbR1PA/Gfp+6HSIsnQOZ8clfdhmn9NBj8kjy9Te87QofmRDa5LHSUKU1aESanTf/ow0WfBRFPvAN6rSlhJ6vyj5wocK6f3NfcSW9Qmi7YnBoYT7JI9s+1eNtOGQliWiDLx9/Qm+n4rC3nrJH/1+C0gjvDPt+HQUKBldaLTY/nIFJ5JZ/gDMdg8XwHZn4UHagguJtaZ77p4SktpHRYfUJxhZI8UmkLDVgt5E3Hj1qzh8F+7p/ALXyBN+VImwznXUV71coa4s+F/hnPZBl8BrscmRAqA2vFtH1+DONJtJVjIQPGTMUmwR8E/zaPosho52jQukypT3QsE0rqpyTzS7DD1T4PoMi4t9Q06qmEic8DZZV56aBz3v54RU07nbcdV6abKRED/Vx+ONqNy6mJV34KJan9PSD35gBSyaGmE6Jm1wIRX2v562JCx+hNQiVK1bWLv1vdMp8j236WllA+y/TrtZoVpUHj0k3jn52F8C/7iIlN+os5DUgL/NwhIVqNTE1+uYQ3Rp44CsM7TbSvq2N5CPqWNCwch69j/n5w1OFIULV/NCzrMcKg6OcoAHAIv15cbAh5bJOs3iztqbJRLREd8G8wUR0kd0hkXRDxdjDbzNHQ4BdsLToJF6Si1i5pe03z9GRqVzf/FyqZTjvE4XwVJJ/L5UTd9v4w0e1pVU/zdPr7YPHYrkdr3KD4dtJSu9+ygbEMvQEA+R09W7cpZ8sej7WU+HkfErTYesvUkq6fegsVbX6ujgwkHCj0sVcVD8ey9CsBQplozlD4p0lDUtT8X7NAPwz+K9z+UKRw5N+UxdYC0PFzF48rOkOhdtlD13XcmLEslj17EnKrfW0fQ+MyA0CvwkOOg4ivRQVQr88bmdPtvRgqEqQH3XHJEyR2plcWOA7LMXDcj9vgjKT9o31aQC11UE+YqNTdZm5EKKh2yCwZH2/N8/o8n/4IjQhGa1Fz72XOd/BKH7biXcU9y9y0sUdf1tny+/54r0uDGth/ZJKJ1g1L3hSNtAVnNRFC7a8vqbFBtXxe6vK7K9ho4BQweB7b4Wh9ij1L50JZni8Y0m75MBP1iOohcPDRycLoEVaQbXPj7w39GKFZn09H198+SbGMF/iD2zk+xWSZ0ZKjjZ+MQtNtDTUjlKMNQADb9M/QrHgdHYp2+N85N5BvfmvSNaVTqMydQWe4YYa4keJYNoohYGeB8sAHb/eWGF7nGl50uE4vjd9QQnl+32U2XfDbuV8FseKR7OuD//HJSAFUFOVpJyx/vnYXyfwLFDS9itgTArmyfErHuytke+qCS4rn/x7tjzjRcfeic50+gjPzQb7e3gC5LjgMwbYv6Sz+UEdlsQRXinPzlL4ycsRZ2E2FmVjR/LzR+loBt0SvJi12cQJ9CZH848N2e0oM3Tt4aH9WIE905ggoSVeq3H1OUsDLX0Lrc0sn1fgITw1cJhKoKiCkyHFJmvkNgyYiCLjyBQrAt7+LGefIP9RB7C1IENNj8BP5vEB8rq8KhXOY5Zy0r1GkMM0ebsgrddsPh/m225gZDm/eWfPjt4Mmqdv2CmuwW7g+2kg6sv9KYlrUxR0is8KLQi8L3awm1onRCtCorql/uIjLHOX5pTSO/PZygVJVZPaXVYPnnRK1DyqUsy9S8AFQPIHsuMDGPD+rtOYXhQrDHyVMtVyHv9iiJZln2gZZNanigcZUj4XsCnPtPkmL0E3L1Ndhx3HimVyPx7tk9zW/4/YAMcDqZJRtMJB7biIGLd9dsvmRwAr44y192wn9yo68jySlosyMDsRfLuzXhguTcudzCYAu49Qib/CONtcg500pVuCZTc/ounB9BfM69MfLqVbjHfcIOE0G8DailHsGsnpTIlxC0cgZaqLoTc/lOoIHYxuUGJA3i3SMUhyYp16cgPF1MxAZ80f87LiwMeHl7dbAvHRUJMSA2x3UrZWP49z7mYfQayHvCBY6IhbE88gbGYESfSo5nJ3vt1/kaA5buiucOt3bjYpuGU+WTvvl58PFDpyx2bjEjj3C8q+PtSx/asIf5Rqa4AGRf9cf4p7NjQ4FDF0AaPNcVn4IpAiHdsZ/FfNx5UDmyDzax/NSoON51EMDc8OMjphpoQrIyrNWqQKhdaFNzTSCQdqZPJa7VPkiH6cL3Qra5/MG5PJNYPP38XEGsveJbwqY8Z2qO1YHj914GwqcefkEmjqNNX9khYiWZfsR24oPGzzJ2Rx81UksVVVHlV/y9kqVEufKzL+r0a9hR0gmsDROMM0rpHhj+vif91robG6t+ijZKGINWeyBA9kdrXTlFXY7umidqGrDQoOdYI5J9uegWnhTOnY3NkFrvLbBinZuEJkVUc7nK9udKyJc2Pkwm+C2FEUFQBNY7oeywJ2V+C+mPaHETdn4+aQOwMHCuWWqNd2MKxVPOw9CM0NYT28M3T1592iU8EfO15Ce03Ue0Xy6CVZ5v9bMjmWwuLV6gi6O7NbFriPeomC2qLzXAcEBeas17P65q0Hxdv5uz2D7E+IRfbTEGkN6Ur1g4+VhdJ8MDKRo3ov9NxC1MD+qEwJIX6IWrXq2igVXX9RfFnxpkPZkpKC8dTbakghP7xiC9AVtfIMXjboIptV73YefIqKivlSu6Ui64udMo2Go1LY/c62zk6R/HV+EDVXtlPZ0S1N3pyL9wUCrCBfnZY6nAiD8i4o1HE4ujiCASjFu9G4XagG4PsmEEQGYTmsGqbW/EmPYMe68W2ksjPKJCagD5BkMzB8FzSqR33JWlozNl91iNCtP3IdZXhQ2UycGss03yGWv0pOsZwaulm1wNQrzyR6CullX+tu8iyH/XZTd8+mh398AdGcHLnFsjuc7K+TCPRX390mN7+DoECqxkdA3I2NxgPKyIHYhcnwdQ25a8zNjFOHNO44RYVvTRcCVR2Xk4U+UAFIyz64cm3HLnWNx/9S/v1jjFgorxz1K845OIhr7QUnM/YzMOA16YWGrIA1TCTwsOigIFpkn3jPtZ/PGoT6J7VHm0vvj/Hl8VVTMK9tVF2SpNhDDp4TQliKo5oBDdVC5UjCOHDog9xAN13KsQCDZUl0Z/tdbcJNctMWnObqHxZ7i+R5vbtJa9hCdg0bYR5gTs1wmL7ANrwvQezdaVr7M5nr6K/JndeABHUdD3GXhXGUTxRhKg+2f5lPA2/vesuIhCfqTJmN5u6BB0bWI4TGj8KkiALbohodJFbPLmfLNS3Z/b0h0U/RHSB/IqVzmynZBzEK+TsmKVn8WcAfwAb0vsqrSAsqFvN37FVziLdERwbVXRVKefVtu44oSFUs3Jy27RGPJZbDmYN6OEiDXrHzqFJx47rKaz5Kt6IU54GUd+ZNC7SpgPtWkPBIoiKQWXSig8Yp6CAtF0poQuMgmR1oATNin3JdsLwEyL4G/mo3GT7D5ukO0yt/SjzkS644YxmC6KqhyMPGREuHXDKjEHiOtKpw80jw3U+yc4YL+hJZilKLU6SOzqDuuZZAwqo38yvEZi3yiz58G2vSZ5OHgEmSIMrWWoaVuXQbKuIIxXcbWMxcMXP3BnChz42w+rZDXFf4CNzEsv6KS12Mzq4Y1CEpzuHVrNzOUEyFcpsnUDJHKbig2OSAFHcZuRypGXevAeu4P9MXZbdYAjlCWe6sTM9I1rBwGcdKfU1Aw4ZOI+Pu1LXRQAdPF2cIpbJfS9QjEpkUe8JjhD2ivR6bEGKJ8Kwln9K3IcRtL9vAp3MWRivDOw9c6PdLYqFgSD1ZyW28DNkG5SArFU15aqDRA4pt/M6IwTI0VsEVKmHUgveDUxWByp1s/rlzXBE1tCrDJZP74EebqWFbf24ZYXmaC/+TcbEvxRh0sLVD1/WvfArTyDgkm7qPcfj8JpSRZaEHrUFAR8mnm7stB/N2ZP4EQ7aS1sVKRsESGxZjYCXUO2iTbM37SH2cc9F81kW/1MS1fD9nt8BIitp2tuEqOpypOZsf6Zk3w24t7SRGghK037QH7gb+KjYacx2egrryzb/milOiqY0YpAlR4GJoeOco6wW4sI/FZccEWo04loUQQ2TNLWcz42Y+/fD7vnEnS3e3iAkBdiygEsyeOWKrByM2+Mymg/CcCqZOJYawQb/Jew3gvhKJnKzdJd5FRNaNv2DUPP8BVDmFFqhjpN0vuTOoV0Io1HqHLOSWVlc09wQwN1iqrMLAMbvvx1kbpBdz5868sbgtGwMQqs+B7Ym70uBJBKtGE1WeEuLPX0L6+wLkd+7SsS+GjtUzFKL5afCYDB21Tef5C92plb34jJ2TTB7D542v82YMD1CahYboVFubE1VlI2RRBvajirqP8tNL/RO2HvOlWdQlRF2OdcAN+UzTKMLq/6Hr/SuyyatkXnLpbHr9K7xUujm3YiSKeFqqM5o5SXOEez//0rpthIfGMcMXUfK5cxx4wwLqzfNdkFiyib72Xzpz+cJAo6F/RYa8k4lkuHewbYc5Prc+QxCwTOubTlNICOpU/FxLhH9XTrx+LjesAhN91wFuF9xX+QXAMQdvOnWhlWjIpAqCYM/HTGtKxRY5kQnzBoh4b9Xx5MFpjysCXhnmMWckKlLLtA63Xbinu482O2M1wPhWrKkCxff4jVQFY/n8rnSDlz9OFfKO5VBQ6Lhvi4W2JHtlJaEgJ2KCnexGDsdEgp3YCVsCyPlkdciHOIo4kIpNB+ZqpkX3dJmBzgUOHnxKVAVtshVzNi/Vb4aoaQSS6PHp3ncT/6AEFhGbDabYlYtjpdu3Ik6A5syoLiujLNJlnRPcz6JFGARKhxUSNkcaECLSsTPPrTx01yV3x1E5+9E7+HTKQaulqlsT7FdKipMdxpcekJTuoS1cBrpp2LYAuE3JIEVhFAqu3XLfx/2Xtsdede5ZXmo9gVLls1fTB4GlJBCY5rgbhl7pwnpEiNko7oIldIlRpiLttJnxfKgJ6qkYW3qPTBVkOIb3IdBaXEWI1Idm77mK6PZqvKGQqeabxefSAwlr8v0ZHLhl8rGiLiss6phlAFaeY4ogVORqCnciYCKc6U6/8QbhO48+QLHljfvMTWvaVyDM4L8qrMzY49FtHi1URFkGOLKsXLgUvnPxvUG4JcfFjsYTCjB40S+Ahkkh7MA+oV7zL0Wew1Op0zsyJZoxbNdfkThEJfgXBdm+Djme3P6AaDfaH8E6esEckfbgaHJiW2A2hGDZ8NR4bBY31nbeBToRXCE2AwwDoCrqVqQWkur201pnWmnEvKaRHBKKIvvYfWFs9nLyTXKMmAB9n2IlTExhv5mweGYU/ehivEg6FNe5xhE7v3KHVKuzV76zjZZPDIQthtwHRVybCiQgJRkmKASH6wv1qgC+nT8zv/sR6vofo6tZ0+tOKfLFa0CNKrzQ1+0LHfN3R/ReZ1EmemBLzd7WZG5DmiWgUwG7lG5xpOrVivraRvD/GhwrBfSvgaGlQSo/4uicNiz23JpztuGItg2WMmhhqY2zBQEDscH5aOKo1zt6W3v21ufqo+/s8wFrnLLjE4xlENaFTYXyiSzSiMZxvdPZOIX7I4wzv2ZslpqeoQh4rsL4/W/x8gmcCx4JRhwtUJFlMkZBU2fyWpIoR1GD9kZrBtyD9gT7lf279auv9Cp8D5aRC7FGRMIul5R62RW71+K+LVOJ7KgjEXGGA7JQl7GBKJ++sXnl6gKQFbF+UTOU7rKCmUUGAfdG7VjE6v7IDUOeAYwVxHdtFCztXRQ+ypg/Kkz6mNd/JijtuBiGmEpsXdTfqtZ4EX4Znl/6EK+/+44wBWta0IAfWmQ9UmAc8Q7Rz2vOohoTdv5sK1lT81zmFFj7wGxA0Cf+sz/qirASz0bdpCdtpgTHhgxtjtO+XaihXayOAU4Yv4KiOiydTNF0zindOg5sPxS1GpQ2W+YjcsrDmw/KObajxT0LL4irR5liNIwUj47He+NB/t3zwWyAAj1Lisq8USUCl+EomIfKe732opNbf8A9+w/3+6nY81AHYKNJSpmQhoLxE1+KaDkNYVmihSlzcWhtADcj2UAirpvFMgeBe80GzSKi09gJ+04V3cOAIAYto8kM/YcBDskNJYGxKacE7xUpIASKmXSHWtuyXV7iSYRE/JD1pQK1LtkTFokF6gqTncLIhYS9E8WC/BNSPJk0tta6yLfhF3PDn+mzrHQK4k377pQCCvjto9SJWkFeGvhUPTKFQi4fEYI/670QHf4QAbU0mebNOg1lKBf7k+gi+QxBcLVv6jTypTYDoRfPTGz4PaGeLx6SJPLSaRn/0OcR2ea3TOU4FL7Mnb/zO7thwZc1QBHq06Pzo7RLCLDKlL6o16wyOBKIUvIxu1CoafwEG0yuhMN6qYuKeTYvXBRsN1QLA4BuUwqjibzmVSHi7V06vxVyinlsZDhmD7fxNEFCZtRqf4EJxs60I7pL8qo48CySHTaiZrY6OQuKLAos9tbZAvGKIS4PBUxachuvwAr4pvQaW6QDrA/c0BpPO94GpLDithi3HDL641Bw5JlzSBiTEQbSkMsRX8J7sj+wpuUhMU6K9u67I3m348sz0XtL/SFdvxhdWtRGPIQ/9VKJiXzNHl2Zyqyyf3g8Wmpw2SccgZbSlImgYT/W5mtBDkkolfOM43/BSlp7O0L2IBEdHc0FRJkdUi/FUeC4uPeMtcccnzOv5RUg5FqOMZVN0BhlUHyMedAgqL9YDRDxuHH5gCeGapW/ZFYgecOaB7QVnt/blZ3RADOe6By6qHXI/8KdxknX2GJZTqT1yo0i8B/kKJ934rUMYEsErSy+0jZpROdhVuuPyJKzXI16Pn/11PXeF7nj0EJGI+EWWeqdNgXebLuwirgdolSE/f5SnfimTnDg+mfJhjQuPQ61IUIWm1787NdpB1AQH7ABy/fauMgp2C3TqxC9OdG8QzTfNWg3a0120ynl5hCDFIF7yi1fSvejUaW3yqo62CrOYFhWQwl4q3oZ4uC3a6uI2rPxrW0a8Mt1FDn5rdQ4P4B2HSxE4AYsHrG7rb2vLBd4X2lqsFAUQ/5zsIyo286VgkpwYygcraczDxWQPU5s4+cOjAYO0HlgxNzrD7SyOpLSSMYhKyYGYc4E1DHvYDgZFRRq2DUHN7lpJXv+cZcJPvd0oouJkhMRwlW7JawoPPB4Z5IiAd9L/X3KhxfXrZzRCFn4QtFbDzyAw3JSs0HMZud4ct4MUe8q9L6PYYMgkz+0Qrj5h6GKQh/KBenr6/MUAshdDDRDsu3Ff+4miAAGoEGxATnWsOAAvp4Ecpx8oaCaqQpFJivjwV247pF5UwYXspRIVwUNHuiJPOx1XNJk6PPEsc2BdP1oArL6h00kuGeX706/NSOjjmS+EN+U9dudnV2ncvRULJ6XoEZ3+Y74zG0UwBQTBLvm0nh0YqfhrigyKVsQJhkT2IdhIH59mOuTLL78SKt1H4EFM4IzoSmG/9NANDCXTR6bQh1wFbF4PuGjVjYdCYJruKckiHF4+FVfCDbXI9ArfZHyf9W8cyMoDKvhEyLpaYyQKzWTY0yTSTBDBc7XVWYhqc6QFVCV03jwCehMLqGnbUfJcpuOGSiRtIwc7pGXm5vVjStIYzxsBKPelQtl1JsGZ4jKD3yoCsJHKwqK8eZc22CsatLA8BVzfkFMhp5hk17y6w6DdxalSgtT6anS31dXRQSOEg0/qAQNOu5LHqPxUxs8gCRLq9xHq/Jm03DHyP7W3xnIvr13KEjBYCBhaspEiQ1zNt5W8XjRDa4oAQ+1Vs91qwIAu1QTZyKGenKMgsGOxz982xc5MW4qFl8spX1WA8+eUB6SiTSf9GyHwzKZMa9dkp5VQHa9j91zsQuBQvarNM1dqcLH5LA+2BOMftv8OdG6mTmgMFa9CbITZaV+PNEXBQ6U8wcXygHZ0axMiiaLfMx9D35x6JYIzcvZRvD8Iq6UyD7ewN7SdbEa1J9rgS49xKPKbawJ162OA01cBOLCII3wOiaA2zdecFpKmbUrDyrNRIkqm/egtc8stmDRYU7xPE9iAy0CPgUo5MG7lXBoG/7zHk5VY1gSGVz4e6KYHlYTjX9dsVohylK8eEe1UdG284oaZF+GsOSmEJ5vuX3Bd5JAEanbSa9q9CHCV9gu+vYBKC3gUYDeZUsZlv8hoIi568UqE/BuBaTo6AT4l9Dwk39g4LS144OLKbmlINaH8GLXx30aLOHekqmamrAIvIprOJznM8LdyyRS7rxO9AHlDT/SLLOaIAuQr50kqtxcsLK+ER1qt4eOthiqxZjTD5qIhugVJgJMhoKDSkzVZvH7DI01Brp4anRlMyQErO83oUk+boiouJQAfhwDDT+q8xAd84cE1rMjWruRiM0lHq3g7jqayoA0GpsEbCVrQK0aNkjjaCe8cxh1LgfJGjnUGOvIQ02wOHrTfBNaFzw/CNfZSmq31TQrmL6lBpOcqEkQRzSIgThE7kxpQCk7fVArlob09N8QQK5pz8jHoZDeMvkGXVTSpve9xFEXWjiO+TZ1kAR9gk9wEh/y7rtX/a0KZGSAiXQWFKRiKleDymXzFvnorhuguAQGZFqMipGLDWyZGnO6wu+JmciAzWoOfNJ0Fk5Zo+Glf+oAn+SsG75d4Ak6G8WQQERwGDDLa4lixJyTRsxpfb8SF9ObB1hH0Rw+NikYavUuCBl1UJCzNL1KeS371LQ+kT3kFAJ08uIfrnmakleW/AbpbxqUMmMcRmVFJS9XE1kQUp7FOSqHOJ1LD75iS0DFfirutIJnZRAEILYUkxST/vjxavAaqAg7IxExSnPHD74SEyI82YyKzQncdThPJLw3dkG0zQLUDIFoMQTNbwGcNvIJE9Uyd9HcLyvUBJgVAJMBHW3CciFwxACLoGItc53vTPDtL4Ydfl0Spfyj6IfMa6RtFqVI42G/wSkLt3yhwnwDqD2bZDuklEDMCASixCnPdNXLIHwe1J9+Gj1Rvd3hCEOi+iNfqRuEchdnwlC9CQASgpCJtSz1oOECoLMmMQg84JcD0S90n+P8hL6P5fpFOBszswseXWVZLqyuPm0/xA9spDMr3iMxwOSglwYkxzc/iNF/agj16j/PGLzNi/WGhGmw4Bn+Oe6oRTtEWvlor1L86Du+DIBGLp1rKUxVPBafeXBkj+ujRU8Q0qAdPwmlNlWjxwHyBvlo7oOJ+3FVEdhQ5HRK6cQng2oVIBvAIfTkPjeKyKuV4pbRlN+LuW1zCcvWzdG5DegaVqLFuhbRrTlw6PRQH6O7fNDWOxD/ewT6O/8/eWqZ2H7CHn8pSeQT+GGRBdxn6IQZ+VzJ+HVDoqGrI24KKUgkKwXcnl+A5tRUlcTnx+RWmzov1je2vw0bBBK/BFsbp6+LSBGLCcM2cJGJ3ouGjCw925YIl+qQfAM0w3JYiQ8pnj5di+Co2E2kcJG7dTBxe5cltRpY1e++LIoxPtJrVIMtiAbyusBJsoEa0aJEWTTe1nKqyIjtFyLXMnvKaW5JpKV7eN8NhzIEEy6uXwG/X6EZwkNTl7RrQCzrwhzDhWdNVouToSEfUJ27Z6qEovaLBaoQetaCYPJibl5jBCCeD/rsi6SizUBzzbaGj37iNdjSfl/vzAhcfu0xN9mn1Kgj/OGZS79QLMi/ciMiFv1l/AoDUa/1oIsQadwcaisvwmNmVR1gl+Nt+ZqenZyFAo0TGnSDRmfpuMCtUCqR1khSVehHsoFjEWZHkp5W3togPwjds4GQlIPCCo+tnlJiVtOhclfDwOSE9KgOwuPF/sYBP0VDmILqXKAP9AxTDVH7f4GQXKN99HImb8J7nNIXzku9gggpNvdmpYnWKNXWjlzRE2sO9h/L8fhvpMR1xIiOTyzMkGj9yC/VJF/HVGe7P7QGvk7EpiwROb3/LN4Tjd003fxPwPDouRdcUwg/bObWfMff7YWsBosAGmh5iyzGs7K9qQD9IPwOBnAuNE8XPB8LVglX0v/l0nukAVFJFQtLqj8soNVMdlsiPRl3QUmn1OLpBE4hsNNbqg2YIPo5hgPv0Q75sKqMRjDDn47gfgpJP8dLZBmDRMwhZ+hCvaRTwqa5knwICUcKI1jhUatDT5HpW4C6ogi+EnaLItdnXEU1Z9CyFdOfCQZA9ueJpP3pDdieRDvL4hc7UKH4lwO8w3ZTgjXcp+YQgFM73rCeRcSqPZn17TVRnDBtiBsA7bMIi9PT68BUhdWjeBvBrdnn3gZBHGPZfEzclXaVINoXI6KNS+nDekavgSAwLkLZ0imYHdR5qkblYeIXO1UOouM+mVI5WibzwxSAmHk3fMZ05DGAEI9Otk9KFkkl56HHzBYj7fJUM7fUwCSWuPGHxUm3zQulk6A/ABdN6FUtKJqeKXMDaZ+Ac5A07abe9VMG5F6OWOKyZa8Wzh8jXDtB0REjiKkNuvaCDVLAxi9+4aFDlt30Zmh4GvCmn6DlqdfRp8S0y/NUh5Z5SSw7xLgAkP0IpUjV7dRcFYXaBaSHlxdDoj2zJiIA/1hh0Tb4QHS+V/QaQyGGSVQHcFYjqV6ms7f2S7c6SJDrAgvvbjGkas6j/hOBWhrMKfucDBCp9FdXGplthbYim2mcnREQZcMlylX1nEgDqmWYgnUozlKK/PZ/6IH3ZXgUZ7ss4TAgIl98WlO0RkufHK1uYUGTTW9HbuZZ2RzEVRoVKgtTxZhpLsr2kPwGsqagfTGgwh+wsepA+KAvMDz0C+g1YwsTGlgSkHv+/fIr/66jqUoPEnwS541AXCupvDlx/TeUknINLPTDO8wDJ418giVZyWaeZ1ALDF1Eyds9nDkFU+zY12FuMxNkLEMefHdAhHkM+LyWa4/lngSWUkLQZfs6PcBznQQuHum7LDtfPNzh5Vv4Vr9gA7DLBThTo17jNOiwG0fu3FBcl1zqGHLJ+CoasFkKX0jFjp0b5/w0B/U7K1SZkrh0Xk29rEhJNtfgBT/CSl7ifFFij0Xdra0jAyB/g3D3ocksfMkUfuQ2u6vpmrFfWaOC3EgeFAaZMd+cGSOFRoaRP3vZTEJgiewIBAVYG7jhUAAz9HcgFpcGgI0We+4gle5TVk8ii6NPvhwJVSiwcIPpQmPdBRpkhGuDCWG95j1OhN7QW9uf7hUPb4kNaGNgRcAdYSv3+iQxGCmTF1mo+bhOipTUQMdSFicAwru1m2iN/oyuRcHS+Tuoz+H9qU/PXhBhmQacT6oUq3Ql7N2cua3DGGpZbc39bUqnEqn6LycXauK3Q4JVmURyND8r9NX7ai3BKD14ttaTxjtTuIOUQZTQqjSUjYWpM975FR2wbnnf2hCjbK6F/ODD+GEj1/7j+jzdLZiUsFmZysvzTSnM5lxUOUCzDQI1dqvU5yBHPhan8RvvAFY9R9GPx7s+1uJQBNgcWbjudqE4n3z4Qa1BUx04BbMFbBPqkjuMJQlWfFaiRDI4MZKV027nZV9+if7/9ijL9kxDHdyaYZwBwq+fKnObCJ/+bDdqTgTTCNoyjyZP1mMZBe0tL34vaCDIibRj+um0FZlEytIn64+gTO89OT+ORHEfPPOIeROTiQIVvkFk+TKvpmYUOK3hkdd4nZp242m5umpJ4H2vgCz4e/raFAkK0S6Jvu8zAeSl2+RQWEp7C85JCkWfuslJG+f9DeriOnjT6Mc5f+OACF9DZH14BET3Lf4EzMhC3cGDe4AdxsshuGwjw68XJ+lXM9QO5z55FiwN181PHnAHNn4lIQ0tE+dMVKHyk+JLsfwsfAkvpeWmNTZHjO58itwaUp9yY13g32ikQ28hjr6CXFfbavf1PlWwghiXsgshBI/pRqHfRii/Q4sX9u7EN1ofFLCtQMxtLGR7AhaDqS+UqY2hkNqNJcvEe14SOghXOlpgWtf2Q9Oa9Yf1GYyayGFway7ZDcflpWZxbXXawxfjoKj91lJJw/gttNIC5zXN6jtFntb+q3VjY5Q9oB6gnJM7nUaEiqYIBwDn1cYsSpr7wWSDxHxAEmHq+JX7bPeAVoKqOZS9bo7SVEAmeh+6GADPaLLQw/Tv2f7cuy8zsRxumbjq6pF72exG6qoNZdxcqzAplLfvYZ2vTNWBO9zzbWIQgXH7JTDfPyCbh7RES0fMikn9/wGTN3du5GKbbVBUWmTF72VbOVVXc85gz66dhHbW513Y+x4ycG4SJbF283Pzlo9NIeiKUxPrM3w3+OoozkPfArV8/GlfVvGkhkK2UkDcAx74dlXGjoWbo3GRNYFY21X1/3LKNMGc5La+u7krsXfU/iXGLZYKuuuydk5YGAlHqQP4rBBSkhIpVPSOVAyIj6N9JNWBs1ffFi+K9dNkMxWqhoqY41VWtGgJX4mqPP0EhAoxjQGFCAPfgIPdED02WhJl0MaKBS5D8RC64iey2fqtn8qUGiptZ9AbONMQf9tcplqAF5VkicH9TVsZdo9XfCGjPqPyTPumSfLawrTdnn9lHRwQ/fBnz/AviP03T1LQ/Kr9jg2th7jNJzf6vVWv+bQlXNVEDvENjY3Vh3QX240P+G+cpGpMNDmeY8COjYQ9YVCoH5YrCNFJgelKVBiYz7Vv6s8TbrboOVwpYrl8KYkWUyExMXxLWxFZ0iljmTUYTHeA3Ny5msWAzBlZgvXhRKNV1irE5fefHdUXw8M8ehtspscRnwtR6HTf+CY7P/RVtEY77azfejalWg7cvTFTuMVwt/hRXBtWfD6rkj1KMbcCuwLu4SgucU7X4v9z6IWtjS44mlWLgNh0UrlhiIIzu25m1VcaHSiRTvDmXbobTUE6GryR6n3u6UK+9aXtCKBdI85X4uYtgAqYdlqaPiTLmZ9mNAWBxsCGuSI5SOvz1jf+w5TSUBshSzQSHQemnhfvB/pnT8ZUOjQuEfpGEwZqp1Bh6KG7BOP/IaTVLW0R1HEHRFPLA2M4XXi1i25GTq/Vc2d2xaXoJhRCHl1TtBn+rpbf/xpwAdK7IUfyRvnRMsNr/VBc2ZykcW+gn/+0VWG90LILLWJN0U9Ey+yRXZvy+qQhTkCGhMkKNf442R5+nIgsstPiv0RHjYdZ9XM8xIf7alb0IJ6UEC6OsaICtZlJnY4yh0zsa8+HrrW35jnKwlEcwOE7xyG/nxliPuhZmlbA10A20RQL3M5/oNf3jIF73wwZ2wJ/SG6jsc4TrsbBRKrNyp/OgbSOj8HCmEkrDN2vha3zWOt7cK1z0+HaqPupw7TgbNC7ngYA7AThoUAgdTpSJlRSq/ULAvO7EJlTVJiLsAAHpSeRcrILmhF2ROAPJ917IR5o/DAUC25j5I68KmuStXG/UqwAwlRKawKWCc41aXcr/f1nYFZo/zQLJNhS5KG3M3YRB+iAefIUysgLBVoJ7JRaMkzv8oPMD57uHo5gV8gJrMydkI+NvlzmjPGgSUB7v7fDiY/YNvq7F0fbLY2WOQw56GB7Ejw/ameJ58B7g3X3gvtvin83/ZS8SDL9O0NCdHv6w7QOgRBodvWidsabklp59yLbdIgaK+NT2t0bjQ1P8JmzihtgM7EgLpLCRICtf2OKCv+0ve5Rvgzj1YNsoPeOhRkxED2ouRI4O6ZkIJmhA3puNtYvAYmpXZThn9sdgHUNrrd0XjFWm+rPYXa7shqFo3q0Gqvx76pkS4uYvmWPefuK6bTMkYwFsFo+eURvAy/Y/2EKYKNRId4O4tXMoGy+snxbKbG0XTevuh+GnA5fsmNJjozObGcJcKi7J09ua8sDHk1732w/hhP0WJINxX01eeGH1kpajHfkzHhWHhyoOC0EJHYt13bre/NtoR/v4AosF5j8bH20Lt+Coa9VYrXdOukwZ/P86ugr4y0p7GX7H8J6ge3frn73Otbz9HQnjSVHLcwx6BxBdwVIj5WzCig0IBSFHLuma2vd1QSX4k7rnM9Rv2+7ct2V1aHs0eC6B7f15CyEq8bnpLOGNsfgIF5T0t9GUdD0O0HhSoQh+OWW9xRiuId9Pfxcz+IFqgsNquO4OxNOUhYD5WlrYOWig5bTAn+7wsaCS+hd029zrP7Kea3cn71GcT1n1tG8DWTbfDxh3NRFcsTqt+0Ux7j5j66ZpdPEUZmQuLlcS8RCWL4rXJjr6+306FfRbdE3pU7Y5ipLUGj6QWGTLAAkrZad6SJ1M+u262MhyleJZeK6kjeFF4aR1jkS+0DqVT6pSm0nl3APp9hcnWa87AZAztmrCq0sX7l+wQMWuYZ3umxN+Dso6lJvga7CjSh57VhFNczaL1fn+h4Qr4+rMjxB7xkAo8/qfuZLyQNM0F/wJx1nlbIxbd3BR5kY2vjfswbyAl2Q08tNfaX8SYOKzdkgoDxUz0K7MLTybLqIXN/zVnlLfsMb9ceOXk8y+XqxCSvwi+Gxi+IzXcsbJSorjqkVXwE0LS1B/h0HVaOOtlBu0ZLG0h4YgNnoTIciwxqleY0dvc4V8f4uupgzzyyFwhv52W/brArcfRvRV8yx9MaCga9oTJGvZ096KyekyzkHBuEHgP6vnr/IpPcNfnIAajL6sY/PWir5BfktXy+JfdLe9nsOPx8mZnMKl5NMkaUby/5cHvaGX/m1meInTb0Z6VVj4VboT/kTq+re7SrQQgtkNpAutqFjzw8+DhZA/1fQAw4NKVWjIAckVKv3MW2BmdRvPi/a3sutjZCBtOI5sxBYgV5Jsi82WEOTSbzpDxiaXxHqJdFXCbrPCabpPo7RQZ3g5vX+41oHXXaqIhr2QIOGf3jB87+OnDKDg42NZ0v7koUgVY4qvx9pED++ZbatpoDk2BcXXleSmACJGJeFjT1/F+ylikNp2NceR45e55qH1iP+3OUcV7NrZhdzCwALtq+E/is4juUEoiIIHYkFGsCTnHATsyDmJzOmNNy6XS0aCPzOvW0KAd9laJwJ4PYzYsUbx7fZ0cI1E9QVTNX1mfiHyXTKTT51cktKUTkrZLL9DVSW4JnK9Trrdx+gsCUbMtktb6GPN8oERRdUM3mW0tTZOsDOoi38Lb05kb+4bdhvXvIkqvuEZm9qt/TmvrVcDEBc34966tgv032FGQRZsk1Zbte7obCHDjrsZ0y/QlfHmTPwIL4MoXWXPuoHne++sYzvZLkZWx1cZvSD3heO99k6ccn3nrB0pebFxeXnnetPW7mhv4+Oie6nU9OgLbygTAxOecExplLQlDdele76nNQpU3rxr7iM2Ka2S07ZpJqMN/Ws8Ap2+Tzt/aMe9Zd3kX0n/uFgg+iGsCOuGWgxQ4Ndj3eV+F4fa8GUGrWNVdRGk+IS20OonCRR5kHFBfkqMOx5DOTZM4h9YTawLPCpbeho8tr6t5iZ4lQUA8fMD2COxZt0ppj2GEScMqzM+zOuizpsrhlZq9zevuK69xGHqOai9zKk++5r08Jc/gHfMZjIhP0vAE+NFzSljeYY3TvgsY02hKWysfhhLlWo84kPVygC2Ua3KHyqtAe8U6KC7PKrcrtQt16E7aY/Qpv950kybrKYSB4s/Q1NsSQ+WjYn1KFWNEKTeefyED64YnxPNy9x6dbVLLQ4ACkJsCG4qiaD1fA2z4wljB8iH7q67PGixWFtYf/zzXEI4MD9IinnibQ/ig+PyB8+0kp5NcNmxkqRMr+V8GXU+4lvRP6PDSIQmMw6xL68HNfT0P9VbtxsJ/uRsAgMkNUj8MG67o/Dz241tINe7aNt7hMmxj7sm9NtGwBtg9AfOrY0BeW/k99u2OQ3wpoAt+FsRyO08ueL77NyaVRfAVsoK67+TEOoN0lysnQH/JRUk4QXrWD5Ax8gC7616qFvu25quiiDlTw0E369qquB5qycP196wiPJSbwpaTey6BWnFL8evGliFqz0RMbJYb83pFC+XKs2tJdY1lfOKc81djqibkQx2vxbQwfHgXXlbXk1pH5nA2VrZo5Nr99ROlns9k5yNBUGRPWWqw8+AcMH6sVsLmvux7pXxrbKJqFiXmwHWyNnzqzwUPdqBF3/X94A1hF1V/qcpfXOFZUfkmMnE0UuBYyxQO2u/7ATUdgZIoLHZ+eb3FATC1t0VFv7zyVNkxQTLmvC+k/dgIkAxc+t8dX9N8CbWj6+HlI/f1NdcZ3GsuWB/86u9Lz5apdXStjhLtE2vJw/XvjhwMaSMietXdtiP7GFmD4VghD5aVaiY8DmV19EiiPGgmyevWcYUAAhHNufrIo2Tqe3cFIOyrNdJgomAR9uW0qmZ6W62YbkS0gtRyWZDHOtqHbtwNoQVY/PNRkFhjEknTIiQnWtjE0LTI/+7onh60PrJgOU7gq8ntpyA7ldx0igxqdrd6duC2oyDqMTLziE2P3W+/J671qQcP62jF8bmPRjtYLdkwr9V35CqCp7N5eT7hk6mYzR2BdUtb7OTx+yXtG0NjrFfQt8KtblZfVuDvDIyQrTWLPahgoa17/UYwxmiaypiN3cnqjTAqsaEozJD1pdnWuYOyLOuh7lBNKbUqeLUAavJ84bZsafclssZ6sX82q7MaC8VzAUB0GdgpYjp4UzsGFZQxJBcFZ9NkSL96rcx/XWm1koN538Hv8DkCGKZaDdNQ/sqta9vUhltXU3LIeLmOfTpZVY9PWjzNshpTy8wpotxzhxZPaUOJLY5XEr7JigwrH6Iq9VR/2iRdrCO6bdMDqpoAqafy+13B9RJxXLXdtVtAcwsnEZL72RAlI4EIi6chqVBXfb38X/zu+RNC06H+mJTw2drzi//DWT8ONiuK5nAHZ+wBGUbn8vv5L6P9r985kg0B3PMYsmxoDdPHIRWpJJMJqwhxxHIYW71FqBGXotsVKK4epVOGNFcsUkt2KtEDioeiy3hmRDTc0BgdRi8RFlQEdmrCIXkxgWo/Dn9r8vkTH8vY06PG46rIE1aRlAiydEaA6PttOZSprKyaAlmz5vyBcbhPWYc35nVKiv1dAisVfM1qQx/pR2ojKDm8kskPYnyS0TTgKD06/87bB24tPFY2hR7SopYFDgTYRHzb9Ox99lV7UtgWOe/fSLnYKsQqmXlyB1ouN495YNPUjxcUwSKMIsa8Z3wGbNXZgB1PQpeaUp9GMzyMZ2aqXEyb+6BW8aKLcD1LCyLV/XkDEcjCbWOLQuBVfJZCs+DoJOMdY8SFgtcCG9ql/n/s5IDuZE9j3rW/yDcU10p6M/BcZvHNxIlZwSXuVxTIOZSQQF7h6+jSxxrfp+GzuTOLNe8oMR5JfnAhxSix6vC13f+XudGvc6Kw6idvQyGFOIC5twoMSLQjo7t/l+QjZseHC4YxRtmeKy527AO64FIlgaiUdXs2XOzUG+fpK4tXL86qNthI1TZG3KvCcg9rnB8jq3BGvNwBfcosdJAwiTlHmKYIapclySjvisiXykQxupxN8+0oxiqzXkti/11qdLubkLeXZoz04feqjwWgX5DmtmE0HTn26+h0V4PSc45uqllca0dOsFs1Z/wWSk3BpWP1WMKs5J8FHRG/yJys13I8EHGjUlijTXOl+WKNCofOQrebYiUrsecxZfcXFdjUhl1bzcrSrPBzY629eIsit9XbhTql8NRWeJ0BcM5eRn5XtSx7wSQDHFBOpPgRXgGYWa+OYWN9nb5LAwAIANMCdgFQFfkEFpAKCVSJHz1P3PvMD6CtBQBmA6ljE8lIQuw/Ube8HzAvaobcmr/9zbvaZjaQZX0w8iJYItjkTE+gb/eDr+tx4sB7yRQ383rTn/x5I5Uz9MKTJFwSWJ8/5n5IRjVWH+R2YzhCnDPGavhCFzIb3Hhxw+gBCv5iUSXDgWcf8Joohp1nWXGVGsx8nmr2dGNDdjka82L+CCk1JbahAEavsVzBVkoAkxKgIaUleGlrweJuoPVJ+ScQoZ9thXPbrRT2I5sZYdP16rfnXZTcfVsdG0B8SaC2ktQpUM53m6ZHS9zE48CQsCMiVb2D5HKlzbNFwTSBjBGOw1gR3xueEDvwk1dIK3BwiQNNkl+GCLKNXZPI7NuBLqDMHmIPY9zwiO392YM4pavr20MODTVarBA79l0489KuMSnsBLvu27WbXnoBg4SMkq/ltTJZO6VLtMiCs+RjSGB9qONKUJJx2Rl/JmVp2+WGnwtnHOG8JDvBg+TxxT2gqye3cHFtCfRYFJbX9U1ZUPVLr1vy/dIeuhpE7KmqZfmdeFlj6KVhnOj1QtrQIVNNs67N1YLalcN02hVXYYVAx22ne35PosjwhoKLtuiA1NBFOKuG+y2fRT92+9Wk/aHmuUCXc2574h8NiNLzkeYnSrORGqB8IQEJKmiPM/OpzJ9WZ6Sqo42jpsvPqQrqWRALt85j+hmqlPHQ/rcY8BseyVBwI/5puWjLkLmfkDKHK8OfL0BZ0sEgtov0WTFyykrWxObYEFfq/m6ArtycyxLWLZ7jvr5bLXShku/7UVFzmeIQc20U+qwtRSYHURyK3jqRl5YLbVA8KBETYc6sulVtjQj6BXwq2fnS7TzZXNxhS4RjJ4i9bb99gXRCHmganQwb2ng4pRTmx5Yq4fhde3tstAutnUdt7Xx0VuLXQiwUMaC8q1FHsbKLAIermOcTvoCqkPbeduoflgvLqyUbJ0gApnzLggEZCirhEqw3FRzKPwdm2buCOM2tt6Z79YqdiuNGKtKeOegse5NnRprAnkoVl466F9SMSWU4uKm2aZ8hgv8yN5ELRzKmSddqkeOIrIiB3AAa6DzSevSCtAyCCk3yo7Mgu3lUxa9T8/zcD1KwlMIOAzUhBcrWEFuUmjz3OeHpAQy5GjYQVYmI5iBerN+Jv5O35F7VtafRRQdjWCkSWw7eI+yjVi5I7VECDyv68LeYbohZs1nP732e4OqcI7Xvp+0E6ogkRwalWTXpveOA6Z4oH/pByE/1UHlS+pbWACg3+ZFUv/iCXXP4xRmFl5zjSuTMBnNnjBTRxCfj1R7hXaEy1c+vQiV17ymdg2tdfMZcmA/bDkiWLran+hLF4WIglqOPXf1/22ZDw4dlBIPHPQFEqOwFKbhPjoogvBA+uWnJnSwyDf9LN1PDswHO2ixKJXmwVtbRKqB68Wr3TCE7FGFl+FoG+OQkR4fkN9z8B2FGc0iKEiWFGvFGTr+HpkfZbQGN2uBEZy++Lzew4hfNiEnF0AF6/K+wW7Ibo7okJC02/QOerlK1huHRXJU7gJkhRzEQErOiedFHNEJlfI6MeIH6jHhGLohMlK6oubXYlDLidGir19JPttZvUQLwnIIA5iWsloblC9+MHNlke2KhTJH1jjSrVhLC3i0Fcyvec5RCLTHuF+KFmbgh3F2tw3l0hdppawhVGJ3WN+D4qFZhwIttxaFhlpAVu26R47X9mbscHYHca6n+YW5dNgDoGXCk3VyIPhc+2b3kvt/x3VLpfRurjlJUI7z9JgfuU5upFPTjyuSx2+wiAB6H51R2/QZ9ZCWndnG45mVL1ttl2G7A2OvbiCJXKd/+ZS23UvKVZuaBORLrXpKePBDyQLKri9DeCnFZd74rX/wFwvvt4I5EfgA9bKiVeZVonoontForK3wbczCYrg3bSvl9zb3VsyJOn60dsZYkbC1Pv/cyhO5oin8xMehdYzzz46na+GOylut28Z0uup7SgNds0BY9ebM3F0isLiDbSTu82LuFy4Fi7d2ItUnYUcne83y5xY223TFY/sK5XI/sm5NGGMbZSOZ3SCVe6lDcC39GDU+4NpLWQ5gM2oZFq1aKab8cLxAK3kchx48UI8l9saForM++xASsCHPuTSWDIYLXHNB6qbzBCHufIQMa7kwm5TYvIYD+W79vI/lYqPpE3KkycExeZkssyG31tjS0LZgzdxVHzbiiuANdpbIMeYXTdZbCzTeLcXpFT6nNrZoBI3b4H4zXPh0IrjtwfdsC5VZF0DYOKBDfSche6Urt3wqKzvODprrw1AdrTJCgqmf2VP5/eF/qt/0AGYo5HFaQgNX9p3ZpAZM3gY7Z0aDtHqAvFL8UPQqSzIMm30EqXoHxnIAwXd+0QNQwvgPRudJesq5fW6+Ednjbm2B1cQ7m6XNVanzS5caCM46nKuS53YzwyoYVIaHoMkyc7EeyYg2AWXcl/1g2isZjFSTvzDp6nfyNoN6gV5w0sdtrSTjfZy7MGiGVKZK8rmiY3QtS5mxXGoOYIQlsc+HFAGF1Qd23hJnMhv8Q9MLT3RESqYVbXRBL6EGkxIayMNE3vENUVwUy4Jh/z3BERaoy5pCQFoE2g5wH5FFiFUL9+twfK2uUOSNwzdTJqXteExy1JBNcKhTYfEZNdeOMGotZc4JMvvU8Oxt1okOZQOJBlt/zbWtK6h7q0GflvW6tBe/Glz2Q3dyv/EkViuGQFi2aE18iV8Xa1QDU6HLuCT7t/sLujxqL2mQC0IRqp2Q12zcj0FP3Pl6P676xaDsNqXRvSt9ueHUQqPtin2mJvb2LWkcHTkWZJ/o+r/tB8fu1XTJ8k3JKQ67S1At9jS52XIm0EtAG+ffW84XWPYFGgVXAtq708q+PqGVLC6iVgtcpa/YKtuMHYmNe2SDwO5gwTyMu3Pbqjm/KcB6jabQOqjCeNbA51We+6cj0ycOhE6LGpRce57AiANz6zEzbJbADp0rrJ36f/9lWRaXaQUSiT2RmZEFX2F5Ub+Dps49P9butuLu9GSi7IxhKXcSWJr8ExOxHfE2ZPnCtqXzHyVhjclqFPVc0yHlNjWRV6c3AE+Uv/zKIPoS/7zTLlvBjU/Jmx+7y2LtXQ+F9t8Fd+XMhvXPCAIYcBq3mPBK45xuxAizR27nfnNbirT801VK2auqmSS8W/Qd4ZgQFCGfyc9FBDL2ZkZktw2a9mDEToIml6lz/cTtMfA7Arv9ToZqSz3ZXaobOcnIHyS33mjSri89NGjyzUs9vBqlbizwady9qlq+Ww2PRLCsX6PT3efopdkgFg8B4R2aioEgBLNIWC3FteINu7WzyPa4HyX6TSk9tjIRwmciSlIF5frjuxMnEqaq0rRNn92nxTAmaH9uVv3Ah45+NE/5J2AP5UE7JFHKBWeVBF97uafSU7gWo6r7v0ziPiMHv/Nvwcr5G2Z0w3Ms9dUbbhWcC4MtettuR8/jhar08YOLE8WjU59qjky1QD3Xd3s/FiHhdeaSjNui+g1uoLMP8MWPPKYxodanyWKZ/CnZJE08ax6hGV/G1WOX5DgIlA0RPXga42SzcpTdirlxqIRyqmO3uqzqKRZlg27FPyGMVmN5LShiBsLUY5j5Pk4dtJpsmhYXunh45iL2PUssmivXkFp9+bC5IK3rQJzUgbO8LmKn2e7C+bKNQUhjj3CRH61nFSNfq7qPUthB6SO5SLxrJqnGXGWUEaf124vwEn3ssra4FG+febjzI+rettxVP3ZSwLM6iPaNk++nQcQQlXqMV7DOOPvDDDB6daIv1J7zs4734dsDooT1235c5YQ2mjxEhyvPtfxmfnwoV6wometqP0poSfBH+yvYakNnfpUoP6GLYjSHrSvEheH0Z7X9ZU4Hd+yqCnwxtkCVhnjV1sOrgoiSue1SVmWtxY9Af9YP2m3qIfvXGnEvFVvUzDCX7yAzXlVrbh+bQ2LhG7NjcJA1jfN6UjaKh+jOTUMyZ19j8qtrThhsnmvUAhveeUFPheUkpuJfuKlOpYx+RGB/W3OfO8EcQxITANlytEvIRbshuRxpPYo+xMRvLPtrbuw6xd3j3EqKRAaSh9jTE3DLKIaSRNnMLy9k8jmmuLybZmKS45AYmaCZMfpKk9uYnhUmqgacayszUGLrWLzpDSjz8ntaM5OVnzxbfTqnvPRTNM48SqyDewDmnambfdsjZD/EO9fVPSX8fDBmJ6mSaYgupDFY187BGsVEXZY1spa/ws1cJTl8L1s+cP3bLGzLFJxtznNkgHTWRKcEixBdUmbGsQ1xzeQeOLsnqp+UyERE4fbnjaDhHYpZBauK4M4bEXEhqQDPZCHiD6SHj41LICwGrW1jnBUxH7wDZdyKxvYox2R4ANf2cN2RUHBy0vXkJYhJrz3Kx0yW9nr5YDIzpKQKyZY6Yk/cXbabSzVDgBcKVHaVNjo8fu5ikHM6S6E+WjFdhv6vnGqZi+nr78vCW/SgrK3+P4Xp8IN1pb2KjPvpggKeTJp7d6Fl5RkXbWm/i0zs07DV0o9qmt1Tk3NmzQ3x1+OQvIvnGJa9MWvqiw7MkJ4V1oygWuGCGLWC2Zo7E+bJxhMOxjp7nWZL5vdAXhmnpEeoH0AA6/g0FGpxFM6FPBEPzpGfxNyc1a9o/+CTrfrslx8/QKx+4l6fcy72KXDS2TQxgXCPeC+Q5dpHVV7erDuZ1Ar5wjfqozrm4m65cwPXMDt5y+XunaWqzODi0Pse3ANjeaeVaEwBS/uo2wqwhVNMZCrc7yZEGLFBByHxvyRbpeA9RBLpkXO3RLIz6FJCVEqt4D8E34huIZSzlB1B9ScvTOALzOv1xalgJixeoy1VSBp1+pIvII5ex39SKIeBABkVesxVEvlFYhpztdWzkQWroZgQufqz0tvtJ9jsBQ0zWt2yndRbZIMXqSO4uXygT0fjhloxEtHhvJzLE3dpAiX+FQsh3U7NRDy1/eTvSsS8aWLlBN7VO1/AvkFolsaj12Yx45C9eEQqa7kVn+AKR7TrchM/BFJN5LJ+d4p1nw8Kcxjmv/CSpeXpT0JCMfL5oq4ZoSuqzMCdUNtw9Xt/H8z6hc1BACPb1FdeBO0aEQVJR94u8Wvrk4ZEkrQa0ADyczhK2jzQt+aomUVz+uhRmmC0oveQjbEIlIbx5XakUvFBkIFcfp8hETWRz/F9cqsgNtNZt7lpg2yC2+o6DeKk/VuDSb41pjtYcrEt24XAIngyKIvmEucjm6u1UeRiGbtnIj3ZW8HxJX05xnen9VOHu23Ne58LaxzdqCIZYDTdntxEmzCSGNgwe2bYjgHaajRMiLNVRj4OnRKsT2GXUNxyRJIAlPqBPFGr/L37n3MjGcP2QfNq7E+UdoGkskWGvW8GeiJ8/ZzIkFP68/8pRI0tg5ZHP+9D+j6Jm2Q2fMJQ1Yvf0gya/JFH4ElyLeL/32cwxNGXpbjxPvdN5xR8lOf4S7r2lOsZYRbjq4OdUp3UGP6OKt8VtKaHTBC+JdVF2Q5+zV+gBOVk8QVb2SobsUM1HTo9qRlXkjXhaInVD26wAYkIB9bKH8OpogBoRuANlovJHtRzH1vkv+TPqWcGs5kLGF9MkDCYXtUDf1kOUaJ17hkbgEt5gV2cCXca0pccrJYXrKBRo72CrrAvE6McJmT+GFcXSsu8uYok3ohfCn/0YY/Ig1CvceHpmPzJB62xI0ol3dk034eX4y1CsCYkVGDQK30vJoCXzzZEJofR82IC5e87cD5885uFjYnUjodsXXL0SHqPwVONPaR8aLKiGTxg3pVX2ryyQfHUfvc3UE4tWttECzKcUZHXdGDYuFzSKWwm3nzSxrIaG6lptUe+uxx7jvGH9QKKsa/TPuI2w+ZvZImu3O5xww4tLLiYY3XIEyofDpqqzobgUFG7KvFz2hG+P9UJM+BQC5YbJtPRniGozjNpHuywgRGwabPRwTinbmnSjK0y9w/cyafuIGC9dVYchEJ1XuQl4zDeLO365J/nYrGGwdhhSCsKGjEKqMASB8kZRcb2fMTXrjE8mW4uSCfnO417IjhDRId8+tpvxgKQ5E/3Z66ZQ2olQ7TRHOCWuGRoL86nXQ1h7E1F35CKCVKclweFL6NcpvViry0hcFfXREDKx2YRIz12OWGPB8n7LxLr2J3DIJUldf1o6gxWK8wMx6PIsAWMiun1j4cxNc3HvVaJPAaIo93x4Xg/TygfIcX+dKD0sQECahPbl4fN+N1o5QQAHwDEBlrl6Jj7P+HSZtcTx03OrSYgBxtydjL2Ux3eYZDtk94MdQHofBXfu9TSo57V4kcIsoXBCwsNZDe8OY2DLPdtNRuHby20NA1LQUaDGKtORfqFQLCSIC2SGKN9O11k16OIMfSmwyJs7ME5IruxY9IF0b1AqwfPA7PuPbRazQpodO5YRGY/RyzBOof8YGL2i8tItxHUtFtInsNV6d5k2Du2kr6WtfUOhUdNwyqP64S+RgXm2NLMHeutwyRIR0Obth9dDn8VuPp9zZsTGKM5jbTJ5C9oqPKW2l8pFZnJURklqeJuxOwvDOdZCLI9fIeg+/ke4jzP1F3HLRxfED7CplYXTGZM6NGf+APbwDfEGZiVE+2DZztPZdb33C27lo3sYJXmeFgwnyYRIqCf/UOswFsns4JND8DhyhwsQrlHQsWT5SerF107kVSE3k+4WgERspU00tB7oV83QtbAD5qTL5Lr64/I8BKS2D1IGsENN24yzbTFT2H4k4lbakxQOxVbYLifhdlHL9zAJNsKB7Lm2m88QGr8s3fvBEioBAv5CIBJi4En8dcf9nz2McFYU0i745LDn+uD9d+TPHAZf8tRAD+HJFgjl7nVLe7yGAGsKkvVOnQ8Ai0AVIByWUE3pDMlHLHabl1TqUPtKKS8mFMT2aT4/KJAR+/GYS27mopqGZdTaZRlDdgfX/IUIF0/8OrIGCTKcfnyc6llZkFQfYFyVdPPAAoA4TfKchZDt4X7/QCb8OVDY9dr3q8jyuMBh+0iJWhUqL1Sy+1e6/BkTW8E8AVYnlr0A+3XslYyVNADPJExUMZ0LC2xl9Yqcw+/pw66uPMNQnE6I1Nfk87SCsL0Sv42yVusa2ZaYnoC1FL7t7+Zwl6Ou3bAosjZt0vXbrfXEM0/7doKPw4zHJ6rO8gaSmyGUtA33NFB9prIpyPOLOx2x9vMI/gD32sTcjLo4QL7MtVPU55gEfSq7D2SkSsmYpLjtXDcFDKuyTi4CVEyww4lbXsvW6rEVkL1moxpGUnkWQ31FrQwiu2PHdQ8b3ubqblJSHd0DPyf+f4ms8Rrw1aVXIfXTZH4IgVBPihwhQvur5bYGw+uqwXsQiJLC8wfiLIdIgXKOtEY755+A9r+QE4673kpMVVQOz1CJ9i+G0GpMd9lD5OZ5XB8ESqN9IaxU6dCaLaGyBtxXs5cbStNuJxJ7a+6/oV0oNXqHHAtGKRZBGvs/L1c+4MHKJ7I7zi8Ot7iO5yqF6aRvZzVPdkwe4Xz3vG1UvNFYl5+sNJHZOGYSL6Hoohtru7UdFTBvfDqqtl2QyjpMYazZUvfRky/drickRTaIqCeDB91Ff5Q3FcubPuxQiKmS4LpT+GX6eKsjg9rlvKonhoW50nzgQaA1hvJyZ4o8nVtzhMabtqjvr+66iIfkO9YdX+00FR7wyFWaxKr4IEZbk0R20FRHvVjJ2dPLaE8GKBRHP3fB2tnnvIEtlfLjIPPdwKqPuotehl1OPWZv0rIUB5GfRnJKSHS8BCP4i2TQZnsCI5SJ/qhfI9d8Vg6ihkuekToDyYGemc+/hd0Bku7PsVBUTBkXA+MrcX9qhj3HGMXP+aF8AceOVb51n6GbT9PSSnGGEiY0qRR54z1zCYW3CO3/Kic8ibv1MWHUd4ZnSDCfoNESwqKPOXjGV6FaXAqLxyyiqbIFsn7EMXsUVdoM+4SKeIIFZAxn3Yit5ueXvbft63b2dZ/8lrzJUOKn2VH0Hn4JAXMRMSlFjmMsuYBFpQkDbAO2exygp9Btbwdwc2d9diYauoyz5/UijTOO40fHUytv0ef2xKZbt17raXrn2mAFVjLF51ypi6B7IzCrEk2eZ+6iPyLE7Vx0Rdq5KiK/y+pyj51rUtRTEyAO8FPuoxMeoMJHkHrx1tdBhVIXuzNOVHVhbejZXlsmL1JnB+5dxHCufq/Gk1Oaly6cnJRzmfQ2yjts11pQkaS1jmR+OZdVWnBXrQm0ybYGRxv0VQZ0Dg9AXTZd7Gf4m3gSfnNMG1c69UoMM+Pjt783ik8Vi9Ji5rz5UCYEalqfOl4IiSubjaD+PxMeeSE7jKUVI5ZgASuSEPHpdrgmj9xXsWEynZW1wWyXpL3OK3xfckPIR16VQlPheJQwaxyExdp+5E54yzEihE4XkzuJ15d3DEvj8++WTCqOjhK+Ly3nI5YjumGYW3CWNVytaKKapC4qSZEsFhC9grEhvJaSeOubFD8rPBjV0AsFz6mftRnIcOkTyrIBQtZHbh7z3WBI9ZiJ4hvZhMsxS5E9crnjLy4njU52U5fOUmd4j1YWLuxopMspy75folnZ1HIwSc/f7qlfuTdQYuI3sPG9Tom6+xlG6e+lSu1lgrWDqknfNwDgDF4AwB7ZQkxgf3h/JVGZFwHB1bWMUZm/g5ZMVbNgu3pcrMOr3nB8MN6NoGxTF8QTC40UcSenByHTdRCAU/1bN3Kpm9TNXdElLbVa+CZVPLLo9QMf3BEGESIrEa39+7xLg1A6i9FN6jnkeE1FCv3PC4Pbi3pWgIVu6L7kv6D1IrEgIS5JabfuqygTGi7Icfb54ZwusWOmMWhIK5XxfK7cCMq36+ALqWQ0Uw9a2StkTrFKdWNGRPV7k8WpTYrDYSjf4P/7zdoFTMZxxerUlSWf9L4YJmeGdqPePxvFT2mACHmWp82lp/fEvhAhEA6Crcwfc46tfNVm/7Z9K8N0DNf1JtO7nsVPsopKx4LdWAdC8Jly8jN6AMrAbaNGatsTGEBIlLGJCCmWUPnXpBoaI/Hp/YrlUNg0r7tCERd9Cn1HjPm0Lwu5hjmWbOCplxvwi/WPdJa92fWzFN7ifCB7TveAwQTcIp6WK7OKeNlXoU+IWzX4+rInfQap3/xU+l0FfCrLvYWYdy1kdPI/X+fVronV0DRXAfbCLTdF4GuRRHD7CIEkXIY34O36tVh3e0mMI04QQdUlZTY0f7XuoaHEupQInumW/xYyOtzECqmEZ6gkErfAMAViiWP7q5nLxfu1JchYvlPaLeJcouhQ9OT3v6wNY8GFfIOglGv6DslCAysqvIjq9bzZo129i9iMTjACE6sm2Ti2cPMj9EIXRTPhcIHt0AKGEq0pjiVhECPp0ONsR+6GnChr0aG0LWT5fETG6qDVXH26gturDC7/IFeaUCZhUqETERY/iaizDvrEHVFVdnITqW+O78a4cyQxwsZQDfoZkCtZ6nc9XVN6IOviUK7P8WbiYDz3LGi7/CgM839tc2yw7a/Q7pzXzWd6ivACm32/X97Cnv232YxXZPV2u9sD5ZkyPXJDOauxhUuAJ2jeDsIJwQBJ5+mGVI9GHUpmA2gJ+74IUQ2cDaJTGisQvmAeQMBskMZibzkYfj3ZK0Y6seFwUlOQcTmtSYG5f6/LFoInNwVTkc2VE1/pZ4tpMmmJncb2/X+kFV3wBT7sgGJT3P28JKLiy+3QbzJC19lwchO4S1gSHplQUt7RXm9i1ivY0mhakWdY2q4JYsj0Cp3Qm85nm+IoW47u4HXpBou4zeVUz+54OE6tgoe1L2YexgtueghbAlZ0CTELCq8MmDWrjBKr+yVTxEaazSm7fiOJOWipOGiGygx+6HHA51GEoj3JNgLLuvfMtPrAv+8k7hjfwm0sZX4zYrzJ/ILyJTVN6Yf4fqpW2T1MeWOScxXKdNsWnXVIH9feqrzW/ClINJO9sZ62MJuT/kpV89iquwVBuctcCafUQoDLgOb/cmka8QGEXzkHPeeqZ3P2V+1JbEkMFXCZyeuJaHzYkD8qeR4i1tCRZrMYr7vKP7g+Q5IBGYjZM6Y755RN2Au7DGbh5JXHzMUskOnM4lz4EIGt+kRSviTM4IrpIvbNdgKkx9nGtQOGm0klOQwTfKwFVjwGaiUtqPsnhy6Rxj6fhp8FF/Y1iZt+wUUtILl6/Q+VrdhKPqSC4HpND35tjFcjGJ9AqPnqfOD3GIv1Ku16oK+WUnmmI8jFMHViTteSH068xkc70HEntsetF8F4JlVJ5AuwAsPcAK/sDLUzdvT4vbroOawzzrP4YoedscK0OWEcsLnxIzQ+DZThsOxuPt4q3/lnIbXOrL79erjiKZPZqmd+sAj6+IOrp9bqkAm/bZkYxLfZoKgnl0UiCYdPhekIvAH8EyVm3cjhFHmc5y95EWyMEOc7o54Z97DJd74suZd38m1DFsgpktUCD+bmeAQR2137WfDj3tF3eKmv54YoATabWi+LKetLNs6aR//9j3DSVXMXR8SkFWAFp9fQnz5LxgQI0LUwQuR1Sq5IvUJl5XHAQraHOL3DNkpyxpX4Jnjy7VxUYXfQsLNx0J8x0jLzgFOJzjR9Pc31E7U8mMfg0u+KpTzmAkbH9+jQI3KKyGWpRafqTDG6F7cTRujtTBKKKN2NuNNuC4Mb+DPMy8H0AHwEL6RzD6pcBaCSrP6Rgksh16/wmAnTFNjmBcKW92R2GVXWSzL+C2ucz3mz9zpGdFTsnterceCkyh/EFoc8fWWG2PDTIt7XUWoA1WreCtve/SNqSrRJ9deYHpmp2+0WbAVlPIZpzvhuDhW7vNPfX4N0tgxEPf9sXGWeZth7MM/+RZHeGCwFEAYjfi87mSS+7kIJwu0OfK5G10DJLBBu7TjgYwDIRLYQn21TgZpfmQjwYY+9LSejWLKPT+2Trib4dHyqhvQ/qKtYe3bPDQPmFHnh3kKHpscTtg/2dBYyeeFe+8Rn2h4fe8O79UwF3snR864oPp1R/Rm05iSwAh3UXqvKAC62G4SyPuTcAXcDkyqjNbDpxIqku9k2WDv4H6r9cRaCXzdw8qALOEgRYrJtRohAaryTKEmjFzac8E7M8mSLTDWw6WzCq3svIU0Cemimpm9/4sON/K+McCUM7uXbdzz8YWjHUnnE5WVj6vvjJIID6rl/O0yIA2iNP5+1OT4rkZv5Lbws/hlMnwxByjmjuQ1ByX00iGmCLFOP8hMb6KTg5zvr4ZBKu88jtzrUhsaH+56+BM/Iz57+DFoXntF0F0EZwEMWfORl7G1wTL+aPGAkGiRQakb/CqMVAtKmwQ6otkoYiK0dk5M57qIxjvGmRULz4cE2d3WO6OstQkwmeygT+nDFsVArCfIQXWrYOT6M3RF2N66vb2o/nx+o2LcI9qBnwdASukL/DoCMhbr+Irm4GwaKGZ7ATI73J/fjB8KGrcTE1gwfFGbPXyr4sKIraIeKaDwet6IYL7yQDOzG/cgk3zgXB8WkVye+I4KMrumCr3WK0Z+uGgezvlgdUSALS/VlvWLQWA6nN9okW+cYJywnAnfjjFcZjrczRXnQ/A95CPaR9lqSzbmLOE30uJLoRjIl1ClKNHwLQnigsdCHFo9hr3UVBed+Y29TXrc8rNngv7ZHvgEhsX33ejh1PtDihcxiVC9k2lPTkUfl4YJorPtcERIqtzLUDVZxWg0xV7uZjf+/lLUfU/f6g7VFA8jfzV+Xln3M/NDRLqfCaWU+VmCBZfrbwP++fOGim/cxWqi2ZpBBOaGoz9j+3Fnh7w2QQUmaZBbIGIFkkXLab20JZTnnScZ6VO2ahS//kGRpT65gfy05ewAP2/G9B8gOryptA1fKkLIiJCTwBN0W4gKAp1DA0/HTDEE2J9qlXkTK/13SOJ2PT7oW6tf62szVVR5nJI7yNWN0bMV1Yp59wcx5nm6z3A9Tc3dCDIo0qDKg5VBB534oTmSupAGR96/7hDd66pQssKiFL1e8ansDCSrGOVXElxV4FhXgjH1Jy4vmfkwkulD3pd+p1S+tS5Oe0/kLib7rNOWZCbQe+Z68J4jlheBfq1PwyuALYmZbMasKR/KWGhvWDRP+f/P2Dyg5BfmXTkCKk/R5F0ZXLUgreGBXABG5u/L1AHtq29ydieBJwYc0+ReZVFTpQvU/V8YIS0n6JvhLNK94x3Ngltt8hoi0EC14tKbHY2z1icY50kDOQyLCV8gNrCFviRgpTcl/nB8Q3tXvkG2RAcVlXyAydzGitga8T8YUNIAOoWY5NbwtGGOIgH+57eXT6WY7MegSAF3ARvhjs5JkNbmiTHcRpicmjPB/M3p2w6Xu0dgPHXb+nolCD5IiavbPLl6lIuQoFCiY4VnoTSbiJvkk9WURfOrEPfIXiTMdjaUXCFCE17wwVqpH8w2zDw08kmsAoLdghEWRCEtY/I2bmU0sHwmhD9gz9kSeVPYER5VUAq2V65smMNdGwJkbqYvQn5KEjXBlV5juBfLfKfewiHMYhN382O9WXL8Sh/iHCcvMHf45AqlN2d+IL/l04KT9+N4aBzrK9DJOKZmvbZC7mesyybRCFHiSMWnAOQRNhUNlEn1vv3RLvS1MB+IbLtu99ETQD83Qe2l6GGVpJLzlJlDf0wEYBkOWFXTie0z/+xKn2GpirisZHiYFGUDfic3mC/653Pi2fS6HmC7wuXK2j7FWNcXB1Sum9i2eM8/mPvFnaXM0vwOpIZ/drFqj/BSQSmlKPwlkKHP9nHgQQ6Fqs1bQRLQhOcWEJENkcq1rADyXkFW5oalsp0NPgP7Zj8p3Gtur3C098UiuERfvSBWiNnYy+1SZbysWHDuy+B3lV8xXlFaNpmVS+QOSNwknrpqqOW7pmmA5Ayeqgm2GMumZaR43XyfB2YUxQT9wS9p+qhmb6uhkO98S5QS5H/Qz9JiKKRSmQpwOfzTm4AiRTCAyttyUPuqMNHR6xGQygiRQVn03B1DdOqcQ5AigCnQONFXHo+Yp76XbFlihRC7pXpT2hwn57mKFMgo3F6B9n4HO4i2EviHEfvxgYk9+E2f76EjLldRsUI2aw80q5Q0dKnuv0WWuEAKP72vEtlEkRYFuYUu65hxwcyDZ67X4fWWjIIwCw2gMBmjW6/bb34xrJCJhvEuWB3/aefm/XvhgOfHZDQBK48Cjd5AcHpJ+HyOFg0uhn5AZs2IKReIYwa9AMrPU/2UAI+UR6iAt/jpOLVQTe1VZFrZp5v63ORNkhnNeC6NZs2waocVe4/ZYg//gD8HeUtzy3Y3B0QvAkkHhYc86s6WfZ5nXEQ/BnlPh4Sj07mlrAFeOszyYSjvw4z+JbyvSMSC5kfZp62boe9vDdPVwEmp3uqPkqXXgIDi230qhoy9pTA37VvsEeCuumssg4zZBeS+5J4eVXavlv/5MF6kKprbl2b7IbNQfklAfacswQ+JkmLCi2sMyIA+w2ZBaWaXyAYx32Tm1GI9qf7Q502iQnH87i2gb03jLox4QV8mkG1kx4fqnenE4CQAOzRUCnk1NTjdGup2BLwYll7StBDRF4F5kQ2mrfVL94yxmFL1pPX7sj/mRuxwFt072eojGKWzedVOIvFwcEuZOBna7eb6IrPXNdo/kqJ7d/Soe6TE5rjZYFy4IBmyOnLiamTDYmqGKb9S0uyu5SkoqEns/uPOUYKGr3P8NmB6aVZ1Zl63r7aR1rcg7X7QHFnYZfvdMP88R8bCrBhHVJOxgotX3vmj5Gh5SKtzqErC3X5+PONbT8K4S5kM4qcCKdYzBtuca641oXyrUDgWqsqCv4ynP4M20jNDPHh+Wxk7uqSO7nPqIOCJZd/cVxyJb/fqGBUBLs+U6Dl38ZaInxH77hUe8jbLLqedmgEbtLmnwKapJ5Sx3Urm/yTvUwNGc6NIL8PLc1ys1yl7+ZcK2BTJ2/HqFxCcY4ZcgYoELkLJQ6K23DbNJaB1JUXU1QYKEJ6VU8GhqDm27UV/b7Cj5PIuYt0kGup3hwacenCY/oIwyKs1k2yxZYJ2w5Y1Y16k48o59lSux0+dRMTKOxK0HDzdJy24QnawRZKsIGCK5dW0iT7hp1omBHNCO2S+HcKzTeTHMUSIEFbAliR8m59a8SA4KyujayvD8or/IIfoVnY4iNu9/DbmdrCbUZcTvBoC3Fum6HaCfi53umsD4J/OpN5NLUE1T7lDVzQu1R2KlHPrR1gQiTXmMAtq77WfHDdowT6UafdFmDDuIu9vGdSdCaI8vZhb9SnwXXe9I3rgKdWw5p+c8fiJfllXG0USs5bqm3PG3tNDe0fsM79uH1FsQ0NYHOQkKY7b81KcsSxhnVctmMw27sjt3lcaqFgBswoaBxk/t6fLtf9o6evBV9lTS34qW44rsxw7DEVfb6XIYZWspEkXHJUPAxmq+UfdofOJrEoPuTRAdTJxiS8yObKicJCeKa7lu+vQKFH7cDyH+SQt0x+fpu/KbB2LuL4lXAEqUXsPLMk+c76Sk1ejvJPG0Kpi+jMNK+SLUwrzLZL++nqPJVmZNV3zXv4puwodAWV2BmitNW1t29Ai0BrM6t4PWXa6e9azXLEgcRz393uehHDE4pRZyrd3NdYgtGsWn2dYv6A390c+tpxBq4z7p4AE6FBTe2Zogyfrbfhipv38/u6ntJ0Vc/OvLwMDvj7Pz6rQR2GePnCZ4WtlCU2/ZbJf4FRLIClBOypew2n2vFhpVhow+cih6prjxBcuvHhxIGxfK371c/R8xhr0iAgLdBrncesXUIsQdmRqX9UGa5zlYQu+DlmXlqc0UC/U1dW8/KgCU21v7YoNkb4txqI5mZmGU9sMGufYflHfmDsaeAyLZ/s2shCmp4DOyi9fJ5uSfYEx1CLvXNZUAImZCGg/Ixn/LDXG+ktSrVWvh3d6sMZojIBHL8X0g3OaWWzG1t2rYzMsnQKP6jQvyH9yWrORlwIPffRY7/yCzMHIjXkrGNps8dyG1YfYGWqkGxc9qyC59RGLbx00bI3lVUercaEcpCDvqBWSOEFrskOJ5bciX7+p+wofeH244hmXTnMIzlhwcPFVzDtibanRyB3ncGOYwvvSVvr7VNAClOqutUNg7BV645f8gpqUmDo071jPC6NoDFeN3S1zDU94zpEMyFZqUlGVvxRCH2ekRldRMOeqbSnTVIDQLmm7vKBMfIHgHAoYv3TU8A6euZDwfgBmFeuIl8o8ucv0Z2PrRPndfG5T+SzJgMugOnTTW0DYeVI1ZeaioV6JQ2iUYh1TqHXa06Kf/eXzapkoi64vpzdfPTh2cIk5qlctKKUdg9fDH5swn4OHZKWVGVLVBemI27FSrlzGFPMYI89iYFPRIWNObYV/FlqGOJDbK5+E3WmeKGl01Vla+2Ra8PtD1CIXCQZUG/uzvcHzy1h7j1QJR/Q+hXQxSLeq7xEdKrS/e/Vhqy9YL9l5TdRDdVvGUJWiQfMxGFnK0gaA/wpcnQsQTwP0HMGhVc1r7R/ICX9z1LyLQYLWz8keFX4HB3z5HxLd1y2ZmdSb86SrUr5gL5YIHzom8Pq9ClVEsre0+omWLsRXjWLKhqYQI/hqVOHRn2n6eLsAGDdjCTSwpK3gaQgRgn/jnkOs+7sjXGI+qS1Ot8xiXGKa8/7Y/vRJ+07COc6AXkWziNwL7GioqEG3tEfUC/Fv6amAkQeSq9cKB3NYjoveTpQmg9ixAC8R+ZDdWInT2iompyYsmhybaLgJHmGSVutayBh991CS1jZ4pAXqGReXqD999OFKVtxB7Z3+JlCRGMy46soiXyW3X//Ye+yV1yeUHCG6k74V25kkuP5XBD0xzUrNVOGuZWuF9EqbVsNVfGhHxcu/BxFezvTn1dYoIWCkFQl5Uaxo+2ItLJFCuQYAYMEaQJG+L/Fxvw0yO0igoMw0k0BDEjmeKO2iLfzbnztsrFGKjfxRIktqbHL2ziRGGvp9OAyG3SHltMzI5RmqAknmRXDGSVCkW3N7KITZjQG/2LL5jkzuV3OS1RBWBnAwtv1MXesQcVwlGOHQmDo0wq9vAb3uxUnxXIVLKGyfkHcgsQVQt/J4nNXX9IPV23elDmvSDclkW1yjNkw/+4V6SyHdP75L/lxNYG+FS3MCVXUE4/WPQiBzuVkIbUH0bdig8MBkpFnioBCPUYgm3d+7hUXffII6Q+UWvUXMu/T3qUVhOpgfXl2B7NMwinw9ldIecOwSm1LaBrOczosrTEdIS55VhQrcH/EDm3fsI0/WDUlT1JNmeQqIkFVs0te8tbcHsBK1XWMA2oMXHGBl/UTwjVm+hDsRhtwaRqm7ba39m2ZBojb4QKV2IgOvwNbzl0Z0yi1W3YN6QLSxH/8jbG5ules3e+QEsagy+RXs3QYB2zsiWBSWu9JwfWJhmuH5ZY2zDDxcGRwkpkUMD/tMXrlN/bRyGYMYnHEnPPvzmVk3/bWNTjGDxvXm8I0gJ3/8OagejRLxv+c9mdz/bXWjOKz1hUUtQ5tUWpTS+CmIhAsWf2CfIX8jRrEc5KwMjP1GTZ4hjA+g4p0VwHCLQ8lpYoEyoonySAuJnk92kGm4zZN8HYHXL5c3ADGxgGNwfb9n10Cog+J6ffTSFmDtYxZPOmLQyydxBv1yspdkeRWuuowublV1NWPVbshWkozGvEQ2ci/F8ij6WS7c74qHlflxtjGZFl+RMupdrudKMM8cEdlsjvz7OPuPNs897YOnCxTa342GZ9+pVnsbceoeJySgGfzY0g9tFqwj6RiU3NV1mUNP6tfpy0VeoHX8vff9AS3bIBUJgTtyDMmSnR2bZr+i2usXdILS7cCdxhNMjn9Y7/Cz3iRvB9Qsbds2MtnCbmkg1Cy4O1Ymxg8CfOW/kNFFd+5RwQgtj7fAtrIcFNLLv0UOLqZglDXjxrEyBkNRKWXJf6aawZByR22l5B0/PL8lyQRxY8k3Y3oGcl5+HO3rM+KzN8SPXwOKbuDEMlZWUQUWYKlokemwovzSs5MDT2pld45X55tC/WJL3qe1wzVJ1g5nNDdl762Qucb/lQ2VQ1ujyYlFhFBDyJNG86fyBtyZCJ3I3NVmf2JttZWhUGEvfXL1XA6bKm2tYmaijmWr0xgNDGiG8FCDP5CLhDKCjApCh+qEgQG63ESbQ/mRAGzDN4+q5hL1+p7oRlBilrXUBFw5EH8eMSIGaiBHBhx3vws55+qYlN3K3jBp4adbkRlwBglAWaCPpS8cGe3JYMRO7gm9JnoZI0fF2Xja+0Y2ClDdjv7puANPtcy1OUIv8PlxRPgT7qssgFPZtI9Njauy8W9pHSvpAyCpGae9k0crpcAUain4B8GRZG6UaJqjd2B/Fx1aj7dczYWg0SfU/5Z4MoRYcJqnOdQRSDl2q6L5s3CONMFMHuwS74mTJzWSTTF11RykNYsnh4MnSVnSGeuKulAYiihlbc7NR/iMNwSI8Hyw2GZpSMqrFF4N6dKUT6N75VznGbNh4JqaC6V+KO2L2CeqxQyN5ROTqZw05jyCnSZRvx0xGdxl0M4jW+8orI3GuNrI6iRd6ijDDrT1hosIb8TfMj07XS+fl5F+3Ec4JaY1vi04o+EGIznqXsPv8+OL7GHxwG05hGYNA9rysHGNlG+OIzElIqdU7IAMXwSQGBmRnuKUdV7nJRh5jzntTiwtJMRtfW+2Vhe/JHcg4sJT5FIOhH06ZRnkIAi2LNS4YCGEpvrmHgEmIl4UUjVoqbx2iiujTf5zBqO+d24vfUYSas+ZeYHJ7sX1uN/zezt0BTkpWNIUuJXwy9QaizKQhq4f9Do+Ne2WtZuJ5soh8RgnYbUEtOzQApYJgDvqB9EMnFPJFg8GgHeosVIe/UsFnfum/kwn5iJFlE00yYL6hwKPUnzLz+5kR11nX30EqM8gO5z/IjRj1NWgfP01z3WsXeX5G26yw3rcly2p8kDSNX0nhW69U84MLXBXPTQpLtjFaR511cFoOeATehZg/ljULL/tkIk8i587dhwGv577pwzoIuyDw1FyMqoKPH8n+jmLCM/+iPCQtMkxD85Vrot99ImgkayMV5ih8JgiLx3yCyGO0P5Q4aOh8RC9Tu8MnvGXLQwXHiH1SB57GnEALEIpfqzwqVsj/pJ2E0QPDzlSLvW+12lrOUziwXJS3BzmSskXcXwds7qAIMmFeznxCWwuQrz4n41TcjDgUBySc1cIUM6idDhSIKGt4Gn++M6aunnGqzO27NYBeXqrlkJm6WpjMIX0vh37E90AquekWJfWVB6HdempGU3NUxjB3hidYKUMOjHBG5XNgv2KinfXGBfINXuvs56MnqZqYOjEzZWgjjjEHb7lDIclJa1T1uQ8tzIrhymjIE3vAP7mSmxUYA5VZgliK/8bxcT4hcsoDNMEtrCJNZrjuQdnm7RNXF4tSF3gR95y81xnQktC1merSecvL8U3qEtGypDOGU7w4QEaDDY+7PfEaYgKJuwCN3S7YDdLmNgTtk7xh/xun4tbJOHAy2HOhNGYOJHH6TQ4OxxYbg1kTx9Doughp8V1/Og9/O9pNv/eRvnHUacQUwaL7TFXVKDlGmiAMp4f8xXHMlshZfRpWyJQZ3ZiNpSTiJj/W9kFw0ppYOlf76q+69FhJBJOL0fLVPEyaELRDFQNZRw+LRJFW9fSNZnDBIrcJwEvXLHSFgYbECW4++TqUaG1n8yRNBcKYZ8vwA4koLU7nO6j04C1YDBbVob1iWxJwZiYXxDwDRThLO7qOyhOWPM9ix0I47c2M5zkpU47KjbIRP17LXEHG7as6UabuxgQv68wXm1r6UfOzMzs/uaC+DRR44coEptH2z5DxkOsz7EWCArZb0wUEajiuf6y5k/FZBcUJ4i0Nc5ed71q/gYKZjDh18Ie+eViN4tL/kkwAVTWGuSmy3ARDeJsTkwlPO6CqpXwsTEmH9ljGL6vXwCzeVsz5yY6HyMuyc7ds5WvGDz8CiJ5SRaJqNsa0MbacSx3QimrzVsGA5E0kpFViHGEd2ytJH/P/nmoRJtHkEbCFRNWXX4+V9eqHi6SHnoGfNMh5LAb/K0aFyZr7NEakZ95VlhAihdn8h6+ePr9gK7zJV9XS9ngFgHWfpGGT2mA2vCd4brsln+iz3Df4FDsem5Opxv3LGoGkNkyS1seqzg3Tp/vwlGhuja4dr990cLfwTwvNJcL2L5BBy3hz/jNdt83Kryc1fIj8F3b5XhuMFQvyZQEwzGxqNrugY4GXUzyndraodLwAy80hMaaxQrxEeNJsAp4jXeYpzX0BwyzQSC676w5Jay13E4Xb7WrWqsNoPt31Eeji9kWAXD7Y0Ilb9fOnc1ZsJ89JOYz8soqe9AbUtWVbFn75wZWXfzOIqqh8xvdxoO+0SuHxTpwShsucOVgdh4NUVlb4OiyYzsQahDnhSjhA+SPPVzp3qRKFhc408GpouXJI0qZtj5gFhQm+d0bsku2LVGIYdk229jyVIkUxtVd2WvwI738QgeEHQRM+nEsuacYLHV3tKPyHErdEddmoIhSaSoWwMGUXhj5NEtdaSut6oVajQGaWD8KrVoebsPcAEIeocZfKakhRVB1GdL462SMbq2YNNjTym/4Q5QEnBeoll64CA442aSX5ue9f0q5oChQljob54iuNjTO7dyzPvKVxIxS5VRccI6vMp7vPOrRr05qj1GN1DoVuBNjIvVtr08xTB/g4JcWJGcVFrgNR7j99Qk58S1er0i9OzMUCkfxgSa2E0SDMR9nj8DHJZWHw4p6RO/vpTQWmB6YubAP/EQowTu1YUfINclvswXAyNV6cyCKmdYwGk1XCMXfNZxEoIuae8Rl0XWTTRyPOPDBnauX5ZRbvy0SLr5p/NHbxsZ3KcmZO7l/EvyzhA1zXNIoPl8g08g9fg34q2lFIO2oMVkItYJ25t1I3ldhd9VmBMik+VJvfjc+WZtJqg3eTPFetX3Cqqjw3zO3CCeBprT+Vi72Nf48MqilBFM4JHSLFE98QgBn0joZU7be47ecDbBtVUDVUe7Ore4MnSUsDdLDXl5HQnn3gQbgMfc27w/gSa7ProNAakDo6Jz3OwYRps1th4Z+k1T5rhDZsYKGkzjUGvUx7JsUs0+ZGztrT8+17trZ3VzLKG4J0+wYVIaWH7s1gjIwybS4pPTMoGlO49oEZtnhR45RRftxA7h0Us3T/WjFQidbk36YOr2ScxKG9eH9q3VyKJNrliC/qPorXsgFRAzpb8rpfYnptxwWYQrXNvaZ3AGiRF2EEelvjS6uDpvmiT5YqRJEr4JKvCaLHXItVRB8wLlqj8pvrGfqmh7oyLmG+Qke37zDXdJVA5xt+kiRyn/kjDHjKzN3c99i8GrA7zp0eGam9Vdg3mJHJW5cWyg7A3GfeDlsBIq7hdRN2tQ+S3nn70kPylXmRJ+bLerG5FkFrH7J1nUFotK5H82HX+fAWj8wriXlnNSOQLNwbHpL/l35ZPabGOpykufPIdpzzE+qjGOvnMMi5WXsdicMgcGgciRtQ6YWMepzANdiBTrF0jx6ty8B9Ly5R2L7V/D9vg/f2g0sbI4esGAwJ4OYkzt7Y8SACJW590yJr6hSvqEDw/jocRBf8fWxEn6VtqHl0c8oBokZxx9lDKGbNUtugyLyLFcK7ohazBz+hNHwULXZNFPl/jJ6NNq0ayJqy5eVC6aJ4xkG3j43zTdWRQmQl7OtCdsZuUmBowcZB9mzJEBI6szh5bCGvztv0eZDc4vcsndC+n4WgvLfgMe5QBEW/QhQ3hFIp9vJA0fsQmSuWjIjVDd/EZlDBIjkhPg4gGMYOxPM2RCXe4IrKyGbY5szb59KaDwEDvLDy5HgovTKMrNTVPs7nBWEQec7nsjGvdcDlOLA3mUhEYpBRRjUHPTf/RHNUKvjI2ByZwV7abRV+Rq8JFNMqovo8rp+PxDM/JuljsrY1LL/e4k37rDy6LOz2Nf+vGyK2ODEZJWbT0zVq1IjZNAgBfGmIW4eLpA7jY4juPifg/0id0vMLyvinkrSL6+54nSp5O8z51AkfRXVak/raj+vqsUj7Ha/Aum1vPnJDvjWt5y54rcnP0MHI2XKBVhIYmdwXh2fxDq7ZTEQBCgEAq2FUrXMsfbDrfsBv4M4X8ATWwnNqt6r5N695qhjU0/8wHMnUBuS/+Pu9QkMxGrz/Pu3qkdCaMCCq9XcVIJ3MxiTuG0H/LrYY0mUuq6BhEyuIGRnEMUZ5dwDf4RXFqGE9hlvWPpimdHEIe5OpUqWGaai2IeN8DtJPQ66PidBBpgS4XxIeFEc0U2ZQe9sGnT8A4TpMUGADvS45nSLiyE8QPU5k5FZtxNrbZ1Cmyl1mXqU/zjbJJPhR4vSPpo6VUvGnttcEXjjn1vkUTrBZBk1Jjs+d+z/jCJo+jHIaDNHYz2HvcM4QXoei7cSjipMCY7ljGxNkB+++4V6vUOC5dp7xSYydWhpDwcH+9YrGRa+Gq5j2PHQ6HtdWBmr0x1wjVimZEWE07Xp0mP8JF/hZS4oOwPSNlc2W/UqQ69WX7PWMIfN0e6Qv0QXDMJ5Va2u984yz+hOak1ayky3G7afwspvssrrREJf3JmcoXYhTUiy1NbdOzo1WqJL1bLI5sUnrTq76uZ9pLRoktL5CYk0TpEfv0CxKjwJEkoJXcgXS1wo+llyZITu14AWqgEdxQGuKU7zJrwJdTq3D42ZVseQqoQn64/Q+wIppPCo3STfi4Jx1Ebg1r51Ak629ornkDuJUs1wPtD2zoxI2jqDSlmX/cBcqdKFb58PDi36fgIIf2Cgzmx6xk4wyDnsIBhYIcXKjDw/L0p+1JEnkFGfG7mZqsPu0SkapDN5Q4vuZMuEQSphaX4NjXLT7fcFVvhKq9PrAi7+PrE0nb5sHda9KCQBe5O2c11CYQMwCl8C+G0fqA6z4HdeCgt1vrRPr7fw5zPST7XPKN9SuxN+LvNFZ5StUdSM4QT7eMKLWDN7B6YTCzihZUwUkl7OPCtJvn2LWNSLwNPJNSdxKYB0rlzHQ4Yp101uGnkva7bp0sWvJZ+LF7G3bHDRWJwOpr9iOiE+Od/xIAzqHVVVsgVxAPubKY2ICcsiDLcGn2lf5zuiREFwH+erD6xlfxPN79optX5zhUFhBHK39lHAudivJ1rYwqQvP+ATdqsvSEOAi5L8KEhiBlZPUHoCzpuqQo+zwg0+yiOa64MpPqS6Wb4I1Bu4KJPKfqQGfGUGAOoRMEzLjISHXa0vGIs/gH30Hd0QOODok4NteMPerIiMxubt/QyI8E6n1DyioTqcC1JPSf2TUTp1g8afma7oP6pcMt6P+aLz56iGrlJr6GmuInU1OYG+YvOLxLIFclL71afbNEVL1QqMRFDFJzAJ8Oulekf4ZKJDGOQX9tz8sTv7uqDBjneclMHhNzyJN+PZbdAJqaCNpzMI0AHJZMuRJZKTLlrEQiS/veYSgx03xCuoHiS0RRIFpZmacbPxXvYgXfCdAjE/WjPcr44khJeclFDbsSXiHR9PEuDrHnVCkUwMctALb4G8LnrzM2AJWCAKA+KdNW8G2r/koNDdJz936dBSjl09jyRJVy7jQhbjLc/f+nhQ+sY40wgCN4SwF1foeNfQhmnyrMa8H6ULaNyx37K34M97uv6a9byyPyw39Mlr0jKuRvoHvs9RyKTPEfbkewGL1MnNKIyrd9SuJEr33y3si4J6Rk1I8QbK8RRK9MCk7F8DatBW3QovvIqnIM23OekLdurxFWruVLnCZ0QI86Ke05ZasNp0y7cuavNAyCI9p2wqG6jqhzNS8+zIVSVx4tMj4uHssP695rHjQeTmowPRi8hln+/24H0XtCurbByo2fwcpPn+Heav1TmPHIX9qHJsFuglOOb2b062XzvE97haqokkNebf1ghMCxk3FL8rwStiEENqpUHhezvMsNc92Dl2L1POWMULnPP8qOBNf3v8+94exB/7V+HNMKRtZWxtetj3jytZjr+5+JRzb1BrUvWGOVRdxzPxjtPVOZkIssit3v5T8BsBfRn9oKXWP6pN4e7PSy/KBTe0ULOSC5/GeXTrlOQwT39n/q0kp62oAwUNL9nHWMOzvHA1dBQChAidcLt44fOAYWq8V5RlwCj27Qw2V+PJrAkjapwDN+oH0XHcNSWSEigspUD5ld9ZuyNQjL2enzjdq9/DxvvRoz1Prtnwwjvm32LTOq4FEtTNdEQ4vBPtlPpowmbbfD4e+OpfXvRjuucTLxdXrzJEIBgILC40EXM799+aLsqT1pEoIz8NIejkO1AsXiCecxEPYgI/AjtgYmxifBCoJ2G2JEZmE1iekR7rGmNK6PMVhh1LFmxaeurlUhejo++3nI1UUY1UnwO6tdL9VxQCLIGXpCDBEFLlS3+1Ca8FAsG/DTTKTbmw52F54sKS7+xlaouG13QjXxt5ZWB98Qc6qL+VhwBP4NxP0V5Rx/v4WwxiM9SZTw+0M+BWONXec5S4a2YJIIFBjU85rGaLI/UKfKR+tfweW2q+FZpXqOkGBJPfXYvfNsYlC/EBMkI9MWgoN7odzzj4QjZCFFkXGoPhORo/bAy3Ms5Bh9RDGnHbG2aWzgR+ZnM7qeFwfar6abJrfEuEJPtLcTvNLLV99KBZOKJ5++p24xJcVho0oDM3ZeHPHAmhW6dDqLb0zHryDaW1TZQnTp9zQRHvSC0ht13kiVe+X77TK12tJqkIFVYy2+HDJGTQCJV3OujgAPmtqDVo0QiTrfECfUPs0e3ALIaT/dDC3wKeuB4nK0/aCGCUg2UiYhL7yocKFUjSzUT7kgbwiyK+AyImLKpYLxYMBSF2+yS5mzmEkOADX34H6xulQsr7cmu/IljPmmwZi3fiRip/xeiS0iCAPvbRshWkMpMMfczOdYefeTPmrF55vpDkuNNxOJIDdg+cb0stiF5A+VP7jEr8gsKdQlier6q3K5Lv2fhBa0N1a704VgCDJ0boqcqZiLw+9Ydr9QdysoGvwZnaCTkgMJbgnGg4pGehXN5z2HRRM87exHeTtWhLvAwN38e/E2cwgmHRzi7+PHAKvfj+cNjyHJelp15ngpBL9aRocINdg80zCDL7qN88AxkyCSPpM0dNnGDYZVQuS5x4DlwjYax3qdztAcG0hkZF7boPh1F6deAGjNefZIeqOLeoEvq1rklzRHxOlVQ5ed0Ii4UJLxFNzc6hhqxX8o+PUna42AMWLWY5Ezu+B8ahiU/fyOEIG8Sh6n35OxZojIID4jzkfn4RDMVe+6AHvcOVUQdBiIVn0FsW2/m/pUHXY28/C4sE9KWf+fHpCPsbWvwg+l1aXz0Jei4wYrkP0VNKEahM8W8nJ6QIPcLHeMvSYvDmpHh6fsL9EeI8SKMVzH9knwfYeI3p69tbWxYwMni7zglhABLYVQHR3z27LkEkFvYoi6rd2QxwecyR6p/nh2ErWBTNcpCkTL+yNHtTP4ujhT8ZmX7Jb0WQ2UMzWhq0Hc7wG/iJX+cJJ6wcqs0CrMY95mXoCEJD6ROAS3HC8uNBSM2vP79g7LdtzBueTcl9V7fCsq77NweBnMtkP6BzVoUsRZ0PElUJ7amQHXnfeGfTKiv1IWwu6QOhb0X2VveTXdmz11Bbv9wQVs1sldBdzVrB0kmEG+xHl3Px1KnD0/zGlJ47mW1ZyLDGWWq++V0wnouiZXIgapl4amdRS2NT6rfFCNucQYhkHflV+Jl/RYnvEZ3J6t0yrx1YSu04fUdy6qePk5scW0ZAvovZVROGtkWFay5kLQa7gm9EvzT8FigEOITOxI/pZE45EUhPuraFXX4b/UAyFoI7GAcnJWmKyhtQ4JYqYJHjc5lC1mBnXVEAi51PXvwoXEqq/pmzjVNa6jEt4dzaa9RpCMVwom0o0mnL2KFJRxWb2x4FHXmdhTDq0FDlJiZKhN41mr7oq7ZP7SrYd7u6TaU0x1nb9d1sW0OEw5P9hmF+n79MCoAzWB3x5UegEu5qbwh4GNHimKu0CfHf8uWfvPx8kulxCT3KsxmALBM1ahBpmixP1YF2pUKBBvSTbuLgTZK1rK3rEbo62GdzB5a8MvFoNgn+zq+3QLBDwkG/bordxFQQeob9g9Ltz467+g/dh8OMHueTtlQ2rs9c5i0JgGqjMsuL0VIxYVUpXeZ8vBGD4lzPfFizMJxYcieHbf7WMjCfIJoLDd0TJ9HTmRQjoVmzOizyhb9Qqf9OtGGm9o9jPxZPHQS2kdoplc+Q41iYTz/cEc+6dtBuGxEmMtY1zLzguL/XMN2lGO/pWwamEUn6OoCuKIdgcwY967x9mAn7K7vB9ypJqfGMJage0UcT1nj8e4g49Ih1j/ezEBjv/kaYVS3gbOB23KYK62o836q8zDePJaZidVGsFpYOKbfIi7MLuJfgb4a1QsBjInBJD3UcgkuVz87/ppAq4nhJztEIlxNRAuudrkmGZh+M6KM0sqQIrUcSQC/QnGoNbD85rUmcdY9lPM+VAWkSn9rkS4Jk5woEoT4M1yrZxN7OgXLdvY6qvCbILANgx+eiBcc/yvg0lUkQNyqTvjiRFb1m1OJ+4aL5xkTo5wQQtTZa4+zs0m/bSVTut55NHUkegPIVhpjJ9dZM7pwi6JN66an1Tou2qG+EvIwnDykCOw0ihhI5WHeDmfQ3QAF+xlx3L+FQz8HyS5qln3CqjTY/BJ5jVPHcHStcmjQLL5dMmS5T/eIfMcCAmf/dwBzJyMT8NDBdGEBsBLfpXl9e2R14UIcYPwWzNMEgvmYt/f1NAqQ28VyAuf4hlnumsqBztUJB7pBP+mplY3PGH063siBcIBoWbT+WW/4Bu2iMtNS/F35h+BW1ulopZN7UTMKy9pQWnuYVlgjCvqWoqDZJGJj4qbJ7d4WuswLE82/iSCFOga0YpehRotWNp5GHCRaPfHvXjXj4NK5lmyglulmpfRGsfEkHCb0iRnLe3njk7mjN9Ic7E44NO+zvD0C16+G/P0TOZGt3mPWJvlXygKO60XSoAzoOdl3z/QmI7RJCaiaG7mmhCoCaXFfmvKv8pziYn4Uj1A3yr3Ld/ero6KtuIJvMQXkDlETF22R08aS91xGJXwSQgq1Ek75M6V9vXf62MMQzH5M/u295yZafAmRAcrZ6aKlPUtGafNAXxqXtO4NIcYE/hbhgtgSA1yfaS5YADfcEjRYC7Zva4ioS/SEtisQSK6kRhypeBcRF6YAtFA1kGusWFB+ZfiyoWb3v6mMaCwdv0mB/Rs4DTZx4jijjfP0SBHKTcHDd4g9xniIO9rvxxxNFOAY06uhaArUnbFTXRFHPlVMnDSc+gRDeMsvNWvQeP4t3ui72VwK6l3MMU+yx32w+m1bFXAJkfJiIxbldholEzG7aeyfiI9quVv47fx4JWPtGPA4v/0SwXkrPM3Zv4QdGHQvBKu1su8yVmVRiBee8HeFs70v0a7oXf/IMz3qA72SzIL0BH9WtPk0LXdPJ+TApM70KLOVkdk/LaV6XcaEgWF3kpSYNYe9cG9+C39g8R9bOJeK424gsC2WzzdoaL/Xsc6uVHmE4yVshD5J69Nlovr8b1f946HeNMryP+2/pPLZ7RYgQMeS+0fZLwcGH+4h0SDeI4sbMRuntYpof/2csvlmIDS+ORuoJ+FGJfbcNRSWPZcFSzTS4Hv2jxilDG1BF0DdkvoGrx7EOaVkFQ+iJbkDGKaaOL7TVC23xQUaLGUShfv0iTM2GZLRT6IDNiMMvK7y0pOAJqYIafIw6/FA7mofevvSmv/klqUjHTKH+j93s43GDWrUPIc0e/jQE+sQjDoFW7ICDHF28NC6Q7tbDWyMGLvQ8+SpVZMKM1seyo4EZWzBFWOGSgvQNw1uX1iM+ZqgAsc5zPBn6dSHFuMSjYSkNPD2XsQcH5h1G8kL22WsJ5ptaOHA6DUvGkKFjt8u+edeynUxT9Ldh4NOREspT6fqwHhw/Zg6RcLEXqqTzfgVn8InPrE2ng8Qx/zzieb3DcoAtIYa8+DojqBc2kLUIFQ4+c+Em7lyPFa2Wb263zMJNgWLRSg48ocp30+UrLgbyC3oCDVBL19hkH5pNeU9Yhv4IQJ0j7NQkMLzmJvBOWiIxP7Pe86bBKL8IBz1MoEHi3WLJfvmp1mmfHSPQrP2xsrCV6JrhbSM6ShWMyYn1z9Ibdr355QTm4IimQ9gaiUvUlzRlplrsxGLE2kt+Ki0GDOdPADx8AsTV05D55D0t2v++le6JN/k1s7v0s9lTs0qmHPFakxQ4v1EwU9Fw2j2nux92K0slaOI49JkiwkWkz/C1Ng87d3uagWp8yQ1c8rh8CC0qbAjl9ReS4HUFch2asbqKsKuD8DBWTfaUf0eqxtQnU20cpz980H80tBpD962N4ndBGNyj6c74JSltXrhUSwUgKw9PXozl+TpV3jIj5SWFroo/ty/YoEpy0+oklbGMd8F2+7Sq0FkSW7Yb+961ODAKi1ReTL4xpvIn7smHnr96S+3DKr9RSX/I5nFxy7YuftNgaz5bkanpHzB89KFLvE/14d2UaiVVpWds6wvqvDSXThqP/nYNhruqQj4SYOMzEYBxH69mb1feN2FHXeW2UTawp3byh3i05cf8sMWuGyOI56ACM40WMVJIjzsCtLhGIfVsUOHrCMTiGsHlYPIn7/Ty4T5KhiAZx2AQbfasRgr7Rb3OvJCaKakdJQqG3Esf2lp+NajGyUUyb90ZFwS9YVUJ8R6R5SQUNfqDQKy+4j8crjU5PYv3bMdbE7QcYl9U351Ta4s9eNikyn4e1OxvdKNoXH+KQpmb1GHRj0C3JHTLcJg3waLMsm0vVcTrBt0DhC0c2jmDQWBubG/vzNqRvg7q3Ff6RdamSFTDL2ofnR38Ug2+40eQRDn2E6B9Yffr+jQSCr0VyWA6RXfU+tiAhoeA20PDbztNhw0r6zvKzoE2kr9HIN6QoM4qMdNgtKM2TuXx1NC3dLE/Zn/MkQK5r183t1G1CIqKw6v/nCKf+y3WkNzDpk29jN8UHG1JoaDnzdtBD0D69d9XDbI0haPta1y/nPJy/AvLqNYq4/UL/+4C2BZqibwNxeKPIEisEUIFFVNKbvHvPM2eZoTJI09DJkAGtnVntmZsYixKhaNYM1kkPMlhDGMRsUZ83m7TJ86TO9wekPigcuKhJi5iPQHZCzu3YH+rTvr5scrxezMYoGrWS3E1RNEvSn+OCLEMMdnc7/kzI2UZdgyCn+wRJ7cm8N6gT308la0pZc6K4USfQBNe1rPle55m8DPAZffMPFL2IjpaaKH5YFZzeb4wEnEGZeWywnWEklHTMnpTZND1e/zLpOBXXRxTCgaJuYpvOWrxdx8AYlDzilMjf2B3ryQivIZ8nG6A6CRX+MsygrRbgpiheEA9Y0jmZsP2JM60VsWr5lcjaGo4pb2oLaks9SIrBMCFR+hnJza7hJlQUc/OhUuD08d4A1DM+ZD9DXht1S6kt1StHJcv2aaXnQEVtNdfZSshTPXju/pSLp/vn0b0ofSW5WHEgSSJ9HBbgnCgrz1fiVfDESJ2R50IRDM8QQIWIQa9wWH7zbJ+YDinpaVHJxMlyAIrMxsgZqBvBTgAQKLAngP33GbFH63SVc7PII7Q6NGTXFBOUxR2A0oxxfBS/BJkAXrmnVINQafbmhnNE/rfE0iIQFuX+4uuqujBXv1dXb7jEUkgiwiESyWqaOxRr3CW01iEFgL+wiYGKT1YiETsXC9fg+TQlwkKbwI6OMT+itoc4VHMlZZxB14xANcky20H9OyOff3Iask2RKkdQtMZkrM7cgjAbEtqAIP13A7K+OVaoMN8kXI8PY5NRBvMTrOcitK7l2x1MJ9L+4rVfbmIbPA0OgNhXssS8Lu2Jz+F9B3Mh7iRguLEXwsmfCCAbVO81HRpzrdeKNbUaEH5QSlGUKavrn62WtBA+rZ6LR69MnSCAaIy51Vi+SfA807Ad1qPkxHzP7nPyIwey1TrvYgEGV8d4yaPsgjN/KhL5ZysM8oxIh7c9gff0UmB0gyRLwJrHCb70tnBrEKD/K6Ob2DLHfSXKqpn1AM1ibklI9zqo729r4DiAH6cnwtLI+d+1sXhLbyri61qF4VEXaJnxAh8Lcbm+nCf1QhfuCDbRloOvk770Clx5+weXz03FqvXanR11d/9+UUlgiTPaxkriVEOUB/PVce51LhepPzgIRhlG43xIWBtK1lwPZY+hK3fF8MEsJEd6AAytOB/CQy2u7XV5pcvXkYgJpYQxjDfvseRopJLNl5P8IvnZM29Spw39FC5KssimhMwpnT4eUjR13DRV+JthPpX8og6FBaRkAZmnIk8ZIa3UyEigDdAgbTBkIN5azvU7OPx636QSAFotGFNCDuwqMM1O/tuxS1fjzjUEiQ9mxl/+BZe27xBKejwqr4APkNQOWlmdeMo7VQEjPXVqFpGSNv2rIYQtyYZ7LQPj174oaBP3NVkl3zvOGB3lRLeWfKKmITGSW6Y0duT6vf5MsmCzOsuyqeOWTrLB+kYfcjdTo1vxRxg+Om6N4io47xhmipoam4s+N6rTKyEClN5Gff55neK0Q8YS6bP+4skxSkziJRNW8bjfLqrPxuEWyBEjovicB5Njllyf5/lfN3xIP1YRXXfcQgKqbs64KSsdScqks0PLzc8VQobBpMiPnMU+8UMPTPcXW1WOE52QQTQKDErcIz1mzVvk7IwGfzShB2betQyEKPjghHmWHN+NrMQyjHSHUsDGPFxrXPqzOSYCV2DfqRd8+CAfRa9T8RQveypGcLDQqFfSKSZbMLQ492Ie5XA1W2xkz75gTO1+QxLoV7z3yN6AKaOpm6LK+a24FYjydF0cEVtu6eqHgUGqq/19adKdvjzt5QWGQrW9+qAOdXI2gKJBARHpCRgYN8p3BUTMUu59wy3FUsgvbCcYsaoxz+VfrJHkaC4IWeUNlIHaHEuyas2+baeK2GjLUA/IR3Kvfv9BEvnw04PVVQVvhN7Dr8ze5wTAye0GwJ+IuXJT3SL2qB0fRVa/GN9qE5mJWewNAKvp6qNft6mzeeeMI+cyJ0cmoxTPI9JCoOIoh8MlyzUBMjLATpEURWZTNcTcQO9cJTe3lZYxSZw5XdVxsivlu9cIqcD69mVg17hdltImRlgKk8m8aWCmjSsNad5IxF/WxallP+MyuCFmllgIxeC+9aXiLuWp3prwHjIaPDd5KlAYR/aEw0sviarBC/VZ2kl7xYIT7FzjCG+tSjNoP48GcrP4/9et1WsxHdBi5swSnb7AMYO5IeJXnAuxg9WDEdsuicOGGCPq/fuhQAKEKG5jTsicEV3cPZHMhqTUXo2gT8HDx58jw/hb5O/Qp/BQUDfqNCQbWACYqlNlB45cApzBskmDGHzCdDbhdqrV6Sn9UG1V7IoNVvdLWZ90s/HUgQ4wkRJrQzgen1iZVzQZuYUBrVnElfFCsQXvWc4t3pFAGWGuIamYtM8VoBk3nayAs9v/gQRs7YxKsNHYD1E47fqBHSjN/5u3s8FFcflBeC2syeP/Zxu1JuXTw55bsjfvxXmeO/FAlvXQKRDYrxaHbVrLv5B6bcLIcp6ZnxrTOtMcpit6tcVrX3KIgKnVG5avDaCWXf8kJYmn816denp8g+PbfrbipCFxLlRviKzSKT/FNoWRT3u8jRAEF9Xfs0N+YF6ZH6H61SsXWJULXaxowpx/4aq0eBPWcRUoouTmVBASDw0TNk9S4+PvaNVWHuyAsI1WrYfS/XbkmvHGerluccsCsFR3d1Yy/gy9N/akakgEOa6nBx6ycgdiXORmRoaTgwIpS/DhyFFLL02AQg7fvTuPKJDUVCwyRAj0hIh5G1phWUARsQEhvePvqXIhpfwqdDgCvVGv8LDx2dIkvntpV3BTsHv1Mf8zm9BjECzHJmFq49vwx84TZZQd36Bjy4s9bdWoN8AtafSOY1DWBAWRFSgiC3Y2Hn2IAf75dGIsJC21VX3plrr+aVrcKlsnnrFdrJeTO7hGBFk+iz4j4nJyhskwcS0WLxfQs1j/DBu5gjX4IO1h4/b9CNUL9UWDfpIayNAvZOdKy0MQNzl6RppDlfzbrBTjh7n7kUvaerxrck2cxhRv5fV7ZOmyVXCDu3DK+cQ3cf8Tkk/9X+WQr+RSO8xosRnsbLl2jsUr1jXpIsU84UKv11WMklJInlC7JpFipM0sbfWKGigaT+u/TzznkdxvGh1l8g3mx029XtMI3Z9n8zjbhR7ZtMuXrp6aIzK4rseAGupj9M8pfnXtwnwBS0qHoTki3pSaXdqoQagEvhyWAn3du2WmBDdd+huy6rCdzJ7iCK/AMX5ZO+iulzo5dx+I6sgefoLhxZ8Nd/Eqq17PBbGz+wt6IQ0cS3914obfmVwLHm8FCbUw1tympuJ7oM04RW/VpeOF8yp//W//vnXP+n9BtA//wWjEIFD//qnbLpiSPrin//6JxuHoci2Iv/3Onb71ozDv5OqGLb/nO53v+pppn//n52xL0bC//pnrRME/7x7ImiGF3n5JWEsTz8kDJMFgn3QBEeIDMs/CZIXBfnBUhIr8fKTklBJ5mWZ5nCOExmZlP/893//659pGY+3KUP2tuX/+mcpkvy//ufw//X/167/+1//LFnzNgH+T+ht5Nrt1fuPJVn+4zfm93+c//H/7vwf/8/Of5vd61b0/37/byuu7Z//Gvau+9c/W1Ktf4fOxqnpxu3f67bnzfhu/v814H+Ou74fTeNZLP+eumR7jaV/P8iLqRv/+ql5f2e1JP/nSO+uR7FsxfLX0ven9e/j/2ntf6L//Pf/BmMAnX67OAEA -->
