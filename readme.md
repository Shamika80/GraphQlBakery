# Bakery Inventory API

This is a GraphQL API for managing the inventory of a bakery. It allows you to perform CRUD (Create, Read, Update, Delete) operations on bakery items.

## Features

*   Query all inventory items
*   Query an item by name
*   Add new items to the inventory
*   Update existing item details
*   Delete items from the inventory

## Technologies Used

*   Python
*   Flask
*   Graphene (GraphQL library for Python)

## Setup

1.  Clone the repository: `git clone <repository_url>`
2.  Install dependencies: `pip install -r requirements.txt`
3.  Run the Flask app:   
 `python app.py`

## Usage

1.  Access the GraphiQL interface at `http://127.0.0.1:5000/graphql`
2.  Use the GraphiQL interface to send queries and mutations to the API.

## Sample Queries and Mutations

**Fetch all inventory items:**

```graphql
query {
  inventory {
    name
    price
    quantity
    category
  }
}