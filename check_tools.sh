#!/bin/bash

# command availability check
is_command_available() {
  command -v "$1" >/dev/null 2>&1
}

# tools check
tools=("whois" "dnsenum")

display_checkmark() {
  echo -e "\xE2\x9C\x94" 
}

display_crossmark() {
  echo -e "\xE2\x9C\x98"
}

# Check if each tool is available
echo "Checking the availability of tools:"
for tool in "${tools[@]}"; do
  if is_command_available "$tool"; then
    echo "$(display_checkmark) $tool: installed"
  else
    echo "$(display_crossmark) $tool: missing"
  fi
done

# installing missing tools
missing_tools=()
for tool in "${tools[@]}"; do
  if ! is_command_available "$tool"; then
    missing_tools+=("$tool")
  fi
done

if [ ${#missing_tools[@]} -eq 0 ]; then
  echo "All necessary tools are installed."
else
  echo "The following tools are missing or not installed:"
  for tool in "${missing_tools[@]}"; do
    echo "$(display_crossmark) $tool"
  done

  # Offer to install missing tools
  read -p "Do you want to install the missing tools? (yes/no): " choice
  if [ "$choice" = "yes" ]; then
    for tool in "${missing_tools[@]}"; do
      case "$tool" in
        "whois")
          echo "Installing whois..."
          sudo apt install -y "$tool"
          ;;
        "dnsenum")
          echo "Installing dnsenum..."
          sudo apt install -y "$tool"
          ;;
      esac
      echo "$(display_checkmark) $tool: installed"
    done
    echo "Missing tools have been installed."
  else
    echo "You can manually install the missing tools and then rerun the script."
  fi
fi
