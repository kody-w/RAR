---
name: "rar-kody-w-connected-solution"
description: "Turn an agent stack (a folder of BasicAgent *.py files + optional metadata.json) or an explicit list of sub-agents into ONE import-ready Microsoft Copilot Studio connected-agent solution: an orchestrator plus one connected sub-agent per agent, wired with InvokeConnectedAgentTaskAction. When an agent.py carries its compiled CapIR (t2p-capir/1.0) \u2014 or one can be recompiled from its seeded data \u2014 each sub-agent ALSO gets a REAL deterministic capability topic that runs the same steps as the agent.py's perform() (trigger -> the user's real query -> filter the seeded records -> branch -> respond, plus the document for artifact capabilities); only the data is mocked, so flipping the in-topic Table() to a live Dataverse / SharePoint connector is the one-line move to production. No code deploy. Bot names are auto-capped to 42 chars and orchestrator channels default off so it imports and publishes fully headlessly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/connected_solution_agent", "rar_sha256": "23c5edf7914db69119e2463a528c4d6a2dee964b94f5f6b90f9dffbd1d58c9af", "source_kind": "rar-agent", "source_commit": "b4ba983328bbb00340c62a83332318dc0ffc22aa", "version": "1.0.3", "author": "Kody Wildfeuer", "tags": ["copilot_studio", "connected_agents", "power_platform", "deploy", "integration", "converter"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/connected_solution_agent`. The original RAPP
agent is preserved byte-for-byte in `connected_solution_agent.py` and in the RCI capsule.

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

<!-- rci-capsule:v1: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 -->
