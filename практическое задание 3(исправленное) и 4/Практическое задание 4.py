class SocialNetwork:
    """Базовый класс для социальных сетей."""

    def __init__(self, name: str, user_count: int):
        """
        :param name: Название социальной сети
        :param user_count: Количество пользователей
        """
        self._name = name  # Название сети не должно изменяться напрямую
        self.user_count = user_count

    @property
    def name(self) -> str:
        """Возвращает название социальной сети."""
        return self._name

    def __str__(self) -> str:
        return f"Социальная сеть {self.name}, пользователей: {self.user_count}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, user_count={self.user_count})"

    def register_user(self) -> None:
        """Увеличивает количество пользователей на 1."""
        self.user_count += 1

    def delete_user(self) -> None:
        """Уменьшает количество пользователей на 1, но не ниже 0."""
        if self.user_count > 0:
            self.user_count -= 1


class VK(SocialNetwork):
    """Класс для социальной сети VK."""

    def __init__(self, user_count: int, groups_count: int):
        """
        :param user_count: Количество пользователей
        :param groups_count: Количество групп в VK
        """
        super().__init__("VK", user_count)
        self.groups_count = groups_count

    def __str__(self) -> str:
        return f"VK: {self.user_count} пользователей, {self.groups_count} групп"

    def __repr__(self) -> str:
        return f"VK(user_count={self.user_count}, groups_count={self.groups_count})"

    def create_group(self) -> None:
        """Создаёт новую группу в VK."""
        self.groups_count += 1


class Facebook(SocialNetwork):
    """Класс для социальной сети Facebook."""

    def __init__(self, user_count: int, pages_count: int):
        """
        :param user_count: Количество пользователей
        :param pages_count: Количество страниц в Facebook
        """
        super().__init__("Facebook", user_count)
        self.pages_count = pages_count

    def __str__(self) -> str:
        return f"Facebook: {self.user_count} пользователей, {self.pages_count} страниц"

    def __repr__(self) -> str:
        return f"Facebook(user_count={self.user_count}, pages_count={self.pages_count})"

    def create_page(self) -> None:
        """Создаёт новую страницу в Facebook."""
        self.pages_count += 1


if __name__ == "__main__":
    pass