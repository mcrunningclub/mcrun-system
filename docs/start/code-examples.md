```py title="add_numbers.py" linenums="1"
# Function to add two numbers
def add_two_numbers(num1, num2):
    return num1 + num2

# Example usage
result = add_two_numbers(5, 3)
print('The sum is:', result)
```

```js title="highlight-code.md" linenums="1" hl_lines="2-4"
// Function to concatenate two strings
function concatenateStrings(str1, str2) {
  return str1 + str2;
}

// Example usage
const result = concatenateStrings("Hello, ", "World!");
console.log("The concatenated string is:", result);
```

<!-- docs/sample-py.md -->

# Module sample

This is a sample module.

## Variables

- **variable**{: #variable } (`int`): Docstrings for module-level variables.

## Classes

### SampleClass {: #SampleClass }

```python
class SampleClass(self, b: str)
```

Class docstrings.

**Attributes**

- **baz** (`str`): Docstrings for attributes.

**Args**

- **b** (`str`): Arguments for initializing.

---

#### Methods {: #SampleClass-methods }

[**method**](#SampleClass.method){: #SampleClass.method }

```python
def method(self, bar: int) -> str
```

Method docstrings.

Cross reference available. [`func `](#variables)

**Args**

- **bar** (`int`)

**Returns**

- `str`
