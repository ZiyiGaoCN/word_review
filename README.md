# Readme
本项目是基于ECDICT词典开发的单词本生成项目```https://github.com/skywind3000/ECDICT```
提供了图形界面的纯单词、英文、中文的单词本生成

## 安装
在```conda```环境下，执行
```shell
conda env create -f env.yml
```

## 使用

### 获取词典
将单词本放在根目录的```wordtable.txt```里

将词典放在/word_app/utils/ECDICT目录下，词典可在```https://cloud.tsinghua.edu.cn/f/bb1dfaf0db24432da312/?dl=1```处下载
```

```


### 执行
```
python graphic.py
```
在```Review```模式内，程序会随机从单词本中抽取词汇，并且给出该词汇的中文，你需要在框内输入该词汇。

### 输出
如果选择```Generate a xxx wordnote```，程序会在```output```文件夹内自动生成生词本。