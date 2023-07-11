#!/usr/bin/env bash

model=$1
prompt=$2
curl https://api.openai.com/v1/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d "{
    \"model\": \"$model\",
    \"prompt\": \"$prompt\",
    \"temperature\": 0.8,
    \"max_tokens\": 256
  }"
