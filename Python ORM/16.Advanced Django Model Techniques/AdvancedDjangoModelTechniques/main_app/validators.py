from django.core.exceptions import ValidationError


def validate_menu_categories(value):
    # if value not in ("Appetizers", "Main Course", "Desserts"):
    #     raise ValidationError('The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')

    required_categories = ["Appetizers", "Main Course", "Desserts"]

    for category in required_categories:
        if category.lower() not in value.lower():
            raise ValidationError('The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')
