# 一言句子库处理脚本

本仓库包含一个用于处理 [一言句子库](https://github.com/hitokoto-osc/sentences-bundle) 的 Python 脚本。从`sentences`文件夹中的每个 JSON 文件中提取 `hitokoto` 和 `from` 字段，整理后将它们写入 `result.txt` 文件。

## 背景

[一言句子库](https://github.com/hitokoto-osc/sentences-bundle) 包含来自各种来源的句子集合。此脚本用于整理句子和识别使用的字符，整理成一个文件后可以自行复制到一个新文章，供同时启用了 Hexo 中的优化字体文件插件的人使用。

## 用法

1. 克隆此仓库或下载 `process_sentences.py` 脚本，同时克隆[一言句子库](https://github.com/hitokoto-osc/sentences-bundle) 或[下载ZIP包](https://github.com/hitokoto-osc/sentences-bundle/archive/refs/heads/master.zip)。
2. 将 `sentences-bundle-master.zip` 文件放在与脚本相同的目录中，或将 `sentences` 文件夹解压到相同的目录中。
3. 运行 `process_sentences.py` 脚本。

该脚本会自动将检查当前目录中是否存在 `sentences-bundle-master.zip` 文件。如果存在，它将解压该文件。然后，它将处理 `sentences` 文件夹中的所有 JSON 文件，提取 `hitokoto` 和 `from` 字段，并将它们写入 `result.txt` 文件。

## License

This project is licensed under the MIT License.
