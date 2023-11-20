import generate

scenario = "Bazooki is a cute bazooka mascot. Write 10 scenarios in which Bazooki might find himself. Write one per line."

scenarios = generate.text(scenario).split("\n")

print("Scenarios:" + str(len(scenarios)))

# for testing, only use the first scenario
scenarios = scenarios[:1]

for i, s in enumerate(scenarios):

    prompt = generate.text(
        "Write a short but descriptive prompt for image generation about this scenario. The prompt should be a few space separated words. Make sure to emphasize that the character is a bazooka.\n" + s)
    path = generate.image(i, "cute bazooka mascot " + prompt)
    description = generate.text(
        "Write a short third person summary for this scenario.\n" + s + "\nReturn only the summary.")
    title = generate.text(
        "What is a good title for this scenario?\n" + s + "\nReturn only the title.")

    print("Title: " + title)
    print("Description: " + description)
    print("Path: " + path)
    print("Prompt: " + prompt)

# generate.image(0, "cat riding a skateboard")
# print(generate.text("write the lore behind larry the cat riding a skateboard"))
