import copy
from prototype_.entity import SelfReferencingEntity
from prototype_.component import SomeComponent


if __name__ == "__main__":
    list_of_objects = [1, {1,2,3}, [1,2,3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    shallow_copied_component = copy.copy(component)

    """Alterando a lista em shallow_copied_component e vendo se ela muda o component"""
    shallow_copied_component.some_list_of_objects.append("another object")
    if component.some_list_of_objects[-1] == "another object":
        print(
                "Adding elements to 'shallow_copied_components' "
                "some_list_of_objects adds it to 'components' "
                "some_list_of_objects. \n\n"

        )
    else:
        print(
                "Adding elements to 'shallow_copied_components' "
                "some_list_of_objects doesn't add it to 'component's "
                "come_list_of_objects \n\n "

        )

    

    """Alterando o conjunto na lista de objetos"""
    component.some_list_of_objects[1].add(4)
    if 4 in shallow_copied_component.some_list_of_objects[1]:
        print(
            "Changing objects in the 'component's some_list_of_objetcs "
            "Changes that object in 'shallow_copied_component's "
            "some_list_of_objects. \n\n" 
        )

    else:
        print(

            "Changing objects in the 'component's some_list_of_objects "
            "doesn't change that object in 'shallow_copied_component's "
            "some_list_of_objects \n\n"
        )

    deep_copied_component = copy.deepcopy(component)


    """Alterando lista em deep_copied_component e ver se muda no componente"""
    deep_copied_component.some_list_of_objects.append("one more object")
    if component.some_list_of_objects[-1] == "one more object":
        print(
            "Adding elements to `deep_copied_component`'s "
            "some_list_of_objects adds it to `component`'s "
            "some_list_of_objects.\n\n"
        )
    else:
        print(
            "Adding elements to `deep_copied_component`'s "
            "some_list_of_objects doesn't add it to `component`'s "
            "some_list_of_objects. \n\n"
        )

    # Let's change the set in the list of objects.
    component.some_list_of_objects[1].add(10)
    if 10 in deep_copied_component.some_list_of_objects[1]:
        print(
            "Changing objects in the `component`'s some_list_of_objects "
            "changes that object in `deep_copied_component`'s "
            "some_list_of_objects. \n\n"
        )
    else:
        print(
            "Changing objects in the `component`'s some_list_of_objects "
            "doesn't change that object in `deep_copied_component`'s "
            "some_list_of_objects.\n\n"
        )

    print(
        f"id(deep_copied_component.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent)}"
    )
    print(
        f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
    )
    print(
        "^^ This shows that deepcopied objects contain same reference, they "
        "are not cloned repeatedly. \n\n"
    )

