from setuptools import setup, find_packages

setup(
    name="neroxbale",
    version="1.0.0",
    author="Media_Blu98",
    author_email="ya3inxd123@gmail.com",
    description="کتابخانه ساخت بات بله",
    long_description="کتابخانه نرو ایکس برای ساخت ربات در پیام‌رسان بله",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=["aiohttp>=3.8.0"],
)