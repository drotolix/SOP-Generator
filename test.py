from modules.sop_repo import add_sop, get_all_sops

add_sop(
    "Sales",
    "Lead Qualification",
    "Qualify incoming leads",
    "Sales Executive",
    "Review lead details",
    "Conversion Rate",
    "Wrong Classification",
    "CRM Automation"
)

sops = get_all_sops()

for sop in sops:
    print(sop)