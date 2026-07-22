# Formatting the docs

In addition to regular markdown, there are other elements you can use.

## Headings

All HTML headings, `<h1>` through `<h6>`, are available. `.h1` through `.h6` classes are also available, for when you want to match the font styling of a heading but still want your text to be displayed inline.

```html
<h1>h1. Heading <small>Secondary text</small></h1>
```

<h1>h1. Heading <small>Secondary text</small></h1>


```html
<h2>h2. Heading <small>Secondary text</small></h2>
```

<h2>h2. Heading <small>Secondary text</small></h2>


```html
<h3>h3. Heading <small>Secondary text</small></h3>
```

<h3>h3. Heading <small>Secondary text</small></h3>


```html
<h4>h4. Heading <small>Secondary text</small></h4>
```

<h4>h4. Heading <small>Secondary text</small></h4>


```html
<h5>h5. Heading <small>Secondary text</small></h5>
```

<h5>h5. Heading <small>Secondary text</small></h5>


```html
<h6>h6. Heading <small>Secondary text</small></h6>
```

<h6>h6. Heading <small>Secondary text</small></h6>


## Body

```html
<samp>This is a sample text example.</samp>
```

<samp>This is a sample text example.</samp>

```html
<strong>This is a bold text example.</strong>
```

<strong>This is a bold text example.</strong>

```html
<em>This is an italic text example.</em>
```

<em>This is an italic text example.</em>

```html
<u>This is an underlined text example.</u>
```

<u>This is an underlined text example.</u>

```html
<s>This is a strikethrough text example.</s>
```

<s>This is a strikethrough text example.</s>

```html
<mark>This is a highlighted text example.</mark>
```

<mark>This is a highlighted text example.</mark>

```html
<small>This is a small text example.</small>
```

<small>This is a small text example.</small>

```html
<del>This is a deleted text example.</del>
```

<del>This is a deleted text example.</del>

```html
<ins>This is an inserted text example.</ins>
```

<ins>This is an inserted text example.</ins>

```html
<sup>This is a superscript text example.</sup>
```

<sup>This is a superscript text example.</sup>

```html
<sub>This is a subscript text example.</sub>
```

<sub>This is a subscript text example.</sub>

```html
<kbd>This is a keyboard input text example.</kbd>
```

<kbd>This is a keyboard input text example.</kbd>

```html
<var>This is a variable text example.</var>
```

<var>This is a variable text example.</var>

```html
<cite>This is a citation text example.</cite>
```

<cite>This is a citation text example.</cite>

```html
<q>This is a short inline quotation text example.</q>
```

<q>This is a short inline quotation text example.</q>

```html
<abbr title="HyperText Markup Language">HTML</abbr> is an example of an abbreviation.
```

<abbr title="HyperText Markup Language">HTML</abbr> is an example of an abbreviation.

```html
<bdo dir="rtl">This is a bidirectional override text example.</bdo>
```

<bdo dir="rtl">This is a bidirectional override text example.</bdo>

## Blockquotes

```html
<blockquote>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
  <footer>Someone famous in <cite title="Source Title">Source Title</cite></footer>
</blockquote>
```

<blockquote>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
  <footer>Someone famous in <cite title="Source Title">Source Title</cite></footer>
</blockquote>

## Code

Syntax highlighting support is available for any of the following languages listed on the <a href="https://highlightjs.org/download/">highlightjs website</a>. See the <a href="https://www.mkdocs.org/user-guide/styling-your-docs/">mkdocs "styling your docs"</a> hljs_languages section for info on how to load languages dynamically.

For fenced code blocks, you can add arguments after the opening ``` to specify the language for syntax hightlighting, as well as line numbering and background hightlighting.

````markdown
```js title="highlight-code.md" linenums="1" hl_lines="2-4"
// Function to concatenate two strings
function concatenateStrings(str1, str2) {
return str1 + str2;
}

// Example usage
const result = concatenateStrings("Hello, ", "World!");
console.log("The concatenated string is:", result);
```
````

```js title="highlight-code.md" linenums="1" hl_lines="2-4"
// Function to concatenate two strings
function concatenateStrings(str1, str2) {
  return str1 + str2;
}

// Example usage
const result = concatenateStrings("Hello, ", "World!");
console.log("The concatenated string is:", result);
```

## Admonition Blocks

These require the "admonition" extension to be enabled under "markdown_extensions". They can be used for notes, warnings, tips, and more. Below are examples of different block types you can use.

Admonitions follow the [python-markdown style](https://python-markdown.github.io/extensions/admonition/). The basic format is:


```markdown
!!! type "block title"
    Write your note here.
```

The following types are supported:

```note```

!!! note "Note Block Title"
    This is a Note Block

    <pre><code>
    \# this is a note
    def func(arg) {
      \# notable things are in here!
      return None
    }
    </code></pre>


```tip```

!!! tip "Tip Block Title"
    This is a Tip Block

```info```

!!! info "Info Block Title"
    This is an Info Block

```example```

!!! example "Example Block Title"
    This is an Example Block

```question```

!!! question "Question Block Title"
    This is a Question Block

```quote```

!!! quote "Quote Block Title"
    This is a Quote Block

```success```

!!! success "Success Block Title"
    This is a Success Block

```warning```

!!! warning "Warning Block Title"
    This is a Warning Block

```bug```

!!! bug "Bug Block Title"
    This is a Bug Block

```failure```

!!! failure "Failure Block Title"
    This is a Failure Block

```danger```

!!! danger "Danger Block Title"
    This is a Danger Block