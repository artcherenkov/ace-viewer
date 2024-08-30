import re
from django.utils.deprecation import MiddlewareMixin


def camel_to_snake(name):
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


class QueryParameterCamelToSnakeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("Middleware triggered")
        query_dict = request.GET.copy()
        new_query_dict = {}

        for key in query_dict.keys():
            snake_key = camel_to_snake(key)
            values = query_dict.getlist(key)

            # Convert each value from camelCase to snake_case
            new_values = [camel_to_snake(value) if isinstance(value, str) else value for value in values]

            # If there is only one value, set it as a string, not a list
            if len(new_values) == 1:
                new_query_dict[snake_key] = new_values[0]
            else:
                new_query_dict[snake_key] = new_values

            print(f"Converting {key} to {snake_key}, values: {values} to {new_values}")

        # Обновляем request.GET с преобразованными ключами и значениями
        request.GET = new_query_dict
        print("Modified query parameters:", request.GET)
