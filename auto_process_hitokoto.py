import os
import json

# 定义压缩文件、解压目录和结果文件的路径
current_dir = os.getcwd()
zip_file = os.path.join(current_dir, 'sentences-bundle-master.zip')
extract_dir = current_dir
sentences_dir = os.path.join(current_dir, 'sentences-bundle-master/sentences')
result_file = os.path.join(current_dir, 'result.txt')

# 检查解压目录是否存在
if not os.path.isdir(sentences_dir):
    # 导入 zipfile 模块
    print(f"尝试自动解压{zip_file}")
    import zipfile
    # 解压缩文件
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

# 初始化结果内容
result_content = ''

# 遍历 sentences 目录
file_count = 0
for root, dirs, files in os.walk(sentences_dir):
    for file in files:
        file_count += 1
        # 打开每个文件
        with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
            print(f'处理{file}')
            # 加载 json 内容
            content = json.load(f)
            # 将 hitokoto 和 from 追加到结果内容
            for item in content:
                result_content += item['hitokoto'] + '\n'
                result_content += item['from'] + '\n'

# 将结果内容写入结果文件
with open(result_file, 'w', encoding='utf-8') as f:
    f.write(result_content)

print(f'\n搞定啦ヾ(≧▽≦*)o\n结果已写入: {result_file}')
