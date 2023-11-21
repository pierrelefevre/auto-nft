import generate

scenario = "Bazooki is a cute bazooka mascot. Write 12 scenarios in which Bazooki might find himself. Write one per line."
scenarios = generate.text(scenario).split("\n")

print(f"Generated {str(len(scenarios))} scenarios")

# Skip first and last scenario as they are usually some kind of intro or outro
scenarios = scenarios[1:-1]

items = []

for i, s in enumerate(scenarios):
    id = i+1

    print(f"Generating NFT, {id} of {len(scenarios)}")

    # Generate image
    prompt = generate.text(
        "Write a short but descriptive prompt for image generation about this scenario. The prompt should be a few space separated words. Make sure to emphasize that the character is a bazooka.\n" + s)
    generate.image(id, "cute bazooka mascot ultra realistic 4k" + prompt)

    # Generate description
    title = generate.text(
        "What is a good title for this scenario? It is about Bazooki the cute bazooka mascot\n" + s + "\nReturn only the title.").replace(",", "").replace("\"", "")
    description = generate.text(
        "Write a short third person summary for this scenario.  It is about Bazooki the cute bazooka mascot\n" + s + "\nReturn only the summary.").replace(",", "").replace("\"", "")

    # Save item
    new_item = {
        "tokenID": id,
        "name": title,
        "description": description,
        "file_name": f"{id}.png",
    }

    items.append(new_item)

# Write metadata file
print("Writing metadata file")
with open("metadata.csv", "w+") as file:
    file.write("tokenID,name,description,file_name\n")
    for item in items:
        file.write(str(item["tokenID"]) + "," + item["name"] + "," +
                   item["description"] + "," + item["file_name"] + "\n")

print("Done")
