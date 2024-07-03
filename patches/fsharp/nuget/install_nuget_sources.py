from os import listdir
from subprocess import run

def install_nuget_sources() -> None:
    for package_filename in listdir("./patches/fsharp/nuget"):
        package_name: str = package_filename.removesuffix(".nupkg")
        print(f"Extracting package {package_filename} into packages/{package_name}")
        run(
            [
                "mkdir", "-p",
                f"packages/{package_name}"
            ],
            capture_output=True
        )
        run(
            [
                "unzip", f"patches/fsharp/nuget/{package_filename}",
                "-d", f"packages/{package_name}"
            ],
            capture_output=True
        )

def main() -> None:
    install_nuget_sources()

if __name__=="__main__":
    main()
