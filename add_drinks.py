from app import app, db, Drink  # Import the Flask app along with db and Drink model

# Your drinks_to_add list remains the same
drinks_to_add = [
    {'name': 'Espresso', 'description': 'Strong coffee brewed by forcing hot water under pressure through finely ground coffee beans.'},
    {'name': 'Latte', 'description': 'Coffee drink made with espresso and steamed milk.'},
    {'name': 'Cappuccino', 'description': 'A coffee drink consisting of espresso and a milk foam mixture.'},
    {'name': 'Green Tea', 'description': 'Tea made from unoxidized leaves, pale in color and slightly bitter in flavor, produced mainly in China and Japan.'},
    {'name': 'Smoothie', 'description': 'A thick, smooth drink of fresh fruit pureed with milk, yogurt, or ice cream.'}
]


def add_drinks():
    # Loop through the drinks list and add each to the database
    for drink_info in drinks_to_add:
        # Check if the drink already exists to avoid duplicates
        existing_drink = Drink.query.filter_by(name=drink_info['name']).first()
        if not existing_drink:
            # Create a new Drink instance
            new_drink = Drink(name=drink_info['name'], description=drink_info['description'])
            # Add the new drink to the session
            db.session.add(new_drink)

    # Commit the session to save all new drinks to the database
    db.session.commit()

if __name__ == '__main__':
    # Wrap the script execution in a with block to push the application context
    with app.app_context():
        try:
            add_drinks()
            print("Drinks added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
