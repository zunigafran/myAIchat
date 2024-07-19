from langchain_community.document_loaders import PyPDFLoader

file_path = "docs/Eloquent Javascript.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()

print(len(docs))