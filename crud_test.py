from modules.sop_repo import *

# print("ALL SOPS")
# print(get_all_sops())

# print("\nSEARCH")
# print(search_sop("Lead"))

# print("\nGET SOP")
# print(get_sop_by_id(1))

#Test Update
# update_sop(
#     1,
#     "Sales",
#     "Lead Qualification",
#     "Updated Objective",
#     "Sales Manager",
#     "Updated Steps",
#     "Conversion Rate",
#     "Lead Errors",
#     "CRM Automation"
# )

# print(get_sop_by_id(1))

#Test Delete
delete_sop(1)

print(get_all_sops())