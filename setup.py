import os
import shutil


VERSIONS = {
    "1": "MQr1",
    "1.1": "MQr1_1",
}
FIRST_VERSION = "1"
LAST_VERSION = "1.1"


if __name__ == '__main__':
    # ask user for revision number
    revision = ""
    while revision not in VERSIONS:
        revision = input(f"Enter CPU version (default: MQr{LAST_VERSION}): ")

        if revision == "":
            revision = LAST_VERSION
        elif revision not in VERSIONS:
            print("Invalid revision; try again;\n")

    # Create folder
    print("\nCreating folder...")
    try:
        os.mkdir("MQ-CPU")
    except FileExistsError:
        pass
    except Exception as e:
        print(f"Failed to create folder!\n\t{e}")
        exit(-1)

    # Move blueprint files
    print("Moving blueprint files...")
    try:
        filepath = f"cpu_blueprints/{VERSIONS[revision]}"
        for file in os.listdir(filepath):
            shutil.copy(os.path.join(filepath, file), "MQ-CPU")
    except Exception as e:
        print(f"Failed to move files!\n\t{e}")
        exit(-1)

    print("Setup successful")
