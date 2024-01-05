import os
import shutil


if __name__ == '__main__':
    # Create folder
    print("Creating folder...")
    try:
        os.mkdir("MQ-CPU")
    except Exception as e:
        print(f"Failed to create folder!\n\t{e}")
        exit(-1)

    # Move blueprint files
    print("Moving blueprint files...")
    try:
        shutil.copy("blueprint.json", "MQ-CPU")
        shutil.copy("description.json", "MQ-CPU")
        shutil.copy("icon.png", "MQ-CPU")
    except Exception as e:
        print(f"Failed to move files!\n\t{e}")
        exit(-1)

    print("Setup successful")
