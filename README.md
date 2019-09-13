# RW_S3

s3にあるファイルを読み書きするためのmodule

# version

0.0.5

# install

```shell
pip install -U RW_S3
```
# usage

read_s3, write_s3は非推奨になりました(今後の更新なし)

## S3Reader

```python
from RW_S3 import S3Reader
s3_reader = S3Reader('hogehoge')
print(s3_reader.ls('hoge-bucket', 'hoge/'))
```

## S3Writer

```python
from RW_S3 import S3Writer
s3_writer = S3Writer('hogehoge')
s3_writer.to_json({"x": 1, "y": 2}, 'hoge-bucket', 'hoge/hoge.json')
```