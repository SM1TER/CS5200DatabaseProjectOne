import helper

def find_transitive_dependencies(relations: list[helper.Relation]):
    transitive_dependencies = []
    """
    for left, rights in fd_dict.items():
        for right in rights:
            if right in fd_dict and left != right:
                transitive_dependencies.append((left, right, fd_dict[right]))
    return transitive_dependencies
    """
    k = []
    for relation in relations:
        k.append(relation.y)
    for r in relations:
        if(r.y in k):
            transitive_dependencies.append(helper.Relation([r.x, r.y]))


def reorganize_for_3NF(relations, primary_keys, transitive_deps):
    new_tables = {}
    for left, middle, rights in transitive_deps:
        # Move the transitive attributes to a new table
        new_table_name = middle + "Details"
        new_tables[new_table_name] = rights + [middle]
        
        # Adjust the original table by removing transitive attributes
        fd_dict[left] = list(set(fd_dict[left]) - set(rights))

        # Update primary key if needed
        if middle in primary_keys:
            primary_keys.remove(middle)
            primary_keys.append(new_table_name)

    return new_tables

# Example usage
fd_input = [
    "StudentID -> FirstName, LastName",
    "Course -> CourseStart, CourseEnd, Professor",
    "Professor -> ProfessorEmail"
]

relations = helper.readInRelations("data/relations")
primary_keys = helper.findPrimaryKeys(relations)

transitive_deps = find_transitive_dependencies(relations)
new_tables = reorganize_for_3NF(relations, primary_keys, transitive_deps)

print("Revised Functional Dependencies:", relations)
print("New Tables for 3NF:", new_tables)
print("Updated Primary Keys:", primary_keys)