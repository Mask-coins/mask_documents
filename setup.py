from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="mask_documents",
    version="0.0.5",
    description="私が整理したデータを公開しています。",
    author="Mask_coins",
    url="https://github.com/Mask-coins/mask_documents",
    packages=find_packages("py"),
    package_dir={"": "py"},
    py_modules=[splitext(basename(path))[0] for path in glob('py/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]
)
