---
name: "rar-discreetrappers-architecture-diagram"
description: "Generate professional architecture diagrams.\n\nSupported diagram types:\n- azure: Azure cloud architecture\n- agent_system: AI agent/orchestrator architecture\n- multi_tier: N-tier application architecture\n- microservices: Microservices architecture\n- data_flow: Data pipeline/flow diagram\n- custom: Custom node/connection diagram\n\nOutput formats: png, svg, pdf, mermaid, drawio\n\nActions:\n- create_diagram: Create a diagram from specification\n- diagram_from_agents: Generate diagram from RAPP agent configurations\n- list_node_types: List available node types\n- generate_mermaid: Generate Mermaid.js code\n\nExample:\n{\n  \"action\": \"create_diagram\",\n  \"diagram_type\": \"azure\",\n  \"title\": \"RAPP Architecture\",\n  \"output_format\": \"png\",\n  \"nodes\": [\n    {\"id\": \"user\", \"type\": \"user\", \"label\": \"User\"},\n    {\"id\": \"func\", \"type\": \"function_app\", \"label\": \"Azure Functions\"},\n    {\"id\": \"openai\", \"type\": \"openai\", \"label\": \"Azure OpenAI\"}\n  ],\n  \"connections\": [\n    {\"from\": \"user\", \"to\": \"func\", \"label\": \"HTTP\"},\n    {\"from\": \"func\", \"to\": \"openai\", \"label\": \"API\"}\n  ]\n}"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/architecture_diagram_agent", "rar_sha256": "d5cac1baac38b585dead94b556dd7c6a5feb8772944bca8b6d88be70985161be", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Bill Whalen", "tags": ["productivity", "diagrams", "architecture", "visualization", "mermaid"]}
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
