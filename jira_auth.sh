#!/bin/bash
# Authenicate and grab Jira Board Details
# Carlos Enamorado
curl -s --request GET \
  --url 'https://[base_url]/rest/agile/1.0/board' \ # CHANGE THIS
  --user '[email_address:API_KEY]' \ # CHANGE THIS
  --header 'Accept: application/json' | jq '.values[] | select(.id == [206])' # CHANGE ID NUMBER

