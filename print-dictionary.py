# Given the below python dictionary, print a list of ebs volumes that are "attached"

volumes = {
    "ebs_volumes": [
        ("vol1", "attached"),
        ("vol2", "attached"),
        ("vol3", "detached"),
        ("vol4", "attached"),
    ]
}

## python 2.7 items would be iteritems for dict instead of items
for key, values in volumes.items():
    for value in values:
        if value[1] == "attached":
            print(value)
