# package release to pypi

modify setup function in setup.py

```
version [new version]
```

upload command

```
pipenv shell

--pipenv install --user --upgrade setuptools wheel twine--
sudo rm -R dist
python3 setup.py sdist bdist_wheel

twine upload dist/*
```
