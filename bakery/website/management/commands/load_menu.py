from django.core.management.base import BaseCommand
from website.models import Category, Product


class Command(BaseCommand):
    help = "Load bakery categories and sample products"

    def handle(self, *args, **kwargs):

        # All food categories and sample prices
        menu = {
            "Burger": [
                ("Veg Burger", 60),
                ("Cheese Burger", 80),
            ],
            "Cake": [
                ("Chocolate Cake", 450),
                ("Black Forest Cake", 500),
                ("Vanilla Cake", 400),
                ("Pineapple Cake", 450),
            ],
            "Chinese": [
                ("Veg Hakka Noodles", 100),
                ("Veg Fried Rice", 100),
                ("Veg Manchurian", 120),
            ],
            "Chocolate": [
                ("Chocolate Pastry", 60),
                ("Chocolate Brownie", 80),
            ],
            "Coffee": [
                ("Hot Coffee", 40),
                ("Cold Coffee", 90),
            ],
            "Cold Drink": [
                ("Cold Drink", 40),
                ("Mineral Water", 20),
            ],
            "Gift": [
                ("Chocolate Gift Box", 250),
                ("Cake Gift Pack", 350),
            ],
            "Indians": [
                ("Veg Thali", 150),
                ("Paneer Masala", 140),
            ],
            "Maggie": [
                ("Plain Maggi", 50),
                ("Veg Maggi", 70),
                ("Cheese Maggi", 90),
            ],
            "Momos": [
                ("Veg Steamed Momos", 80),
                ("Veg Fried Momos", 100),
            ],
            "Other": [
                ("Special Snack", 60),
                ("Special Combo", 150),
            ],
            "Pasta": [
                ("White Sauce Pasta", 120),
                ("Red Sauce Pasta", 120),
            ],
            "Patties": [
                ("Aloo Patties", 25),
                ("Paneer Patties", 40),
            ],
            "Pizza": [
                ("Margherita Pizza", 120),
                ("Farmhouse Pizza", 180),
            ],
            "Rice": [
                ("Veg Fried Rice", 100),
                ("Jeera Rice", 90),
            ],
            "Roll": [
                ("Veg Roll", 60),
                ("Paneer Roll", 90),
            ],
            "Sandwich": [
                ("Veg Sandwich", 60),
                ("Cheese Sandwich", 80),
            ],
            "Shake": [
                ("Chocolate Shake", 100),
                ("Strawberry Shake", 100),
            ],
            "Snacks": [
                ("French Fries", 80),
                ("Garlic Bread", 100),
            ],
            "Soup": [
                ("Tomato Soup", 70),
                ("Veg Manchow Soup", 90),
            ],
            "Tacos & Garlic Breads": [
                ("Veg Tacos", 100),
                ("Cheese Garlic Bread", 120),
            ],
            "Tea": [
                ("Masala Tea", 20),
                ("Ginger Tea", 25),
            ],
            "Waffles": [
                ("Chocolate Waffle", 100),
                ("Oreo Waffle", 120),
            ],
        }

        # Different images for each category
        image_urls = {
            "Burger": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600",
            "Cake": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600",
            "Chinese": "https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600",
            "Chocolate": "https://images.unsplash.com/photo-1511381939415-e44015466834?w=600",
            "Coffee": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=600",
            "Cold Drink": "https://images.unsplash.com/photo-1544145945-f90425340c7e?w=600",
            "Gift": "https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?w=600",
            "Indians": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=600",
            "Maggie": "https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600",
            "Momos": "https://images.unsplash.com/photo-1563245372-f21724e3856d?w=600",
            "Other": "https://images.unsplash.com/photo-1547592180-85f173990554?w=600",
            "Pasta": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=600",
            "Patties": "https://images.unsplash.com/photo-1608039829572-78524f79c4c5?w=600",
            "Pizza": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600",
            "Rice": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=600",
            "Roll": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=600",
            "Sandwich": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?w=600",
            "Shake": "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=600",
            "Snacks": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=600",
            "Soup": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600",
            "Tacos & Garlic Breads": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?w=600",
            "Tea": "https://images.unsplash.com/photo-1544787219-7f47ccb76574?w=600",
            "Waffles": "https://images.unsplash.com/photo-1562376552-0d160a2f238d?w=600",
        }

        # Different images for individual products
        product_images = {
            "Veg Burger": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600",
            "Cheese Burger": "https://images.unsplash.com/photo-1553979459-d2229ba7433a?w=600",

            "Chocolate Cake": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600",
            "Black Forest Cake": "https://images.unsplash.com/photo-1571115177098-24ec42ed204d?w=600",
            "Vanilla Cake": "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600",
            "Pineapple Cake": "https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?w=600",

            "Veg Hakka Noodles": "https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600",
            "Veg Fried Rice": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=600",
            "Veg Manchurian": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600",

            "Chocolate Pastry": "https://images.unsplash.com/photo-1511381939415-e44015466834?w=600",
            "Chocolate Brownie": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=600",

            "Hot Coffee": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=600",
            "Cold Coffee": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=600",

            "Cold Drink": "https://images.unsplash.com/photo-1544145945-f90425340c7e?w=600",
            "Mineral Water": "https://images.unsplash.com/photo-1564419320461-6870880221ad?w=600",

            "Chocolate Gift Box": "https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?w=600",
            "Cake Gift Pack": "https://images.unsplash.com/photo-1519225421980-715cb0215aed?w=600",

            "Veg Thali": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=600",
            "Paneer Masala": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=600",

            "Plain Maggi": "https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600",
            "Veg Maggi": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=600",
            "Cheese Maggi": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=600",

            "Veg Steamed Momos": "https://images.unsplash.com/photo-1563245372-f21724e3856d?w=600",
            "Veg Fried Momos": "https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?w=600",

            "Special Snack": "https://images.unsplash.com/photo-1547592180-85f173990554?w=600",
            "Special Combo": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600",

            "White Sauce Pasta": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=600",
            "Red Sauce Pasta": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=600",

            "Aloo Patties": "https://images.unsplash.com/photo-1608039829572-78524f79c4c5?w=600",
            "Paneer Patties": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600",

            "Margherita Pizza": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600",
            "Farmhouse Pizza": "https://images.unsplash.com/photo-1571407970349-bc81e7e96d47?w=600",

            "Jeera Rice": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=600",

            "Veg Roll": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=600",
            "Paneer Roll": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=600",

            "Veg Sandwich": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?w=600",
            "Cheese Sandwich": "https://images.unsplash.com/photo-1539252554453-80ab65ce3586?w=600",

            "Chocolate Shake": "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=600",
            "Strawberry Shake": "https://images.unsplash.com/photo-1553530666-ba11a7da3888?w=600",

            "French Fries": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=600",
            "Garlic Bread": "https://images.unsplash.com/photo-1573140247632-f8fd74997d5c?w=600",

            "Tomato Soup": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600",
            "Veg Manchow Soup": "https://images.unsplash.com/photo-1547592180-85f173990554?w=600",

            "Veg Tacos": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?w=600",
            "Cheese Garlic Bread": "https://images.unsplash.com/photo-1573140247632-f8fd74997d5c?w=600",

            "Masala Tea": "https://images.unsplash.com/photo-1544787219-7f47ccb76574?w=600",
            "Ginger Tea": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?w=600",

            "Chocolate Waffle": "https://images.unsplash.com/photo-1562376552-0d160a2f238d?w=600",
            "Oreo Waffle": "https://images.unsplash.com/photo-1568051243858-533a6078096e?w=600",
        }

        # Add or update all categories and products
        for category_name, products in menu.items():

            slug = (
                category_name.lower()
                .replace("&", "and")
                .replace(" ", "-")
            )

            image_url = image_urls.get(category_name, "")

            category, created = Category.objects.get_or_create(
                slug=slug,
                defaults={
                    "name": category_name,
                    "description": f"Explore our {category_name} menu",
                    "image_url": image_url,
                }
            )

            # Update existing category
            category.name = category_name
            category.image_url = image_url
            category.save()

            # Add or update products
            for product_name, price in products:
                # Product ki apni image select hogi
                product_image = product_images.get(
                    product_name,
                    image_url
                )

                Product.objects.update_or_create(
                    category=category,
                    name=product_name,
                    defaults={
                        "description": f"Fresh and delicious {product_name}",
                        "price": price,
                        "image_url": product_image,
                    }
                )

        self.stdout.write(
            self.style.SUCCESS(
                "All categories and products updated successfully!"
            )
        )
