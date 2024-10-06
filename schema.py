from graphene import ObjectType, String, Int, Float, List, Field, Mutation, Schema, Boolean

class InventoryItem(ObjectType):
    name = String(required=True)
    price = Float(required=True)
    quantity = Int(required=True)
    category = String()

inventory = [
    InventoryItem(name="Croissant", price=2.50, quantity=100, category="Pastry"),
    InventoryItem(name="Baguette", price=3.00, quantity=50, category="Bread"),
    InventoryItem(name="Chocolate Cake", price=20.00, quantity=10, category="Cake"),
]

class Query(ObjectType):
    inventory = List(InventoryItem)
    item = Field(InventoryItem, name=String(required=True))

    def resolve_inventory(root, info):
        return inventory

    def resolve_item(root, info, name):
        for item in inventory:
            if item.name == name:
                return item
        return None

class AddItem(Mutation):
    class Arguments:
        name = String(required=True)
        price = Float(required=True)
        quantity = Int(required=True)
        category = String()

    item = Field(lambda: InventoryItem)

    def mutate(root, info, name, price, quantity, category):
        new_item = InventoryItem(
            name=name, price=price, quantity=quantity, category=category
        )
        inventory.append(new_item)
        return AddItem(item=new_item)

class UpdateItem(Mutation):
    class Arguments:
        name = String(required=True)
        price = Float()
        quantity = Int()
        category = String()

    item = Field(lambda: InventoryItem)

    def mutate(root, info, name, price=None, quantity=None, category=None):
        for item in inventory:
            if item.name == name:
                if price:
                    item.price = price
                if quantity:
                    item.quantity = quantity
                if category:
                    item.category = category
                return UpdateItem(item=item)
        return None

class DeleteItem(Mutation):
    class Arguments:
        name = String(required=True)

    ok = Boolean()

    def mutate(root, info, name):
        global inventory  
        inventory = [item for item in inventory if item.name != name]
        return DeleteItem(ok=True)

class Mutations(ObjectType):
    add_item = AddItem.Field()
    update_item = UpdateItem.Field()
    delete_item = DeleteItem.Field()

schema = Schema(query=Query, mutation=Mutations)