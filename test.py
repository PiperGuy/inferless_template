import pexpect


def automate_inferless_init():
    # Start the inferless init command
    child = pexpect.spawn("inferless init")

    # Define the expected prompts and responses
    prompts = [
        "Enter config file name: ",
        "How do you want to upload the model (GIT, LOCAL) ?",
    ]

    # Define the responses for each prompt
    responses = ["my_config.yaml", "GIT"]  # Response for "Enter config file name: "

    child.expect("Welcome to the Inferless Model Initialization!")

    # Iterate over the prompts and send the responses
    for prompt, response in zip(prompts, responses):
        child.expect("Enter config file name: ")
        child.sendline(response)

    # Wait for the command to finish
    # child.expect(pexpect.EOF)

    # Print the output
    print(child.after.decode("utf-8"))


if __name__ == "__main__":
    automate_inferless_init()
