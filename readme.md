## Description

This repo shows an apparent bug in the `html.fromstring()` function from the `lxml` Python library, which causes a particular web page to lose most of its content when parsed.

## Running

```sh
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

## Output

Running the program should print the following:

```sh
example-a.html

input:
69 characters
"<!DOCTYPE html><body>  <div>Hello</div>  <div>World</div></body>"

output:
65 characters, 1 nodes
"b'<html><body>\n  <div>Hello</div>\n  <div>World</div>\n</body></html>'"

-------------

example-b.html

input:
459505 characters
"<!DOCTYPE html><html lang="en" class="story nytapp-vi-article" xmlns:og="http://opengraphprotocol.or"

output:
456581 characters, 2 nodes
"b'<html lang="en" class="story nytapp-vi-article" xmlns:og="http://opengraphprotocol.org/schema/">\n\n<head>\n  <meta charset="utf-8"/>\n  <title data-rh="true">In UK, Covid Has Made NHS Delays for Other Il'"

-------------

example-c.html

input:
269094 characters
"<!DOCTYPE html><!--[if lte IE 8]> <html class="ie" lang="de-DE" prefix="og: http://ogp.me/ns#"> <![e"

output:
96 characters, 1 nodes
"b'<html><body><p>!   D   O   C   T   Y   P   E       h   t   m   l   &gt;   \n   </p></body></html>'"
```

The first two examples are parsed correctly, which is reflected in the similar input and output character counts.

The third example, by contrast, loses most of its data, and the output text is corrupted.