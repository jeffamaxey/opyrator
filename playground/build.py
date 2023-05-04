import os

from universal_build import build_utils
from universal_build.helpers import build_docker

COMPONENT_NAME = "opyrator-playground"
DOCKER_IMAGE_PREFIX = "mltooling"

HERE = os.path.abspath(os.path.dirname(__file__))


def main(args: dict) -> None:
    # set current path as working dir
    os.chdir(HERE)

    version = args.get(build_utils.FLAG_VERSION)
    docker_image_prefix = args.get(build_docker.FLAG_DOCKER_IMAGE_PREFIX)

    if not docker_image_prefix:
        docker_image_prefix = DOCKER_IMAGE_PREFIX  # type: ignore

    if args.get(build_utils.FLAG_MAKE):
        build_docker.build_docker_image(COMPONENT_NAME, version, exit_on_error=True)

    if args.get(build_utils.FLAG_RELEASE):
        build_docker.release_docker_image(
            COMPONENT_NAME,
            version,
            docker_image_prefix,
            exit_on_error=True,
        )


if __name__ == "__main__":
    main(build_docker.parse_arguments())
