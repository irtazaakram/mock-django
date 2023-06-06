"""
mock_django.models
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 DISQUS.
:license: Apache License 2.0, see LICENSE for more details.
"""

import mock

__all__ = ("ModelMock",)


# TODO: make foreignkey_id == foreignkey.id
class _ModelMock(mock.MagicMock):
    def __init__(self, *args, **kwargs):
        super(_ModelMock, self).__init__(*args, **kwargs)

        # Django ORM needed state for write status
        self._state = mock.Mock()
        self._state.db = None

    def _get_child_mock(self, **kwargs):
        name = kwargs.get("name", "")
        if name == "pk":
            return self.id
        return super(_ModelMock, self)._get_child_mock(**kwargs)


def ModelMock(model):
    """
    >>> Post = ModelMock(Post)
    >>> assert post.pk == post.id
    """
    return _ModelMock(spec=model())
