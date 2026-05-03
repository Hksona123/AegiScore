from huggingface_hub import HfApi
import os
import sys

token = os.getenv("HF_TOKEN")
if not token:
    print("Error: HF_TOKEN environment variable not set.")
    sys.exit(1)

api = HfApi(token=token)
repo_id = "hksona/aegiscore-backend"

files_to_upload = {
    "Dockerfile": "Dockerfile",
    "Server/resources/weights/cyber_sec_category.weights.h5": "Server/resources/weights/cyber_sec_category.weights.h5",
    "Server/resources/weights/cyber_sec_label.weights.h5": "Server/resources/weights/cyber_sec_label.weights.h5",
    "Server/resources/chat_model.pkl": "Server/resources/chat_model.pkl",
    "Server/data/chat_model.pkl": "Server/data/chat_model.pkl",
    "Server/resources/datasets/UNSW_NB15_training-set.csv": "Server/resources/datasets/UNSW_NB15_training-set.csv",
    "Server/requirements.txt": "Server/requirements.txt",
    "Server/VectorData/default__vector_store.json": "Server/VectorData/default__vector_store.json",
    "Server/VectorData/docstore.json": "Server/VectorData/docstore.json",
    "Server/instance/aegiscore.db": "Server/instance/aegiscore.db",
}

for local_path, path_in_repo in files_to_upload.items():
    if os.path.exists(local_path):
        print(f"Uploading {local_path} to {path_in_repo}...")
        try:
            api.upload_file(
                path_or_fileobj=local_path,
                path_in_repo=path_in_repo,
                repo_id=repo_id,
                repo_type="space"
            )
            print(f"Successfully uploaded {local_path}")
        except Exception as e:
            print(f"Failed to upload {local_path}: {e}")
    else:
        print(f"File not found: {local_path}")

print("Upload process completed.")
