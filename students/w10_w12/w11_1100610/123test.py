import os

log_dir = "C:\\Users\\stanley\\OneDrive\\文件\\GitHub\\python_course\\students\\w10_w12\\w11_1100610\\logs2\\fit\\"
os.makedirs(log_dir, exist_ok=True)
if os.path.exists(log_dir):
    print(f"目錄 {log_dir} 成功創建或已存在。")

import os

log_dir = "C:\\Users\\stanley\\OneDrive\\文件\\GitHub\\python_course\\students\\w10_w12\\w11_1100610\\logs2\\fit\\"

# 確認 log_dir 是否存在
if os.path.exists(log_dir):
    if os.path.isdir(log_dir):
        print(f"{log_dir} 是一個目錄。")
    else:
        print(f"{log_dir} 不是一個目錄，是一個檔案或其他物件。")
else:
    print(f"{log_dir} 不存在。")