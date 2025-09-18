# Short recipes


## For Translators


Create the `es` lang file to be translated

```
msginit --input=po/aihordeclient.pot --locale=es_CO.UTF-8 --output=po/es.po  
```

Compile the `es` translations

```
msgfmt --output-file=src/locale/es/LC_MESSAGES/aihordeclient.mo po/es.po
```

## For Developers

To generate the catalog for the first time:

```
xgettext -o po/aihordeclient.pot --add-comments=TRANSLATORS: --keyword=_ --flag=_:1:pass-python-format --directory=src/aihordeclient/ __init__.py
```

Create the `es` lang file to be translated

```
msginit --input=po/aihordeclient.pot --locale=es_CO.UTF-8 --output=po/es.po  
```

Update the `es` lang file for translators

```
xgettext -j -o po/aihordeclient.pot --add-comments=TRANSLATORS: --keyword=_ --flag=_:1:pass-python-format --directory=src/aihordeclient/ __init__.py
msgmerge -q --update po/es.po po/aihordeclient.pot
```

Oneliner to fire everything up

```
xgettext -j -o po/aihordeclient.pot --add-comments=TRANSLATORS: --keyword=_ --flag=_:1:pass-python-format --directory=src/aihordeclient/ __init__.py && msgmerge -q --update po/es.po po/aihordeclient.pot && msgfmt --output-file=src/locale/es/LC_MESSAGES/aihordeclient.mo po/es.po && postats po/es.po
```
