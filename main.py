from js import document

grade7 = {"Adrian Bennett", "Sophia Reynolds", "Ethan Caldwell", "Isabella Hayes"}
grade8 = {"Nathaniel Brooks", "Amelia Foster", "Lucas Montgomery", "Gabrielle Santos", "Caleb Anderson"}
grade9 = {"Victoria Collins", "Sebastian Rivera", "Chloe Mitchell"}
grade10 = {"Dominic Parker", "Alexandra Flores", "Julian Prescott"}

members = grade7 | grade8 | grade9 | grade10

# Function to display all members
def display():
    names = "<br>".join(sorted(members))

    document.getElementById("result").innerHTML = f"""
    All members:<br>
    {names}<br>
    Total members: {len(members)}
    """

def add(event):
    global members

    # Get the first and last name
    first = document.getElementById("firstname").value
    last = document.getElementById("lastname").value

    # Combine the names
    name = first + " " + last

    # Add the new member
    members = members | {name}

    # Update the results
    display()

# Display the original members
display()