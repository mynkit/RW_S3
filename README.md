# RW_S3

s3にあるexcelやcsvをpandasのデータフレームで読み書きするためのmodule

# install

```shell
pip install -U RW_S3
```
# usage

## read_s3

```python
from RW_S3 import read_s3
s3 = read_s3(s3_profile = "hogehoge")
df = s3.read_csv("bucket_name", "key_name")
```

## write_s3

```python
from RW_S3 import write_s3
w_s3 = write_s3(s3_profile = "hogehoge")
s3.to_csv(df, "bucket_name", "key_name")
```