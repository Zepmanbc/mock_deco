import functools


def mondecorateur_avant(func):
    """Recreate driver if not exists."""

    @functools.wraps(func)
    def wrapper(self, url):
        new_url = f"https://{url}"
        return func(self, new_url)

    return wrapper


def mondecorateur_apres(func):
    """Recreate driver if not exists."""

    @functools.wraps(func)
    def wrapper(self, url):
        new_url = f"{url}.com"
        return func(self, new_url)

    return wrapper
