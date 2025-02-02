import os
import unicodedata

def normalize_names(root):
    """
    지정한 root 폴더와 그 하위 폴더의 모든 파일 및 폴더 이름을 NFC 정규화
    """
    # topdown=False를 사용하여 하위 폴더부터 처리함으로써 디렉터리 이름 변경 시 문제가 발생하지 않도록 함
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        # 파일 이름 변경
        for filename in filenames:
            original_path = os.path.join(dirpath, filename)
            normalized_filename = unicodedata.normalize('NFC', filename)
            if normalized_filename != filename:
                new_path = os.path.join(dirpath, normalized_filename)
                # 동일한 이름의 파일이 이미 있는 경우 확인
                if os.path.exists(new_path):
                    print(f"[WARNING] {new_path} 이미 존재합니다. {original_path}은(는) 건너뜁니다.")
                else:
                    print(f"파일 이름 변경: {original_path} -> {new_path}")
                    os.rename(original_path, new_path)
                    
        # 폴더 이름 변경
        for dirname in dirnames:
            original_dir_path = os.path.join(dirpath, dirname)
            normalized_dirname = unicodedata.normalize('NFC', dirname)
            if normalized_dirname != dirname:
                new_dir_path = os.path.join(dirpath, normalized_dirname)
                # 동일한 이름의 폴더가 이미 있는 경우 확인
                if os.path.exists(new_dir_path):
                    print(f"[WARNING] {new_dir_path} 이미 존재합니다. {original_dir_path}은(는) 건너뜁니다.")
                else:
                    print(f"폴더 이름 변경: {original_dir_path} -> {new_dir_path}")
                    os.rename(original_dir_path, new_dir_path)

if __name__ == "__main__":
    # 변환을 적용할 폴더 경로를 지정
    target_folder = "your/path"  # 실제 경로로 수정

    normalize_names(target_folder)
    print("NFC 정규화 작업이 완료되었습니다.")
