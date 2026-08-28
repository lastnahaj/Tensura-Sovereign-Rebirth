@echo off
setlocal
if not exist "libraries\net\neoforged\neoforge\21.1.248\win_args.txt" (
  echo NeoForge server libraries are missing.
  exit /b 1
)
java @user_jvm_args.txt @libraries/net/neoforged/neoforge/21.1.248/win_args.txt nogui %*
pause
