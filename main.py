import generate

scenarios = generate.scenarios()

items = []

for i, s in enumerate(scenarios, start=1):
    title = generate.title(s)
    description = generate.description(s)
    generate.image(i, generate.prompt(s))

    new_item = {
        "tokenID": i,
        "name": title,
        "description": description,
        "file_name": f"{i}.png",
    }

    items.append(new_item)

generate.metadata_file(items)
