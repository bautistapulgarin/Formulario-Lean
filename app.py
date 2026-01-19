import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

creds_dict = json.loads(st.secrets["GSPREAD_CREDS"])  # Ahora funciona

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

sheet = client.open_by_key("1G8GvBqkTs7WamLRe_h-s9tJxRCCsNtmZEl15WXIggP4").sheet1
st.write(sheet.get_all_records())
