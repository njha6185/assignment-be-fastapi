# app/config/org_config.py

ORG_COLUMNS = {
    "org1": ["first_name", "last_name", "email", "department", "location", "position"],
    "org2": ["first_name", "department", "location", "position"],  # no email
    "org3": ["first_name", "last_name", "position"],  # minimal fields
}

def get_org_visible_columns(org_id: str):
    return ORG_COLUMNS.get(org_id, ["first_name", "last_name", "email"])  # default
