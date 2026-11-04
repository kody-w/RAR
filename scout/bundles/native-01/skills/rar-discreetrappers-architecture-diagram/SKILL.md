---
name: "rar-discreetrappers-architecture-diagram"
description: "Generate professional architecture diagrams.\n\nSupported diagram types:\n- azure: Azure cloud architecture\n- agent_system: AI agent/orchestrator architecture\n- multi_tier: N-tier application architecture\n- microservices: Microservices architecture\n- data_flow: Data pipeline/flow diagram\n- custom: Custom node/connection diagram\n\nOutput formats: png, svg, pdf, mermaid, drawio\n\nActions:\n- create_diagram: Create a diagram from specification\n- diagram_from_agents: Generate diagram from RAPP agent configurations\n- list_node_types: List available node types\n- generate_mermaid: Generate Mermaid.js code\n\nExample:\n{\n  \"action\": \"create_diagram\",\n  \"diagram_type\": \"azure\",\n  \"title\": \"RAPP Architecture\",\n  \"output_format\": \"png\",\n  \"nodes\": [\n    {\"id\": \"user\", \"type\": \"user\", \"label\": \"User\"},\n    {\"id\": \"func\", \"type\": \"function_app\", \"label\": \"Azure Functions\"},\n    {\"id\": \"openai\", \"type\": \"openai\", \"label\": \"Azure OpenAI\"}\n  ],\n  \"connections\": [\n    {\"from\": \"user\", \"to\": \"func\", \"label\": \"HTTP\"},\n    {\"from\": \"func\", \"to\": \"openai\", \"label\": \"API\"}\n  ]\n}"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/architecture_diagram_agent", "rar_sha256": "d5cac1baac38b585dead94b556dd7c6a5feb8772944bca8b6d88be70985161be", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Bill Whalen", "tags": ["productivity", "diagrams", "architecture", "visualization", "mermaid"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/architecture_diagram_agent`. The original RAPP
agent is preserved byte-for-byte in `architecture_diagram_agent.py` and in the RCI capsule.

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

Architecture Diagram Agent
Purpose: Generate professional architecture diagrams for system documentation

Supported diagram types:
- Cloud architecture (Azure, AWS, GCP, On-premise)
- Multi-tier/N-tier architecture
- Microservices architecture
- Data flow diagrams
- Agent/AI system architecture
- Network topology

Output formats:
- PNG (default)
- SVG (for web/scalable)
- PDF (for documents)
- Mermaid (text-based, for markdown)
- Draw.io XML (for Visio compatibility)

Dependencies:
- diagrams: Python library for cloud architecture diagrams
- graphviz: Graph visualization (required by diagrams)

Usage:
1. Simple: action="create_diagram", diagram_type="azure", title="My Architecture"
2. Custom: action="create_diagram", nodes=[...], connections=[...], clusters=[...]
3. From agent config: action="diagram_from_agents", agents=[...]

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "enum": [
        "create_diagram",
        "diagram_from_agents",
        "list_node_types",
        "generate_mermaid"
      ],
      "type": "string"
    },
    "agents": {
      "description": "Agent configurations for diagram_from_agents",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "clusters": {
      "items": {
        "properties": {
          "id": {
            "type": "string"
          },
          "label": {
            "type": "string"
          },
          "nodes": {
            "items": {
              "type": "string"
            },
            "type": "array"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "connections": {
      "items": {
        "properties": {
          "from": {
            "type": "string"
          },
          "label": {
            "type": "string"
          },
          "style": {
            "type": "string"
          },
          "to": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "customer": {
      "description": "Customer name - creates a subfolder in arch_diagrams for this customer",
      "type": "string"
    },
    "diagram_type": {
      "enum": [
        "azure",
        "agent_system",
        "multi_tier",
        "microservices",
        "data_flow",
        "custom"
      ],
      "type": "string"
    },
    "nodes": {
      "items": {
        "properties": {
          "cluster": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "label": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "output_dir": {
      "type": "string"
    },
    "output_filename": {
      "type": "string"
    },
    "output_format": {
      "enum": [
        "png",
        "svg",
        "pdf",
        "mermaid",
        "drawio"
      ],
      "type": "string"
    },
    "style": {
      "enum": [
        "default",
        "dark",
        "minimal"
      ],
      "type": "string"
    },
    "title": {
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `architecture_diagram_agent.py` and embedded as the fenced Python below (sha256 d5cac1baac38b585…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `architecture_diagram_agent.py` first:

```bash
python3 architecture_diagram_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 architecture_diagram_agent.py   # or on stdin
python3 architecture_diagram_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/architecture_diagram_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/architecture_diagram_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/architecture_diagram_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Architecture Diagram Agent
Purpose: Generate professional architecture diagrams for system documentation

Supported diagram types:
- Cloud architecture (Azure, AWS, GCP, On-premise)
- Multi-tier/N-tier architecture
- Microservices architecture
- Data flow diagrams
- Agent/AI system architecture
- Network topology

Output formats:
- PNG (default)
- SVG (for web/scalable)
- PDF (for documents)
- Mermaid (text-based, for markdown)
- Draw.io XML (for Visio compatibility)

Dependencies:
- diagrams: Python library for cloud architecture diagrams
- graphviz: Graph visualization (required by diagrams)

Usage:
1. Simple: action="create_diagram", diagram_type="azure", title="My Architecture"
2. Custom: action="create_diagram", nodes=[...], connections=[...], clusters=[...]
3. From agent config: action="diagram_from_agents", agents=[...]
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/architecture_diagram_agent",
    "version": "1.0.1",
    "display_name": "ArchitectureDiagramAgent",
    "description": "Generates architecture diagrams as PNG, SVG, PDF, Mermaid, or Draw.io XML from node/connection configs via the diagrams+graphviz library.",
    "author": "Bill Whalen",
    "tags": ["productivity", "diagrams", "architecture", "visualization", "mermaid"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import logging
import os
import tempfile
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
from agents.basic_agent import BasicAgent

# Check for diagrams library and set up Graphviz path
DIAGRAMS_AVAILABLE = False
DIAGRAMS_IMPORT_ERROR = ""

# Ensure Graphviz is on PATH for Windows
import platform
if platform.system() == "Windows":
    graphviz_paths = [
        r"C:\Program Files\Graphviz\bin",
        r"C:\Program Files (x86)\Graphviz\bin",
    ]
    for gv_path in graphviz_paths:
        if os.path.exists(gv_path) and gv_path not in os.environ.get("PATH", ""):
            os.environ["PATH"] = gv_path + os.pathsep + os.environ.get("PATH", "")
            break

try:
    from diagrams import Diagram, Cluster, Edge
    from diagrams.azure.compute import FunctionApps, VM, ContainerInstances, KubernetesServices
    from diagrams.azure.database import CosmosDb, SQLDatabases, CacheForRedis, DatabaseForPostgresqlServers
    from diagrams.azure.integration import LogicApps, ServiceBus, APIManagement
    from diagrams.azure.ml import CognitiveServices, MachineLearningServiceWorkspaces, BotServices
    from diagrams.azure.network import LoadBalancers, VirtualNetworks, ApplicationGateway, CDNProfiles, Firewall
    from diagrams.azure.security import KeyVaults, ApplicationSecurityGroups
    from diagrams.azure.storage import StorageAccounts, BlobStorage, DataLakeStorage
    from diagrams.azure.web import AppServices, AppServicePlans
    from diagrams.azure.analytics import AnalysisServices, DataFactories, Databricks
    from diagrams.onprem.client import Users, Client
    from diagrams.onprem.compute import Server
    from diagrams.onprem.network import Internet
    from diagrams.programming.language import Python
    from diagrams.generic.compute import Rack
    from diagrams.generic.database import SQL
    from diagrams.generic.storage import Storage
    from diagrams.saas.chat import Slack, Teams
    DIAGRAMS_AVAILABLE = True
except ImportError as e:
    DIAGRAMS_IMPORT_ERROR = str(e)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ArchitectureDiagramAgent(BasicAgent):
    """
    Agent for generating professional architecture diagrams.
    Supports Azure, AWS, GCP, and custom architectures.
    """

    # Node type mappings for Azure
    AZURE_NODES = {
        "function": "FunctionApps",
        "function_app": "FunctionApps",
        "functions": "FunctionApps",
        "vm": "VM",
        "container": "ContainerInstances",
        "aks": "KubernetesServices",
        "kubernetes": "KubernetesServices",
        "app_service": "AppServices",
        "web_app": "AppServices",
        "cosmos": "CosmosDb",
        "cosmosdb": "CosmosDb",
        "sql": "SQLDatabases",
        "postgres": "DatabaseForPostgresqlServers",
        "redis": "CacheForRedis",
        "blob": "BlobStorage",
        "storage": "StorageAccounts",
        "datalake": "DataLakeStorage",
        "logic_app": "LogicApps",
        "service_bus": "ServiceBus",
        "apim": "APIManagement",
        "api_management": "APIManagement",
        "cognitive": "CognitiveServices",
        "openai": "CognitiveServices",
        "ai": "CognitiveServices",
        "bot": "BotServices",
        "ml": "MachineLearningServiceWorkspaces",
        "databricks": "Databricks",
        "data_factory": "DataFactories",
        "load_balancer": "LoadBalancers",
        "vnet": "VirtualNetworks",
        "app_gateway": "ApplicationGateway",
        "cdn": "CDNProfiles",
        "firewall": "Firewall",
        "key_vault": "KeyVaults",
        "security": "ApplicationSecurityGroups",
    }

    # Generic node types
    GENERIC_NODES = {
        "user": "Users",
        "users": "Users",
        "client": "Client",
        "internet": "Internet",
        "teams": "Teams",
        "slack": "Slack",
        "server": "Server",
        "database": "SQL",
        "storage": "Storage",
        "compute": "Rack",
        "python": "Python",
        "agent": "Rack",
    }

    # Diagram styles - Professional Visio-quality settings
    STYLES = {
        "default": {
            "graph_attr": {
                "fontsize": "16",
                "fontname": "Segoe UI",
                "bgcolor": "white",
                "pad": "1.0",
                "splines": "spline",
                "nodesep": "1.2",
                "ranksep": "1.5",
                "dpi": "300",
                "overlap": "false",
            },
            "node_attr": {
                "fontsize": "13",
                "fontname": "Segoe UI",
            },
            "edge_attr": {
                "fontsize": "11",
                "fontname": "Segoe UI",
                "color": "#666666",
                "penwidth": "1.5",
            }
        },
        "professional": {
            "graph_attr": {
                "fontsize": "18",
                "fontname": "Segoe UI Semibold",
                "bgcolor": "white",
                "pad": "1.5",
                "splines": "spline",
                "nodesep": "1.5",
                "ranksep": "2.0",
                "dpi": "300",
                "overlap": "false",
                "sep": "+25,25",
            },
            "node_attr": {
                "fontsize": "14",
                "fontname": "Segoe UI",
            },
            "edge_attr": {
                "fontsize": "12",
                "fontname": "Segoe UI",
                "color": "#0078D4",
                "penwidth": "2.0",
            }
        },
        "microsoft": {
            "graph_attr": {
                "fontsize": "18",
                "fontname": "Segoe UI Semibold",
                "bgcolor": "#FAFAFA",
                "pad": "1.5",
                "splines": "spline",
                "nodesep": "1.8",
                "ranksep": "2.5",
                "dpi": "300",
                "overlap": "false",
                "sep": "+30,30",
                "esep": "+15,15",
            },
            "node_attr": {
                "fontsize": "14",
                "fontname": "Segoe UI",
            },
            "edge_attr": {
                "fontsize": "12",
                "fontname": "Segoe UI",
                "color": "#0078D4",
                "penwidth": "2.0",
                "arrowsize": "1.0",
            }
        },
        "enterprise": {
            "graph_attr": {
                "fontsize": "20",
                "fontname": "Segoe UI Semibold",
                "bgcolor": "white",
                "pad": "2.0",
                "splines": "spline",
                "nodesep": "2.0",
                "ranksep": "3.0",
                "dpi": "300",
                "overlap": "false",
                "sep": "+40,40",
                "esep": "+20,20",
                "concentrate": "false",
            },
            "node_attr": {
                "fontsize": "15",
                "fontname": "Segoe UI",
                "margin": "0.3,0.2",
            },
            "edge_attr": {
                "fontsize": "13",
                "fontname": "Segoe UI",
                "color": "#0078D4",
                "penwidth": "2.5",
                "arrowsize": "1.2",
                "labeldistance": "3.0",
                "labelangle": "25",
            }
        },
        "dark": {
            "graph_attr": {
                "fontsize": "16",
                "fontname": "Segoe UI",
                "bgcolor": "#1a1a2e",
                "fontcolor": "white",
                "pad": "1.0",
                "dpi": "300",
                "overlap": "false",
                "nodesep": "1.5",
                "ranksep": "2.0",
            },
            "node_attr": {
                "fontsize": "13",
                "fontname": "Segoe UI",
                "fontcolor": "white",
            },
            "edge_attr": {
                "fontsize": "11",
                "fontname": "Segoe UI",
                "fontcolor": "white",
                "color": "#00BCF2",
                "penwidth": "1.5",
            }
        },
        "minimal": {
            "graph_attr": {
                "fontsize": "14",
                "fontname": "Segoe UI Light",
                "bgcolor": "white",
                "pad": "0.8",
                "splines": "polyline",
                "nodesep": "1.0",
                "ranksep": "1.2",
                "dpi": "300",
                "overlap": "false",
            },
            "node_attr": {
                "fontsize": "12",
                "fontname": "Segoe UI Light",
            },
            "edge_attr": {
                "fontsize": "10",
                "fontname": "Segoe UI Light",
                "color": "#999999",
                "penwidth": "1.0",
            }
        }
    }

    def __init__(self):
        self.name = 'ArchitectureDiagramAgent'
        self.metadata = {
            "name": self.name,
            "description": """Generate professional architecture diagrams.

Supported diagram types:
- azure: Azure cloud architecture
- agent_system: AI agent/orchestrator architecture
- multi_tier: N-tier application architecture
- microservices: Microservices architecture
- data_flow: Data pipeline/flow diagram
- custom: Custom node/connection diagram

Output formats: png, svg, pdf, mermaid, drawio

Actions:
- create_diagram: Create a diagram from specification
- diagram_from_agents: Generate diagram from RAPP agent configurations
- list_node_types: List available node types
- generate_mermaid: Generate Mermaid.js code

Example:
{
  "action": "create_diagram",
  "diagram_type": "azure",
  "title": "RAPP Architecture",
  "output_format": "png",
  "nodes": [
    {"id": "user", "type": "user", "label": "User"},
    {"id": "func", "type": "function_app", "label": "Azure Functions"},
    {"id": "openai", "type": "openai", "label": "Azure OpenAI"}
  ],
  "connections": [
    {"from": "user", "to": "func", "label": "HTTP"},
    {"from": "func", "to": "openai", "label": "API"}
  ]
}""",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["create_diagram", "diagram_from_agents", "list_node_types", "generate_mermaid"]
                    },
                    "diagram_type": {
                        "type": "string",
                        "enum": ["azure", "agent_system", "multi_tier", "microservices", "data_flow", "custom"]
                    },
                    "title": {"type": "string"},
                    "output_format": {
                        "type": "string",
                        "enum": ["png", "svg", "pdf", "mermaid", "drawio"]
                    },
                    "style": {
                        "type": "string",
                        "enum": ["default", "dark", "minimal"]
                    },
                    "nodes": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "type": {"type": "string"},
                                "label": {"type": "string"},
                                "cluster": {"type": "string"}
                            }
                        }
                    },
                    "connections": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "from": {"type": "string"},
                                "to": {"type": "string"},
                                "label": {"type": "string"},
                                "style": {"type": "string"}
                            }
                        }
                    },
                    "clusters": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "label": {"type": "string"},
                                "nodes": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                }
                            }
                        }
                    },
                    "agents": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Agent configurations for diagram_from_agents"
                    },
                    "customer": {
                        "type": "string",
                        "description": "Customer name - creates a subfolder in arch_diagrams for this customer"
                    },
                    "output_filename": {"type": "string"},
                    "output_dir": {"type": "string"}
                },
                "required": ["action"]
            }
        }
        super().__init__(self.name, self.metadata)
        self.base_path = self._find_base_path()

    def _find_base_path(self) -> str:
        """Find the base path for the RAPP project."""
        possible_paths = [
            os.getcwd(),
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        ]
        for path in possible_paths:
            if os.path.exists(os.path.join(path, "agents")):
                return path
        return os.getcwd()

    def perform(self, **kwargs) -> str:
        """Execute the requested action."""
        action = kwargs.get('action', 'create_diagram')

        try:
            if action == 'list_node_types':
                return self._list_node_types()
            elif action == 'generate_mermaid':
                return self._generate_mermaid(**kwargs)
            elif action == 'diagram_from_agents':
                return self._diagram_from_agents(**kwargs)
            elif action == 'create_diagram':
                output_format = kwargs.get('output_format', 'png')
                if output_format == 'mermaid':
                    return self._generate_mermaid(**kwargs)
                elif output_format == 'drawio':
                    return self._generate_drawio(**kwargs)
                else:
                    return self._create_diagram(**kwargs)
            else:
                return json.dumps({
                    "status": "error",
                    "error": f"Unknown action: {action}",
                    "available_actions": ["create_diagram", "diagram_from_agents", "list_node_types", "generate_mermaid"]
                })
        except Exception as e:
            logger.error(f"Diagram generation error: {e}")
            import traceback
            return json.dumps({
                "status": "error",
                "error": str(e),
                "traceback": traceback.format_exc()
            })

    def _list_node_types(self) -> str:
        """List available node types."""
        return json.dumps({
            "status": "success",
            "azure_nodes": list(self.AZURE_NODES.keys()),
            "generic_nodes": list(self.GENERIC_NODES.keys()),
            "note": "Use these type values in the 'type' field of node definitions"
        }, indent=2)

    def _create_diagram(self, **kwargs) -> str:
        """Create a diagram using the diagrams library."""
        if not DIAGRAMS_AVAILABLE:
            return json.dumps({
                "status": "error",
                "error": f"diagrams library not available: {DIAGRAMS_IMPORT_ERROR}",
                "suggestion": "Install with: pip install diagrams",
                "fallback": "Use output_format='mermaid' for text-based diagrams"
            })

        title = kwargs.get('title', 'Architecture Diagram')
        diagram_type = kwargs.get('diagram_type', 'custom')
        output_format = kwargs.get('output_format', 'png')
        output_filename = kwargs.get('output_filename', 'architecture_diagram')
        customer = kwargs.get('customer', '')
        style = kwargs.get('style', 'professional')  # Default to professional style
        nodes = kwargs.get('nodes', [])
        connections = kwargs.get('connections', [])
        clusters = kwargs.get('clusters', [])

        # Build output directory - create customer subfolder if specified
        base_output_dir = kwargs.get('output_dir', os.path.join(self.base_path, 'docs', 'arch_diagrams'))
        if customer:
            # Sanitize customer name for folder (lowercase, replace spaces with underscores)
            customer_folder = customer.lower().replace(' ', '_').replace('-', '_')
            customer_folder = ''.join(c for c in customer_folder if c.isalnum() or c == '_')
            output_dir = os.path.join(base_output_dir, customer_folder)
        else:
            output_dir = base_output_dir

        # Ensure output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Clean filename (remove extension if present)
        if output_filename.endswith(('.png', '.svg', '.pdf')):
            output_filename = output_filename.rsplit('.', 1)[0]

        # Use temp directory for rendering to avoid path issues with spaces/OneDrive
        import shutil
        temp_dir = tempfile.mkdtemp()
        temp_output_path = os.path.join(temp_dir, output_filename)
        final_output_dir = output_dir
        final_output_path = os.path.join(final_output_dir, f"{output_filename}.{output_format}")

        # Get style configuration
        style_config = self.STYLES.get(style, self.STYLES["professional"])

        try:
            with Diagram(
                title,
                filename=temp_output_path,
                outformat=output_format,
                show=False,
                graph_attr=style_config["graph_attr"],
                node_attr=style_config.get("node_attr", {}),
                edge_attr=style_config.get("edge_attr", {})
            ):
                # Create node objects
                node_objects = {}

                # Handle clusters
                cluster_objects = {}
                for cluster in clusters:
                    cluster_id = cluster.get('id', cluster.get('label', 'Cluster'))
                    cluster_label = cluster.get('label', cluster_id)
                    cluster_objects[cluster_id] = {"label": cluster_label, "nodes": cluster.get('nodes', [])}

                # Create nodes within clusters first
                for cluster_id, cluster_info in cluster_objects.items():
                    with Cluster(cluster_info["label"]):
                        for node in nodes:
                            if node.get('cluster') == cluster_id:
                                node_obj = self._create_node(node)
                                if node_obj:
                                    node_objects[node['id']] = node_obj

                # Create standalone nodes
                for node in nodes:
                    if node['id'] not in node_objects:
                        node_obj = self._create_node(node)
                        if node_obj:
                            node_objects[node['id']] = node_obj

                # Create connections
                for conn in connections:
                    from_id = conn.get('from')
                    to_id = conn.get('to')
                    label = conn.get('label', '')
                    
                    if from_id in node_objects and to_id in node_objects:
                        if label:
                            node_objects[from_id] >> Edge(label=label) >> node_objects[to_id]
                        else:
                            node_objects[from_id] >> node_objects[to_id]

            # Move file from temp to final location
            temp_file = f"{temp_output_path}.{output_format}"
            if os.path.exists(temp_file):
                shutil.copy2(temp_file, final_output_path)
                # Clean up temp directory
                shutil.rmtree(temp_dir, ignore_errors=True)
            
            return json.dumps({
                "status": "success",
                "filename": f"{output_filename}.{output_format}",
                "path": final_output_path,
                "diagram_type": diagram_type,
                "style": style,
                "node_count": len(nodes),
                "connection_count": len(connections),
                "note": "Professional Visio-quality diagram with Azure icons"
            }, indent=2)

        except Exception as e:
            logger.error(f"Diagram creation failed: {e}")
            # Clean up temp directory
            if 'temp_dir' in locals():
                shutil.rmtree(temp_dir, ignore_errors=True)
            # Fallback to mermaid
            return self._generate_mermaid(**kwargs)

    def _create_node(self, node: Dict) -> Any:
        """Create a diagram node based on type."""
        node_type = node.get('type', 'server').lower()
        label = node.get('label', node.get('id', 'Node'))

        # Try Azure nodes first
        if node_type in self.AZURE_NODES:
            node_class_name = self.AZURE_NODES[node_type]
            # Get the class from the appropriate module
            if node_class_name == "FunctionApps":
                return FunctionApps(label)
            elif node_class_name == "VM":
                return VM(label)
            elif node_class_name == "ContainerInstances":
                return ContainerInstances(label)
            elif node_class_name == "KubernetesServices":
                return KubernetesServices(label)
            elif node_class_name == "AppServices":
                return AppServices(label)
            elif node_class_name == "CosmosDb":
                return CosmosDb(label)
            elif node_class_name == "SQLDatabases":
                return SQLDatabases(label)
            elif node_class_name == "DatabaseForPostgresqlServers":
                return DatabaseForPostgresqlServers(label)
            elif node_class_name == "CacheForRedis":
                return CacheForRedis(label)
            elif node_class_name == "BlobStorage":
                return BlobStorage(label)
            elif node_class_name == "StorageAccounts":
                return StorageAccounts(label)
            elif node_class_name == "DataLakeStorage":
                return DataLakeStorage(label)
            elif node_class_name == "LogicApps":
                return LogicApps(label)
            elif node_class_name == "ServiceBus":
                return ServiceBus(label)
            elif node_class_name == "APIManagement":
                return APIManagement(label)
            elif node_class_name == "CognitiveServices":
                return CognitiveServices(label)
            elif node_class_name == "BotServices":
                return BotServices(label)
            elif node_class_name == "MachineLearningServiceWorkspaces":
                return MachineLearningServiceWorkspaces(label)
            elif node_class_name == "Databricks":
                return Databricks(label)
            elif node_class_name == "DataFactories":
                return DataFactories(label)
            elif node_class_name == "LoadBalancers":
                return LoadBalancers(label)
            elif node_class_name == "VirtualNetworks":
                return VirtualNetworks(label)
            elif node_class_name == "ApplicationGateway":
                return ApplicationGateway(label)
            elif node_class_name == "CDNProfiles":
                return CDNProfiles(label)
            elif node_class_name == "Firewall":
                return Firewall(label)
            elif node_class_name == "KeyVaults":
                return KeyVaults(label)
            elif node_class_name == "ApplicationSecurityGroups":
                return ApplicationSecurityGroups(label)

        # Try generic nodes
        if node_type in self.GENERIC_NODES:
            node_class_name = self.GENERIC_NODES[node_type]
            if node_class_name == "Users":
                return Users(label)
            elif node_class_name == "Client":
                return Client(label)
            elif node_class_name == "Internet":
                return Internet(label)
            elif node_class_name == "Teams":
                return Teams(label)
            elif node_class_name == "Slack":
                return Slack(label)
            elif node_class_name == "Server":
                return Server(label)
            elif node_class_name == "SQL":
                return SQL(label)
            elif node_class_name == "Storage":
                return Storage(label)
            elif node_class_name == "Rack":
                return Rack(label)
            elif node_class_name == "Python":
                return Python(label)

        # Default to Server
        return Server(label)

    def _generate_mermaid(self, **kwargs) -> str:
        """Generate Mermaid.js diagram code."""
        title = kwargs.get('title', 'Architecture Diagram')
        diagram_type = kwargs.get('diagram_type', 'custom')
        nodes = kwargs.get('nodes', [])
        connections = kwargs.get('connections', [])
        clusters = kwargs.get('clusters', [])
        output_filename = kwargs.get('output_filename', 'architecture_diagram')
        customer = kwargs.get('customer', '')

        # Build output directory - create customer subfolder if specified
        base_output_dir = kwargs.get('output_dir', os.path.join(self.base_path, 'docs', 'arch_diagrams'))
        if customer:
            customer_folder = customer.lower().replace(' ', '_').replace('-', '_')
            customer_folder = ''.join(c for c in customer_folder if c.isalnum() or c == '_')
            output_dir = os.path.join(base_output_dir, customer_folder)
        else:
            output_dir = base_output_dir

        # Build mermaid code
        lines = ["```mermaid", "flowchart TB"]
        
        # Add title as comment
        lines.append(f"    %% {title}")
        lines.append("")

        # Group nodes by cluster
        cluster_nodes = {}
        standalone_nodes = []
        
        for node in nodes:
            cluster_id = node.get('cluster')
            if cluster_id:
                if cluster_id not in cluster_nodes:
                    cluster_nodes[cluster_id] = []
                cluster_nodes[cluster_id].append(node)
            else:
                standalone_nodes.append(node)

        # Add clusters
        for cluster in clusters:
            cluster_id = cluster.get('id', '')
            cluster_label = cluster.get('label', cluster_id)
            lines.append(f"    subgraph {cluster_id}[{cluster_label}]")
            
            # Add nodes in this cluster
            for node in cluster_nodes.get(cluster_id, []):
                node_id = node.get('id', '')
                label = node.get('label', node_id)
                shape = self._get_mermaid_shape(node.get('type', 'server'))
                lines.append(f"        {node_id}{shape[0]}{label}{shape[1]}")
            
            lines.append("    end")
            lines.append("")

        # Add standalone nodes
        for node in standalone_nodes:
            node_id = node.get('id', '')
            label = node.get('label', node_id)
            shape = self._get_mermaid_shape(node.get('type', 'server'))
            lines.append(f"    {node_id}{shape[0]}{label}{shape[1]}")

        lines.append("")

        # Add connections
        for conn in connections:
            from_id = conn.get('from', '')
            to_id = conn.get('to', '')
            label = conn.get('label', '')
            style = conn.get('style', 'arrow')
            
            arrow = self._get_mermaid_arrow(style)
            if label:
                lines.append(f"    {from_id} {arrow}|{label}| {to_id}")
            else:
                lines.append(f"    {from_id} {arrow} {to_id}")

        lines.append("```")

        mermaid_code = "\n".join(lines)

        # Save to file if requested
        if output_dir:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            md_path = os.path.join(output_dir, f"{output_filename}.md")
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(mermaid_code)

            return json.dumps({
                "status": "success",
                "format": "mermaid",
                "filename": f"{output_filename}.md",
                "path": md_path,
                "mermaid_code": mermaid_code
            }, indent=2)

        return json.dumps({
            "status": "success",
            "format": "mermaid",
            "mermaid_code": mermaid_code
        }, indent=2)

    def _get_mermaid_shape(self, node_type: str) -> Tuple[str, str]:
        """Get Mermaid shape markers for a node type."""
        shapes = {
            "user": ["((", "))"],       # Circle
            "users": ["((", "))"],
            "database": ["[(", ")]"],   # Cylinder
            "sql": ["[(", ")]"],
            "cosmos": ["[(", ")]"],
            "cosmosdb": ["[(", ")]"],
            "storage": ["[(", ")]"],
            "blob": ["[(", ")]"],
            "function": ["[/", "\\]"],  # Trapezoid
            "function_app": ["[/", "\\]"],
            "openai": ["{{", "}}"],     # Hexagon
            "cognitive": ["{{", "}}"],
            "ml": ["{{", "}}"],
            "agent": [">", "]"],        # Flag
            "server": ["[", "]"],       # Rectangle
            "default": ["[", "]"],
        }
        return shapes.get(node_type.lower(), shapes["default"])

    def _get_mermaid_arrow(self, style: str) -> str:
        """Get Mermaid arrow style."""
        arrows = {
            "arrow": "-->",
            "dotted": "-.->",
            "thick": "==>",
            "bidirectional": "<-->",
        }
        return arrows.get(style, "-->")

    def _generate_drawio(self, **kwargs) -> str:
        """Generate Draw.io XML (compatible with Visio import)."""
        title = kwargs.get('title', 'Architecture Diagram')
        nodes = kwargs.get('nodes', [])
        connections = kwargs.get('connections', [])
        output_filename = kwargs.get('output_filename', 'architecture_diagram')
        customer = kwargs.get('customer', '')

        # Build output directory - create customer subfolder if specified
        base_output_dir = kwargs.get('output_dir', os.path.join(self.base_path, 'docs', 'arch_diagrams'))
        if customer:
            customer_folder = customer.lower().replace(' ', '_').replace('-', '_')
            customer_folder = ''.join(c for c in customer_folder if c.isalnum() or c == '_')
            output_dir = os.path.join(base_output_dir, customer_folder)
        else:
            output_dir = base_output_dir

        # Draw.io XML structure
        xml_parts = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<mxfile host="app.diagrams.net">',
            '  <diagram name="Page-1">',
            '    <mxGraphModel dx="1000" dy="600" grid="1" gridSize="10">',
            '      <root>',
            '        <mxCell id="0"/>',
            '        <mxCell id="1" parent="0"/>',
        ]

        # Add nodes
        x, y = 100, 100
        node_positions = {}
        
        for i, node in enumerate(nodes):
            node_id = node.get('id', f'node_{i}')
            label = node.get('label', node_id)
            node_type = node.get('type', 'server')
            
            # Calculate position (simple grid layout)
            pos_x = 100 + (i % 4) * 200
            pos_y = 100 + (i // 4) * 150
            node_positions[node_id] = (pos_x, pos_y)
            
            # Get shape style based on type
            style = self._get_drawio_style(node_type)
            
            xml_parts.append(f'        <mxCell id="{node_id}" value="{label}" style="{style}" vertex="1" parent="1">')
            xml_parts.append(f'          <mxGeometry x="{pos_x}" y="{pos_y}" width="120" height="60" as="geometry"/>')
            xml_parts.append('        </mxCell>')

        # Add connections
        for i, conn in enumerate(connections):
            from_id = conn.get('from', '')
            to_id = conn.get('to', '')
            label = conn.get('label', '')
            edge_id = f'edge_{i}'
            
            xml_parts.append(f'        <mxCell id="{edge_id}" value="{label}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" source="{from_id}" target="{to_id}" parent="1">')
            xml_parts.append('          <mxGeometry relative="1" as="geometry"/>')
            xml_parts.append('        </mxCell>')

        xml_parts.extend([
            '      </root>',
            '    </mxGraphModel>',
            '  </diagram>',
            '</mxfile>',
        ])

        xml_content = '\n'.join(xml_parts)

        # Save to file
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        xml_path = os.path.join(output_dir, f"{output_filename}.drawio")
        with open(xml_path, 'w', encoding='utf-8') as f:
            f.write(xml_content)

        return json.dumps({
            "status": "success",
            "format": "drawio",
            "filename": f"{output_filename}.drawio",
            "path": xml_path,
            "note": "Open with draw.io or import into Visio"
        }, indent=2)

    def _get_drawio_style(self, node_type: str) -> str:
        """Get Draw.io style for a node type."""
        styles = {
            "user": "shape=ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;",
            "database": "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;fillColor=#f5f5f5;strokeColor=#666666;",
            "function": "shape=step;perimeter=stepPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#fff2cc;strokeColor=#d6b656;",
            "openai": "shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#d5e8d4;strokeColor=#82b366;",
            "agent": "shape=process;whiteSpace=wrap;html=1;backgroundOutline=1;fillColor=#e1d5e7;strokeColor=#9673a6;",
            "server": "rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;",
        }
        return styles.get(node_type.lower(), styles["server"])

    def _diagram_from_agents(self, **kwargs) -> str:
        """Generate diagram from RAPP agent configurations."""
        agents = kwargs.get('agents', [])
        title = kwargs.get('title', 'RAPP Agent Architecture')
        output_format = kwargs.get('output_format', 'png')

        if not agents:
            # Try to load agents from the agents directory
            agents = self._discover_agents()

        # Build nodes and connections from agent configs
        nodes = []
        connections = []

        # Add user node
        nodes.append({"id": "user", "type": "user", "label": "User"})

        # Add RAPP core
        nodes.append({"id": "rapp_core", "type": "function_app", "label": "RAPP Core\n(Azure Functions)", "cluster": "azure"})
        connections.append({"from": "user", "to": "rapp_core", "label": "HTTP"})

        # Add OpenAI
        nodes.append({"id": "openai", "type": "openai", "label": "Azure OpenAI", "cluster": "azure"})
        connections.append({"from": "rapp_core", "to": "openai", "label": "API"})

        # Add agents
        for i, agent in enumerate(agents):
            agent_id = f"agent_{i}"
            agent_name = agent.get('name', agent.get('id', f'Agent {i+1}'))
            nodes.append({
                "id": agent_id,
                "type": "agent",
                "label": agent_name,
                "cluster": "agents"
            })
            connections.append({"from": "rapp_core", "to": agent_id, "label": ""})

        # Define clusters
        clusters = [
            {"id": "azure", "label": "Azure Cloud"},
            {"id": "agents", "label": "RAPP Agents"}
        ]

        # Create the diagram
        return self._create_diagram(
            title=title,
            nodes=nodes,
            connections=connections,
            clusters=clusters,
            output_format=output_format,
            **kwargs
        )

    def _discover_agents(self) -> List[Dict]:
        """Discover agents from the agents directory."""
        agents = []
        agents_dir = os.path.join(self.base_path, 'agents')
        
        if os.path.exists(agents_dir):
            for filename in os.listdir(agents_dir):
                if filename.endswith('_agent.py') and not filename.startswith('__'):
                    agent_name = filename.replace('_agent.py', '').replace('_', ' ').title()
                    agents.append({"name": agent_name, "file": filename})

        return agents[:10]  # Limit to 10 agents for readability
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
