from huggingface_hub import upload_file

repo_id = "shivammmmmmm/image-classification-models" 

for i in range(1, 7):
    model_filename = f"real-fake-class{i}.ipynb"        
    local_path = f"notebook/{model_filename}"           
    repo_path = f"notebook/{model_filename}"            

    print(f"Uploading: {local_path} → {repo_path}")
    upload_file(
        path_or_fileobj=local_path,
        path_in_repo=repo_path,
        repo_id=repo_id,
        repo_type="model"
    )

print("All notebooks uploaded successfully into Hugging Face repo's notebook/ folder.")
