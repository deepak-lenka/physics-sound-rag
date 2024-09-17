import os
import json

def read_file_in_chunks(file_path, chunk_size=1000):
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

def process_text():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(project_root, 'data', 'iesc111.txt')
    chunks_dir = os.path.join(project_root, 'data', 'chunks')
    
    if not os.path.exists(chunks_dir):
        os.makedirs(chunks_dir)
    
    print(f"Project root: {project_root}")
    print(f"Attempting to read file: {file_path}")
    
    chunk_number = 0
    total_characters = 0
    
    for chunk in read_file_in_chunks(file_path):
        chunk_number += 1
        chunk_file = os.path.join(chunks_dir, f'chunk_{chunk_number}.json')
        with open(chunk_file, 'w') as f:
            json.dump({"text": chunk}, f)
        total_characters += len(chunk)
        print(f"Processed chunk {chunk_number}, total characters: {total_characters}")
    
    print(f"Successfully processed file. Total size: {total_characters} characters")
    print(f"Chunks saved in: {chunks_dir}")

if __name__ == "__main__":
    process_text()