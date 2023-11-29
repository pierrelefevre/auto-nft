import llm

def scenarios():
    scenario = "Bazooki is a cute bazooka mascot. Write 12 scenarios in which Bazooki might find himself. Write one per line."
    scenarios = llm.text(scenario).split("\n")

    # Skip first and last scenario as they are usually some kind of intro or outro
    scenarios = scenarios[1:-1]

    return scenarios

def prompt(scenario):
    prompt = llm.text(
        "Write a short but descriptive prompt for image generation about this scenario. The prompt should be a few space separated words. Make sure to emphasize that the character is a bazooka.\n" + scenario)
    return prompt

def title(scenario):
    title = llm.text(
        "What is a good title for this scenario? It is about Bazooki the cute bazooka mascot\n" + scenario + "\nReturn only the title.").replace(",", "").replace("\"", "")
    return title

def description(scenario):
    description = llm.text(
        "Write a short third person summary for this scenario.  It is about Bazooki the cute bazooka mascot\n" + scenario + "\nReturn only the summary.").replace(",", "").replace("\"", "")
    return description

def image(id, prompt):
    llm.image(id, "cute bazooka mascot ultra realistic 4k" + prompt)

def metadata_file(items):
    with open("metadata.csv", "w+") as file:
        file.write("tokenID,name,description,file_name\n")
        for item in items:
            file.write(str(item["tokenID"]) + "," + item["name"] + "," +
                    item["description"] + "," + item["file_name"] + "\n")

