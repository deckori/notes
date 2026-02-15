#!/usr/bin/env bash
# Script to find broken git-annex pointer files using ripgrep

# Base directory (defaults to current)
BASE_DIR="${1:-.}"

# Output directory for backup (optional)
FIX_DIR="/tmp/annex-fix"
mkdir -p "$FIX_DIR"

number=1

# Use ripgrep to find files containing git-annex pointers
rg -l '^/annex/objects/SHA256E-s[0-9]+--[a-f0-9]+\.' "$BASE_DIR" | while read -r file; do
  printf "Run number %s starts\n\n" $number
  echo "Broken annex pointer found: $file"

  # Extract the SHA key from the pointer
  SHA_FILE=$(rg -o '^/annex/objects/SHA256E-s[0-9]+--[a-f0-9]+\.[a-z0-9]+' "$file" | head -n1 | xargs basename)
  if [ -z "$SHA_FILE" ]; then
    echo "  Could not extract SHA key from $file"
    ((number++))
    continue
  fi

  # Search for the real file in the annex object store
  FOUND=$(rg --files --glob "$SHA_FILE" "/inc/annex/.git/annex/objects" | head -n1)
  if [ -z "$FOUND" ]; then
    echo "  No matching file found for $SHA_FILE"
    ((number++))
    continue
  fi
  echo "Actual file found: $FOUND"

  # Backup broken file first (optional)
  cp "$file" "$FIX_DIR/$(basename "$file")"

  # Copy the real file in place of broken file
  DEST=$(realpath "$file")
  cp "$FOUND" "$DEST"
  echo "  Replaced $DEST with $FOUND"

  printf "Run number %s ends\n\n" $number
  ((number++))
done
