from setuptools import setup, find_packages

package_name = "example-python"
package_version = "1.0.0"

setup(
    name=package_name,
    version=package_version,
    author="some author",
    install_requires=["requests", "numpy", "Django==1.7.11"],
)
