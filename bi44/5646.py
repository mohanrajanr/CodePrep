from typing import List


def minimumTeachings(n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

    languages = [set(l) for l in languages]

    min_users = len(friendships)

    for i in range(1, n+1):

        no_of_users = 0
        user_name = set()

        # For each language
        lang_match = True

        for relation in friendships:
            friend1 = relation[0]
            friend2 = relation[1]

            l1 = languages[friend1 - 1]
            l2 = languages[friend2 - 1]

            # By Default they don't match
            if not l1.intersection(l2):

                new_l1 = l1 | {i}
                new_l2 = l2 | {i}

                # print(i, new_l1, new_l2, l1, l2)

                if new_l1 != l1:
                    no_of_users += 1
                    user_name = user_name | {friend1}
                if new_l2 != l2:
                    no_of_users += 1
                    user_name = user_name | {friend2}

                if not new_l1.intersection(l2) or not new_l2.intersection(l1):
                    lang_match = False
                    break

        if lang_match:
            min_users = min(min_users, no_of_users)
            # print("lang:{} match :{}".format(i, min_users))

    return min_users


print(minimumTeachings(2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]]))
print(minimumTeachings(4, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]]))
print(minimumTeachings(11, [[3,11,5,10,1,4,9,7,2,8,6],[5,10,6,4,8,7],[6,11,7,9],[11,10,4],[6,2,8,4,3],[9,2,8,4,6,1,5,7,3,10],[7,5,11,1,3,4],[3,4,11,10,6,2,1,7,5,8,9],[8,6,10,2,3,1,11,5],[5,11,6,4,2]], [[7,9],[3,7],[3,4],[2,9],[1,8],[5,9],[8,9],[6,9],[3,5],[4,5],[4,9],[3,6],[1,7],[1,3],[2,8],[2,6],[5,7],[4,6],[5,8],[5,6],[2,7],[4,8],[3,8],[6,8],[2,5],[1,4],[1,9],[1,6],[6,7]]))
print(minimumTeachings(17, [[4,7,2,14,6],[15,13,6,3,2,7,10,8,12,4,9],[16],[10],[10,3],[4,12,8,1,16,5,15,17,13],[4,13,15,8,17,3,6,14,5,10],[11,4,13,8,3,14,5,7,15,6,9,17,2,16,12],[4,14,6],[16,17,9,3,11,14,10,12,1,8,13,4,5,6],[14],[7,14],[17,15,10,3,2,12,16,14,1,7,9,6,4]], [[4,11],[3,5],[7,10],[10,12],[5,7],[4,5],[3,8],[1,5],[1,6],[7,8],[4,12],[2,4],[8,9],[3,10],[4,7],[5,12],[4,9],[1,4],[2,8],[1,2],[3,4],[5,10],[2,7],[1,7],[1,8],[8,10],[1,9],[1,10],[6,7],[3,7],[8,12],[7,9],[9,11],[2,5],[2,3]]))