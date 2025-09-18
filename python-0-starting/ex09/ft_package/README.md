# This package is learning project of 42Bangkok

## Resourses
[Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

## To test with command

```
python -m unittest
```

## To build with command
```
python -m pip install --upgrade build
python -m build
```

When build successed 'dist' directory created and have *.whl and *.tar.gz
List file in tar is
```
% tar -tzf dist/ft_package-0.0.1.tar.gz
ft_package-0.0.1/ft_package/__init__.py
ft_package-0.0.1/ft_package/count_in_list.py
ft_package-0.0.1/tests/__init__.py
ft_package-0.0.1/tests/test_count_in_list.py
ft_package-0.0.1/.gitignore
ft_package-0.0.1/README.md
ft_package-0.0.1/pyproject.toml
ft_package-0.0.1/PKG-INFO
```

[What Is a Python Wheel?](https://realpython.com/python-wheels/#what-is-a-python-wheel)

```
% unzip -l dist/ft_package-0.0.1-py3-none-any.whl
Archive:  dist/ft_package-0.0.1-py3-none-any.whl
  Length      Date    Time    Name
---------  ---------- -----   ----
       70  02-02-2020 00:00   ft_package/__init__.py
      332  02-02-2020 00:00   ft_package/count_in_list.py
     1263  02-02-2020 00:00   ft_package-0.0.1.dist-info/METADATA
       87  02-02-2020 00:00   ft_package-0.0.1.dist-info/WHEEL
      375  02-02-2020 00:00   ft_package-0.0.1.dist-info/RECORD
---------                     -------
     2127                     5 files
```

> .tar.gz = source code, must build/complie when install.

> .whl = compiled/builded, fast ready to use.