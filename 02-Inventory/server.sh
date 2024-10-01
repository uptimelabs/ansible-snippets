#!/bin/bash

inventory=$(curl -sf "https://raw.githubusercontent.com/x70b1/ansible-snippets/refs/heads/main/02-Inventory/server.json" | jq --monochrome-output)

echo "$inventory"
