import os 
from git import Repo 
from langchain.doucment_loaders.generic import GenricLoader
from langchain.document_loaders.parsers import LanguageParser
from langhchain.text_splitter import Language
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langhcain.embeddings.openai import OpenAIEmbeddings



# Clone any github repositories
def repo_ingestion(repo_url):
    os.makedirs("repo", exit_ok=True)
    repo_path = "repo/"
    Repo.clone_from(repo_url, to_path=repo_path)




# Loading repositories as documents
def load_repo(repo_path):
    loader = GenericLoader.from_filesystem(repo_path,
                                           glob = "**/*",
                                           suffixes = [".py"],
                                           parser = LanguageParser(language=Language.PYTHON))
    

    documents = loader.load()

    return documents




# Loading embeddings model
def load_embedding():
    
