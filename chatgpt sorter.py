from bs4 import BeautifulSoup

# Sample HTML content for demonstration
html = """
<html>
  <body>
    <div class="class1 class2" id="div1">This is a div</div>
    <p class="paragraph">This is a paragraph</p>
  </body>
</html>
"""

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Initialize a list to store the CSS class names and values
css_classes = []

# Find all elements with class attribute
elements = soup.find_all(class_=True)

# Loop through the elements and extract CSS class names and values
for element in elements:
    classes = element['class']
    for i in range(0, len(classes), 2):
        name = classes[i]
        value = classes[i + 1] if i + 1 < len(classes) else ""
        css_classes.extend([name, value])

# Print the list of CSS class names and values
print(css_classes)