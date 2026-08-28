#!/usr/bin/env sh
set -eu

if [ ! -f "libraries/net/neoforged/neoforge/21.1.248/unix_args.txt" ]; then
  echo "NeoForge server libraries are missing." >&2
  exit 1
fi

java @user_jvm_args.txt @libraries/net/neoforged/neoforge/21.1.248/unix_args.txt nogui "$@"
