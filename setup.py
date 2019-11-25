from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name="soco-sentence-transformers",
    version="0.0.1",
    author="Tony Zhao",
    description="Sentence Embeddings using BERT / XLNet",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    url="https://github.com/UKPLab/sentence-transformers",
    download_url="https://github.com/UKPLab/sentence-transformers/archive/v0.2.3.zip",
    packages=find_packages(),
    install_requires=[
        "pytorch-transformers==1.1.0",
        "tqdm",
        "torch>=1.0.1",
        "numpy",
        "scikit-learn",
        "scipy",
        "nltk"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    keywords="Transformer Networks BERT XLNet sentence embedding PyTorch NLP deep learning"
)
