"""记录高级的bash命令"""

1. tar 压缩特定文件夹中特定的文件后缀

`find ./someDir -name "*.php" -o -name "*.html" | tar -cf my_archive -T -`  
[src](https://stackoverflow.com/questions/18731603/how-to-tar-certain-file-types-in-all-subdirectories)
