# Typography

## Typefaces

- Headers: [Inter](https://github.com/rsms/inter)
- Code: [Hack](http://sourcefoundry.org/hack/)

---
## Body

- ```<samp>``` <samp>This is a sample text example.</samp>
- ```<strong>``` <strong>This is a bold text example.</strong>
- ```<em>``` <em>This is an italic text example.</em>
- ```<u>``` <u>This is an underlined text example.</u>
- ```<s>``` <s>This is a strikethrough text example.</s>
- ```<mark>``` <mark>This is a highlighted text example.</mark>
- ```<small>``` <small>This is a small text example.</small>
- ```<del>``` <del>This is a deleted text example.</del>
- ```<ins>``` <ins>This is an inserted text example.</ins>

- ```<sup>``` <sup>This is a superscript text example.</sup>
- ```<sub>``` <sub>This is a subscript text example.</sub>

- ```<kbd>``` <kbd>This is a keyboard input text example.</kbd>
- ```<var>``` <var>This is a variable text example.</var>
- ```<cite>``` <cite>This is a citation text example.</cite>
- ```<q>``` <q>This is a short inline quotation text example.</q>
- ```<abbr title="">``` <abbr title="HyperText Markup Language">HTML</abbr> is an example of an abbreviation.

- ```<bdo> dir=""``` <bdo dir="rtl">This is a bidirectional override text example.</bdo>

---
## Headings

All HTML headings, `<h1>` through `<h6>`, are available. `.h1` through `.h6` classes are also available, for when you want to match the font styling of a heading but still want your text to be displayed inline.

<br>

<h1>h1. Heading <small>Secondary text</small></h1>
<h2>h2. Heading <small>Secondary text</small></h2>
<h3>h3. Heading <small>Secondary text</small></h3>
<h4>h4. Heading <small>Secondary text</small></h4>
<h5>h5. Heading <small>Secondary text</small></h5>
<h6>h6. Heading <small>Secondary text</small></h6>

---
## Blockquotes

<blockquote>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
  <footer>Someone famous in <cite title="Source Title">Source Title</cite></footer>
</blockquote>

---
## Code

This is an example of inline code `#import requests`

<h3>Preformatted Code Blocks <small>with Syntax Highlighting</small></h3>

```python
def request(method, url, **kwargs):
    """Constructs and sends a :class:`Request <Request>`.
    Usage::
      >>> import requests
      >>> req = requests.request('GET', 'https://httpbin.org/get')
      <Response [200]>
    """

    # By using the 'with' statement we are sure the session is closed, thus we
    # avoid leaving sockets open which can trigger a ResourceWarning in some
    # cases, and look like a memory leak in others.
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs)
```

<small>(Source code sample from the Python <a href="https://github.com/requests/requests">requests library</a>, <a href="https://github.com/requests/requests/blob/master/LICENSE">Apache License, v2.0</a>)</small>


Syntax highlighting support is available for and of the following languages listed on the <a href="https://highlightjs.org/download/">highlightjs website</a>. See the <a href="https://www.mkdocs.org/user-guide/styling-your-docs/">mkdocs "styling your docs"</a> hljs_languages section for info on how to load languages dynamically.

---

## Admonitions

The following admonitions are formatted like the callouts above but can be implemented in Markdown when you include the `admonition` Markdown extension in your `mkdocs.yml` file.  

Add the following setting to `mkdocs.yml`:

```yaml
markdown_extensions:
  - admonition
```

and then follow the instructions in [the extension documentation](https://python-markdown.github.io/extensions/admonition/) to author admonitions in your documentation.

---

## Blocks

Blocks are a way to add special formatting to sections of your documentation. They can be used for notes, warnings, tips, and more. Below are examples of different block types you can use.

```markdown
!!! <block-type> "block title"
    Write your note here.
```

### General Blocks

!!! note "Note Block"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

    <pre><code>
    \# this is a note
    def func(arg) {
      \# notable things are in here!
      return None
    }
    </code></pre>


!!! tip "Tip Block"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


!!! info "Info Block"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


!!! example "Example Block"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


!!! question "Question Block"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


!!! quote "Quote Block"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.



### Positive Blocks

!!! success "Success Block"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


### Negative Blocks

!!! warning "Warning Block"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


!!! bug "Bug Block"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


!!! failure "Failure Block"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


!!! danger "Danger Block"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


