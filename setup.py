from setuptools import find_packages, setup
setup(
    name='MCQ-generator',
    version='0.0.1',
    author="Meghana N",
    author_email='meghananoochilaagmail.com',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages(),
    description="An application to generate MCQs from PDF files",
    license="MIT"
)