---
name: "rar-discreetrappers-architecture-diagram"
description: "Generate professional architecture diagrams.\n\nSupported diagram types:\n- azure: Azure cloud architecture\n- agent_system: AI agent/orchestrator architecture\n- multi_tier: N-tier application architecture\n- microservices: Microservices architecture\n- data_flow: Data pipeline/flow diagram\n- custom: Custom node/connection diagram\n\nOutput formats: png, svg, pdf, mermaid, drawio\n\nActions:\n- create_diagram: Create a diagram from specification\n- diagram_from_agents: Generate diagram from RAPP agent configurations\n- list_node_types: List available node types\n- generate_mermaid: Generate Mermaid.js code\n\nExample:\n{\n  \"action\": \"create_diagram\",\n  \"diagram_type\": \"azure\",\n  \"title\": \"RAPP Architecture\",\n  \"output_format\": \"png\",\n  \"nodes\": [\n    {\"id\": \"user\", \"type\": \"user\", \"label\": \"User\"},\n    {\"id\": \"func\", \"type\": \"function_app\", \"label\": \"Azure Functions\"},\n    {\"id\": \"openai\", \"type\": \"openai\", \"label\": \"Azure OpenAI\"}\n  ],\n  \"connections\": [\n    {\"from\": \"user\", \"to\": \"func\", \"label\": \"HTTP\"},\n    {\"from\": \"func\", \"to\": \"openai\", \"label\": \"API\"}\n  ]\n}"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/architecture_diagram_agent", "rar_sha256": "97485b27444625b332f52f9df07e46ed70d6a24dd250eba01bb78660056c36ba", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Bill Whalen", "tags": ["productivity", "diagrams", "architecture", "visualization", "mermaid"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `architecture_diagram_agent.py` and embedded as the fenced Python below (sha256 97485b27444625b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `architecture_diagram_agent.py` first:

```bash
python3 architecture_diagram_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 architecture_diagram_agent.py   # or on stdin
python3 architecture_diagram_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
