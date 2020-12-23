from textwrap import dedent

class Marketplace:
    def __init__(self, id: int, name: str, categories:list):
        self.__id = id
        self.__name = name
        self.__categories = categories

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_categories(self) -> list:
        return self.__categories

    def __str__(self):
        return dedent(f"""
                Id: {self.get_id()}
                Name: {self.get_name()}
                Categories: {self.get_categories()}
                """)
 
class Category:

    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name

    def set_id(self, id: int) -> None:
        self.__id = int(id)

    def get_id(self) -> int:
        return self.__id

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def __str__(self):
        return dedent(f"""
                Id: {self.get_id()}
                Name: {self.get_name()}
                """)
        
class SubCategory(Category):

    def __init__(self, id: int, name: str, parent: Category):
        self.__parent = parent
        super().__init__(id, name)
    
    def get_parent(self) -> Category:
        return self.__parent
    
    def set_parent(self, parent: Category) -> None:
        self.__parent = parent
    
    def get_parent_id(self) -> str:
        return self.get_parent().get_id()
    
    def __str__(self):
        return dedent(f"""
                Id: {self.get_id()}
                Name: {self.get_name()}
                Parent: {self.get_parent_id()}
                """)
