# 定义输入和输出文件的路径
input_file = 'result.txt'
output_file = 'characters.txt'

# 读取输入文件的内容
with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 提取所有的字符，并删除重复字符
characters = set(content)

# 将字符集转换为字符串
characters_str = ''.join(characters)

# 写入输出文件
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(characters_str)

print(f'结果已写入: {output_file}')
