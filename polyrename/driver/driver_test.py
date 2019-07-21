import shutil

from polyrename.transformation import TRANSFORMATIONS


def main(files):
    print("Choose a transformation:")
    for i, tranformation in enumerate(TRANSFORMATIONS):
        print("{}) {}".format(i, tranformation.schema["metadata"]["name"]))

    # Ask for selection input
    choice = None
    while choice not in range(len(TRANSFORMATIONS)):
        try:
            choice = int(input("Selection: "))
        except ValueError:
            pass

    # Gather arguments for selected transformation
    transformation_class = TRANSFORMATIONS[choice]
    transformation_args = []
    for option in transformation_class.schema["options"]:

        # Change prompt to show default value if it is specified
        if option["required"] and "default_value" in option:
            input_prompt = "{} ({}) (Default: {}):".format(
                option["name"], option["description"], option["default_value"]
            )
        else:
            input_prompt = "{} ({}):".format(option["name"], option["description"])

        choice = None
        while choice is None:
            try:
                user_input = input(input_prompt)

                # Allow for none_value to be used
                if user_input != "":
                    choice = option["datatype"](user_input)
                else:
                    if "default_value" in option:
                        choice = option["default_value"]
            except ValueError:
                print("Invalid input!")
        transformation_args.append(choice)

    # Create transformation with selected arguments
    tranformation = transformation_class(*transformation_args)
    transformed_file_sequence = tranformation.resolve(files)
    print("Preview:")
    file_pairs = list(zip(files, transformed_file_sequence))
    for file_pair in file_pairs:
        print("{} -> {}".format(*file_pair))

    # Ask to perform rename operation
    response = None
    while response not in ["y", "n"]:
        response = input("Perform rename operation(s)? (y/n): ").lower()

    if response == "y":
        for file_pair in file_pairs:
            shutil.move(*file_pair)
