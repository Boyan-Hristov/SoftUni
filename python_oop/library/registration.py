from library.user import User
from library.library import Library


class Registration:

    def add_user(self, user: User, library: Library):

        if user not in library.user_records:
            library.user_records.append(user)

        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):

        if user not in library.user_records:
            return "We could not find such user to remove!"

        try:
            del library.rented_books[user.username]
        except KeyError:
            pass

        library.user_records.remove(user)


    def change_username(self, user_id: int, new_username: str, library: Library):

        try:
            user = next(filter(lambda u: u.user_id == user_id, library.user_records))
        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if user.username == new_username:
            return "Please check again the provided username - " \
                   "it should be different than the username used so far!"

        try:
            library.rented_books[new_username] = library.rented_books.pop(user.username)
        except KeyError:
            pass

        user.username = new_username

        return f"Username successfully changed to: {new_username} for user id: {user_id}"

        # for current_user in library.user_records:
        #     if current_user.user_id == user_id:
        #         if not new_username == current_user.username:
        #             if current_user.username in library.rented_books.keys():
        #                 library.rented_books[new_username] = library.rented_books[current_user.username]
        #                 del library.rented_books[current_user.username]
        #             current_user.username = new_username
        #             return f"Username successfully changed to: {new_username} for user id: {user_id}"
        #
        #         return "Please check again the provided username - " \
        #                "it should be different than the username used so far!"
        #
        # return f"There is no user with id = {user_id}!"
