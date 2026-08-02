import gc
import sys


def section_header(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


# =====================================================================
# ЧАСТЬ 1: Подсчет ссылок (sys.getrefcount)
# =====================================================================
section_header("ЧАСТЬ 1: Исследование счетчика ссылок (Reference Counting)")


# 1. Создаем объект списка
my_list = [1, 2, 3]

# ВАЖНО: sys.getrefcount(x) всегда возвращает значение на 1 больше реального,
# так как сам вызов функции передает х как аргумент и создает временную ссылку
# в фрейме стека этой функции.
initial_refs = sys.getrefcount(my_list)
print(f"[1] Список создан: my_list = [1, 2, 3]")
print(f"    - sys.getrefcount(my_list): {initial_refs}")
print(f"    - Реальное кол-во ссылок в CPython (ob_refcnt): {initial_refs - 1} (только 'my_list')")

# 2. Добавляем ссылку через присваивание
another_ref = my_list
refs_after_assign = sys.getrefcount(my_list)
print(f"\n[2] Выполнено: another_ref = my_list")
print(f"    - sys.getrefcount(my_list): {refs_after_assign}")
print(f"    - Реальное кол-во ссылок (ob_refcnt): {refs_after_assign - 1} ('my_list' + 'another_ref')")


# 3. Передаем список аргументом в функцию
def inspect_refcount(arg_list):
    # В момент входа в функцию создается локальная переменная arg_list в Стеке
    in_func_refs = sys.getrefcount(arg_list)
    print(f"\n[3] Внутри функции inspect_refcount(arg_list):")
    print(f'Вывод gc.get_referrers(arg_list):\n{gc.get_referrers(arg_list)}\n')
    print(f'Вывод gc.get_referents(arg_list):\n{gc.get_referents(arg_list)}\n')
    print(f"    - sys.getrefcount(arg_list): {in_func_refs}")
    print(f"    - Реальное кол-во ссылок (ob_refcnt): {in_func_refs - 1} ('my_list' + 'another_ref' + 'arg_list')")


inspect_refcount(my_list)

# 4. Проверяем счетчик после выхода из функции
refs_after_func = sys.getrefcount(my_list)
print(f"\n[4] После завершения работы функции (фрейм функции удален):")
print(f"    - sys.getrefcount(my_list): {refs_after_func}")
print(f"    - Реальное кол-во ссылок (ob_refcnt): {refs_after_func - 1} ('my_list' + 'another_ref')")


# =====================================================================
# ЧАСТЬ 2: Циклические ссылки и Garbage Collector
# =====================================================================
section_header("ЧАСТЬ 2: Циклические ссылки и сборщик мусора (GC)")


class Node:

    def __init__(self, name: str):
        self.name = name
        self.peer = None

    def __repr__(self):
        return f"Node({self.name})"


# 1. Отключаем автоматический сборщик мусора
gc.disable()
print(f"[1] Автоматический сборщик мусора отключен (gc.isenabled() = {gc.isenabled()})")

# 2. Создаем структуру циклических ссылок
obj1 = Node("A")
obj2 = Node("B")

obj1.peer = obj2  # obj2.ob_refcnt увеличивается до 2
obj2.peer = obj1  # obj1.ob_refcnt увеличивается до 2

# Фиксируем C-адреса памяти (id) объектов для последующего поиска в Куче
id_obj1, id_obj2 = id(obj1), id(obj2)
print(f"[2] Созданы объекты {obj1} (id: {id_obj1}) и {obj2} (id: {id_obj2})")
print(f"    - obj1.peer указывает на {obj1.peer}")
print(f"    - obj2.peer указывает на {obj2.peer}")

# 3. Включаем дебаг-флаг SAVEALL, чтобы GC сохранял найденный мусор в gc.garbage
# (Это позволит нам физически «потрогать» изолированные объекты)
gc.set_debug(gc.DEBUG_SAVEALL)

# 4. Удаляем внешние переменные из Стека
del obj1
del obj2
print("\n[3] Выполнены команды `del obj1` и `del obj2` (переменные удалены из Стека).")

# Проверяем, что объекты всё ещё физически существуют в Куче
heap_objects = [o for o in gc.get_objects() if id(o) in (id_obj1, id_obj2)]
print(f"    - Проверка Кучи: найдено объектов с нашими id: {len(heap_objects)}")
print(f"    - Вывод: Подсчет ссылок БЕССИЛЕН. Объекты изолированы, но живы в Куче!")

# 5. Принудительно запускаем сборщик мусора
print("\n[4] Запускаем принудительную сборку мусора через gc.collect()...")
unreachable_count = gc.collect()

print(f"    - gc.collect() вернул зачищенных объектов/циклов: {unreachable_count}")
print(f"    - Содержимое gc.garbage (изолированный мусор): {gc.garbage}")

# 6. Полная очистка и восстановление состояния
gc.garbage.clear()  # Очищаем ссылки из списка отладки
gc.set_debug(0)  # Сбрасываем дебаг-флаги

# Проверяем Кучу повторно
post_gc_heap_objects = [
    o for o in gc.get_objects() if id(o) in (id_obj1, id_obj2)
]
print(
    f"\n[5] Проверка Кучи после полной зачистки: найдено объектов с нашими id: {len(post_gc_heap_objects)}"
)

# Включаем автоматический GC обратно
gc.enable()
print(
    f"    - Сборщик мусора снова включен (gc.isenabled() = {gc.isenabled()})"
)
