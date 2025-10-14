from pathlib import Path
from huggingface_hub import snapshot_download

Path("plm").mkdir(exist_ok=True)

# 1) 다국어 SBERT
snapshot_download(
    repo_id="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    local_dir="plm/paraphrase-multilingual-MiniLM-L12-v2",
    local_dir_use_symlinks=False
)

print("모델이 plm/ 디렉터리에 준비되었습니다.")
