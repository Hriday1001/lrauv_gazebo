from setuptools import find_packages, setup

package_name = 'lrauv_perception'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vampweeknd',
    maintainer_email='hridaybhardwaj_se21a14_30@dtu.ac.in',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'listener = lrauv_perception.camera_subscriber:main',
        ],
    },
)
