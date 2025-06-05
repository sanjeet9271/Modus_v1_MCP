# Modus Components MCP Server

This repository contains a Model Context Protocol (MCP) server that provides information about Modus React components.

## Docker Setup

### Building the Docker Image

To build the Docker image, run the following command from the project root directory:

```powershell
docker build -t modus-mcp-server .
```

### Running the Docker Container

To run the Docker container, execute:

```powershell
docker run -p 3001:3001 modus-mcp-server
```

This will start the MCP server and expose it on port 3001.

### Accessing the MCP Server

The MCP server will be available at:

```
http://localhost:3001
```

## Available Tools

The MCP server provides the following tools:

- `getting_started_installation_and_guidelines`: Get guidelines for installation and usage of Modus components
- `get_list_of_all_modus_components`: Get a list of all available Modus components
- `get_component_details`: Get properties and usage examples for a specific component
- `get_modus_icons_by_char`: Get Modus icon names that start with a specified character prefix

## Project Structure

- `src/`: Contains the Python source code
  - `ModusFromMCP.py`: Main MCP server implementation
  - `modules/`: Supporting modules
  - `SvgTool/`: SVG processing utilities
- `Knowledge Base/`: Contains component documentation and examples
  - `db.json`: Form component data
  - `db_ui.json`: UI component data
  - `modus_icons.json`: Modus icon names
  - Other documentation files

## Requirements

The server requires Python 3.11+ and the following packages:
- mcp-server (Model Context Protocol)
- Pillow (for image processing)
